class BankAccount:
    def __init__(self,name,num):
        self.name = name
        self.num = num
        self.money = 0.0
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

class InterestAccount(BankAccount):
    def __init__(self,name,num,rate):
        BankAccount.__init__(self,name,num)
        self.rate = rate

    def addInterest(self,year):
        self.money+=self.money*self.rate
        return self.money
        
myCount = InterestAccount("Victor","543",0.02)
myCount.saveMoney(100.0)
myCount.addInterest(2)
print myCount

        



        
