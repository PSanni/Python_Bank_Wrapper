# Python_Bank_Wrapper
Python API wrapper for https://github.com/mangrep/ifsc-rest-api

###Requirements
1. [Python 2 or 3]
2. [Request](http://docs.python-requests.org/en/master/)

###Example Code
```python
from IFSCWrapper import Wrapper
from IFSCException import IFSCWrapperException

obj=Wrapper()
try:
    obj.init()
    print(obj.getBankList())
except IFSCWrapperException as es:
    print(es)

```
