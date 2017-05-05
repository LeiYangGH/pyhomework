#!/usr/bin/python3
import sys
import os
from datetime import datetime

#读入文件，写法需求文档已经有了，照抄
def get_data_list(file_name):
    data_file = open(file_name,"r")
    data_list = []
    for line_str in data_file:
        data_list.append(line_str.strip().split(r','))
    return data_list #返回的是每行，每单词的嵌套List

#计算一个月的平均
#cv_list是最后两列的值的集合
def get_onemonth_average(cv_list):
    s1 = 0
    s2 = 0
#下面完全按照公式计算
    for (strc,strv) in cv_list:
        c = float(strc)
        v = float(strv)
        s1 += c * v
        s2 += v
    return s1 / s2
   
#计算每个月的平均       
def get_monthly_averages(data_list):
    simple_lines = []
    for v in data_list:
        date = datetime.strptime(v[0], r'%Y/%m/%d')#通过格式转换为时间
        year_month = date.strftime('%Y') + date.strftime('%m')#得到年和月，因为需求说要按月统计
        simple_lines.append((year_month,(v[5],v[6])))#得到了年月、最后两列的集合
#下面这段是按月添加到字典，便于处理
    d = dict()
    for k,x in simple_lines:
        if(k in d):
            d[k].append(x)
        else:
            d[k] = [x]
    monthly_averages = []
    for k in d.keys():#遍历每个月
        r = get_onemonth_average(d[k])#计算月平均
        monthly_averages.append((k,r))
    return monthly_averages

#打印结果
def print_info(monthly_averages):
#排序，根据月平均
    monthly_averages.sort(key=lambda ma: ma[1])

    print('------Six worst------')
    print('Month \t average')
    for (month,r) in monthly_averages[0:6]:
         print(month + '\t' + str(r))
#倒过来
    monthly_averages.reverse();

    print()
    print('------Six Best------')
    print('Month \t average')
    for (month,r) in monthly_averages[0:6]:
         print(month + '\t' + str(r))
#下面是调用上面的函数
data_list = get_data_list(r'table.csv')
monthly_averages = get_monthly_averages(data_list)

print_info(monthly_averages)
