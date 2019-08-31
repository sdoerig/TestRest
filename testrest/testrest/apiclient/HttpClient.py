'''
Created on Jan 29, 2014

@author: doerig
'''
import json
import re
import urllib.parse
import urllib.request


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
            ptoken.append(key + "=" + urllib.parse.quote(str(val)))
        self.__parameterQS = '&'.join(ptoken)

    def setUrl(self, url):
        self.__baseUrl = url

    def setHeader(self, header):
        if type(header) is dict:
            self.__header.update(header)

    def setMethod(self, method):
        if method in ['GET', 'POST', 'DELETE', 'PUT']:
            self.__method = method

    def getUrlInMethodContext(self):
        if self.__method == "GET":
            return self.__baseUrl + "?" + self.__parameterQS
        else:
            return self.__baseUrl

    def doWork(self):
        print(self.getUrlInMethodContext())
        req = None
        if self.__method == "POST" or self.__method == "DELETE" or self.__method == "PUT":
            print(self.getUrlInMethodContext())
            req = urllib.request.Request(self.getUrlInMethodContext(), \
                                         json.dumps(self.__parameters).encode('utf_8'))
            req.get_method = lambda: self.__method
        else:
            req = urllib.request.Request(self.getUrlInMethodContext())

        for header, val in self.__header.items():
            req.add_header(header, val)
        resp = urllib.request.urlopen(req)
        raw_data = resp.read().decode('utf-8')

        # return raw_data
        raw_data = re.sub('^[a-zA-Z]+[^(]+\(', '', raw_data)
        raw_data = re.sub('\)$', '', raw_data)

        ret = {'header': self._dictifyHeader(resp.getheaders())}
        try:
            ret['body'] = json.loads(raw_data)
        except ValueError as e:
            ret['body'] = None
        return ret

    def _dictifyHeader(self, headers):
        """
        Getting the header from urllib in the form
        [('Date', 'Fri, 27 Jun 2014 14:26:30 GMT'), 
         ('Location', 'http://localhost:8080/contact/32'), 
         ('Content-Type', 'application/json'), 
         ('Connection', 'close')]
        Since using internaly JSON transform this to a valid JSON
        """
        ret = {}
        for tupel in headers:
            ret[tupel[0]] = tupel[1]
        return ret
