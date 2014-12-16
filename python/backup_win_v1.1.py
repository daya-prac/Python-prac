#!/usr/bin/env python
#coding: utf-8
#Filename: backup_win_v1.1.py

import os
import time

source = [r'D:\back', r'D:\other\Screenshots']
target_dir = r'D:\code'
target = target_dir + '\\' + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr %s %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print '备份成功:', target
else:
    print '备份失败'