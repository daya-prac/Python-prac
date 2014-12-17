#!/usr/bin/env python
#coding: utf-8
#Filename: backup_v2.0.py

import os
import time
source = [r'D:\back', r'D:\other\Screenshots']
target_dir = r'D:\code'
today = time.strftime('%Y%m%d')
target = target_dir + os.sep + today + time.strftime('%H%M%S') + '.zip'

