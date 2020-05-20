# -*- coding: cp936 -*-
my_file = open("new_file.txt",'w')
print >> my_file,"Hello there, neighbor!"#>>重定向,告诉print要把输出发送到一个文件中，而不是屏幕
my_file.close()
