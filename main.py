
import os
import re
from bs4 import BeautifulSoup
import requests


def get_aim():
    global word
    word = input('需要的图片关键词\n')
    global pages
    pages = input('需要的页数\n')
    pages = int(pages)
    global count
    count = 0


def baidu():
    get_aim()
    base_url = 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }

    for page in range(1, pages+1):
        param = {'word': word, 'pn': page}
        html = requests.get(base_url, headers=headers, params=param)
        # print(html.url)

        html.encoding = 'utf-8'
        #print(html.text)
        image_url = re.findall('"thumbURL":"(.*?)",', html.text)
        if not image_url:
            print("检测到百度反爬虫，建议几分钟后尝试")
            print(html.text)

        # print(image_url)
        way = 'C:\\Users\\小凯文\\Desktop\\{}\\'.format(word)
        if not os.path.exists(way):
            os.makedirs(way)
        for url in image_url:
            global count
            count += 1
            path = way + str(count) + '.jpg'
            print(path)
            image_data = requests.get(url, headers=headers)
            with open(path, 'wb')as f:  # 将图片以二进制写入
                f.write(image_data.content)

def bing():
    get_aim()
    base_url = "https://cn.bing.com/images/search"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    param = {'q': word, 'pn': 1}
    html = requests.get(base_url, headers = headers, params = param)
    html.encoding = 'utf-8'
    # print(html.text)
    html_soup = BeautifulSoup(html.text)
    html_soup.find_all('lnkw')
    # print(html_soup.prettify())
    # image_url = re.findall('src="(.*?)" alt="', html.text)
    # print("下面输出图像url")
    # print(image_url)
    # way = 'C:\\Users\\小凯文\\Desktop\\{}\\'.format(word)
    # if not os.path.exists(way):
    #     os.makedirs(way)
    # for url in image_url:
    #     global count
    #     count += 1
    #     path = way + str(count) + '.jpg'
    #     print(path)
    #     image_data = requests.get(url, headers=headers)
    #     with open(path, 'wb')as f:  # 将图片以二进制写入
    #         f.write(image_data.content)
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    bing()


