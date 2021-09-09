# coding=utf-8

#用for循环实现x到num的求和
from math import *


sum = 0
x=int(input('请输入开始数字：'))
num=int(input('请输入结束数字'))
y=int(num+1)


for x in range(x, y):
    sum += x
print(sum)
