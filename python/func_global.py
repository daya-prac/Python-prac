#!/usr/bin/python
#coding: utf-8
#Filename: func_global.py


def testGlobal():
	global x
	print x

	x = 2
	print '更改后x的值为',x

x = 50
testGlobal()
print 'x的值是：',x