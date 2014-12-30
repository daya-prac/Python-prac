#!/usr/bin/env python
#coding: utf-8
#Filename: objvar.py

class Persion:
    population = 0

    def __init__(self, name):
        self.name = name
        print '正在初始化：%s' % self.name

        Persion.population += 1

    def __del__(self):
        print '%s say bye.' % self.name

        Persion.population -= 1

        if Persion.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people.' % Persion.population

    def sayHi(self):
        print 'Hi, my name is %s ' % self.name

    def howMany(self):
        if Persion.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persion here.' % Persion.population

xiaoming = Persion('小明')
xiaoming.sayHi()
xiaoming.howMany()

xchs = Persion('小红')
xchs.sayHi()
xchs.howMany()
