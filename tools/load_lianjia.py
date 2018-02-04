# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : get_urls.py
'''
import urllib2,re,os,datetime,json,time
from lxml import etree
exec_dict={}
def res_data(url):
    try:
        response = urllib2.urlopen(url,timeout=30)
        if response.getcode() == 200:
            data = response.read()
        return data
    except urllib2.URLError,e:
        ##try 3 time
            try_t = True
            try_t_s = 0
            while try_t:
                try:
                    print   '*'*30,try_t_s
                    response = urllib2.urlopen(url,timeout=30+30*try_t_s)
                    data = response.read()
                    return data
                except urllib2.URLError, e:
                    print 'error:',url,e
                try_t_s += 1
                if try_t_s == 3:
                    try_t = False

    ##choise agent one
    # agents = [
    #     "Dalvik/1.6.0 (Linux; U; Android 4.4; Nexus 5 Build/KRT16M)",
    #     "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi 3S MIUI/7.3.9)",
    #     "JUC (Linux; U; 2.3.7; zh-cn; MB200; 320*480) UCWEB7.9.3.103/139/999",
    #     "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    #     "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    #     "Mozilla/5.0 (Linux; Android 4.4.4; en-us; Nexus 5 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Mobile Safari/537.36",
    #     "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N9200 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.4 Chrome/38.0.2125.102 Mobile Safari/537.36",
    #     "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.94 Mobile Safari/537.36",
    #     "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043124 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/WIFI Language/zh_CN",
    #     "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    #     "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    #     "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3S Build/MMB29M) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
    #     "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.3 Mobile Safari/537.36",
    #     "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.1812",
    #     "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    #     "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    #     "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3",
    #     "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7",
    #     "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    #     "Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; en-us) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3 XiaoMi/MiuiBrowser/8.7.0",
    #     "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    #     "NOKIA5700/ UCWEB7.0.2.37/28/999",
    #     "Openwave/ UCWEB7.0.2.37/28/999",
    #     "Opera/8.0 (Windows NT 5.1; U; en)",
    #     "Opera/9.25 (Windows NT 5.1; U; en)",
    #     "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    #     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    #     "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    #     "UCWEB7.0.2.37/28/999",
    # ]
    # import random
    # agent_one = random.choice(agents)
    # timeout = 10
    # try:
    #     request_headers = {'User-Agent': agent_one}
    #     request = urllib2.Request(url, None, request_headers)
    #     response = urllib2.urlopen(request, timeout=timeout)
    #     if response.getcode() == 200:
    #         data = response.read()
    #         # print data
    # except urllib2.URLError as e:
    #     ##try 3 time
    #     try_t = True
    #     try_t_s = 0
    #     while try_t:
    #         try:
    #             print try_t_s
    #             response = urllib2.urlopen(url)
    #             data = response.read()
    #             # print data
    #         except urllib2.URLError, e:
    #             pass
    #         try_t_s += 1
    #         if try_t_s == 3:
    #             try_t = False
    # finally:
    #     return data
def get_urls(es_url):
    g_urls= {"create_dt":str(datetime.datetime.now()),}
    g_pro_name=es_url.split("/")[2].split(".")[0]
    g_pro_type = es_url.split("/")[-2]
    g_base_url = es_url.replace("/" + g_pro_type + "/", "")
    data = res_data(es_url)
    tree = etree.HTML(data)
    if  g_pro_name in ['bj']:
        area_list=tree.xpath('//div[@class="sub_nav section_sub_nav"]/a')
    elif    g_pro_name in ['sh','su']:
        xpath_reg_area='//div[@data-role="%s"]/div/a'%g_pro_type
        area_list=tree.xpath(xpath_reg_area)
    for area in area_list:
        area_sum = {}
        area_name = area.xpath('./text()')[0]
        area = area.xpath('./@href')[0]
        if g_pro_type in  area:
            if area in ['https://lf.lianjia.com/ershoufang/yanjiao/','https://lf.lianjia.com/ershoufang/xianghe/']:
                area_url=area
            else:
                area_url = str(g_base_url + area)
            area_data = res_data(area_url)
            area_tree = etree.HTML(area_data)
            search_result = area_tree.xpath('//div[@class="resultDes clear"]//span/text()')[0]
            if g_pro_name in ['bj']:
                town_list=area_tree.xpath('//div[@class="sub_sub_nav section_sub_sub_nav"]/a')
            elif    g_pro_name in ['sh','su']:
                xpath_reg_town = '//div[@data-role="%s"]/div' % g_pro_type
                town_list = area_tree.xpath(xpath_reg_town)[1].xpath('./a')
            if area in ['https://lf.lianjia.com/ershoufang/yanjiao/', 'https://lf.lianjia.com/ershoufang/xianghe/']:
                town_list = area_tree.xpath('//div[@data-role="ershoufang"]/div')[1].xpath('./a')
            town_urls = []
            town_detail={}
            for town in town_list:
                        town_name = town.xpath('./@href')
                        town_name_u_text=town.xpath('./text()')
                        town_url = str(g_base_url + town_name[0])
                        if  town_url!=area_url:
                            town_urls.append(town_url)
                            town_detail[town_name_u_text[0]]=town_url
            area_sum["search_sum"] = search_result
            area_sum["list"] = town_urls
            area_sum["detail"]=town_detail
        g_urls[area_name]=area_sum
    return g_urls
def load_urls(filename):
    with open(filename, 'r') as fb:
        urls = json.load(fb)
    return  urls
def save_json(data,filename):
    # print data
    with open(filename,'wb') as f_save_json:
        f_save_json.write(json.dumps(data))
        # f_save_json.write(json.dumps(data, ensure_ascii=False))
        # f_save_json.write(data)
def save_csv(data,filename,file_dt):
    current_dir = os.getcwd()
    data_dir = current_dir+os.sep + "data"+os.sep+file_dt+os.sep
    if os.path.exists(data_dir):
        pass
    else:
        os.mkdir(data_dir)
    filename=data_dir+filename
    # print   filename
    if os.path.exists(filename):
        pass
    else:
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        data_key = ','.join(data[data.keys()[0]].keys())
        # print data_key
        with open(filename,'ab') as file_write:
            file_write.write(data_key)
            file_write.write('\n')
    with open(filename,'ab') as file_write:
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        for data_key in data.keys():
            data_values = '"' + '","'.join(data[data_key].values()) + '"'
            file_write.write(data_values+"\n")

def get_data(url,url_name,sum,file_dt,down_sum):
    get_data_start=datetime.datetime.now()
    url_name_area=url_name
    if  down_sum>=30:
        url_name_town = url.split("/")[-2]
    else:
        url_name_town=url.split("/")[-1]
    file_type = '_'.join(url.split("/")[2:4]).replace(".lianjia.com", "")
    data=res_data(url)
    tree = etree.HTML(data)
    info_dict={}
    seq_sum_i=0
    start_page=url[0:(10+len('lianjia.com'))]
    #  = tree.xpath('//div[@class="search-result"]//span')
    search_result=tree.xpath('//div[@class="search-result"]//span/text()')[0]
    # print   search_result,url
    name_area=tree.xpath('//div[@class="level1"]//a[@class="level1-item on"]/text()')[-1]
    name_town = tree.xpath('//div[@class="level2 gio_plate"]//a[@class="on"]/text()')[-1]
    # print   name_area,name_town
    # print   search_result
    # search_result_sum = search_result.xpath('./text()')[0]
    # print   search_result_sum
    try:
        end_page= tree.xpath('//div[@class="c-pagination"]/a/text()')[-1]##下一页
    except Exception,e:
        end_page=u'error'
    if end_page==u'next_page'or end_page==u'\u4e0b\u4e00\u9875':
        # print u'继续爬'
        now_page=int(tree.xpath('//span[@class="current"]/text()')[0])
        current_page=int(tree.xpath('//span[@class="current"]/text()')[0])+1
        page_url=tree.xpath('//div[@class="c-pagination"]/a/@href')[-1]
        # print u'now_page',str(start_page)+str(page_url).replace(u"d"+str(current_page),u"d"+str(now_page))
        # print u'next_page',str(start_page)+str(tree.xpath('//div[@class="c-pagination"]/a/@href')[-1])
        next_page=str(start_page)+str(tree.xpath('//div[@class="c-pagination"]/a/@href')[-1])
        # print u'随机等待'
        # while end_page==u'下一页'or end_page==u'\u4e0b\u4e00\u9875':
    for res in tree.xpath('//ul[@class="js_fang_list"]//li'):
            seq_sum_i+=1
            url = res.xpath('.//div[@class="info"]//a/@href')[0]##url link /ershoufang/sh4702459.html
            url_uq = url
            # # # title =地铁直达，低区出入方便，装修精美，满5年
            title = str(res.xpath('.//div[@class="info"]//a/@title')).decode("unicode-escape")  ##title 地铁直达，低区出入方便，装修精美，满5年
            # print title
            # # # text =4室2厅 | 148.49平| 低区/20层| 朝南
            text = res.xpath('.//div[@class="info"]//span[@class="info-col row1-text"]/text()')[1].replace("\t","").replace("\n", "")  ##4室2厅 | 148.49平| 低区/20层| 朝南
            text = text.split("|")
            text_dict = {"text0": "", "text1": "", "text2": "", "text3": ""}
            for seq in range(len(text)):
                text_dict[str("text" + str(seq))] = text[seq]
            # # # price =960 万
            price = res.xpath('.//div[@class="info"]//span[@class="total-price strong-num"]/text()')[0].replace("\t","").replace("\n", "") + res.xpath('.//div[@class="info"]//span[@class="unit"]/text()')[0].replace("\t","").replace( "\n", "")  ##960 万
            # # xiaoqu = scrapy.Field()  ##span虹延小区
            xiaoqu = res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]//@title')[0]
            # # xiaoqu_link = scrapy.Field()  ##/xiaoqu/5011000015991.html
            xiaoqu_link = res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/@href')[0]
            # # area = scrapy.Field()  ## 长宁
            area = res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/text()')[0]
            # # area_link = scrapy.Field()  ##/ershoufang/changning/
            area_link = res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/@href')[1]
            # # area_town = scrapy.Field()  ##泗泾
            area_town = res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/text()')[1]
            # # area_town_link = scrapy.Field()  ##/ershoufang/sijing/
            area_town_link = res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/@href')[2]
            # # create_time = scrapy.Field()  ##|2012年建
            create_time = res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/text()')[-1].replace("\t", "").replace("\n", "").replace("|", "").replace(" ", "").replace(u"年建", "")
            # print res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/text()')[-1].replace("\t","").replace("\n","").replace("|","").replace(" ","")
            # # price_minor = scrapy.Field()  ##单价31280元/平
            price_minor = res.xpath('.//div[@class="info"]//span[@class="info-col price-item minor"]/text()')[0].replace("\t", "").replace("\n", "")
            tag = ','.join(res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()'))
            info_dict_one={
                'load_time': str(datetime.datetime.now()),
                'uq_url': url_uq,  # 'uq_url': u'sh4628068'
                'tag': tag,  # "tag": "满五,有钥匙"
                'url': url,  # = scrapy.Field()  ##url link /ershoufang/sh4702459.html
                'title': title,  # = scrapy.Field()  ##title 地铁直达，低区出入方便，装修精美，满5年
                # 'text':text,# = scrapy.Field()  ##4室2厅 | 148.49平| 低区/20层| 朝南
                'price': price,  # = scrapy.Field()  ##960 万
                'xiaoqu': xiaoqu,  # = scrapy.Field()  ##span虹延小区
                'xiaoqu_link': xiaoqu_link,  # = scrapy.Field()  ##/xiaoqu/5011000015991.html
                'area': area,  # = scrapy.Field()  ## 长宁
                'area_link': area_link,  # = scrapy.Field()  ##/ershoufang/changning/
                'area_town': area_town,  # = scrapy.Field()  ##泗泾
                'area_town_link': area_town_link,  # = scrapy.Field()  ##/ershoufang/sijing/
                'create_time': create_time,  # = scrapy.Field()  ##|2012年建
                'price_minor': price_minor,  # = scrapy.Field()  ##单价31280元/平
                'text0': text_dict["text0"],  # 4室2厅 | 148.49平| 低区/20层| 朝南
                'text1': text_dict["text1"],  # 4室2厅 | 148.49平| 低区/20层| 朝南
                'text2': text_dict["text2"],  # 4室2厅 | 148.49平| 低区/20层| 朝南
                'text3': text_dict["text3"],  # 4室2厅 | 148.49平| 低区/20层| 朝南
                'search_result_sum': search_result,
            }
            info_dict[url]=info_dict_one

    filename=str(datetime.datetime.now().strftime( '%Y_%m_%d' ))+"_"+file_type+"_"+area_link.split("/")[-2]+"_"+area_town_link.split("/")[-2]+".csv"
    filename = str(datetime.datetime.now().strftime('%Y_%m_%d')) + "_" + file_type + "_" + name_area + "_" + name_town + ".csv"
        # print   filename
    save_csv(info_dict, filename,file_dt)
    # print next_page, 'next'
    get_data_end = datetime.datetime.now()
    msg = 'start:' + str(get_data_start) + ',' + 'end:' + str(get_data_end) + ',execute:' + str(get_data_end - get_data_start)
    down_sum=len(info_dict)+down_sum
    print "%s,%s,load_sum:%s,down_sum:%s" %(name_area,name_town,search_result,down_sum)
    # try:
    #     print os.getpid(),os.getppid()
    # except Exception,e:
    #     pass
    get_data(next_page,url_name,sum,file_dt,down_sum)
    print "info_all,%s,%s,load_sum:%s,down_sum:%s" % (name_area, name_town, search_result, down_sum)
def config(url):
    es_url_type = es_url.split("/")[-2]
    current_dir = os.getcwd()
    data_dir = current_dir + os.sep + "data"
    if os.path.exists(data_dir):
        pass
    else:
        os.mkdir(data_dir)
    file_type='_'.join(es_url.split("/")[2:4]).replace(".lianjia.com", "")
    filename = data_dir + os.sep + file_type + ".list"
    if os.path.exists(filename):
        urls = load_urls(filename)
        file_dt=urls["create_dt"]
        now_dt=datetime.datetime.now()
        file_dt=datetime.datetime.strptime(file_dt, "%Y-%m-%d %H:%M:%S.%f")
        diff_dt=now_dt-file_dt
        diff_s=diff_dt.days*24*60*60+diff_dt.seconds
        if  diff_s>=1*24*60*60: ## days
            urls = get_urls(es_url)
            save_json(urls, filename)
    else:
        urls = get_urls(es_url)
        save_json(urls, filename)
    return urls
def dataset_config(file_dt):
    try:
        file_sum={}
        file_list=os.listdir(os.getcwd()+os.sep+"data"+os.sep+file_dt)
        # file_list = os.listdir(os.getcwd() + os.sep + file_dt)
        file_name=os.getcwd() + os.sep +"data"+os.sep+file_dt+"_all.csv"
        for file_one in file_list:
            file_one_name=os.getcwd() + os.sep +"data"+os.sep+ file_dt+os.sep+file_one
            with open(file_name, 'ab') as f_file_name:
                with open(file_one_name) as f_file_one_name:
                    data=f_file_one_name.readlines()[1:]
                    f_file_name.writelines(data)
            key_name=file_one.split("_")[5]
            if file_sum.has_key(key_name):
                file_sum[key_name]=file_sum[key_name]+(len(open(file_one_name).readlines()))-1
            else:
                file_sum[key_name] =len(open(file_one_name).readlines()) - 1
        return file_sum
    except Exception,e:
        return file_sum
if __name__ == '__main__':
    start_dt = datetime.datetime.now()
    print   "start_dt:",start_dt
    try:
        # es_url = "http://bj.lianjia.com/ershoufang/"
        es_url  =   "http://su.lianjia.com/ditiefang/"
        es_url = "http://su.lianjia.com/ershoufang/"
        file_dt = '_'.join(es_url.split("/")[2:4]).replace(".lianjia.com", "") + "_" + str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f_%p'))
        urls=config(es_url)
        if urls.has_key("create_dt"):
            urls.pop("create_dt")
        if urls.has_key("shanghaizhoubian"):
            urls.pop("shanghaizhoubian")
        urls_name_list=urls.keys()
        # print urls_name_list
        import multiprocessing
        pool = multiprocessing.Pool(processes=20)
        from multiprocessing import Process, Lock
        for url_name in urls_name_list:
            search_sum=urls[url_name]["search_sum"]
            url_list=urls[url_name]["list"]
            exec_dict[url_name]={"search_sum":search_sum}
            for url in url_list:
                pool.apply_async(get_data, args=(url,url_name,search_sum,file_dt,0,), )
        pool.close()
        pool.join()
    except Exception,e:
        print e
    res_sum = dataset_config(file_dt)
    # print urls
    load_sum=0
    down_sum=0
    for data_key in urls.keys():
        if res_sum.has_key(data_key.encode("gbk")):
            print data_key, 'load data sum', urls[data_key]["search_sum"], 'down data sum', res_sum[data_key.encode("gbk")]
            load_sum += int(urls[data_key]["search_sum"])
            down_sum += int(res_sum[data_key.encode("gbk")])
        else:
            print data_key, 'load data sum', urls[data_key]["search_sum"]
            load_sum += int(urls[data_key]["search_sum"])
    end_dt = datetime.datetime.now()
    msg = 'start:' + str(start_dt) + ',' + 'end:' + str(end_dt) + ',execute:' + str(end_dt - start_dt),'total:load_sum',load_sum,',down_sum',down_sum
    print   "all end_dt:",end_dt
    print   "msg:",msg
