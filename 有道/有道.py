# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests
from hashlib import md5
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

url = "https://dict.youdao.com/webtranslate"

tm = str(int(time.time() * 1000))

str_temp = f'client=fanyideskweb&mysticTime={tm}&product=webfanyi&key=fsdsogkndfokasodnaso'

obj = md5()
obj.update(str_temp.encode("utf-8"))
sign = obj.hexdigest()

word = input("请输入一个单词:")
data = {
    "i": word,
    "from": "auto",
    "to": "",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": sign,
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": tm,
    "keyfrom": "fanyi.web"
}

headers = {
    "Referer": "https://fanyi.youdao.com/",
    "Cookie": "OUTFOX_SEARCH_USER_ID_NCOO=119698985.05373167; OUTFOX_SEARCH_USER_ID=-317747724@2408:8207:7892:c51:5a1d:c86e:753e:2525",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

session = requests.session()

resp = session.post(url, data=data, headers=headers)
# print(resp.text)


def my_md5(data):
    obj2 = md5()
    obj2.update(data.encode())
    ret = obj2.digest()  # 返回字节
    return ret


t = resp.text
# t = 'Z21kD9ZK1ke6ugku2ccWuwRmpItPkRr5XcmzOgAKD0GcaHTZL9kyNKkN2aYY6yiOQXFI3D7RP4_e7hP07ZgORviZXWZKf4FffFcQFOosBBe8jQd4mwR9kTXelgpJc4ZSi4slgGNvt3ZRTXugWrfToCTG8_aV-Nuc2JSAQrOVV7Gi_HBoLlfcx1lS9kIKR17-JkhbGt10PnUD8FoXEH0_jg=='
o = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
n = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'

key = my_md5(o)
iv = my_md5(n)

t = t.replace("_", "/").replace("-", "+")
aes = AES.new(key=key, iv=iv, mode=AES.MODE_CBC)

ming_bs = aes.decrypt(base64.b64decode(t))
ming_bs = unpad(ming_bs, 16)
print(ming_bs.decode("utf-8"))
