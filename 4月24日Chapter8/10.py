print "Which multiplication table would you like?"
number = int(raw_input())
print "Here's your table:"
for i in range(1,11):
    print number,'x',i,'=',number*i
