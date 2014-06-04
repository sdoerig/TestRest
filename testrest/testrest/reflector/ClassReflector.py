'''
Created on Jun 3, 2014

@author: doerig
'''

import importlib

class ClassReflector(object):
     
    lh = None
    logger = None    
    
    def __init__(self):
        if (ClassReflector.lh != None):
            ClassReflector.logger = ClassReflector.lh.getLogger(ClassReflector.__class__.__name__)
    
    def getInstance(self, moduleclass, *argv):
        moduleClassTokens = moduleclass.split('.')
        module = ".".join(moduleClassTokens[:-1])
        className = moduleClassTokens[-1]
        module = importlib.import_module(module)
        myClass = getattr(module, className)
        try:
            if (myClass.logger == None):
                myClass.logger = ClassReflector.lh.getLogger(myClass.__class__.__name__)
        except:
            ClassReflector.logger.warn("Class " + myClass.__class__.__name__ + " does not have a logger attribute...")
        return myClass(*argv)
