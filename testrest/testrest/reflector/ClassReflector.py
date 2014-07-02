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
            ClassReflector.logger = ClassReflector.lh.getLogger(ClassReflector.__name__)
    
    def getInstance(self, moduleclass, *argv, **kwargs):
        myClass = self.getInstancableClass(moduleclass, *argv, **kwargs)
        try:
            if (myClass.logger == None):
                myClass.logger = ClassReflector.lh.getLogger(myClass.__name__)
        except:
            ClassReflector.logger.warn("Class " + myClass.__name__ + " does not have a logger attribute...")
        return myClass(*argv, **kwargs)
        
    def getInstancableClass(self,  moduleclass, *argv, **kwargs):
        moduleClassTokens = moduleclass.split('.')
        module = ".".join(moduleClassTokens[:-1])
        className = moduleClassTokens[-1]
        ClassReflector.logger.debug("module: " + module)
        ClassReflector.logger.debug("className: " + className)
        try:
            module = importlib.import_module(module)
            myClass = getattr(module, className)
            return myClass
        except ImportError as err:
            ClassReflector.logger.error('Package could not be found: ' + moduleclass)
            return None
        except AttributeError as err:
            ClassReflector.logger.error('Module could not be found: ' + className)
            return None