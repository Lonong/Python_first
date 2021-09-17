# ±éÀúì³²¨ÄÇÆõº¯Êı
def f():
    f = [1, 1]
    for i in range(2, 20):
        f += [f[i - 1] + f[i - 2]]
        # f.append(f[i - 1] + f[i - 2])
    # print(val, end=' ')
    for val in f:
        print(val, end=' ')


if __name__ == '__main__':
    f()
