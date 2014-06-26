'''
Created on May 11, 2014

Testcases to work on. Note the testcases behave like a double linked 
list.

'''


from testrest.handler.JsonHandler import JsonHandler
from testrest.reflector.ClassReflector import ClassReflector
from testrest.apiclient.HttpClient import HttpClient


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
    _jsonResult = None
    _classReflector = None
    _httpClient = None
    _assertions = None
    _authenticator = None
    

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
        TestRestCase.logger = TestRestCase.lh.getLogger(TestRestCase.__name__) 
        self._authenticator = self._classReflector.getInstance(self._params.get('authenticator', 'class'), 
                                                           **self._params.get('authenticator', 'params'))
        configuredAssertions = self._params.get('assertions')
        TestRestCase.logger.debug(self._caseName +": Configured assertions: " + str(configuredAssertions))
        self._assertions = {}
        
        for ak in configuredAssertions:
            TestRestCase.logger.debug(self._caseName + ': Adding assertion key: ' + ak)
            if (self._assertions.get(ak, None) == None):
                self._assertions[ak] = {'class': self._classReflector.getInstance(configuredAssertions[ak]['class']), 
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
        self._apiClient.setHeader(self._params.get('header'))
        self._apiClient.setHeader(self._authenticator.getHeaders())
        self._apiClient.setUrl(self._params.get('url'))
        params = self._params.get('params')
        TestRestCase.logger.info(self._caseName + ": Params: " + str(params))
        self._apiClient.setParameters(**params)
        try:
            res = self._apiClient.doWork()
        except Exception as e:
            res = None
            TestRestCase.logger.warning('Http client has thown an error: ' + str(e.args))
        self._jsonResult.set(res)
        for ak in self._assertions:
            TestRestCase.logger.info(self._caseName + ": runCase: assertion key: " + ak)
            if (self._assertions[ak]['class'] != None):
                # if having an instance - ok let's check
                for assertion in self._assertions[ak]['assertions']:
                    self._assertions[ak]['class'].doAssert(self._jsonResult.get(*assertion['expr']), assertion['msg'])
            
        
    
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