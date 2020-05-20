import time
times = int(raw_input("Countdown timer: How many seconds? "))
for i in range(times,0,-1):
    print i,
    for j in range(i,0,-1):
        print "*",
    print
    time.sleep(1)
print "BLAST OFF!"
