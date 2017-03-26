#!/usr/bin/env python
# coding: UTF-8
import urllib2
import re
import os
import numpy as np
import pandas as pd

df20105=pd.read_csv('fbr_d_n_b.csv',names=['date','film','BoxOfficeReturn'])
print df20105
df20105=df20105[df20105.BoxOfficeReturn.notnull()]
print u'删除NaN的行---------------'
print df20105

val20105=df20105.values
lst00=[]
for i in range(0,len(val20105)):
    x = val20105[i][0] #请填入4位数字
    lx=x.split('-')
    lst00.append(lx[0]+lx[1]+lx[2])
df20105.index= lst00
df20105=df20105.drop(['date'],axis=0)
print u'更换索引日期格式---------------'
print df20105

print u'输出数据类型---------------'
print  type(df20105)

#df20105 = df20105.sort(['date'], ascending=[1])
df20105 = df20105.sort_values(by='date')
print u'按日期排序---------------'
print df20105

print u'票房大于1亿---------------'
dfbig=df20105[(df20105['BoxOfficeReturn'] > 100000)]
print dfbig

dfrzdf=df20105[(df20105['film'] == r'让子弹飞')]
print u'让子弹飞---------------'
print dfrzdf


print 'hello'
