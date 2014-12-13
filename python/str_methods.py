#!/usr/bin/env python
#coding: utf-8
#Filename: str_methods.py

name = 'microzonek'

if name.startswith('mic'):
    print 'Yes! is you!'


if 'z' in name:
    print '\na在你的名字里'


if name.find('zonek') != -1:
    print '\n你的名字里含有zonek'
    print name.find('zonek')


delimiter = '_*_'
list = ['apple','mango','carrot','banana']
print delimiter.join(list)
