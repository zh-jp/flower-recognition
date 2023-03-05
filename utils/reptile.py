import re
import requests

reg = r'src=("http.+?pid=\d\.\d")'  # 匹配网页中的图片文件正则表达式

urls = {
    '鸡蛋花' : 'https://cn.bing.com/images/search?q=%e9%b8%a1%e8%9b%8b%e8%8a%b1&form=HDRSC2&first=1',
    '牡丹' : 'https://cn.bing.com/images/search?q=%e7%89%a1%e4%b8%b9&form=HDRSC2&first=1',
    '牵牛花' : '',
    ''
}
