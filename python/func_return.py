#!/usr/bin/bash
#coding: utf-8
#Filename: func_return.py
def max(x,y):
	'''测试文档功能

	这个第二行，
	这个是第三行，
	vegeuidisihh.'''
	if x > y:
		return x
	if x < y:
		return y

print max(3,4)

def test():
	pass

print max.__doc__