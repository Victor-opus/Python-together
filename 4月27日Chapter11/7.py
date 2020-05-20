numBlocks = int(raw_input("How many blocks of stars do you want? "))
for block in range(1, numBlocks + 1):
    print "block =", block
    for line in range(1, block*2):
        for star in range(1, (block+line)*2):
            print '*',
        print 'line =',line,'star =',star
    print
