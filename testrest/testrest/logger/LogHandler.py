'''
Created on May 25, 2014

@author: doerig
'''
import logging, logging.config, os, shutil
from testrest.handler.JsonHandler import JsonHandler


class LogHandler(object):
    '''
    classdocs
    '''
    _dict = None
    
    
    
    
    def __init__(self, dict):
        '''
        Constructor
        '''
        self._dict = JsonHandler()
        self._dict.set(dict)
        
        
    def getLogger(self, name):
        logger = logging.getLogger(self._dict.get('name') + ' ' + name)
        
        # Not checking for any error - if the user configured a 
        # inexistent level option the program must die        
        logger.setLevel(getattr(logging, self._dict.get('fileloglevel')))
        # create file handler which logs even debug messages
        fh = logging.FileHandler(self._dict.get('file'))
        fh.setLevel(getattr(logging, self._dict.get('fileloglevel')))
        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(getattr(logging, self._dict.get('consoleloglevel')))
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # add the handlers to logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger
        