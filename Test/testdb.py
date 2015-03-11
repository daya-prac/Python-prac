#!/usr/bin/env python
# coding: utf-8
# Filename: testdb.py

import MySQLdb
import os
import re
import sys

target_url = 'find.flyme.cn'       # 待检测网址
ping_command = 'ping -c 1 -n %s > /tmp/testping.txt' % target_url
del_pingfile = 'rm -rf /tmp/testping.txt'
os.system(ping_command)
f = file('/tmp/testping.txt')       # 将ping的结果存入f中
line = f.readline()         # 将f中的第一行存入line中
pattern = re.compile(r'.*\d+')          # 判断line中是否含有数字
boo = pattern.match(line)
if ( boo == None ):
    print 'ping %s 失败，没有接收到ip' % target_url         # 如果不含有数字则ping失败
    sys.exit()                                           # 退出程序
os.system(del_pingfile)
line_split = line.split(" ")
ip_kuohao = line_split[2]
ping_ip = ip_kuohao.strip("(").rstrip(")")
print 'ping %s 得到的ip为: %s' % (target_url,  ping_ip)        # ping出来的ip
print ''


data_url = target_url.split(".")
table_url = data_url[1]
for i in range(2, len(data_url)):
    table_url += "_" + data_url[i]
print '如果%s已存在数据库中则所在的表的名称应该为：%s' % (target_url, table_url)        # 从输入的url里获取到数据库表里所存的表名
print ''

conn = MySQLdb.connect(host="127.0.0.1", user="webtest", passwd="webtest", db="DNS", charset="utf8")
cursor = conn.cursor()

select_commond = 'select name,rdata from %s' % table_url
cursor.execute(select_commond)
test = '%s' % cursor.execute(select_commond)
boo = pattern.match(test)
if ( boo == None ):
    print '%s数据库中没有该表' % table_url
table_url_data = cursor.fetchall()
global db_ip
db_ip = '0.0.0.0'
for i in range(3, len(table_url_data)):
    if table_url_data[i][0] == target_url:
        db_ip = table_url_data[i][1]
        break
if ( db_ip == '0.0.0.0' ):
    print '%s该域名不在数据库中' % target_url

if ping_ip == db_ip:
    print '%s 所在主机的ip与数据库中所存ip一致' % target_url
else:
    print '%s 所在主机的ip与数据库中所存ip不一致' % target_url