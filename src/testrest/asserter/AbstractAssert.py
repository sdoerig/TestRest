__author__ = 'sdoerig@bluewin.ch'


#from unittest import TestCase
import unittest

class AbstractAssert(unittest.TestCase):
    '''
    classdocs
    '''
    _success = False

    def __init__(self):
        '''
        Constructor
        '''


    def doAssert(self):
        raise NotImplementedError("Subclasses should implement this!")

    def isSuccess(self):
        return self._success

    def setSuccess(self, isSuccess):
        if isSuccess:
            self._success = True
        else:
            self._success = False
