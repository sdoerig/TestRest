from testrest.asserter.AbstractAssert import AbstractAssert

__author__ = 'sdoerig@bluewin.ch'





class AssertIsNotNone(AbstractAssert):
    '''
    classdocs
    '''
    logger = None

    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()

    def doAssert(self, expr, msg):
        AssertIsNotNone.logger.debug("doAssert called...")
        try:
            self.assertIsNotNone(expr, msg)
            self.setSuccess(True)
        except AssertionError as error:
            AssertIsNotNone.logger.error("Assertion failed: " + str(error))
            self.setSuccess(False)