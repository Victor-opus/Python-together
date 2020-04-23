tank = float(raw_input("Size of tank: "))
percent = float(raw_input("percent full: "))
velocity = float(raw_input("km per liter: "))

distance=velocity*(percent*0.01)*tank
print "You can go another", int(distance),"km away"
print "The next gas station is 200 km away"
if distance > 200:
    print "You can wait for next station."
else:
    print "Get gas now!"
