# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

import requests




import requests


headers = {
    "authority": "jad-api.jin10.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "handleerror": "true",
    "origin": "https://www.jin10.com",
    "referer": "https://www.jin10.com/",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-app-id": "bVBF4FyRTn5NJF5n",
    "x-version": "1.0.0"
}
cookies = {
    "Hm_lvt_522b01156bb16b471a7e2e6422d272ba": "1682384897",
    "__gads": "ID=52691e667ce3e82f-2225795e75df0046:T=1682384895:RT=1682384895:S=ALNI_MYo8whBgzorgn0jdc9UxujIeknQYQ",
    "__gpi": "UID=00000bfd4e14623f:T=1682384895:RT=1682384895:S=ALNI_MaWuDm6mLWSrIBxr_qr5fOhibdIUQ",
    "UM_distinctid": "187b5f4550b102c-066bbe43876e17-26031b51-151800-187b5f4550c1456",
    "x-token": "",
    "did": "0837e21e-e66d-445f-8f46-9846d9e60ec3",
    "env": "prod",
    "CALENDAR_FAVOR_INDEX_LIST": "%5B%5D",
    "Hm_lpvt_522b01156bb16b471a7e2e6422d272ba": "1682385324"
}
time =time.time()
url = f"https://www.jin10.com/flash_newest.js?t={time}"

response = requests.get(url, headers=headers, cookies=cookies)

print(response.text)