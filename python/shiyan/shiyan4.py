# coding=utf-8

year = int(input('请输入年份: '))
leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
if leap:
    print(str(year)+'是闰年')
else:
    print(str(year) + '不是闰年')
