print "Which multiplication table would you like?"
number = int(raw_input())
print "high do you want to go?"
maxNum = int(raw_input())
print "Here's your table:"

for i in range(1,maxNum+1):
     print number,'x',i,'=',number*i
