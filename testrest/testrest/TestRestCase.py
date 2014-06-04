'''
Created on May 11, 2014

Testcases to work on. Note the testcases behave like a single linked 
list.

'''


from testrest.handler.JsonHandler import JsonHandler
from testrest.reflector.ClassReflector import ClassReflector

__author__ = 'sdoerig@bluewin.ch'






class TestRestCase(object):
    '''
    classdocs
    '''
    lh = None
    _next = None
    _previous = None
    _caseName = None
    _params = None
    _jsonResult = {}
    _classReflector = None
    

    def __init__(self, previous, caseName, individualParams):
        '''
        Constructor
        '''
        self._caseName = caseName
        self._params = JsonHandler()
        self._params.set(individualParams)
        self._next = None
        self._jsonResult = JsonHandler()
        ClassReflector.lh = TestRestCase.lh
        self._classReflector = ClassReflector()
        if isinstance(previous, TestRestCase):
            print("Setting to Previous" +  previous._caseName)
            self._previous = previous
        else:
            self._previous = None
        
            TestRestCase.logger = TestRestCase.lh.getLogger(TestRestCase.__class__.__name__) 
        
    def setLogHandler(self, lh):
        self._lh = lh
        self._logger = lh.getLogger(TestRestCase.__class__.__name__) 
    
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