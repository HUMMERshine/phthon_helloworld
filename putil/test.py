#!/usr/bin/python
# encoding:utf-8

import os, sys


dir = sys.path[0]
print os.listdir(dir)

for name in os.listdir(dir):
    fileName = dir + os.path.sep + name
    if os.path.isfile(fileName):
        if len(name) > 4 and fileName[-4:] == '.txt':
            os.rename(fileName, fileName[:-4])

        

