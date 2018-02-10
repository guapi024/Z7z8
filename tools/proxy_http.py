# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : proxy_http.py
'''

import random
import re
import sys
import urllib2
import tools_dict
import requests
import datetime
import json
from lxml import etree
class main(object):
        def __init__(self):
            global  urls
            urls={}
            urls["url_66ip"]="http://www.66ip.cn"
        def get_proxy_ips(self,ips):
            for key_name in urls:
                for seq in range(1,6):
                    # print seq
                    url=urls[key_name]+"/%s.html" %seq
                    data=self.get_proxy_data(key_name,url)
                    tree_data = etree.HTML(data)
                    xpath_data = tree_data.xpath('//*[@id="main"]/div/div[1]/table/tr')[1:]
                    for ip_data in xpath_data:
                        ip_data_list=ip_data.xpath('.//text()')
                        ips[ip_data_list[0]]=str(ip_data_list[0]+":"+ip_data_list[1])
            return ips
        def get_proxy_data(self,key_name,url):
            res_data=urllib2.urlopen(url)
            data=res_data.read()
            return data
        def get_ips_check(self,ip):
                testurl = "http://httpbin.org/get"
                try:
                    random_choice_user_agents = tools_dict.random_choice_user_agents
                    proxy = {'http': ip}
                    headers = {'User-Agent': random.choice(random_choice_user_agents)}
                    response = requests.get(testurl, headers=headers, proxies=proxy,timeout=10)
                    response.encoding = 'utf-8'
                    res= response.text
                    data=json.loads(res)
                    print ip,'ok',"origin is ",data["origin"]
                except Exception, e:
                    print ip,'fail'
                    # print e
        def config(self):
            ips={"dt":str(datetime.datetime.now()),}
            ips=self.get_proxy_ips(ips)
            # print ips
            import multiprocessing
            pool = multiprocessing.Pool(processes=20)
            from multiprocessing import Process, Lock
            for ips_name in ips.keys():
                if ips_name!="dt":
                    ip=ips[ips_name]
                    get_ips_check=self.get_ips_check(ip)
                    pool.apply_async(get_ips_check, args=(ip,), )
            pool.close()
            pool.join()

if __name__ == '__main__':
    proxy=main()
    proxy.config()


