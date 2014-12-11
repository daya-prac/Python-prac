#!/usr/bin/python
#coding: utf-8
#Filename: break.py

while True:
	s = raw_input('请输入：')
	if s == '离开':
		print '结束'
		break
	print len(s)

else:
	print '啊哈'