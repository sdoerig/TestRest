'''
Created on May 11, 2014

Testcases to work on. Note the testcases behave like a single linked 
list.

'''

__author__ = 'sdoerig@bluewin.ch'






class TestRestCase(object):
    '''
    classdocs
    '''
    _next = None
    _caseName = None
    _params = None
    _global = None
    

    def __init__(self, caseName, globalParams, individualParams):
        '''
        Constructor
        '''
        self._caseName = caseName
        self._global = globalParams
        self._params = individualParams
        self._next = None
    
    
    def getNext(self):
        return self._next
        
    def add(self, caseName, globalParams, individualParams):
        self._next = TestRestCase(caseName, globalParams, individualParams)
        return self._next
        
    def __str__(self, *args, **kwargs):
        return str(self._caseName + " Params: " + str(self._params))