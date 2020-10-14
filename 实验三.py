#!/usr/bin/env python3
#题目，模拟蒙特卡罗计算方法计算圆周率的近似值
from random import random
times = int(input("请输入投入飞镖的个数 "))
hits=0
for i in range(times):
    x=random()
    y=random()
    if x*x+y*y<=1:
        hits+=1
print('击中次数',hit99s)
print('圆周率近似值', 4.0*hits/times)