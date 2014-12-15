#!/usr/bin/env python
#coding: utf-8
#Filename: backop_v1_2.py

import os
import time

source = ['/home/zonek/test', '/home/zonek/projects']
target_dir = '/home/zonek/'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print '备份成功', target
else:
    print '备份失败'
