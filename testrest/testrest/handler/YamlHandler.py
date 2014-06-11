'''
Created on May 11, 2014

'''

__author__ = 'sdoerig@bluewin.ch'

import yaml
from testrest.handler.JsonHandler import JsonHandler
class YamlHandler(JsonHandler):
    '''
    classdocs
    '''
    lh = None
    logger = None
    
    _yamlDict = {}
    _yamlFile = None

    def setLogHandler(lh):
        if (YamlHandler.lh == None):
            YamlHandler.lh = lh
        if (YamlHandler.logger == None):
            YamlHandler.lh.getLogger(YamlHandler.__name__) 

    def __init__(self):
        '''
        Constructor
        '''
        JsonHandler.setLogHandler(YamlHandler.lh)
        super().__init__()
        
    def load(self, file):
        self._yamlFile = file
        fileHandler = open(file,'r')
        self.set(yaml.load(fileHandler))
        
        fileHandler.close()
        
        
   
        
        
    
        
        