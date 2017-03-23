#!/usr/bin/env python
# coding: UTF-8
import urllib2
import re
import os
url=r'file:///C:/SDK/G/pyhomework/pymoviecontest/w/h.htm'
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




