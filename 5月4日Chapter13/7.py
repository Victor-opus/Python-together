def printData(data):
    for i in data:
        print i,


list=[]
name = raw_input("Enter your name ")
list.append(name)
address = raw_input("Enter your address ")
list.append(address)
street = raw_input("Enter your street ")
list.append(street)
city = raw_input("Enter your city ")
list.append(city)
province = raw_input("Enter your province ")
list.append(province)
code = raw_input("Enter your post code ")
list.append(code)
country = raw_input("Enter your country ")
list.append(country)
printData(list)
