#!/bin/python

import os

IoC = 'hel'
basedir = 'testdir'
for dirName, subdirList, fileList in os.walk(basedir):
    print("Now we will search %s" % dirName)
    for file in fileList:
        print('\t%s' % file)
        f = open(file,"r")
        for line in f:
            print line
            if (line.find(IoC) != -1):
                print( "Uh oh, you found an IoC!!")
                i = open("IoCfound.txt","a+")
                i.write("IoC find in %s\n" % file)
                i.close()
            else:
                print("Looks good so far in %s" % file)



 
