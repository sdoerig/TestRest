'''
Created on May 11, 2014

@author: doerig
'''

class JsonHandler(object):
    '''
    classdocs
    '''
    _jsonDict = None;

    def __init__(self):
        '''
        Constructor
        '''
    
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
            print (keyToken)
            if keyToken in jsonPtr:
                print ("Setting" + keyToken)
                jsonPtr = jsonPtr[keyToken]
            else:
                # out of any sequence 
                jsonPtr = None  
                break
        return jsonPtr