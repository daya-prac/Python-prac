#!/usr/bin/python
#coding: utf-8
#Filename: func_param.py

def printMax(x,y):
	if x > y:
		print x,'大于',y
	elif x < y:
		print x,'小于',y
	else:
		print '相等'


printMax(4,5)

x = 7
y = 8

printMax(x,y)