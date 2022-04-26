# -*- coding: utf-8 -*-
import hashlib

def md5value(value):
    md5 = hashlib.md5()
    md5.update(value)
    return md5.hexdigest()
#对字典中的值进行加密
def md5encode():
    code=input("请输入：")
    clear_character= ''+code+''
    print(clear_character, '->',md5value(code.encode()))

if __name__ == '__main__':
    md5encode()
