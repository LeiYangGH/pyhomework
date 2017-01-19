#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import time
import shutil

url = r'http://you.ctrip.com/sight/shunyi120473/137221.html';
#url = r'http://docs.python-requests.org/en/master/';
pic = r'https://dimg08.c-ctrip.com/images/tg/053/059/075/a3b050a7ecc7462199a93b57ffd1c031_C_350_230.jpg'
try:
    r = requests.get(url)
    print(r.encoding)
    #print(r.text.encode('utf-8'))

    r = requests.get(pic, stream=True)
    if r.status_code == 200:
        with open('t.jpg', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)  
except Exception as e:
    print(e)
