'''
Created on May 11, 2014

'''

__author__ = 'sdoerig@bluewin.ch'



from testrest.handler import YamlHandler
from testrest.TestRestCase import TestRestCase

from testrest.logger.LogHandler import LogHandler




class TestRestManager(object):
    '''
    classdocs
    '''
    lh = None
    logger = None
    _configHandler = None
    _testCaseRoot = None
    

    def __init__(self, configFile):
        '''
        Constructor
        '''      
        self._configHandler = YamlHandler.YamlHandler()
        
        self._configHandler.load(configFile)
        TestRestManager.lh = LogHandler(self._configHandler.get('logger'))
        TestRestCase.lh = TestRestManager.lh
        YamlHandler.YamlHandler.setLogHandler(TestRestManager.lh)
        TestRestManager.logger = TestRestManager.lh.getLogger("Hammer")
        
        self._prepareTestRestCases()
        
    def _prepareTestRestCases(self):
        #cl = ClassReflector()
        #lh = cl.getInstance('testrest.logger.LogHandler.LogHandler', self._configHandler.get('logger'))
        
        #logger.info('Hellos')
        #logger.error('Error')
        testCases = self._configHandler.get('test')
        testCasesKeys = list(testCases.keys())
        testCasesKeys.sort()
        globalTestCase = {}
        if 'global' in testCasesKeys:
            globalTestCase = testCases['global']
            testCasesKeys.remove('global')
        
        self._testCaseRoot = TestRestCase(None, testCasesKeys[0], \
                                          testCases[testCasesKeys[0]])
        testCasePtr = self._testCaseRoot
        for testCaseKey in testCasesKeys[1:]:
            testCasePtr = testCasePtr.add(testCaseKey, \
                                          testCases[testCaseKey])
            
    def iterateTestCases(self):
        tc = self._testCaseRoot
        while tc is not None:
            tc.runCase()
            tc = tc.getNext()
      
    def generateReport(self):
        if self._testCaseRoot != None:
            return self._testCaseRoot.generateReport()        
    def __str__(self):
        return str(self._testCaseRoot)
            