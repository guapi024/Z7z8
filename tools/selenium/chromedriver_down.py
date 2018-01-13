# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : chromedriver_down.py
'''
from selenium import webdriver
import re
import os,datetime,logging,sys
import urllib2
from selenium import webdriver
logdt=datetime.datetime.now().strftime('%Y%m%d')
sep=os.sep
logdir=os.getcwd()+"%slog%s"  %(sep,sep)
datadir=os.getcwd()+"%sdata%s"  %(sep,sep)
# print logdir
if os.path.exists(logdir)==False:
    os.mkdir(logdir)
else:
    pass
if os.path.exists(datadir)==False:
    os.mkdir(datadir)
else:
    pass
logfile=logdir+os.path.split(os.path.realpath( sys.argv[0]))[-1].split('.')[0]+logdt+".log"
logging.basicConfig(level=logging.DEBUG,
                    format='"%(asctime)s","%(filename)s","%(module)s","%(funcName)s","%(lineno)d","%(thread)d","%(threadName)s","%(process)d","%(levelno)s","%(levelname)s","%(relativeCreated)d","%(name)s","%(message)s"',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=logfile,
                    filemode='a')
driver = webdriver.Chrome()
downurl='http://chromedriver.storage.googleapis.com/index.html'
driver.get(downurl)
print driver.title  # 把页面title 打印出来
import  time
time.sleep(1)
res_data=driver.page_source
import re
reg = r'<a href="(.path.*?)">'
# print   res_data
res_versions=re.findall(reg,res_data,re.S)
for res_version in res_versions:
    # res_version='?path=2.0/'
    downurl = 'http://chromedriver.storage.googleapis.com/index.html'
    driver.get(downurl+res_version)
    import  time
    time.sleep(1)
    res_data=driver.page_source
    reg = r'<tbody>(.*?)</tbody>'
    # print   res_data
    a=re.findall(reg,res_data,re.S)
    down_all = a[0].split("<tr>")
    for i in down_all[4:-1]:
        reg = r'a href="(.*?)"'
        down = re.findall(reg, i, re.S)
        # print i
        reg = r'pre>(.*?)</pre>'
        pre = re.findall(reg, i, re.S)
        reg = r'<td align="right">(.*?)</td><td'
        dt = re.findall(reg, i, re.S)
        # print dt[0]
        reg = r'<td align="right">(.*)</td><td'
        size = re.findall(reg, i, re.S)
        size = size[0].replace("</td><td align=\"right\">", ",")
        filename = down[0].split("/")
        filename.remove(u'')
        msg=filename[0]+filename[1]+size.split(",")[0]+size.split(",")[1]+pre[0]
        down_url = "http://chromedriver.storage.googleapis.com" + "/" + filename[0] + "/" + filename[1]
        print down_url
        logging.info('start')
        logging.info(msg)
        logging.info(down_url)
        f = urllib2.urlopen(down_url)
        down_version=datadir+sep+sep+filename[0]
        print   down_version
        if os.path.exists(down_version) == False:
            os.mkdir(down_version)
        else:
            pass
        downname=down_version+sep+sep+filename[1]
        print   downname
        start_dt = datetime.datetime.now()
        msg = 'start:' + str(start_dt)
        logging.info(msg)
        try:
            with open(downname, "wb") as code:
                code.write(f.read())
        except Exception,e:
            logging.info(e)
        logging.info('end')
        end_dt = datetime.datetime.now()
        msg = 'start:' + str(start_dt) + ',' + 'end:' + str(end_dt) + ',execute:' + str(end_dt - start_dt)
        logging.info(msg)
