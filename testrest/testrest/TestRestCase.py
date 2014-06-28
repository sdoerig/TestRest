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
    Logical representation of one test case. Example config file:
    test:
        global:
            ..
        testCase1:
            ..
    In the configfile there is the section "test" any key in the next deeper 
    level is logically represented by an instance of this class. This applies 
    for anything on this level but "global". Note also any instance knows its 
    previous and its next test case - kind of double linked list.
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
    _regressData = None
    

    def __init__(self, previous, caseName, individualParams):
        '''
        Constructor
        '''
        JsonHandler.setLogHandler(TestRestCase.lh)
        self._caseName = caseName
        self._params = JsonHandler()
        self._params.set(individualParams)
        self._next = None
        self._regressData = {}
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
        #TestRestCase.logger.debug(self._caseName + ': assertions: ' + str(self._assertions))
        
            
        
    def runCase(self):
        self._prepareRegress()
        TestRestCase.logger.info('Running case ' + self._caseName + " method " + self._params.get('method'))
        self._apiClient.setMethod(self._params.get('method'))
        self._apiClient.setHeader(self._params.get('header'))
        self._apiClient.setHeader(self._authenticator.getHeaders())
        
        self._apiClient.setUrl(self._regressedSubstitution('url'))
        params = self._params.get('params')
        TestRestCase.logger.info(self._caseName + ": Params: " + str(params))
        self._apiClient.setParameters(**params)
        try:
            res = self._apiClient.doWork()
        except Exception as e:
            res  = None
            TestRestCase.logger.warning('Http client has thown an error: ' + str(e.args))
        TestRestCase.logger.debug("runCase: HTTP result: " + str(res))
        self._jsonResult.set(res)
        
        for ak in self._assertions:
            TestRestCase.logger.info(self._caseName + ": runCase: assertion key: " + ak)
            if (self._assertions[ak]['class'] != None):
                TestRestCase.logger.debug(self._caseName + ": runCase: assertion key: " + ak + ": class instantiated")
                for assertion in self._assertions[ak]['assertions']:
                    TestRestCase.logger.debug('asserter: checking expression: ' + 
                                              str(self._jsonResult.get(*assertion['expr'])))
                    self._assertions[ak]['class'].doAssert(self._jsonResult.get(*assertion['expr']), assertion['msg'])
                    TestRestCase.logger.info(self._caseName + ": assertion: success:  " + str(self._assertions[ak]['class'].isSuccess()))
            
    def _regressedSubstitution(self, *argv):
        """
        Substitutes anything - if possible with regressed data
        """
        print(str(self._regressData))
        param = str(self._params.get(*argv))
        if param == None:
            return ""
        for k in self._regressData.keys():
            param = param.replace(k, self._regressData[k])
        return param
        
    
    def _prepareRegress(self):
        regress = self._params.get('regress')
        if regress != None:
            # ok having regresss
            for k in regress.keys():
                TestRestCase.logger.debug("_prepareRegress: regress key: " + str(k))
                TestRestCase.logger.debug("_prepareRegress: regress path: " + str(regress[k]['path']))
                self._regressData[regress[k]['alias']] = str(self.getPreviousTestResult(k, *regress[k]['path']))
    
    def getNext(self):
        return self._next
        
    def getPrevious(self):
        return self._previous    
        
    def getPreviousTestResult(self, caseName, *argv):
        TestRestCase.logger.debug("getPreviousTestResult: my case name is: " + self._caseName)
        if caseName == self._caseName:
            for a in argv:
                TestRestCase.logger.debug("getPreviousTestResult: path value: " + str(a))
            TestRestCase.logger.debug("getPreviousTestResult: " + self._caseName + ": json result: " + str(self._jsonResult))
            TestRestCase.logger.debug("getPreviousTestResult: " + self._caseName + ": json returned: " + str(self._jsonResult.get(*argv)))
            return self._jsonResult.get(*argv)
        elif self._previous != None:
            return self._previous.getPreviousTestResult(caseName, *argv)
        
            
        
    def add(self, caseName, individualParams):
        self._next = TestRestCase(self, caseName, individualParams)
        return self._next
        
    def __str__(self, *args, **kwargs):
        TestRestCase.logger.debug('__str__ called')
        return str(self._caseName + " Params: " + str(self._params))