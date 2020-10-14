#!/usr/bin/env python3
#实验四，random函数的应用，随机编写一个猜数字小游戏
import random
num = random.ranint(1,10)
print('游戏开始了')
a1 = 0
print('开始猜数字：')
while a1 != num:
    temp = input()
    a1 = int(temp)
    if a1 == num:
        print("你赢了")
        print("厉害")
    else:
        print("你输了")
        if a1 < num:
            print("太小了")
        else:
            print("太大了"）
print("game over")
