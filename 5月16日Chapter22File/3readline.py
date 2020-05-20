my_file = open('Note.txt','r')
first_line = my_file.readline().decode('gb2312')
second_line = my_file.readline().decode('gb2312')
print "first line =",first_line,
print "second line =",second_line
my_file.close()
