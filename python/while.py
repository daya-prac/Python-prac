#!/usr/bin/python
#coding: utf-8
#Filename: while.py

run = True
number = 55

while run:
	guss = int(raw_input('输入一个数：'))
	if number == guss:
		print '对了' 
		run = False
	elif number > guss:
		print '小了'
	else:
		print '大了'

else:
	print '结束'