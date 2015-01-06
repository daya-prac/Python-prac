#!/usr/bin/env python
#coding: utf-8
#Filename: pickling.py

import cPickle as p

shoplist = ['apple', 'mango', 'banana']
txt = 'shoplist.txt'
f = file(txt, 'w')
p.dump(shoplist, f)
f.close()

del shoplist
f = file(txt)
storedlist = p.load(f)
print storedlist