
name = raw_input("Enter your name: ")
years = raw_input("Enter your age: ")
color = raw_input("Enter your perfered color: ")
food = raw_input("Enter your perfered food: ")

person_file = open('person.txt','a')

person_file.write(name+'\n')
person_file.write(years+'\n')
person_file.write(color+'\n')
person_file.write(food+'\n')
person_file.close()
