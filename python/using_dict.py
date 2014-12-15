#!/usr/bin/env python
#coding: utf-8
#Filename: using_dict.py

#!/usr/bin/env python
#coding: utf-8
#Filename: using_dict

ab = {
    '小明': 'xiaoming@gmail.com',
    '小华': 'xiaohua@outlook.com',
    '小刚': 'xiaogang@hotmail.com'
}

print '小明的邮箱地址是：%s' % ab['小明']
ab['红领巾'] = 'honglingjin@qq.com'
print '\n红领巾的邮箱地址是：%s' % ab['红领巾']

del ab['小明']
print '\n现在有%d个联系人' % len(ab)

for name, address in ab.items():
    print '\n%s的邮箱地址是%s' % (name, address)

if '小刚' in ab:
    print '\n小刚的邮箱地址是：%s' % ab['小刚']

if ab.has_key('小华'):
    print '\n小华的邮箱地址是：%s' % ab['小华']
