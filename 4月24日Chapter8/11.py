print "Which multiplication table would you like?"
number = int(raw_input())
print "Here's your table:"
i=1
while(i<11):
    print number,'x',i,'=',number*i
    i+=1
