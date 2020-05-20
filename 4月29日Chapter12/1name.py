print "Enter 5 names:"
name = []
for i in range(5):
    temp_name = raw_input()
    name.append(temp_name)
print "The names are",
for i in range(5):
    print name[i],
