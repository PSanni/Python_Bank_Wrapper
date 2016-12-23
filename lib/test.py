from IFSCWrapper import Wrapper
from IFSCException import IFSCWrapperException

obj=Wrapper()
try:
    obj.init()
    print(obj.getBankList())
except IFSCWrapperException as es:
    print(es)
