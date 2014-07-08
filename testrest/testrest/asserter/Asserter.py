from testrest.asserter.AbstractAssert import AbstractAssert
'''
Module aggregating all general purpose Asserters

Created on Jun 30, 2014

@author: doerig
'''

class AssertIsGreater(AbstractAssert):
    '''
    classdocs
    '''
    logger = None
    _a = None

    doAssertArgs = {'b': AbstractAssert.JSONRESULT, 'msg': AbstractAssert.LITERAL}

    def __init__(self, a):
        '''
        Constructor
        '''
        super().__init__()
        self._a = a
        AssertIsGreater.logger.debug("AssertIsGreater: a " + str(self._a))

    def doAssert(self, b=None, msg=None):
        self.setStatusMessage("a = " + str(self._a) + "; b = " + str(b) )
        AssertIsGreater.logger.debug("doAssert: expr=" + str(b))
        try:
            self.assertGreater(self._a, b, msg)
            self.setSuccess(True)
        except AssertionError as error:
            AssertIsGreater.logger.error("Assertion failed: " + str(error))
            self.setSuccess(False)
        except Exception as error:
            AssertIsGreater.logger.error("Assertion failed: " + str(error))
            self.setSuccess(False)
            

    
    
            
class AssertIsNotNone(AbstractAssert):
    '''
    classdocs
    '''
    logger = None

    doAssertArgs = {'expr': AbstractAssert.JSONRESULT, 'msg': AbstractAssert.LITERAL}


    def __init__(self, *argv, **kv):
        '''
        Constructor
        '''
        super().__init__()

    def doAssert(self, expr=None, msg=None):
        self.setStatusMessage("expr = " + str(expr))
        AssertIsNotNone.logger.debug("doAssert called...")
        try:
            self.assertIsNotNone(expr, msg)
            self.setSuccess(True)
        except AssertionError as error:
            AssertIsNotNone.logger.error("Assertion failed: " + str(error))
            self.setSuccess(False)
            
class AssertTrue(AbstractAssert):
    '''
    classdocs
    '''
    logger = None

    doAssertArgs = {'expr': AbstractAssert.JSONRESULT, 'msg': AbstractAssert.LITERAL}

    def __init__(self, *argv, **kv):
        '''
        Constructor
        '''
        super().__init__()

    def doAssert(self, expr=None, msg=None):
        self.setStatusMessage("expr = " + str(expr))
        AssertTrue.logger.debug("doAssert: " + str(expr))
        try:
            self.assertTrue(expr, msg)
            self.setSuccess(True)
        except AssertionError as error:
            AssertTrue.logger.error("Assertion failed: " + str(error))
            self.setSuccess(False)
            
