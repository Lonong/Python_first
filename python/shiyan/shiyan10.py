# coding=utf-8

def sorce():
    s = float(input('请输入成绩'))
    if s >= 90:
        print('成绩优秀')
    elif s >= 75:
        print('成绩良好')
    elif s >= 60:
        print('成绩一般')
    else:
        print('成绩不及格')


def main():
    sorce()
    answer = input('是否继续查询？y/n')
    if answer == "y":
        sorce()
    else:
        exit()


if __name__ == '__main__':
    main()
