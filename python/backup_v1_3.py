#!/usr/bin/env python
#coding: utf-8
#Filename: backup_v1_3.py

import os
import time

source = ['/home/zonek/testa', '/home/zonek/testb']
target_dir = '/home/zonek/backup'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command):
    print '备份成功%s' % target
else:
    print '备份失败'