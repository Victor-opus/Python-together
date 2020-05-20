# -*- coding: cp936 -*-
my_file = open('Note.txt','r')
first_line = my_file.readline().decode('gb2312')
second_line = my_file.readline().decode('gb2312')
my_file.seek(0) #参数0表示0字节，即回到第0个字节（起始位置）
first_line_again = my_file.readline().decode('gb2312')
print "first line =",first_line,
print "second line =",second_line,
print "first again line=",first_line_again
my_file.close()
