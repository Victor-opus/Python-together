# -*- coding: cp936 -*-
my_file = open('Note.txt','r')
lines = (my_file.readline()).decode('gb2312')#decode解码 encode编码
zhong='\xd6\xd0\xce\xc4'
print zhong
print lines

#python默认处理的是unicode，若文件存在中文，必须先解码成Unicode
#若想编码成其他格式可使用encode('utf-8')
#line = (file1.readline()).decode('utf-8').encode('gb2312')
#先解码将utf-8转化成Unicode（其实是这两种格式是一样），再将Unicode转化成gb2312
