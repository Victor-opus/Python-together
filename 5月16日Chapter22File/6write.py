# -*- coding: cp936 -*-
new_file = open("my_new_notes.txt",'w') #存在将覆盖其中的内容，没有则创建新文件
new_file.write("Eat supper\n")
new_file.write("Play soccer\n")
new_file.write("Go to bed")
new_file.close()
