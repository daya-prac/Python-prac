#! /usr/bin/env python
#coding: utf-8 
#Filename: using_tuple.py
import types
def myPrint(tuple):
	for item in tuple:
		if type(item) == type(zoo):
			for i in item:
				print i,
		else:
			print item,
zoo = ('鸭子','天鹅','凤凰')

print 'zoo元组里有',len(zoo),'只动物'

new_zoo = ('猪','牛',zoo)
print '新元组里包含动物的数量为：',len(new_zoo)
print '新元组里的动物是：',myPrint(new_zoo)

