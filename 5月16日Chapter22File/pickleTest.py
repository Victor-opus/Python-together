import pickle
name = raw_input("Enter your name: ")
years = raw_input("Enter your age: ")
color = raw_input("Enter your perfered color: ")
food = raw_input("Enter your perfered food: ")

list=[]
list.append(name)
list.append(years)
list.append(color)
list.append(food)
#list=[name,age,color,food]
pickle_file=open('pickle_Victor.pkl','w')
pickle.dump(list,pickle_file)
pickle_file.close()
pickle_file=open('pickle_Victor.pkl','r')
lists=pickle.load(pickle_file)
print lists

