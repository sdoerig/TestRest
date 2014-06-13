'''
Created on Jan 29, 2014

@author: doerig
'''
import json

import urllib.request
import urllib.parse
import re

class HttpClient(object):
    '''
    classdocs
    '''
    __url = None
    __baseUrl = None
    
    __parameters = {}
    __header = {}
    __parameterQS = ""
    
    __method = 'GET'
    def __init__(self):
        '''
        Constructor
        '''
        self.__parameters = {}
        self.__header = {}
    
    def setParameters(self, **parameters):
        self.__parameters = parameters
        print("setParameters: " + str(self.__parameters))
        ptoken = []
        for key, val in parameters.items():
            ptoken.append( key + "=" + urllib.parse.quote(str(val)) )
        self.__parameterQS = '&'.join(ptoken)
       
    def setUrl(self, url):
        self.__baseUrl = url
    
    def setHeader(self, header):
        if type(header) is dict:
            self.__header.update(header)
    
    def setMethod(self, method):
        if method == 'GET' or method == 'POST' or method == 'DELETE':
            self.__method = method 
    
    def getUrlInMethodContext(self):
        if self.__method == "GET":
            return self.__baseUrl + "?" + self.__parameterQS
        else:
            return self.__baseUrl
    
    def doWork(self):
        print (self.getUrlInMethodContext())
        req = None
        if self.__method == "POST" or self.__method == "DELETE":
            print (self.getUrlInMethodContext())
            req = urllib.request.Request(self.getUrlInMethodContext(), self.__parameters)
            req.get_method = lambda: self.__method
        else:
            req = urllib.request.Request(self.getUrlInMethodContext())
        print('#######' + str(self.__header))
        for header, val in self.__header.items():
            req.add_header(header, val)
        resp = urllib.request.urlopen(req)
        raw_data = resp.read().decode('utf-8')
        print(raw_data)
        
        #return raw_data
        raw_data = re.sub('^[a-zA-Z]+[^(]+\(', '', raw_data)
        raw_data = re.sub('\)$', '', raw_data)
        
        return json.loads(raw_data)
        