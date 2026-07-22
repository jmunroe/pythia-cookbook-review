# marine-heatwave-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/marine-heatwave-cookbook)

Run 2026-07-22 21:46:47 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [marine-heatwave-cookbook](https://github.com/ProjectPythia/marine-heatwave-cookbook) at ref [`main`](https://github.com/ProjectPythia/marine-heatwave-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `incubating` |
| Time to a ready session | 5m 37s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 26.9s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 0.48 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 5.6% |
| Peak rss (upper bound, shared pages double-counted) | 0.50 GB |
| Errors raised | 1 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/foundation/mhw_observation_myst.ipynb`](https://github.com/ProjectPythia/marine-heatwave-cookbook/blob/main/notebooks/foundation/mhw_observation_myst.ipynb) | 7.42s |

Executed 1 notebook(s) from the project toc: [`notebooks/foundation/mhw_observation_myst.ipynb`](https://github.com/ProjectPythia/marine-heatwave-cookbook/blob/main/notebooks/foundation/mhw_observation_myst.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/marine-heatwave-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`ChunkedEncodingError`** — Response ended prematurely

in `site/content/notebooks.foundation.mhw-observation-myst.json`

```
---------------------------------------------------------------------------
ProtocolError                             Traceback (most recent call last)
File /srv/conda/envs/notebook/lib/python3.14/site-packages/requests/models.py:820, in Response.iter_content.<locals>.generate()
    819 try:
--> 820     yield from self.raw.stream(chunk_size, decode_content=True)
    821 except ProtocolError as e:

File /srv/conda/envs/notebook/lib/python3.14/site-packages/urllib3/response.py:1088, in HTTPResponse.stream(self, amt, decode_content)
   1087 if self.chunked and self.supports_chunked_reads():
-> 1088     yield from self.read_chunked(amt, decode_content=decode_content)
   1089 else:

File /srv/conda/envs/notebook/lib/python3.14/site-packages/urllib3/response.py:1248, in HTTPResponse.read_chunked(self, amt, decode_content)
   1247 while True:
-> 1248     self._update_chunk_length()
   1249     if self.chunk_left == 0:

File /srv/conda/envs/notebook/lib/python3.14/site-packages/urllib3/response.py:1178, in HTTPResponse._update_chunk_length(self)
   1176 else:
   1177     # Truncated at start of next chunk
-> 1178     raise ProtocolError("Response ended prematurely") from None

ProtocolErro
```

