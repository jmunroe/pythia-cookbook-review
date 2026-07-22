# vapor-python-cookbook

Live outcome: **ran with errors**. [← All live checks](../live.md) · [Repository](https://github.com/ProjectPythia/vapor-python-cookbook)

Run 2026-07-22 08:03:57 UTC against [https://binder.projectpythia.org](https://binder.projectpythia.org), building [vapor-python-cookbook](https://github.com/ProjectPythia/vapor-python-cookbook) at ref [`main`](https://github.com/ProjectPythia/vapor-python-cookbook/tree/main).

| Measure | Value |
|---|---|
| Live outcome | **ran with errors** |
| Static tier | `healthy` |
| Time to a ready session | 2m 41s (fresh build) |
| Build succeeded | yes |
| Notebook execution | 14.09s |
| Build command exit code | 0 (zero despite cell errors) |
| Notebooks ran clean | no |
| Execution cache | **reused — timing is not execution** |
| Peak memory (pss) | 0.69 GB |
| Pod memory limit | 8.59 GB |
| Peak as share of limit | 8.0% |
| Peak rss (upper bound, shared pages double-counted) | 0.92 GB |
| Errors raised | 15 |

| Notebook | Execute + render |
|---|---|
| [`notebooks/numpy_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/numpy_example.ipynb) | 3.01s |
| [`notebooks/quickstart.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/quickstart.ipynb) | 3.02s |
| [`notebooks/dataset_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/dataset_example.ipynb) | 3.1s |
| [`notebooks/keyframing_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/keyframing_example.ipynb) | 3.23s |
| [`notebooks/workflow_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/workflow_example.ipynb) | 3.41s |
| [`notebooks/AGU_2023_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/AGU_2023_example.ipynb) | 3.51s |
| [`notebooks/custom_images_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/custom_images_example.ipynb) | 3.52s |
| [`notebooks/cloudfield_visualizer.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/cloudfield_visualizer.ipynb) | 3.56s |
| [`notebooks/camera_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/camera_example.ipynb) | 3.67s |
| [`notebooks/xarray_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/xarray_example.ipynb) | 4.16s |
| [`notebooks/animation_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/animation_example.ipynb) | 5.57s |
| [`notebooks/transfer_function_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/transfer_function_example.ipynb) | 5.58s |
| [`notebooks/annotation_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/annotation_example.ipynb) | 5.77s |
| [`notebooks/flow_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/flow_example.ipynb) | 5.76s |
| [`notebooks/visualizer_widget_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/visualizer_widget_example.ipynb) | 5.98s |

Executed 15 notebook(s) from the project toc: [`notebooks/AGU_2023_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/AGU_2023_example.ipynb), [`notebooks/animation_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/animation_example.ipynb), [`notebooks/annotation_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/annotation_example.ipynb), [`notebooks/camera_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/camera_example.ipynb), [`notebooks/cloudfield_visualizer.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/cloudfield_visualizer.ipynb), [`notebooks/custom_images_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/custom_images_example.ipynb), [`notebooks/dataset_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/dataset_example.ipynb), [`notebooks/flow_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/flow_example.ipynb), [`notebooks/keyframing_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/keyframing_example.ipynb), [`notebooks/numpy_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/numpy_example.ipynb), [`notebooks/quickstart.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/quickstart.ipynb), [`notebooks/transfer_function_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/transfer_function_example.ipynb), [`notebooks/visualizer_widget_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/visualizer_widget_example.ipynb), [`notebooks/workflow_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/workflow_example.ipynb), [`notebooks/xarray_example.ipynb`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/notebooks/xarray_example.ipynb). Notebooks not listed in [`myst.yml`](https://github.com/ProjectPythia/vapor-python-cookbook/blob/main/myst.yml) are never executed by a build, so a repo can carry notebooks no build ever touches.

### Errors

**`ModuleNotFoundError`** — No module named 'numpy'

in `site/content/notebooks.workflow-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import example_utils
      2 from vapor import session, renderer, dataset, camera

File ~/notebooks/example_utils.py:20
     16     sys.path.append('..')
     19 from inspect import signature
---> 20 import numpy as np
     21 from math import sin
     23 def SampleFunctionOnRegularGrid(f, ext=None, shape=None):

ModuleNotFoundError: No module named 'numpy'
```

**`ModuleNotFoundError`** — No module named 'numpy'

in `site/content/notebooks.visualizer-widget-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import example_utils
      2 from vapor import session, renderer, dataset, camera, widget
      3 import ipywidgets as widgets

File ~/notebooks/example_utils.py:20
     16     sys.path.append('..')
     19 from inspect import signature
---> 20 import numpy as np
     21 from math import sin
     23 def SampleFunctionOnRegularGrid(f, ext=None, shape=None):

ModuleNotFoundError: No module named 'numpy'
```

**`ModuleNotFoundError`** — No module named 'numpy'

in `site/content/notebooks.dataset-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import example_utils
      2 from vapor import session, renderer, dataset, camera

File ~/notebooks/example_utils.py:20
     16     sys.path.append('..')
     19 from inspect import signature
---> 20 import numpy as np
     21 from math import sin
     23 def SampleFunctionOnRegularGrid(f, ext=None, shape=None):

ModuleNotFoundError: No module named 'numpy'
```

**`ModuleNotFoundError`** — No module named 'numpy'

in `site/content/notebooks.numpy-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import example_utils
      2 from vapor import session, renderer, dataset, camera
      3 import numpy as np

File ~/notebooks/example_utils.py:20
     16     sys.path.append('..')
     19 from inspect import signature
---> 20 import numpy as np
     21 from math import sin
     23 def SampleFunctionOnRegularGrid(f, ext=None, shape=None):

ModuleNotFoundError: No module named 'numpy'
```

**`ModuleNotFoundError`** — No module named 'numpy'

in `site/content/notebooks.transfer-function-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import example_utils
      2 from vapor import session, renderer, dataset, camera, transferfunction
      3 from vapor.utils import histogram

File ~/notebooks/example_utils.py:20
     16     sys.path.append('..')
     19 from inspect import signature
---> 20 import numpy as np
     21 from math import sin
     23 def SampleFunctionOnRegularGrid(f, ext=None, shape=None):

ModuleNotFoundError: No module named 'numpy'
```

**`ModuleNotFoundError`** — No module named 'matplotlib'

in `site/content/notebooks.custom-images-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 7
      4 import zipfile
      6 # Plotting libraries:
----> 7 import matplotlib.pyplot as plt
      8 import cartopy.crs as ccrs
      9 import cartopy.feature as cf

ModuleNotFoundError: No module named 'matplotlib'
```

**`ModuleNotFoundError`** — No module named 'numpy'

in `site/content/notebooks.camera-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import example_utils
      2 from vapor import session, renderer, dataset, camera
      4 ses = session.Session()

File ~/notebooks/example_utils.py:20
     16     sys.path.append('..')
     19 from inspect import signature
---> 20 import numpy as np
     21 from math import sin
     23 def SampleFunctionOnRegularGrid(f, ext=None, shape=None):

ModuleNotFoundError: No module named 'numpy'
```

**`SSLError`** — HTTPSConnectionPool(host='data.rda.ucar.edu', port=443): Max retries exceeded with url: /ds897.7/Katrina.zip (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1017)')))

in `site/content/notebooks.xarray-example.json`

```
---------------------------------------------------------------------------
SSLCertVerificationError                  Traceback (most recent call last)
File /srv/conda/envs/notebook/lib/python3.10/site-packages/urllib3/connectionpool.py:464, in HTTPConnectionPool._make_request(self, conn, method, url, body, headers, retries, timeout, chunked, response_conn, preload_content, decode_content, enforce_content_length)
    463 try:
--> 464     self._validate_conn(conn)
    465 except (SocketTimeout, BaseSSLError) as e:

File /srv/conda/envs/notebook/lib/python3.10/site-packages/urllib3/connectionpool.py:1093, in HTTPSConnectionPool._validate_conn(self, conn)
   1092 if conn.is_closed:
-> 1093     conn.connect()
   1095 # TODO revise this, see https://github.com/urllib3/urllib3/issues/2791

File /srv/conda/envs/notebook/lib/python3.10/site-packages/urllib3/connection.py:790, in HTTPSConnection.connect(self)
    788 server_hostname_rm_dot = server_hostname.rstrip(".")
--> 790 sock_and_verified = _ssl_wrap_socket_and_match_hostname(
    791     sock=sock,
    792     cert_reqs=self.cert_reqs,
    793     ssl_version=self.ssl_version,
    794     ssl_minimum_version=self.ssl_minimum_version,
```

**`ModuleNotFoundError`** — No module named 'vapor'

in `site/content/notebooks.keyframing-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 from vapor import session, dataset, renderer
      2 from vapor.animation import Animation

ModuleNotFoundError: No module named 'vapor'
```

**`ModuleNotFoundError`** — No module named 'vapor'

in `site/content/notebooks.agu-2023-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[2], line 1
----> 1 from vapor import session
      2 ses = session.Session()

ModuleNotFoundError: No module named 'vapor'
```

**`ModuleNotFoundError`** — No module named 'numpy'

in `site/content/notebooks.animation-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import example_utils
      2 from vapor import session, renderer, dataset, camera
      3 from vapor.animation import Animation

File ~/notebooks/example_utils.py:20
     16     sys.path.append('..')
     19 from inspect import signature
---> 20 import numpy as np
     21 from math import sin
     23 def SampleFunctionOnRegularGrid(f, ext=None, shape=None):

ModuleNotFoundError: No module named 'numpy'
```

**`ModuleNotFoundError`** — No module named 'numpy'

in `site/content/notebooks.annotation-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import example_utils
      2 from vapor import session, renderer, dataset, camera
      3 from vapor.utils import histogram

File ~/notebooks/example_utils.py:20
     16     sys.path.append('..')
     19 from inspect import signature
---> 20 import numpy as np
     21 from math import sin
     23 def SampleFunctionOnRegularGrid(f, ext=None, shape=None):

ModuleNotFoundError: No module named 'numpy'
```

**`ModuleNotFoundError`** — No module named 'numpy'

in `site/content/notebooks.flow-example.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import example_utils
      2 from vapor import session, renderer, dataset, camera
      4 ses = session.Session()

File ~/notebooks/example_utils.py:20
     16     sys.path.append('..')
     19 from inspect import signature
---> 20 import numpy as np
     21 from math import sin
     23 def SampleFunctionOnRegularGrid(f, ext=None, shape=None):

ModuleNotFoundError: No module named 'numpy'
```

**`ModuleNotFoundError`** — No module named 'xarray'

in `site/content/notebooks.cloudfield-visualizer.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 import xarray as xr
      2 from pathlib import Path
      3 from vapor import session, renderer, dataset, camera

ModuleNotFoundError: No module named 'xarray'
```

**`ModuleNotFoundError`** — No module named 'vapor'

in `site/content/notebooks.quickstart.json`

```
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[1], line 1
----> 1 from vapor import session, renderer, dataset
      2 from vapor.animation import Animation
      3 from vapor.dataset import Dataset

ModuleNotFoundError: No module named 'vapor'
```

