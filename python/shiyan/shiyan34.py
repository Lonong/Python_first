# encoding=utf8
"""
定义和使用时钟类

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""

import time
import os


# class Clock(object):

    # Python中的函数是没有重载的概念的
    # 因为Python中函数的参数没有类型而且支持缺省参数和可变参数
    # 用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
while True:
    tm = time.localtime(time.time())
    hour = tm.tm_hour
    minute = tm.tm_min
    second = tm.tm_sec
    print(hour,':',minute,':',second)
# if __name__ == '__main__':
#     # clock = Clock(hour=10, minute=5, second=58)
#     clock = Clock()
#     while True:
#
#         print(clock.show())
#         time.sleep(1)
#         clock.run()
