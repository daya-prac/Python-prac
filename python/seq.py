#!/usr/bin/env python
#coding: utf-8
#Filename: seq.py

shoplist0 = ['苹果','芒果','萝卜','香蕉']
shoplist1 = ['apple','mango','carrot','banana']

print '第一个是：',shoplist0[0]
print '第二个是：',shoplist0[1]
print '第三个是：',shoplist0[2]
print '第四个是：',shoplist0[3]
print '倒数第一个是：',shoplist0[-1]
print '倒数第二个是：',shoplist0[-2]

print '1 to 3 :',shoplist1[1:3]    #无法支持中文
print '2 to end :',shoplist1[2:]
print '1 to -1 :',shoplist1[1:-1]
print 'start to end :',shoplist1[:]

name = 'helloworld'
print '1 to 3',name[1:3]
print '2 to end',name[2:]
print '1 to -1',name[1:-1]
print 'start to end',name[:]

hehe = '你是我的小呀小苹果'    #也不是按照中文来计算第几个的
print '第一个到第四个是：',hehe[0:12]
print '第二个到最后一个是：',hehe[3:]
print '第二个到倒数第二个是：',hehe[3:-6]
print '开始到最后是：',hehe[:]
