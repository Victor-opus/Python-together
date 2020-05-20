# -*- coding: cp936 -*-
import pickle #腌菜，腌制
my_list = ['Victor',20,'Hello there',81.9876e-13]
pickle_file = open('my_pickle_list.pkl','w')
pickle.dump(my_list,pickle_file)#将列表腌制（存储）到pickle_file中
pickle_file.close()
