#-*- coding:utf-8 -*-
"""Main wrapper module for API's

This module works as wrapper class for REST API's, API URI used in class are extracted here from
Uris.config file.

Example:
    obj_W = Wrapper()
    obj_W.getBankList()

Attributes:

    Wrappe class: to wrap up API'S using functions.
"""

from IFSCException import IFSCWrapperException
import csv
from os.path import exists
from IFSCRequest import IFSCRequests
import json

class Wrapper:


    _Uris={}
    _ifsc_req = IFSCRequests()

    def init(self):
        self._readConfig()

    def _readConfig(self):

        """ Private: function to read the configuration file.
            Raise: Exception if file not found on given path
        """

        if exists('Uri.conf') == False:
            raise IFSCWrapperException('Unable to read configuration file')

        with open('Uri.conf','r')as reader:
            csv_reader = csv.reader(reader,delimiter=",")

            for row in csv_reader:
                if len(row) == 0:
                    continue
                self._Uris[row[1]]=[str(row[0]),str(row[2]),str(row[3]),str(row[4])]

    def getBankList(self):
        """Get supported bank list
        if_fail: Returns IFSCWrapperException.
        Returns: List of bankes in python list()
        """

        Uri = self._Uris["G_BL"]
        responce = self._ifsc_req.sendGet(Uri[1])
        if responce[0] == False:
            raise IFSCWrapperException(responce[1])
        data = json.loads(responce[1].text)
        if data['status'] == 'failed':
            raise IFSCWrapperException(data['message'])
        return list(data["data"])


    def getBranch_by_Bank(self,bank_name):
        """ Get branch list by bank name
        Arguments:
            bank_name: Bank name to get associated branches
        Returns: List of branches in python list()
        """
        Uri = self._Uris["G_BRL_BN"]
        responce = self._ifsc_req.sendGet(Uri[1].format(bank_name))
        if responce[0] == False:
            raise IFSCWrapperException(responce[1])
        data = json.loads(responce[1].text)
        if data['status'] == 'failed':
            raise IFSCWrapperException(data['message'])
        return list(data["data"])


    def getBranchDetails_by_Bank_Branch(self,bank_name,branch_name):
        Uri = self._Uris["G_BRD_BN_BRN"]
        responce = self._ifsc_req.sendGet(Uri[1].format(bank_name,branch_name))
        if responce[0] == False:
            raise IFSCWrapperException(responce[1])
        data = json.loads(responce[1].text)
        if data['status'] == 'failed':
            raise IFSCWrapperException(data['message'])
        return dict(data["data"])

    def getbank_IFSC(self,IFSC_code):
        Uri = self._Uris["G_BN_IFSC"]
        responce = self._ifsc_req.sendGet(Uri[1].format(IFSC_code))
        if responce[0] == False:
            raise IFSCWrapperException(responce[1])
        data = json.loads(responce[1].text)
        if data['status'] == 'failed':
            raise IFSCWrapperException(data['message'])
        return dict(data["data"])

    def getbank_MICR(self,MICR_code):
        Uri = self._Uris["G_BN_MICR"]
        responce = self._ifsc_req.sendGet(Uri[1].format(MICR_code))
        if responce[0] == False:
            raise IFSCWrapperException(responce[1])
        data = json.loads(responce[1].text)
        if data['status'] == 'failed':
            raise IFSCWrapperException(data['message'])
        return dict(data["data"])

    def getbank_Location(self,branch_location):
        Uri = self._Uris["G_BN_BRL"]
        responce = self._ifsc_req.sendGet(Uri[1].format(branch_location))

        if responce[0] == False:
            raise IFSCWrapperException(responce[1])
        data = json.loads(responce[1].text)
        #if data['status'] == 'failed':
        #    raise IFSCWrapperException(data['message'])
        return list[data]

    def getBankList_District(self,district_name):
        Uri = self._Uris["G_BNL_District"]
        responce = self._ifsc_req.sendGet(Uri[1].format(district_name))
        if responce[0] == False:
            raise IFSCWrapperException(responce[1])
        data = json.loads(responce[1].text)
        if data['status'] == 'failed':
            raise IFSCWrapperException(data['message'])
        return list(data["data"])

    def getBankList_State(self,state_name):
        Uri = self._Uris["G_BNL_State"]
        responce = self._ifsc_req.sendGet(Uri[1].format(state_name))
        if responce[0] == False:
            raise IFSCWrapperException(responce[1])
        data = json.loads(responce[1].text)
        if data['status'] == 'failed':
            raise IFSCWrapperException(data['message'])
        return list(data["data"])
