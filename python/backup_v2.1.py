#!/usr/bin/env python
#coding: utf-8
#Filename: backup_v2.1

import os
import time

source = ['/home/zonek/test', '/home/zonek/projects']
target_dir = '/home/zonek/code'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
#target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)

#zip_command = 'zip -qr %s %s' % (target, " ".join(source))

comment = raw_input('请输入：')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
    zip_command = 'zip -qr %s %s' % (target, " ".join(source))
    if os.system(zip_command) == 0:
        print '备份成功：', target
    else:
        print '备份失败'
else:
    target = today + os.sep + now + '_' + comment + '.zip'
    zip_command = 'zip -qr %s %s' % (target, " ".join(source))
    if os.system(zip_command) == 0:
        print '备份成功：', target
    else:
        print '备份失败'
