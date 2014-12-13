#!/usr/bin/env python
#coding: utf-8
#Filename: reference.py
#记住列表的赋值语句不创建拷贝。你得使用切片操作符来建立序列的拷贝。

shoplist = ['apple','mango','carrot','banana']
mylist = shoplist

del shoplist[0]
print shoplist
print mylist

mylist = shoplist[:]
del mylist[0]
print shoplist
print mylist
