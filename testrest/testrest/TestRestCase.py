'''
Created on May 11, 2014

Testcases to work on. Note the testcases behave like a single linked 
list.

'''


from testrest.handler.JsonHandler import JsonHandler
from testrest.reflector.ClassReflector import ClassReflector
from testrest.apiclient.HttpClient import HttpClient
from unittest.case import TestCase


__author__ = 'sdoerig@bluewin.ch'






class TestRestCase(object):
    '''
    classdocs
    '''
    lh = None
    logger = None
    _next = None
    _previous = None
    _caseName = None
    _params = None
    _jsonResult = {}
    _classReflector = None
    _httpClient = None
    

    def __init__(self, previous, caseName, individualParams):
        '''
        Constructor
        '''
        JsonHandler.setLogHandler(TestRestCase.lh)
        self._caseName = caseName
        self._params = JsonHandler()
        self._params.set(individualParams)
        self._next = None
        self._apiClient = HttpClient() 
        self._jsonResult = JsonHandler()
        ClassReflector.lh = TestRestCase.lh
        self._classReflector = ClassReflector()
        TestRestCase.logger = TestRestCase.lh.getLogger(TestRestCase.__class__.__name__) 
        if isinstance(previous, TestRestCase):
            TestRestCase.logger.debug("Setting to Previous " +  previous._caseName)
            self._previous = previous
        else:
            self._previous = None
        
            
        
    def runCase(self):
        TestRestCase.logger.info('Running case ' + self._caseName + " method " + self._params.get('method'))
        self._apiClient.setMethod(self._params.get('method'))
    
    def getNext(self):
        return self._next
        
    def getPrevious(self):
        return self._previous    
        
    def getPreviousTestResult(self, caseName, *argv):
        if caseName == self._caseName:
            return self._jsonResult.get(argv)
        elif self._previous != None:
            return self._previous.getPreviousTestResult(caseName, argv)
        else: 
            return None
            
        
    def add(self, caseName, individualParams):
        self._next = TestRestCase(self, caseName, individualParams)
        return self._next
        
    def __str__(self, *args, **kwargs):
        TestRestCase.logger.debug('__str__ called')
        return str(self._caseName + " Params: " + str(self._params))