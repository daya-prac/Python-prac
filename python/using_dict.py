#!/usr/bin/env python
#coding: utf-8
#Filename: using_dict.py

ab = {
	'小明':'xiaoming@gmail.com',
	'小红':'xiaohong@hotmail.com',
	'小刚':'xiaogang@outlook.com'
}

print '小明的邮箱地址是：%s' % ab['小明']
if ab.has_key('小刚'):
	print '小刚的邮箱地址是：%s' % ab['小刚']