#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import shutil
import re
import os
import os.path


dir = 'pics'
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
