'''
Created on May 11, 2014

@author: doerig
'''
import yaml
from testrest.handler.JsonHandler import JsonHandler
class YamlHandler(JsonHandler):
    '''
    classdocs
    '''
    _yamlDict = {}
    _yamlFile = None

    def __init__(self):
        '''
        Constructor
        '''
        super().__init__()
        
    def load(self, file):
        self._yamlFile = file
        fileHandler = open(file,'r')
        self.set(yaml.load(fileHandler))
        fileHandler.close()
        
        
   
        
        
    
        
        