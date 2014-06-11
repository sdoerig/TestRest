'''
Created on Jun 10, 2014

'''
__author__ = 'sdoerig@bluewin.ch'

from testrest.authenticator.AbstractAuthenticator import AbstractAuthenticator
import base64


class BasicAuthenticator(AbstractAuthenticator):
    '''
    classdocs
    '''
    lh = None
    logger = None
    _username = None
    _password = None

    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        if (BasicAuthenticator.lh != None):
            BasicAuthenticator.logger = BasicAuthenticator.lh.getLogger(BasicAuthenticator.__name__)
        for attr in ('username', 'password'):
            if (kwargs.get(attr, None) == None):
                msg = self.__class__.__name__ + ": Property username is None - please set it in the config.yaml"
                BasicAuthenticator.logger.critical(msg)
                raise AttributeError(msg)
        self._username = kwargs.get('username')
        self._password = kwargs.get('password')
        BasicAuthenticator.logger.debug("Set username to: " + \
                                        self._username + \
                                        ' set password to: ' + \
                                        self._password)
        

    def getHeader(self):
        return "Authorization: Basic " + \
            base64.b64encode(str.encode(self._username)).decode("utf-8") + \
            base64.b64encode(b':').decode("utf-8") + \
            base64.b64encode(str.encode(self._password)).decode("utf-8")
            
        