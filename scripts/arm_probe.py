#!/usr/bin/env python3
"""Test ARM Live credentials locally, the exact way the radar notebooks do.

The radar cookbook fetches data through ACT's `download_arm_data(username,
token, ...)`, which builds this query and reads it:

    https://adc.arm.gov/armlive/data/query?user=USERNAME:TOKEN&ds=...&wt=json

So a credential can be checked without a Binder session at all -- and iterating
here takes seconds instead of a seven-minute pod. This mirrors ACT's own logic
(ARM-DOE/ACT, act/discovery/arm.py): same URL, same "an HTML body means the
credential was rejected" check.

Credentials come from the environment or --env-file, never from the command
line. Values are never printed; only their shape and the server's verdict are.

Usage:
    python scripts/arm_probe.py --env-file ~/.config/pythia-cookbook-review/arm.env
    ARM_USERNAME=... ARM_PASSWORD=... python scripts/arm_probe.py
"""

import argparse
import http.client
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

# A small, known-good datastream and a short window, purely to exercise auth.
DATASTREAM = "houcsapr2cfrS2.a1"
START = "2022-06-02T11:30:00"
END = "2022-06-02T11:40:00"

# ACT sends a browser-like UA; matched so we test the same request it makes.
HEADERS = {
    "user-agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    )
}


def load_env_file(path):
    values = {}
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip().strip("'\"")
    return values


def describe(name, value):
    """Report a credential's shape without ever revealing it."""
    spaces = [i for i, c in enumerate(value) if c == " "]
    other_ws = any(c.isspace() and c != " " for c in value)
    return (
        f"{name}: length {len(value)}, "
        f"{'no spaces' if not spaces else f'SPACES at {spaces}'}"
        f"{', other whitespace' if other_ws else ''}, "
        f"{'alphanumeric only' if value.isalnum() else 'has punctuation/symbols'}"
    )


def build_query_url(username, token):
    """The query URL exactly as ACT builds it: user=username:token, unencoded.

    ACT does not percent-encode, so a space in the token yields a URL that
    Python's http.client refuses ("URL can't contain control characters") --
    the failure the radar run hit. We reproduce that here rather than paper over
    it, so a bad credential fails the same way it would in the cookbook.
    """
    start = f"&start={START}"
    end = f"&end={END}"
    user = ":".join([username, token])
    return (
        "https://adc.arm.gov/armlive/data/query?"
        f"user={user}&ds={DATASTREAM}{start}{end}&wt=json"
    )


def probe(username, token, encode=False):
    """Hit the ARM query endpoint. Returns (verdict, detail)."""
    if encode:
        # What ACT *should* arguably do: percent-encode the credential so a
        # space cannot break the URL. Offered as a comparison point.
        user = urllib.parse.quote(f"{username}:{token}", safe="")
        url = (
            "https://adc.arm.gov/armlive/data/query?"
            f"user={user}&ds={DATASTREAM}&start={START}&end={END}&wt=json"
        )
    else:
        url = build_query_url(username, token)

    try:
        request = urllib.request.Request(url, None, HEADERS)
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode("utf-8", errors="replace")
    except http.client.InvalidURL:
        # A malformed URL (e.g. a space in the token) never leaves the machine.
        # CRITICAL: the exception message embeds the full URL, credential and
        # all, so we must NEVER surface it. Report only the shape of the fault.
        return "invalid-url", (
            "the credential produced an invalid URL (contains a space or "
            "control character); request was not sent"
        )
    except urllib.error.HTTPError as err:
        return "http-error", f"HTTP {err.code} {err.reason}"
    except urllib.error.URLError as err:
        # URLError.reason can echo the URL on some paths; keep it generic.
        return "network-error", err.__class__.__name__

    # ACT's own tell: an HTML body means the credential was rejected.
    if body[1:14] == "!DOCTYPE html":
        return "rejected", "server returned an HTML error page (bad username or token)"

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError:
        return "unexpected", f"non-JSON body: {body[:120]!r}"

    status = parsed.get("status")
    files = parsed.get("files") or []
    if status == "success":
        return "ok", f"authenticated; {len(files)} file(s) match the test query"
    return "rejected", f"status={status!r}, body={body[:160]!r}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file")
    parser.add_argument(
        "--encode",
        action="store_true",
        help="percent-encode the credential (comparison; not what ACT does)",
    )
    parser.add_argument(
        "--trim-at-space",
        action="store_true",
        help="test the token truncated at its first whitespace (a common "
        "copy-paste fix); the value is never printed",
    )
    args = parser.parse_args()

    values = load_env_file(args.env_file) if args.env_file else {}
    username = values.get("ARM_USERNAME") or os.environ.get("ARM_USERNAME")
    token = values.get("ARM_PASSWORD") or os.environ.get("ARM_PASSWORD")

    if not username or not token:
        sys.exit("Need ARM_USERNAME and ARM_PASSWORD (env or --env-file)")

    if args.trim_at_space:
        trimmed = token.split()[0] if token.split() else token
        print(f"(trimming token from length {len(token)} to {len(trimmed)} "
              "at first whitespace)")
        token = trimmed

    print(describe("ARM_USERNAME", username))
    print(describe("ARM_PASSWORD/token", token))
    print()

    verdict, detail = probe(username, token, encode=args.encode)
    print(f"verdict: {verdict}")
    print(f"detail:  {detail}")
    return 0 if verdict == "ok" else 1


if __name__ == "__main__":
    sys.exit(main())
