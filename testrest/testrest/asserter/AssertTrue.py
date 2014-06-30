from testrest.asserter.AbstractAssert import AbstractAssert

__author__ = 'sdoerig@bluewin.ch'





class AssertTrue(AbstractAssert):
    '''
    classdocs
    '''
    logger = None

    def __init__(self, *argv, **kv):
        '''
        Constructor
        '''
        super().__init__()

    def doAssert(self, expr, msg):
        AssertTrue.logger.debug("doAssert called...")
        try:
            self.assertTrue(expr, msg)
            self.setSuccess(True)
        except AssertionError as error:
            AssertTrue.logger.error("Assertion failed: " + str(error))
            self.setSuccess(False)