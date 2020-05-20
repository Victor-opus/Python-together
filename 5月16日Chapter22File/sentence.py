# -*- coding: cp936 -*-
import random


adj_file=open('adj.txt','r')
i=0
adjs = adj_file.readlines()
for adj in adjs:       #除去末尾的换行符
    adjs[i]=adj.strip()
    i=i+1
adj = random.choice(adjs) #从列表中随机产生一个

i=0
n_file=open('n.txt','r')
ns = n_file.readlines()
for n in ns:
    ns[i]=n.strip()
    i=i+1
n = random.choice(ns)

i=0
v_file=open('v.txt','r')
vs = v_file.readlines()
for v in vs:
    vs[i]=v.strip()
    i+=1
v = random.choice(vs)

i=0
adv_file=open('adv.txt','r')
advs = adv_file.readlines()
for adv in advs:
    advs[i]=adv.strip()
    i+=1
adv = random.choice(advs)

print "The",adj,n,v,adv
adv_file.close()
v_file.close()
n_file.close()
adj_file.close()



