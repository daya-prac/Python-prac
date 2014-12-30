#!/usr/bin/env python
#coding: utf-8
#Filename: class_init.py

class Persion:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print 'Hello, how are you', self.name

p = Persion('Petter')
p.sayHi()