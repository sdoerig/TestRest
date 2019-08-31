'''
Created on May 25, 2014

@author: doerig
'''
import logging
import logging.config

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
        self._logger = None

    def getLogger(self, name):
        if (self._logger == None):
            logger = logging.getLogger(self._dict.get('name'))

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
            self._logger = logger

        return LoggerWrapper(name, self._logger)


class LoggerWrapper(object):
    """
    Wrapper class around the logger class. It's purpose is just to make
    it easy printing the class name of to instance using the LoggerWrapper.
    
    """

    _class = None

    def __init__(self, name, logger):
        self._class = name
        self._logger = logger

    def critical(self, msg):
        self._logger.critical(self._class + ": " + str(msg))

    def info(self, msg):
        self._logger.info(self._class + ": " + str(msg))

    def debug(self, msg):
        self._logger.debug(self._class + ": " + str(msg))

    def warning(self, msg):
        self._logger.warning(self._class + ": " + str(msg))

    def error(self, msg):
        self._logger.error(self._class + ": " + str(msg))
