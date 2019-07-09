#!/bin/python

import os

directory = os.listdir('testdir')
print directory
IoC = 'li'
len(directory)

for file in directory:
    print file
    f = open(file,"r")
    for line in f:
        print line
        if (line.find('hel') != -1):
            print( "Uh oh, you found an IoC!!")
        else:
            print("Looks good in %s" % file)



 
