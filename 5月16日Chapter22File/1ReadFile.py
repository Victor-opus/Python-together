# -*- coding: cp936 -*-
my_file = open('Note.txt','r')
lines = (my_file.readline()).decode('gb2312')#decode���� encode����
zhong='\xd6\xd0\xce\xc4'
print zhong
print lines

#pythonĬ�ϴ������unicode�����ļ��������ģ������Ƚ����Unicode
#��������������ʽ��ʹ��encode('utf-8')
#line = (file1.readline()).decode('utf-8').encode('gb2312')
#�Ƚ��뽫utf-8ת����Unicode����ʵ�������ָ�ʽ��һ�������ٽ�Unicodeת����gb2312
