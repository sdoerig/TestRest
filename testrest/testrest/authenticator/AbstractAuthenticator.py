'''
Created on Jun 10, 2014
'''
__author__ = 'sdoerig@bluewin.ch'


class AbstractAuthenticator(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def getHeaders(self):
        """
        Must return a dict of HTTP headers.
        """
        raise NotImplementedError('Authenticator must implement getHeaders')
