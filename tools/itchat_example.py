# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : itchat_example.py
'''
import json
import itchat
import numpy as np
import pandas as pd
from collections import defaultdict
import re
import jieba
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
def save2json(filename, filedata):
    try:
        with open(filename, 'wb') as file:
            json.dump(filedata, file)
            file.write('\n')
    except Exception, e:
        print e
        file.write(e)
def save_data(filename):
    ##hotReload 该参数生成一个静态文件itchat.pkl用于存储登录状态
    itchat.auto_login(hotReload=True)
    # 爬取自己好友相关信息， 返回一个json文件
    ##保存刚刚爬取的json文件方便后续分析
    friends = itchat.get_friends(update=True)[0:]
    save2json(filename,friends)

filename = 'itchat_example.json'

##第一次运行保存数据，以后只需要读取本地文件简化相应操作
# save_data(filename)
data = json.load(file(filename))
# test_data=data[9]
# for i in test_data.keys():
#     print i,test_data[i]
# pd.set_option('display.height',2000)
# pd.set_option('display.max_rows',500)
# pd.set_option('display.max_columns',500)
# pd.set_option('display.width',2000)
df = pd.DataFrame(data)
# df.info()



##性别
df_p=df["Sex"]
df_p=df_p.replace(1,u"男")
df_p=df_p.replace(2,u"女")
df_p=df_p.replace(0,u"未知")
# print   df_p
df_count=df_p.value_counts()

x1=[x for x,y in df_count.iteritems()]
y1=[y for x,y in df_count.iteritems()]
labels = [u'{}:{}'.format(city, value) for city, value in df_count.iteritems()]

df_count.plot(kind="bar")

plt.rcParams['font.sans-serif'] = ['SimHei']
fig = plt.figure(figsize=(9,9))
ax1 = fig.add_subplot(111)
ax1.set_title(u'性别饼图')
ax1.pie(y1, labels = labels, autopct="%5.2f%%", pctdistance=0.6,shadow=True, labeldistance=1.1, startangle=None, radius=None)



#省
df_p=df["Province"]
df_p=df_p.replace("",u"未知")
df_count=df_p.value_counts()
x1=[x for x,y in df_count.iteritems()]
y1=[y for x,y in df_count.iteritems()]
labels = [u'{}:{}'.format(city, value) for city, value in df_count.iteritems()]
plt.rcParams['font.sans-serif'] = ['SimHei']
fig = plt.figure(figsize=(16,16))
ax1 = fig.add_subplot(111)
ax1.set_title(u'省份饼图')
ax1.pie(y1, labels = labels, autopct="%5.2f%%", pctdistance=0.6,shadow=True, labeldistance=1.1, startangle=None, radius=None)
plt.axis('equal')
plt.show()

