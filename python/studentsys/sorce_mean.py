#��ѧ���ɼ�ƽ����
#
# def main():
#     number = int(input('������ѧ������: '))
#     names = [None] * number
#     scores = [None] * number
#     for index in range(len(names)):
#         names[index] = input('�������%d��ѧ��������: ' % (index + 1))
#         scores[index] = float(input('�������%d��ѧ���ĳɼ�: ' % (index + 1)))
#     total = 0
#     for index in range(len(names)):
#         print('%s: %.1f��' % (names[index], scores[index]))
#         total += scores[index]
#     print('ƽ���ɼ���: %.1f��' % (total / number))
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
        # nam = input('�������%d��ѧ������' % (a))
        # name.append(nam)
        sorc = input('�������%d��ѧ���ɼ�' % (a))
        sorce.append(sorc)
        # print(sorce)
        need = input('�Ƿ������ӣ�y/n')

    total = 0
    for i in range(0, len(sorce)):
        total += int(sorce[i])
    print("ƽ���ɼ�Ϊ: ", total // len(sorce))


if __name__ == '__main__':
    main()

