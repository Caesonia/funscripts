#!/bin/python

import os

IoC = 'hel'
basedir = 'testdir'
for dirName, subdirList, fileList in os.walk(basedir):
    print("Now we will search %s" % dirName)
    for file in fileList:
        print('\t%s' % file)
        file_path = os.path.join(dirName,file)
        if os.path.isfile(file_path):
            f = open(file,"r")
            for line in f:
                print line
                if (line.find(IoC) != -1):
                    print( "Uh oh, you found an IoC!!")
                    i = open("IoCfound.txt","a+")
                    i.write("IoC found in %s\n" % file)
                    i.close()
                else:
                    print("Looks good so far in %s" % file)
        else:
            print("This cannot be something you see!")


 
