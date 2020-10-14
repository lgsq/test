#!/usr/bin/env python3
#题目，输入一个大于二的自然数，输出小于该数的所有素数
num = int(input('输入一个大于2的自然数: '))
lst = list(range(2,num))
#输入的数的最大平方根
m=int(num**0.5)
for index,value in enumerate(lst):
    if value>m:
        break
#如果当前数字大于最大整数的平方根，结束
    lst[index+1:]=filter(lambda x:x%value!=0, lst[index+1])
print(lst)
for index,value in enumerate(lst,1):
    if value>m:
        break
    lst[index: ]=filter(lambda x:x%value!=0,lst[index:])
    print(lst)