# coding:utf8
import requests

page = input("多少页：")
page = int(page) + 1

header = {

    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    'Upgrade-Insecure-Requests': '1'
}
n = 0
pn = 1
for m in range(1, page):

    url = 'https://image.baidu.com/search/acjson?'
    param = {
        "tn": "resultjson_com",
        'logid': '10548527383123046523',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': '路人',
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '0',
        'hd': '',
        'latest': '',
        'copyright': '',
        'word': '路人',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'fr': '',
        'expermode': '',
        'nojc': '',
        'pn': pn,
        'rn': '30',
        'gsm': '1e',
    }

    page_text = requests.get(url=url, headers=header, params=param)
    page_text.encoding = 'utf-8'
    page_text = page_text.json()
    # 先取出所有链接所在的字典，并将其存储在一个列表当中
    info_list = page_text['data']
    # 由于利用此方式取出的字典最后一个为空，所以删除列表中最后一个元素
    del info_list[-1]
    # 定义一个存储图片地址的列表
    img_path_list = []
    for info in info_list:
        img_path_list.append(info['thumbURL'])
    # 再将所有的图片地址取出，进行下载
    # n将作为图片的名字
    for img_path in img_path_list:
        img_data = requests.get(url=img_path, headers=header).content
        img_path = './' + str(n) + 'p.jpg'
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
        n = n + 1

    pn += 29
