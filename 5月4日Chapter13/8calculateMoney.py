# -*- coding: utf-8-*-
def calculateMoney(money):
    total = money[0]*0.25+money[1]*0.1+money[2]*0.05+money[3]*0.01
    return total

list=[]
quarters = int(raw_input("quarters: ")) #25分
list.append(quarters)
dimes = int(raw_input("dimes: "))  #10分
list.append(dimes)
nickels = int(raw_input("nickels: ")) #5分
list.append(nickels)
pennies = int(raw_input("pennies: ")) #1分
list.append(pennies)
print "total is $%s "%calculateMoney(list)
