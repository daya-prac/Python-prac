#!/usr/bin/python
#coding: utf-8
#Filename: using_sys.py

import sys

print 'The command line arguments are:'
for i in sys.argv:
	print i

print '\n\npythonpath的路径为：',sys.path,'\n'