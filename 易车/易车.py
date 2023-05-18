# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests
import time
import json
from hashlib import md5


session = requests.session()
url = "https://mapi.yiche.com/web_api/car_model_api/api/v1/car/config_new_param"

cid = "508"
param = {
    "cityId": "201",
    "serialId": "3152"
}

params = {
    "cid": cid,
    "param": json.dumps(param,separators=(',', ':'))
}


tm = str(int(1000 * time.time()))
pm = f"cid={cid}&param={json.dumps(param, separators=(',', ':'))}19DDD1FBDFF065D3A4DA777D2D7A81EC{tm}"

obj = md5()
obj.update(pm.encode("utf-8"))
sign = obj.hexdigest()

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "content-type": "application/json;charset=UTF-8",
    "x-city-id": "201",
    "x-ip-address": "2408:8207:7892:c51:5a1d:c86e:753e:2525",
    "x-platform": "pc",
    "x-sign": sign,
    "x-timestamp": tm,
    "x-user-guid": "bbf83b6180c92a4c7486913f08f79fd7"
}

resp = session.get(url, params=params, headers=headers)

print(resp.request.url)
print(resp.json)
