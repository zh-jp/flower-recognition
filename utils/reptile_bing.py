from bs4 import BeautifulSoup
import urllib.request
import requests
import time
import json
import sys
import re
import os

# 爬取图片的网址模板，其中%s部分将会被替换成具体的搜索关键字和图片编号，用于构建实际的爬取网址。（bing）
CRAWL_TARGET_URL = 'https://cn.bing.com/images/async?q=%s&first=%d&count=%d&relp=%d&lostate=r&mmasync=1'
# 每次抓取图片数量(35是此网页每次翻页请求数量)
NUMS_PER_CRAWL = 35
# 抓取图片最小大小(单位字节)，小于此值抛弃
MIN_IMAGE_SIZE = 10


def get_image(url, path, count):
    try:

        u = urllib.request.urlopen(url, timeout=5)  # 使用urllib模块打开图片地址，并读取图片数据
        t = u.read()
        if sys.getsizeof(t) < MIN_IMAGE_SIZE:   # 如果图片数据大小小于设定的MIN_IMAGE_SIZE值，则直接返回-1
            return -1
    except Exception as e:
        print(url, e)
        return -2
    # 提取图片格式，获取图片扩展名
    frmt = url[url.rfind('.'):]
    p = re.compile("^\\.[a-zA-Z]+")
    m = p.match(frmt)
    frmt = m.group(0)
    # 如果保存路径不存在，则创建该路径
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        f = open(os.path.join(path, str(count) + frmt), 'wb')   # 以二进制方式打开文件并写入图片数据，最后返回0表示下载成功，返回负数表示下载失败
        f.write(t)
        f.close()
    except Exception as e:
        print(os.path.join(path, str(count) + frmt), e)
        return -3
    return 0


def crawl_data(info, num):
    first = 0
    count = 0
    s = requests.Session()                              # 首先创建了一个会话，并设置了超时时间。
    path = "D:/practice/data/targets/" + info + '/'     # 创建文件路径
    if not os.path.exists(path):
        os.mkdir(path)

    index = len(os.listdir(path))   # 获取该路径下已有的图片数量
    count = index
    while (count < num):
        u = CRAWL_TARGET_URL % (info, first, NUMS_PER_CRAWL, NUMS_PER_CRAWL)
        req = s.get(url=u, timeout=(3.05, 10))          # 使用requests模块访问该网址，3.05s为发送超时时间，10s为接收到数据超时时间
        bf = BeautifulSoup(req.text, "html.parser")     # 使用BeautifulSoup模块解析返回的html内容
        imgtags = bf.find_all("a", class_="iusc")       # 找到所有带有class为"iusc"的a标签，提取出该标签中的图片地址
        for e in imgtags:
            if count == num:                            # 达到最大下载数退出
                return False
            urldict = json.loads(e.get('m'))
            if get_image(urldict["murl"], path, index) < 0:     # 如果下载失败，则跳过该图片并继续循环
                continue
            print("Downloaded %d picture" % (count + 1))        # 如果下载成功，则将该图片的编号index加1，将下载的图片数量count加1
            sys.stdout.flush()
            count = count + 1
            index = index + 1
            time.sleep(0.01)
        first = first + NUMS_PER_CRAWL
        time.sleep(0.1)

    return True


if __name__ == '__main__':

    # 关键词，可设置为多个
    key_words = ['牡丹']
    # 下载的图片数量
    picture_num = 300

    for i in range(len(key_words)):
        word = key_words[i]
        print(word)
        if crawl_data(word, picture_num):
            i = i + 1
