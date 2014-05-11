from testrest.asserter.AbstractAssert import AbstractAssert

__author__ = 'sdoerig@bluewin.ch'





class AssertTrue(AbstractAssert):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()

    def doAssert(self):
        try:
            self.assertTrue(1, "ssss")
            self.setSuccess(True)
        except AssertionError as error:
            self.setSuccess(False)