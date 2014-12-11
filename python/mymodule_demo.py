#!/usr/bin/python
#coding: utf-8
#Filename: mymodule_demo.py
import mymodule

mymodule.sayHi()

print 'Version',mymodule.version
print mymodule.__builtins__,mymodule.__doc__,mymodule.__name__,mymodule.__package__