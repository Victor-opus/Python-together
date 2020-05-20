print "Enter 5 names:"
name = []
for i in range(5):
    temp_name = raw_input()
    name.append(temp_name)
print "The names are",
for i in range(5):
    print name[i],
print
num=int(raw_input("Replace one name.Which one?(1-5): "))
new_name = raw_input("New name: ")
name.insert(num-1,new_name)
print "The names are",
for i in range(5):
    print name[i],
