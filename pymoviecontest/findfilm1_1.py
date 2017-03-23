#!/usr/bin/env python
# coding: UTF-8
import urllib2
import re
import os
curdir = os.getcwd()
url = 'file:///' + os.path.join(curdir,u'www1\北京影讯,北京电影院-在线选座购票-购电影票.htm')
#url=u'file:///C:\SDK\G\pyhomework\pymoviecontest\www1\北京影讯,北京电影院-在线选座购票-购电影票.htm'
print url
req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0"})
webpage= urllib2.urlopen(req)
strw=webpage.read()
tg_start=strw.find('hotplaySvList = [')
if tg_start==-1:
	print 'not find start tag'
	os.exit()
tmp=strw[tg_start:-1]

tg_end=tmp.find(';')
if tg_end==-1 :
	print 'not find end tag'
	os.exit()
tmp=tmp[len(' hotplaySvList = ['):tg_end]
print tmp
tar_ls=tmp.split(r'},{')
dict_film={}
for t0 in tar_ls:
	ls_t=t0.split(',')
	id=ls_t[0].split(':')[1].strip()
	film=ls_t[-1].split('"')[-2].strip()
	dict_film[id]=film
for t in dict_film:
	print "id: "+t+"  film:  " + dict_film[t]
print 'ok  total : '+`len(dict_film)`
 
print 'hello'




