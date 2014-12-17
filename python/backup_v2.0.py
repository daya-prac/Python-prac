#!/usr/bin/env python
#coding: utf-8
#Filename: backup_v2.0.py

import os
import time
#source = [r'D:\back', r'D:\other\Screenshots']
source = ['/home/zonek/test', '/home/zonek/projects']
#target_dir = r'D:\code'
target_dir = '/home/zonek/code/'
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print '创建了目录：', today

zip_command = 'zip -qr %s %s' % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print '备份成功：', target
else:
    print '备份失败'