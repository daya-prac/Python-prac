#!/usr/bin/env python
#coding: utf-8
#Filename: try_except.py

import sys

try:
    s = raw_input('Enter something -->')
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit()
except:
    print '\nSome error/exception occured.'

print 'Done'