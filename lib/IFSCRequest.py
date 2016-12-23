"""Module to handle REST API requestes for this library"""

import requests

class IFSCRequests:

    def sendPost(self,uri,req_header=None):
        try:
            if req_header != None:
                responce = request.get(uri,header=req_header)
            else:
                responce = requests.get(uri)
                if responce.status_code == 200:
                    return [True,responce]
        except Exception as e:
            return [False,e]

    def sendGet(self,uri,req_header=None):
        try:
            if req_header != None:
                responce = request.get(uri,header=req_header)
            else:
                responce = requests.get(uri)
                if responce.status_code == 200:
                    return [True,responce]
                else: return[False,responce.status_code]
        except Exception as e:
            return [False,e]
