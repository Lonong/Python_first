#求学生成绩平均数
#
# def main():
#     number = int(input('请输入学生人数: '))
#     names = [None] * number
#     scores = [None] * number
#     for index in range(len(names)):
#         names[index] = input('请输入第%d个学生的名字: ' % (index + 1))
#         scores[index] = float(input('请输入第%d个学生的成绩: ' % (index + 1)))
#     total = 0
#     for index in range(len(names)):
#         print('%s: %.1f分' % (names[index], scores[index]))
#         total += scores[index]
#     print('平均成绩是: %.1f分' % (total / number))
#
#
# if __name__ == '__main__':
#     main()

def main():
    name = []
    sorce = []
    a = 0
    need = 'y'
    while need == 'y':
        a += 1
        # nam = input('请输入第%d个学生姓名' % (a))
        # name.append(nam)
        sorc = input('请输入第%d个学生成绩' % (a))
        sorce.append(sorc)
        # print(sorce)
        need = input('是否继续添加？y/n')

    total = 0
    for i in range(0, len(sorce)):
        total += int(sorce[i])
    print("平均成绩为: ", total // len(sorce))


if __name__ == '__main__':
    main()

