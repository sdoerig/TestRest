'''
Created on Jun 3, 2014

@author: doerig
'''

import importlib

class ClassReflector(object):
     
    
        
    
    def getInstance(self, module, classname, *argv):
        module = importlib.import_module(module)
        myClass = getattr(module, classname)
        print(str(argv))
        return myClass(*argv)
