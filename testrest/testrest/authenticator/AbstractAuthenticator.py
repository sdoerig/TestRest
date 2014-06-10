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
        
    def getHeader(self):
        raise NotImplementedError('Authenticator must implement getHeader')