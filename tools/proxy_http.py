# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : proxy_http.py
'''

import random,re,sys,urllib2,datetime,time,json
import tools_dict
import requests
from lxml import etree
def get_proxy_ips(ips):
    urls={
        "ip3366": {
                 'url': 'http://www.ip3366.net',
                'xpath_reg1': '//*[@id="list"]/table/tbody/tr',
                'xpath_reg2': './/text()',
                'url_reg':'?stype=1&page=',
                'ip_data_reg':'1',
                'ip_port_reg':'3',
                'end_paga':'10'
                },
        "66ip": {
                 'url': 'http://www.66ip.cn',
                'xpath_reg1': '//*[@id="main"]/div/div[1]/table/tr',
                'xpath_reg2': './/text()',
                'url_reg':'.html',
                'ip_data_reg':'0',
                'ip_port_reg':'1',
                'end_paga':'10'
                },
        "kuaidaili_inha": {
                'url': 'https://www.kuaidaili.com/free/inha',
                'xpath_reg1': '//*[@id="list"]/table/tbody/tr',
                'xpath_reg2': './/text()',
                'url_reg': '',
                'ip_data_reg':'1',
                'ip_port_reg':'3',
                'end_paga':'10'
        },
         "kuaidaili_intr": {
             'url': 'https://www.kuaidaili.com/free/intr',
             'xpath_reg1': '//*[@id="list"]/table/tbody/tr',
             'xpath_reg2': './/text()',
             'url_reg': '',
             'ip_data_reg': '1',
             'ip_port_reg': '3',
             'end_paga': '10'
         },
        "ip181": {
            'url': 'http://www.ip181.com/',
            'xpath_reg1': '/html/body/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr',
            'xpath_reg2': './/text()',
            'url_reg': '',
            'ip_data_reg': '1',
            'ip_port_reg': '3',
            'end_paga': '2'
        },
        "data5u_gngn": {
            'url': 'http://www.data5u.com/free/gngn/index.shtml',
            'xpath_reg1': '/html/body/div[5]/ul/li[2]/ul',
            'xpath_reg2': './/text()',
            'url_reg': '',
            'ip_data_reg': '1',
            'ip_port_reg': '3',
            'end_paga': '2'
        },
        "data5u_gnpt": {
            'url': 'http://www.data5u.com/free/gnpt/index.shtml',
            'xpath_reg1': '/html/body/div[5]/ul/li[2]/ul',
            'xpath_reg2': './/text()',
            'url_reg': '',
            'ip_data_reg': '1',
            'ip_port_reg': '3',
            'end_paga': '2'
        },
        "data5u_gwgn": {
            'url': 'http://www.data5u.com/free/gwgn/index.shtml',
            'xpath_reg1': '/html/body/div[5]/ul/li[2]/ul',
            'xpath_reg2': './/text()',
            'url_reg': '',
            'ip_data_reg': '1',
            'ip_port_reg': '3',
            'end_paga': '2'
        },
        "data5u_gwpt": {
            'url': 'http://www.data5u.com/free/gwpt/index.shtml',
            'xpath_reg1': '/html/body/div[5]/ul/li[2]/ul',
            'xpath_reg2': './/text()',
            'url_reg': '',
            'ip_data_reg': '1',
            'ip_port_reg': '3',
            'end_paga': '2'
        },
    }

    for key_name in urls:
        # print key_name,urls[key_name]
        url=urls[key_name]["url"]
        xpath_reg1 = urls[key_name]["xpath_reg1"]
        xpath_reg2 = urls[key_name]["xpath_reg2"]
        url_reg=urls[key_name]["url_reg"]
        ip_data_reg = int(urls[key_name]["ip_data_reg"])
        ip_port_reg = int(urls[key_name]["ip_port_reg"])
        end_paga = int(urls[key_name]["end_paga"])
        for seq in range(1,end_paga):
            try:
                if end_paga==2:
                    url_full=url
                else:
                    if key_name=='ip3366':
                        url_full = url + "/%s%s" % (url_reg,seq)
                    else:
                        url_full=url+"/%s%s" %(seq,url_reg)
                data=get_proxy_data(key_name,url_full)
                tree_data = etree.HTML(data)
                xpath_data = tree_data.xpath(xpath_reg1)[1:]
                for ip_data in xpath_data:
                    ip_data_list=ip_data.xpath(xpath_reg2)
                    ips[ip_data_list[ip_data_reg]]=str(ip_data_list[ip_data_reg]+":"+ip_data_list[ip_port_reg])
            except Exception,e:
                pass
    return ips

def get_proxy_data(key_name,url):
    try:
        random_choice_user_agents = tools_dict.random_choice_user_agents
        headers = {'User-Agent': random.choice(random_choice_user_agents)}
        req = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(req)
        if response.getcode() == 200:
            data = response.read()
            return data
    except urllib2.URLError,e:
        try_t = True
        try_t_s = 0
        while try_t:
            try:
                time.sleep(1)
                print   '*try*' * 30, try_t_s+1, url
                random_choice_user_agents = tools_dict.random_choice_user_agents
                headers = {'User-Agent': random.choice(random_choice_user_agents)}
                req = urllib2.Request(url, headers=headers)
                response = urllib2.urlopen(req, timeout=30 + 10 * try_t_s)
                if response.getcode() == 200:
                    data = response.read()
                    return data
                else:
                    print 'error', response.getcode(), 'try ', try_t_s, ' s'
            except urllib2.URLError, e:
                print 'error:', url, e
            try_t_s += 1
            if try_t_s == 3:
                try_t = False
def get_ips_check(ip):
        testurl = "http://httpbin.org/get"
        try:
            random_choice_user_agents = tools_dict.random_choice_user_agents
            proxy = {'http': ip}
            headers = {'User-Agent': random.choice(random_choice_user_agents)}
            response = requests.get(testurl, headers=headers, proxies=proxy,timeout=10)
            response.encoding = 'utf-8'
            res= response.text
            data=json.loads(res)
            if ip.split(":")[0] in data["origin"]:
                print ip,'ok'
        except Exception, e:
            get_ips_check_urllib2(ip)
def get_ips_check_urllib2(ip):
    testurl = "http://httpbin.org/get"
    try:
        random_choice_user_agents = tools_dict.random_choice_user_agents
        request = urllib2.Request(testurl)
        request.add_header('User-Agent', random.choice(random_choice_user_agents))
        request.add_header('Pragma', 'no-cache')
        request.set_proxy(ip,'http')
        opener = urllib2.build_opener()
        res = opener.open(request,timeout=10)
        ret_data = res.read()
        data = json.loads(ret_data)
        if ip.split(":")[0] in data["origin"]:
            print ip, 'ok'
    except urllib2.URLError,e:
        try_t = True
        try_t_s = 0
        while try_t:
            try:
                time.sleep(1)
                print   '*try*' * 30, try_t_s + 1,ip ,testurl
                random_choice_user_agents = tools_dict.random_choice_user_agents
                request = urllib2.Request(testurl)
                request.add_header('User-Agent', random.choice(random_choice_user_agents))
                request.add_header('Pragma', 'no-cache')
                request.set_proxy(ip, 'http')
                opener = urllib2.build_opener()
                res = opener.open(request, timeout=10+10*try_t_s)
                ret_data = res.read()
                data = json.loads(ret_data)
                if ip.split(":")[0] in data["origin"]:
                    print ip, 'ok'
                else:
                    print 'error', res.getcode(), 'try ', try_t_s, ' s'
            except urllib2.URLError, e:
                print 'error:', testurl, e
            try_t_s += 1
            if try_t_s == 3:
                try_t = False


def config():
    ips={"dt":str(datetime.datetime.now()),}
    ips=get_proxy_ips(ips)
    # ips["182.74.200.200:80"]="182.74.200.200:80"
    # print ips
    import multiprocessing
    pool = multiprocessing.Pool(processes=20)
    from multiprocessing import Process, Lock
    for ips_name in ips.keys():
        if ips_name!="dt":
            ip=ips[ips_name]
            # get_ips_check_urllib2(ip)
            ##choice
            pool.apply_async(get_ips_check_urllib2, args=(ip,), )
            # pool.apply_async(get_ips_check, args=(ip,), )
    pool.close()
    pool.join()
    #
if __name__ == '__main__':
    config()


