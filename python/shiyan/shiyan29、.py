# encoding=utf8

# for i in range(5):
#     i+=1
#     print("-------")
#     if i==3:
#         continue
# print(i)

counter = 1


# def doLotsOfStuff():
#     global counter  # 当内部作用域想修改外部变量时，需要使用global声明
#     for i in (1, 2, 3):
#         counter += 1
#
#
# doLotsOfStuff()
# print(counter)


import math
def sieve(size):
    sieve= [True] * size
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.sqrt(size)) + 1):
        k= i * 2
        while k < size:
           sieve[k] = False
           k += i
    return sum(1 for x in sieve if x)
print(sieve(1000))