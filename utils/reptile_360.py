import json
import os
import requests

# 路径
BASE_URL = './戴口罩'
# 关键词
NAME = '戴口罩'


class PictureDownload(object):
    def __init__(self, q=None, sn=100):
        self.url = 'https://m.image.so.com/j?q={}&src=srp&pn=100&sn={}&kn=0&gn=0&cn=0'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
        }
        self.q = q
        self.sn = sn
        self.num = 0
        self.total = 2

    def makedir(self):
        if not os.path.exists(os.path.join(BASE_URL, self.q)):
            os.makedirs(os.path.join(BASE_URL, self.q))

    def parse_url(self):
        response = requests.get(self.url.format(self.q, self.num), headers=self.headers)
        return response.content.decode()

    def parse_image_list(self, html_json_str):
        image_list = json.loads(html_json_str)['list']
        total = json.loads(html_json_str)['total']
        return image_list, total

    def save_image(self, image_list):

        for item in image_list:
            response = requests.get(item['thumb'], headers=self.headers)
            with open(os.path.join(BASE_URL, '%s\%s.jpg' % (self.q, item['index'])), 'wb') as f:
                f.write(response.content)

    def run(self):
        self.makedir()
        while self.num < self.total:
            html_json_str = self.parse_url()
            image_list, self.total = self.parse_image_list(html_json_str)
            self.save_image(image_list)
            self.num += 100
            print(self.num)


if __name__ == '__main__':
    xxx = PictureDownload(NAME)
    xxx.run()
