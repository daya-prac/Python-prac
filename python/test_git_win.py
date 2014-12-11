#!/usr/bin/python
#coding: utf-8
#Filename: using_list.py
shoplist = ['苹果','芒果','萝卜','香蕉']

print '我有一个长度为',len(shoplist),'的购物列表'
print '列表里面的内容为：'
for item in shoplist:
	print item,

print ''
shoplist.append('大米')

#print '[',shoplist[0],',',shoplist[1],',',shoplist[2],',',shoplist[3],',',shoplist[4],']'

def myPrint():
	i = 0
	while i < len(shoplist):
		print shoplist[i],
		i = i + 1	

print '加了一个大米后列表变为：',
myPrint()
shoplist.sort()

print ''

print '排序后列表变为：',
myPrint()

print ''
print '要买的第一个东西是：',shoplist[0]
oldtem = shoplist[0]
del shoplist[0]
print '我已经买了：',oldtem
print '现在还要买：',
myPrint()