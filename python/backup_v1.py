#!/usr/bin/env python
#coding: utf-8
#Filename: backup_v1.py

import os
import time

source = ['/home/zonek/testa', '/home/zonek/testb']
target_dir = '/home/zonek/backup'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'Succeful backup to', target
else:
    print 'Backup failed'

