# -*- coding: cp936 -*-
name_string = 'Sam,Brad,Alex, Cameron,Toby,Gwen,Jenn,Connor'
names = name_string.split(',')#�ֽ��ַ�������','��Ϊ�ֽ��������һ���б���������ֽ����
print names
for name in names:
    print name

parts = name_string.split('Toby,')
print parts
for part in parts:
    print part

names = name_string.split()#�����������հ׷��ֽ�
print names         #�հ׷���ʾ���пո��Ʊ�������з� whitespace

    
