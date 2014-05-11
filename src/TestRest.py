import sys, getopt

#from testrest.asserter import AssertTrue
from testrest.TestRestManager import TestRestManager

__author__ = 'sdoerig@bluewin.ch'



def main():
    execName = sys.argv[0]
    argv = sys.argv[1:]
    configfile = None
    
    try:
        opts, args = getopt.getopt(argv,"hc:",["config="])
    except getopt.GetoptError:
        print (execName + " -c <inputfile> ")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print (execName + ' -c <inputfile>')
            sys.exit()
        elif opt in ("-c", "--config"):
            configfile = arg
    if configfile == None:
        print ("No configFile given. Usage: " + execName + " -c <inputfile> ")
        sys.exit(2)
    print ('Config file is "' + configfile)
    testRestManager = TestRestManager(configfile)
    testRestManager.iterateTestCases()
    #a = AssertTrue.AssertTrue()
    #a.doAssert()
    #print(a.isSuccess())


if __name__ == "__main__":
    main()