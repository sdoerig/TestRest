'''
Created on May 11, 2014

Testcases to work on. Note the testcases behave like a single linked 
list.

'''
from testrest.handler.JsonHandler import JsonHandler

__author__ = 'sdoerig@bluewin.ch'






class TestRestCase(object):
    '''
    classdocs
    '''
    _next = None
    _previous = None
    _caseName = None
    _params = None
    _global = None
    _jsonResult = {}
    

    def __init__(self, previous, caseName, globalParams, individualParams):
        '''
        Constructor
        '''
        self._caseName = caseName
        self._global = globalParams
        self._params = individualParams
        self._next = None
        self._jsonResult = JsonHandler()
        if isinstance(previous, TestRestCase):
            print("Setting to Previous" +  previous._caseName)
            self._previous = previous
        else:
            self._previous = None
    
    
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
            
        
    def add(self, caseName, globalParams, individualParams):
        self._next = TestRestCase(self, caseName, globalParams, individualParams)
        return self._next
        
    def __str__(self, *args, **kwargs):
        return str(self._caseName + " Params: " + str(self._params))