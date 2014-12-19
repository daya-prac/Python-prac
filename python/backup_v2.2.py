#!/usr/bin/env python
#coding: utf-8
#Filename: backup_v2.2.py  win

import os
import time

source = [r'D:\back', r'D:\other\Screenshots']
target_dir = r'D:\code'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
if not os.path.exists(today):
    os.mkdir(today)
    print '新建了目录：%s' % today
comment = raw_input('请输入：').decode('gbk')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + comment.replace(' ', '_').encode('gbk') + \
        now + '.zip'

zip_command = 'zip -qr %s %s' % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print '备份成功', target
else:
    print '备份失败'
