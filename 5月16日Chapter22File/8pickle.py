# -*- coding: cp936 -*-
import pickle #��ˣ�����
my_list = ['Victor',20,'Hello there',81.9876e-13]
pickle_file = open('my_pickle_list.pkl','w')
pickle.dump(my_list,pickle_file)#���б����ƣ��洢����pickle_file��
pickle_file.close()
