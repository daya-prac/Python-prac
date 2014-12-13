#!/usr/bin/env python
#coding: utf-8
#Filename: reference.py

shoplist = ['apple','mango','carrot','banana']
mylist = shoplist

del shoplist[0]
print shoplist
print mylist

mylist = shoplist[:]
del mylist[0]
print shoplist
print mylist
