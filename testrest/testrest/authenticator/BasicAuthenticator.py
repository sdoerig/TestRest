'''
Created on Jun 10, 2014

'''
__author__ = 'sdoerig@bluewin.ch'

import base64

from testrest.authenticator.AbstractAuthenticator import AbstractAuthenticator


class BasicAuthenticator(AbstractAuthenticator):
    '''
    classdocs
    '''
    lh = None
    logger = None
    _username = None
    _password = None
    _usertoken = None

    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        if (BasicAuthenticator.lh != None):
            BasicAuthenticator.logger = BasicAuthenticator.lh.getLogger(BasicAuthenticator.__name__)
        for attr in ('username', 'password'):
            if (kwargs.get(attr, None) == None):
                msg = self.__class__.__name__ + ": Property " + attr + " is None - please set it in the config.yaml"
                BasicAuthenticator.logger.critical(msg)
                raise AttributeError(msg)
        self._username = kwargs.get('username')
        self._password = kwargs.get('password')
        self._usertoken = str(self._username) + ":" + str(self._password)
        BasicAuthenticator.logger.debug("Set username to: " + \
                                        self._username + \
                                        ' set password to: ' + \
                                        self._password)

    def getHeaders(self):
        return {"Authorization": "Basic " + \
                                 base64.b64encode(str.encode(self._usertoken)).decode("utf-8")}
