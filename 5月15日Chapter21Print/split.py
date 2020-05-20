# -*- coding: cp936 -*-
name_string = 'Sam,Brad,Alex, Cameron,Toby,Gwen,Jenn,Connor'
names = name_string.split(',')#分解字符串，以','作为分解符，返回一个列表，里面包含分解的项
print names
for name in names:
    print name

parts = name_string.split('Toby,')
print parts
for part in parts:
    print part

names = name_string.split()#不带参数按空白符分解
print names         #空白符表示所有空格、制表符、换行符 whitespace

    
