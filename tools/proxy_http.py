# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : proxy_http.py
'''

import urllib
import random
import re
import sys
# apiUrl="http://www.89ip.cn/apijk/?&tqsl=1000&sxa=&sxb=&tta=&ports=&ktip=&cf=1"
# res = urllib.urlopen(apiUrl).read()
# pt=re.compile(r'<BR>.*<BR>',re.S)
# ress=re.findall(pt,res)
# res=ress[0].split('<BR>')
# # print list(set(res))
# print len(res)
# while '' in res:
#     res.remove('')
# print res
# print len(res)

import requests
import urllib
import urllib2
import re
import tools_dict
class main(object):
        def __init__(self):
                self.random_choice_user_agents=tools_dict.random_choice_user_agents
                self.load_proxy_urls={}
                # self.load_proxy_urls["http://www.89ip.cn/apijk/?&tqsl=999999999&sxa=&sxb=&tta=&ports=&ktip=&cf=1"]="url_89ip"
                self.load_proxy_urls["http://www.xicidaili.com/nn/"]="url_xicidaili"
                self.load_proxy_urls["http://www.xicidaili.com/nt/"]="url_xicidaili"
                self.load_proxy_reg={}
                for name in self.load_proxy_urls.keys():
                        self.load_proxy_reg[self.load_proxy_urls[name]]=""
                self.load_proxy_reg['url_89ip']="r'\d+\.\d+.\d+.\d+:\d+'"
                self.load_proxy_reg['url_xicidaili'] = "r'\d+\.\d+.\d+.\d+"
        def get_proxy_ips(self):
                for ipname in self.load_proxy_urls.keys():
                        # print ipname,self.load_proxy_urls[ipname]
                        self.get_proxy_data(ipname, self.load_proxy_reg[self.load_proxy_urls[ipname]])
        def get_proxy_data(self,proxy_url,proxy_reg):
                print   proxy_url,proxy_reg
                res_data=urllib2.urlopen(proxy_url)
                # print res_data.read()
        def start(self):
                self.get_proxy_ips()

proxy=main()
print proxy
# proxy.start()

random_choice_ips=[]


# http://www.xicidaili.com/



# res_get,random_choice_url_one=random_choice_url(random_choice_urls)
# print res_get.status_code
# ip_re = re.findall(r'\d+\.\d+.\d+.\d+:\d+', res_get.text, re.S)
# # for ip in ip_re:
# #     random_choice_ips.append(ip.strip())
# random_choice_ips=map(lambda x:x,ip_re)
# random_choice_ip_one=random.choice(random_choice_ips)
# import datetime
# ip_dict={}
# ip_dict['time']=str(datetime.datetime.now())
# ip_dict['random_choice_ips']=random_choice_ips
# ip_dict['random_choice_url_one']=random_choice_url_one

random_choice_user_agents =tools_dict.random_choice_user_agents
# testurl="http://www.ip181.com/"
# testurl="https://www.baidu.com/s?ie=utf8&oe=utf8&wd=ip&tn=94749616_hao_pg&ch=3"
testurl='http://www.whatismyip.com.tw/'
testurl="http://ip.chinaz.com/getip.aspx"
# testurl="http://www.renouh.com"
# random_choice_ips=["110.73.3.198:8123",
# "24.113.137.207:53281","182.253.83.58:65205","173.249.15.109:3128","200.85.120.218:8080","172.93.111.106:1080","43.239.75.242:8080",
# "104.243.47.152:1080","182.253.176.170:3128","213.160.167.31:80","24.113.137.207:53281"
# ]
random_choice_ips=["110.136.233.160:80",]
for i in    random_choice_ips:
    # print i
    try:
        ip=i
        # print 'proxy:',ip
        proxy = {'http': ip}
        headers = {'User-Agent': random.choice(random_choice_user_agents)}
        # response = requests.get(testurl, headers =headers , proxies = proxy,)
        response = requests.get(testurl, headers=headers)
        # response.encoding = 'gbk'
        response.encoding = 'utf-8'
        # print response.status_code,response.text
        local_ip = re.findall(r'\d+\.\d+.\d+.\d+', response.text, re.S)
        # print local_ip
        print 'ok',local_ip
        print response.text
    except Exception,e:
        print 'fail',i,e
# import time
# for i in    random_choice_ips:
#     try:
#         s = requests.session()
#         api_url="http://www.xicidaili.com/nn"
#         # api_url="http://www.renouh.com"
#         proxy = {'http': i}
#         headers = {'User-Agent': random.choice(random_choice_user_agents)}
#         time.sleep(1)
#         response=requests.get(api_url, headers =headers ,timeout = 6)
#         print   response.status_code,'end'
#         s.keep_alive = False
#         # print response.status_code,'status_code'
#         # print   proxy, headers, 'end'
#     except Exception,e:
#         print 'error',e
#
# print time

