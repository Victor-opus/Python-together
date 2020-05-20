class BankAccount:
    def __init__(self,name,num,money):
        self.name = name
        self.num = num
        self.money = money
    def __str__(self):
        msg = self.name+" "+self.num+" "+"balance:"+str(self.money)
        return msg
    def balance(self):
        print self.money

    def saveMoney(self,money):
        self.money+=money
        return self.money

    def drawMoney(self,money):
        if(self.money>=money):
            self.money-=money
        else:
            print "balance not enough"
        return self.money

myCount = BankAccount('Victor','543',100.0)
print "Read my balance"
myCount.balance()
print "Now , I save 200"
print "Balance",myCount.saveMoney(200)
print "Now , I draw 100"
print "Balance",myCount.drawMoney(100)
print myCount

        



        
