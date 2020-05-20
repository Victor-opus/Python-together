dictionaries={}
while True:
    opt=raw_input("Add or look up a word(a/l)? ")
    if opt=='a':
        word=raw_input("Type the word: ")
        definition=raw_input("Type the definition: ")
        dictionaries[word]=definition
        print "Word added!"
    elif opt=='l':
        word=raw_input("Type the word: ")
        if word in dictionaries:
            print dictionaries[word]
        else:
            print "That word isn't in the dictionary yet."
    else:
        print "enter error"
        break
