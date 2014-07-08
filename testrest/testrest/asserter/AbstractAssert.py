__author__ = 'sdoerig@bluewin.ch'


#from unittest import TestCase
import unittest

class AbstractAssert(unittest.TestCase):
    '''
    classdocs
    '''
    _success = False
    _status = ""
    # Argument is JSON
    JSONRESULT = 'JSONRESULT'
    # Use value literal
    LITERAL = 'LITERAL'

    def __init__(self):
        '''
        Constructor
        '''
        self._status = ""
    
    def getStatusMessage(self):
        return self._status
    
    def setStatusMessage(self, msg):
        self._status = msg

    def doAssert(self, expr, msg ):
        raise NotImplementedError("Subclasses should implement this!")

    def isSuccess(self):
        return self._success

    def setSuccess(self, isSuccess):
        if isSuccess:
            self._success = True
        else:
            self._success = False

    def getName(self):
        return str(self.__class__)