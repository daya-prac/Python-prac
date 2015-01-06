#!/usr/bin/env python
#coding: utf-8
#Filename: inherit.py

class SchoolMember():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(初始化SchoolMember:%s)' % self.name

    def tell(self):
        print 'Name:"%s" Age:"%s"' % (self.name, self.age)

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary:"%d"' % self.salary

    def __del__(self):
        print '%s say bye' % self.name

class Student(SchoolMember):
    def __init__(self, name, age, mark):
        SchoolMember.__init__(self, name, age)
        self.mark = mark

    def tell(self):
        SchoolMember.tell(self)
        print 'Mark:"%d"' % self.mark

    def __del__(self):
        print '%s say bye' % self.name


t = Teacher('Mike', 25, 4000)
s = Student('Mali', 18, 98)

t.tell()
s.tell()

print

members = [t, s]
for member in members:
    member.tell()

