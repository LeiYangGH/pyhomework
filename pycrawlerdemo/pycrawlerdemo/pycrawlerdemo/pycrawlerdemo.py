#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import time
import shutil
import re
import os
import os.path

#ctripurl = r'http://you.ctrip.com/sight/shunyi120473/137221.html';
#url = r'http://docs.python-requests.org/en/master/';
#jpgurl = r'https://dimg08.c-ctrip.com/images/tg/053/059/075/a3b050a7ecc7462199a93b57ffd1c031_C_350_230.jpg'

#allurls = ['http://you.ctrip.com/sight/shunyi120473/137221.html','http://huodong.ctrip.com/activity/10226914.html','http://huodong.ctrip.com/activity/3226120.html','http://hotels.ctrip.com/hotel/484119.html']
#allurls = []
dir = 'pics'
#https://dimg
regex = re.compile(r'"(https?:\/\/dimg.+?\.(?:jpg|png))')
picsfile = open('pics.txt','w')

def readurls(filename):
    with open(filename) as f:
        content = f.readlines()
        return [x.strip() for x in content]
        #print(allurls)

def downloadjpg(jpgurl,filename):
    print('downloading ' + jpgurl)
    
    r = requests.get(jpgurl, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)  

def downfirstjpg(url,cnt):
    print('---------------------')
    print('searching ' + url)
    r = requests.get(url)
    content = r.text
    jpgurl = regex.search(content).group(1)
    
    filename, file_extension = os.path.splitext(jpgurl)
    
    pic = os.path.join(dir, str(cnt)+file_extension)
    print('pic file ' + pic)
    downloadjpg(jpgurl, pic)
    return jpgurl

allurls = readurls('urls.txt')
print(allurls)


if not os.path.exists(dir):
    os.makedirs(dir)

cnt = 0
for ctripurl in allurls:
    try:
        cnt=cnt+1
        jpgurl = downfirstjpg(ctripurl,cnt)
        picsfile.write(jpgurl+'\n')
    except Exception as e:
        picsfile.write('\n')
        print(e)

picsfile.close()
