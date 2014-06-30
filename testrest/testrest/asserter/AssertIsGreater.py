from testrest.asserter.AbstractAssert import AbstractAssert
'''
Created on Jun 30, 2014

@author: doerig
'''

class AssertIsGreater(AbstractAssert):
    '''
    classdocs
    '''
    logger = None
    _a = None

    def __init__(self, a):
        '''
        Constructor
        '''
        super().__init__()
        self._a = a
        AssertIsGreater.logger.debug("AssertIsGreater: a " + str(self._a))

    def doAssert(self, expr, msg):
        AssertIsGreater.logger.debug("doAssert called...")
        try:
            self.assertGreater(self._a, expr, msg)
            self.setSuccess(True)
        except AssertionError as error:
            AssertIsGreater.logger.error("Assertion failed: " + str(error))
            self.setSuccess(False)
        except Exception as error:
            AssertIsGreater.logger.error("Assertion failed: " + str(error))
            self.setSuccess(False)