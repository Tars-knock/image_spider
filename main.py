# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 Double Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import os
import re

import requests


def get_aim():
    global word
    word = input('关键词\n')
    global pages
    pages = input('需要页数\n')
    pages = int(pages)
    global count
    count = 0


def main():
    get_aim()
    for page in range(1, pages+1):
        base_url = 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
        }
        param = {'word': word, 'pn': page }
        html = requests.get(base_url, headers=headers, params=param)
        # print(html.url)

        html.encoding = 'utf-8'
        #print(html.text)
        image_url = re.findall('"thumbURL":"(.*?)",', html.text)
        if not image_url:
            print(检测到百度反爬虫，建议几分钟后尝试)
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


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # print_hi('PyCharm')
    main()
