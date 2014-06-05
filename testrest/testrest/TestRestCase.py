'''
Created on May 11, 2014

Testcases to work on. Note the testcases behave like a double linked 
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
    _assertions = {}

    def __init__(self, previous, caseName, individualParams):
        '''
        Constructor
        '''
        print("IND PARAMS: " + str(individualParams))
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
        configuredAssertions = self._params.get('assertions')
        TestRestCase.logger.debug(self._caseName +": Configured assertions: " + str(configuredAssertions))
        for ak in configuredAssertions:
            TestRestCase.logger.debug('Adding assertion key: ' + ak)
            if (self._assertions.get(ak, None) == None):
                self._assertions[ak] = {'instance': self._classReflector.getInstance(ak), 
                                        'assertions': []}
            TestRestCase.logger.debug(self._caseName + ': Appending to: ' + ak + " " + str(configuredAssertions[ak]))
            self._assertions[ak]['assertions'].append(configuredAssertions[ak])
        if isinstance(previous, TestRestCase):
            TestRestCase.logger.debug("Setting to Previous " +  previous._caseName)
            self._previous = previous
        else:
            self._previous = None
        
            
        
    def runCase(self):
        TestRestCase.logger.info('Running case ' + self._caseName + " method " + self._params.get('method'))
        self._apiClient.setMethod(self._params.get('method'))
        for ak in self._assertions:
            TestRestCase.logger.debug("runCase: looping in: " + ak)
            if (self._assertions[ak]['instance'] != None):
                # if having an instance - ok let's check
                print(self._assertions[ak]['assertions'])
                for assertion in self._assertions[ak]['assertions']:
                    self._assertions[ak]['instance'].doAssert(self._jsonResult.get(*assertion['expr']), assertion['msg'])
            
        
    
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