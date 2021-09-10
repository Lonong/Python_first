test_list = [12, 3, 1, 13, 10, 5, 9]
for i in range(len(test_list)):
    for j in range(len(test_list) - i - 1):
        if test_list[j] > test_list[j + 1]:
            tmp = test_list[j]
            test_list[j] = test_list[j + 1]
            test_list[j + 1] = tmp
    print('第{0}循环后的结果是='.format(str(i)), test_list)
print('最终结果是=', test_list)
