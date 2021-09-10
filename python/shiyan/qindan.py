def dongxi():
    file = open('C:/Users/18201李龙/Desktop/qingdan.txt', 'a', encoding='utf-8', );
    file.write(input('你要带啥？') + '\r');
    file.close();
    answer = input('还要带吗？y/n:')
    if answer == 'y':
        dongxi()
    else:
        exit()


def main():
    dongxi()


if __name__ == '__main__':
    main()
