width = raw_input("What is the width of your house?")
length = raw_input("What is the length of your house?")
price = raw_input("How much is the carpet")

print "You need",int(width)*int(length),"carpets (the unit is smeter)"
print "You need",int(width)*int(length)/9.0,"carpets (the unit is sfeet)"
print "Sum of the price is",int(price)*int(width)*int(length)
