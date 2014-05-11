'''
Created on May 11, 2014

'''

__author__ = 'sdoerig@bluewin.ch'

from testrest.handler import YamlHandler
from testrest.TestRestCase import TestRestCase

class TestRestManager():
    '''
    classdocs
    '''
    _configHandler = None
    _testCaseRoot = None

    def __init__(self, configFile):
        '''
        Constructor
        '''
        self._configHandler = YamlHandler.YamlHandler()
        self._configHandler.load(configFile)
        self._prepareTestRestCases()
        print(str(self._configHandler.get()))
        
    def _prepareTestRestCases(self):
        testCases = self._configHandler.get('test')
        testCasesKeys = list(testCases.keys())
        testCasesKeys.sort()
        globalTestCase = {}
        if 'global' in testCasesKeys:
            globalTestCase = testCases['global']
            testCasesKeys.remove('global')
        
        self._testCaseRoot = TestRestCase(testCasesKeys[0], \
                                          globalTestCase, \
                                          testCases[testCasesKeys[0]])
        testCasePtr = self._testCaseRoot
        for testCaseKey in testCasesKeys[1:]:
            testCasePtr = testCasePtr.add(testCaseKey, \
                                       globalTestCase, \
                                       testCases[testCaseKey])
            
    def iterateTestCases(self):
        tc = self._testCaseRoot
        while tc is not None:
            print(str(tc))
            tc = tc.getNext()
            