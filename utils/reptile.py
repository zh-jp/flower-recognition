import re
import requests
import os

suffix = 'D:/workspace/down_img/'  # 爬虫下载文件路径
pattern = r'src=("http.+?pid=\d\.\d")'  # 匹配网页中的图片文件正则表达式

urls = {  # 爬虫目标urls
    '蒲公英': 'https://cn.bing.com/images/search?q=%e8%92%b2%e5%85%ac%e8%8b%b1&form=HDRSC2&first=1',
    '牵牛花': 'https://cn.bing.com/images/search?q=%e7%89%b5%e7%89%9b%e8%8a%b1&form=HDRSC2&first=1',
    '牡丹': 'https://cn.bing.com/images/search?q=%e7%89%a1%e4%b8%b9&form=HDRSC2&first=1',
    '鸡蛋花': 'https://cn.bing.com/images/search?q=%e9%b8%a1%e8%9b%8b%e8%8a%b1&form=HDRSC2&first=1',
    '玫瑰花': 'https://cn.bing.com/images/search?q=%e7%8e%ab%e7%91%b0%e8%8a%b1&form=HDRSC2&first=1',
    '向日葵': 'https://cn.bing.com/images/search?q=%e5%90%91%e6%97%a5%e8%91%b5&form=HDRSC2&first=1',
    '郁金香': 'https://cn.bing.com/images/search?q=%e9%83%81%e9%87%91%e9%a6%99&form=HDRSC2&first=1'
}
urls = {
    '鸡蛋花2' : 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1678021801074_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&dyTabStr=&ie=utf-8&sid=&word=%E9%B8%A1%E8%9B%8B%E8%8A%B1'
}

if __name__ == "__main__":
    reg = re.compile(pattern)
    for url in urls:
        # 查看图片保存的路径是否存在，若不存在则新建目录
        if not os.path.exists(suffix + url):
            os.mkdir(suffix + url)
        page = requests.get(urls[url]).text
        print(page)
        links = re.findall(reg, page)   # 匹配网页中所有的url
        links_ = []                    # 清洗爬取的url
        for link in links:
            links_.append(link[1:-1])  # 去除url两边的引号
        num = 0
        pos = suffix + url + '/'
        for i in links_:            # 保存图片
            a = requests.get(i)
            with open(pos + '%s.jpg' % num, 'wb') as f:
                f.write(a.content)
            num += 1
        print(url + '爬取完毕！')