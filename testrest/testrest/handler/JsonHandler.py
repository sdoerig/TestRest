'''
Created on May 11, 2014

@author: doerig
'''

import json


class JsonHandler(object):
    '''
    classdocs
    '''
    lh = None
    logger = None
    loggerFP = None
    _jsonDict = None;

    def __init__(self):
        '''
        Constructor
        '''
        if (JsonHandler.loggerFP == None):
            JsonHandler.loggerFP = JsonHandler.logSTDOUT
        self._jsonDict = {}

    def setLogHandler(lh):
        if (JsonHandler.lh == None):
            JsonHandler.lh = lh
        if ((JsonHandler.logger == None) and (JsonHandler.lh != None)):
            JsonHandler.logger = JsonHandler.lh.getLogger(JsonHandler.__name__)
            JsonHandler.loggerFP = JsonHandler.log

    def set(self, dict):
        self._jsonDict = dict

    def get(self, *argv):
        """
        Returns a part of the loaded dictionary. 
        Parameter
        - argv - Path to a dictionaray element.
              given {'a': {'a1': 'a1value'}}
              get('a', 'a1') would return 'a1value' where as
              get('a') would return {'a1': 'a1value'}
        """
        if self._jsonDict == None:
            return None
        jsonPtr = self._jsonDict
        for keyToken in argv:
            if keyToken in jsonPtr:
                JsonHandler.loggerFP('DEBUG', "Setting jsonPtr" + keyToken)
                jsonPtr = jsonPtr[keyToken]
            else:
                # out of any sequence 
                jsonPtr = None
                break
        return jsonPtr

    def logSTDOUT(level, msg):
        print(level + "" + msg)

    def log(level, msg):
        if (level == "DEBUG"):
            JsonHandler.logger.debug(msg)

    def __str__(self):
        return str(json.dumps(self._jsonDict, sort_keys=True, indent=4, separators=(',', ': ')))
