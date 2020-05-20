# -*- coding: cp936 -*-
import random

totals = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(1000):
    dice_total = random.randint(2,12) #dice 骰子
    totals[dice_total]+=1

for i in range(2,13):
    print "total",i,"came up",totals[i],"times"
