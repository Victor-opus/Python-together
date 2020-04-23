# -*- coding: utf-8 -*-
money = float(raw_input("输入你的购买金额："))
if money <= 10:
    money*=0.9
    print "折扣为10% 最终价格为",money,"元"
else:
    money*=0.8
    print "折扣为20% 最终价格为",money,"元"
    
