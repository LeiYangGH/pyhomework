#!/usr/bin/env python
# coding: UTF-8
import urllib2
import re
import os
import numpy as np
import pandas as pd

df20105=pd.read_csv('fbr_d_n_b.csv',names=['date','film','BoxOfficeReturn'])
#print df20105
df20105=df20105[df20105.BoxOfficeReturn.notnull()]
print df20105

val20105=df20105.values
lst00=[]
for i in range(0,len(val20105)):
    x = val20105[i][0] #请填入4位数字
    lx=x.split('-')
    lst00.append(lx[0]+lx[1]+lx[2])
df20105.index= lst00
df20105=df20105.drop(['date'],axis=0)



print  type(df20105)

df20105 = df20105.sort(['date'], ascending=[1])
print df20105

#df20105=df20105.filter(date='bbi', axis=0)

##curdir = os.getcwd()
##url = 'file:///' + os.path.join(curdir,u'www3\电影票房数据库.htm')
##print url

print 'hello'
