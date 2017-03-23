#!/usr/bin/env python
# coding: UTF-8
import urllib2
import re
import os
curdir = os.getcwd()
url = 'file:///' + os.path.join(curdir,u'www3\电影票房数据库.htm')
print url
BOR_amount=0.0
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
webpage= urllib2.urlopen(req)
strw=webpage.read()
s=strw.find("电影名称</th><th>总场次/占比")
e=strw[s:].find("各平台场次存在重叠，实时与预计票房为程序自行计算，仅供参考")
strw_tab=strw[s:s+e]
m=[]
m=re.findall(r'<tr class="[a-z]{3,4}"><td><a href="http://58921.com/film/[0-9]+/boxoffice" title=.+</tr>',strw_tab)
print '----------------------'
if not m:
        os.exit()
for t in m:
        print t
        ss=[]
        ss=re.findall(r'<td>([0-9.]+).*?</td>(?:<td>.*?</td>){2}\s*</tr>',t)
        if len(ss)==1:
                BOR_amount+= float(ss[0])
        else:
                print "error"
print "票房总额是:  "+str(BOR_amount)
print 'hello'
