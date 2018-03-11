# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : get_urls.py
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2,re,os,datetime,json,time
from lxml import etree
exec_dict={}
def choice_agent():
    agents = [
        "Dalvik/1.6.0 (Linux; U; Android 4.4; Nexus 5 Build/KRT16M)",
        "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Redmi 3S MIUI/7.3.9)",
        "JUC (Linux; U; 2.3.7; zh-cn; MB200; 320*480) UCWEB7.9.3.103/139/999",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (Linux; Android 4.4.4; en-us; Nexus 5 Build/JOP40D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2307.2 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-N9200 Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.4 Chrome/38.0.2125.102 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.94 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043124 Safari/537.36 MicroMessenger/6.5.7.1041 NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3S Build/MMB29M) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.3 Mobile Safari/537.36",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.1812",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/1A542a Safari/419.3",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; en-us) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B206 Safari/7534.48.3 XiaoMi/MiuiBrowser/8.7.0",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        "Openwave/ UCWEB7.0.2.37/28/999",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Opera/9.25 (Windows NT 5.1; U; en)",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "UCWEB7.0.2.37/28/999",
    ]
    import random
    agent_one = random.choice(agents)
    return agent_one
def res_data(url):
    try:
        response = urllib2.urlopen(url,timeout=30)
        if response.getcode() == 200:
            data = response.read()
            return data
        else:
            print 'error',response.getcode()
    except urllib2.URLError,e:
            try_t = True
            try_t_s = 0
            while try_t:
                try:
                    print   'try'*30,try_t_s,url
                    response = urllib2.urlopen(url,timeout=30+10*try_t_s)
                    if response.getcode() == 200:
                        data = response.read()
                        return data
                    else:
                        print 'error', response.getcode(),'try ',try_t_s,' s'
                except urllib2.URLError, e:
                    print 'error:',url,e
                try_t_s += 1
                if try_t_s == 3:
                    try_t = False
def get_urls(url):
    g_urls= {"create_dt":str(datetime.datetime.now()),}
    g_pro_name=url.split("/")[2].split(".")[0]
    g_pro_type = url.split("/")[-2]
    g_base_url = url.replace("/" + g_pro_type + "/", "")
    data = res_data(url)
    tree = etree.HTML(data)

    if  g_pro_name in ['bj']:
        area_list=tree.xpath('//div[@class="sub_nav section_sub_nav"]/a')
    elif    g_pro_name in ['sh','su']:
        xpath_reg_area='//div[@data-role="%s"]//div/a'%g_pro_type
        area_list=tree.xpath(xpath_reg_area)


    for area in area_list:
        area_sum = {}
        area_name = area.xpath('./text()')[0]
        area = area.xpath('./@href')[0]
        if g_pro_type in  area:
            if area in ['https://lf.lianjia.com/ershoufang/yanjiao/','https://lf.lianjia.com/ershoufang/xianghe/']:
                area_url=area
                g_base_url = "https://lf.lianjia.com"
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
    if os.path.exists(filename):
        pass
    else:
        data_key = ','.join(data[data.keys()[0]].keys())

        with open(filename,'ab') as file_write:
            file_write.write(data_key)
            file_write.write('\n')
    with open(filename,'ab') as file_write:
        for data_key in data.keys():
            data_values = '"' + '","'.join(data[data_key].values()) + '"'
            file_write.write(data_values+"\n")

def get_data(url,url_name,sum,file_dt,down_sum):
    try:
        get_data_start=datetime.datetime.now()
        url_name_area=url_name
        url_name_town = url.split("/")[-1]
        g_pro_type = url.split("/")[-3]
        # print   g_pro_type
        file_type = '_'.join(url.split("/")[2:4]).replace(".lianjia.com", "")
        data=res_data(url)
        tree = etree.HTML(data)
        info_dict={}
        seq_sum_i=0
        start_page=url[0:(11+len('lianjia.com'))]
        search_result = tree.xpath('//div[@class="resultDes clear"]//span/text()')[0] #area sum
        if int(search_result)==0:
            pass
        else:
            xpath_reg_area = '//div[@data-role="%s"]/div/a[@class="selected"]' % g_pro_type ## ershoufang
            selected=tree.xpath(xpath_reg_area)
            if  len(selected)==2:
                selected_area_name_u=selected[0].xpath('./text()')[0] #姑苏 area
                selected_area_name=selected[0].xpath('./@href')[0]  #/ershoufang/gusu/
                selected_town_name_u=selected[1].xpath('./text()')[0] #十全街 town
                selected_town_name=selected[1].xpath('./@href')[0]#/ershoufang/shiquanjie1/
            page_sum=tree.xpath('//div[@class="page-box house-lst-page-box"]/@page-data')[0].encode('utf-8')
            page_sum_dict = json.loads(page_sum)
            page_sum_dict_totalPage=page_sum_dict["totalPage"]
            page_sum_dict_curPage=page_sum_dict["curPage"]
            sellListContent = tree.xpath('.//ul[@class="sellListContent"]/li')
            if len(sellListContent) == 0:
                sellListContent = tree.xpath('.//ul[@class="sellListContent LOGVIEWDATA"]/li')
            sellListContent_dict={}
            clear_sum=0
            url_p=url.split("/")[2].split(".")[0]
            if url_p in ['bj']:
                sellListContent=tree.xpath('//li[@class="clear"]')
            for clear in sellListContent:
                clear_dict={}
                title_housecode = clear.xpath('.//div[@class="title"]/a/@data-housecode')  ##107002155593
                if len(title_housecode) == 0:
                    title_housecode = clear.xpath('.//div[@class="title"]/a/@data-lj_action_housedel_id')[0]
                else:
                    title_housecode = clear.xpath('.//div[@class="title"]/a/@data-housecode')[0]
                clear_dict["title_housecode"] = title_housecode
                title_href= clear.xpath('.//div[@class="title"]/a/@href')[0] #https://su.lianjia.com/ershoufang/107000997409.html
                clear_dict["title_href"]=title_href
                title_text= clear.xpath('.//div[@class="title"]/a/text()')[0] #钟楼新村 4室2厅 184万
                clear_dict["title_text"] = title_text
                address_href= clear.xpath('.//div[@class="address"]/div/a/@href')[0] #https://su.lianjia.com/xiaoqu/239821887922515/
                clear_dict["address_href"] = address_href
                address_text= clear.xpath('.//div[@class="address"]/div/a/text()')[0] #钟楼新村
                clear_dict["address_text"] = address_text
                flood_text= clear.xpath('.//div[@class="flood"]/div/text()')[0]#中楼层(共4层)2000年建平房  -
                clear_dict["flood_text"] = flood_text
                flood_href= clear.xpath('.//div[@class="flood"]/div/a/@href')[0]#https://su.lianjia.com/ershoufang/shiquanjie1/
                clear_dict["flood_href"] = flood_href
                flood_area= clear.xpath('.//div[@class="flood"]/div/a/text()')[0]#十全街
                clear_dict["flood_area"] = flood_area
                if url_p in ['bj']:
                    followInfo_sum_people=clear.xpath('.//div[@class="followInfo"]/text()')[0]
                    followInfo_sum_see=clear.xpath('.//div[@class="followInfo"]/text()')[1]
                    followInfo_release=clear.xpath('.//div[@class="timeInfo"]/text()')[0]
                else:
                    followInfo_text = clear.xpath('.//div[@class="followInfo"]/text()')[0]  # 8人关注 / 共2次带看 / 4个月以前发布
                    followInfo = followInfo_text.split("/")
                    followInfo_sum_people = followInfo[0]
                    followInfo_sum_see = followInfo[1]
                    followInfo_release = followInfo[-1]
                clear_dict["followInfo_sum_people"] = followInfo_sum_people
                clear_dict["followInfo_sum_see"] = followInfo_sum_see
                clear_dict["followInfo_release"] = followInfo_release

                subway=clear.xpath('.//span[@class="subway"]/text()')
                haskey=clear.xpath('.//span[@class="haskey"]/text()')
                taxfree=clear.xpath('.//span[@class="taxfree"]/text()')
                if len(subway)!=0:
                    subway= subway[0] ##距离1号线相门站192米
                    clear_dict["subway"] = subway
                else:
                    clear_dict["subway"] = ''
                if len(haskey)!=0:
                    haskey= haskey[0] ##随时看房
                    clear_dict["haskey"] = haskey
                else:
                    clear_dict["haskey"] = ''
                if len(taxfree)!=0:
                    taxfree= taxfree[0] ##随时看房
                    clear_dict["taxfree"] = taxfree
                else:
                    clear_dict["taxfree"] = '' ##房本满五年
                totalPrice_text= clear.xpath('.//div[@class="totalPrice"]/span/text()')[0]#378
                clear_dict["totalPrice_text"] = totalPrice_text
                totalPrice_href= clear.xpath('.//div[@class="totalPrice"]/text()')[0]#万
                clear_dict["totalPrice_href"] = totalPrice_href
                unitPrice_text= clear.xpath('.//div[@class="unitPrice"]/span/text()')[0]#单价30265元/平米
                clear_dict["unitPrice_text"] = unitPrice_text
                unitPrice_href= clear.xpath('.//div[@class="houseInfo"]/a/@href')[0]  ##东小桥弄散盘
                # clear_dict["unitPrice_href"] = unitPrice_href
                houseInfo_a_text= clear.xpath('.//div[@class="houseInfo"]/a/text()')[0]##东小桥弄散盘
                clear_dict["houseInfo_a_text"] = houseInfo_a_text
                if url_p in ['bj']:
                    houseInfo_text_split= clear.xpath('.//div[@class="houseInfo"]/text()')[0:5]
                else:
                    houseInfo_text= clear.xpath('.//div[@class="houseInfo"]/text()')[0]# | 2室2厅 | 114平米 | 南 | 精装 | 无电梯
                    houseInfo_text_split = houseInfo_text.split("|")
                    houseInfo_text_split.remove(houseInfo_text_split[0])
                houseInfo_text_type=houseInfo_text_split[0] ##2室1厅
                clear_dict["houseInfo_text_type"] = houseInfo_text_type
                houseInfo_text_size=houseInfo_text_split[1] ##47.39平米
                clear_dict["houseInfo_text_size"] = houseInfo_text_size
                houseInfo_text_major=houseInfo_text_split[2] ##南
                clear_dict["houseInfo_text_major"] = houseInfo_text_major
                houseInfo_text_style=houseInfo_text_split[3] ##精装
                clear_dict["houseInfo_text_style"] = houseInfo_text_style
                if len(houseInfo_text_split)>4:
                    houseInfo_text_eve=houseInfo_text_split[-1] ##无电梯
                else:
                    houseInfo_text_eve=u'未知' ##无电梯
                clear_dict["houseInfo_text_eve"] = houseInfo_text_eve
                sellListContent_dict[title_housecode] = clear_dict
                clear_sum+=1
            down_sum=down_sum+clear_sum
            filename = str(datetime.datetime.now().strftime('%Y_%m_%d')) + "_" + file_type + "_" + selected_area_name_u + "_" + selected_town_name_u + ".csv"
            save_csv(sellListContent_dict, filename, file_dt)
            get_data_end = datetime.datetime.now()
            msg = 'start:' + str(get_data_start) + ',' + 'end:' + str(get_data_end) + ',execute:' + str(get_data_end - get_data_start)
            down_sum=len(info_dict)+down_sum
            if  page_sum_dict_totalPage>page_sum_dict_curPage:
                next_page_i=page_sum_dict_curPage+1
                now_page=url.split("/")[-1]
                if now_page[0:2]=='pg':
                    next_page='pg%s' %next_page_i
                    next_url=url.replace(now_page,next_page)
                else:
                    next_url=url+'pg%s' % next_page_i
                # print next_url, url_name, sum, file_dt, down_sum
                print "%s:%s,%s,load_sum:%s,down_sum:%s,next url:%s" % (str(datetime.datetime.now()),selected_area_name_u, selected_town_name_u, search_result, down_sum,next_url)
                get_data(next_url, url_name, sum, file_dt, down_sum)
            # else:
                # print "%s,%s,%s,load_sum:%s,down_sum:%s,end" % (str(datetime.datetime.now()),selected_area_name_u, selected_town_name_u, search_result, down_sum)
                # pass
            if page_sum_dict_totalPage == page_sum_dict_curPage:
                print "%s,info all:%s,%s,load_sum:%s,down_sum:%s" % (str(datetime.datetime.now()),selected_area_name_u, selected_town_name_u, search_result, down_sum)
    except Exception,e:
        print url,url_name,sum,file_dt,down_sum,'error',e
def config(url):
    es_url_type = url.split("/")[-2]
    current_dir = os.getcwd()
    data_dir = current_dir + os.sep + "data"
    if os.path.exists(data_dir):
        pass
    else:
        os.mkdir(data_dir)
    file_type='_'.join(url.split("/")[2:4]).replace(".lianjia.com", "")
    filename = data_dir + os.sep + file_type + ".list"
    if os.path.exists(filename):
        urls = load_urls(filename)
        file_dt=urls["create_dt"]
        now_dt=datetime.datetime.now()
        file_dt=datetime.datetime.strptime(file_dt, "%Y-%m-%d %H:%M:%S.%f")
        diff_dt=now_dt-file_dt
        diff_s=diff_dt.days*24*60*60+diff_dt.seconds
        if  diff_s>=1*24*60*60: ##1 days
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
        es_url  =   "https://su.lianjia.com/ditiefang/"
        es_url = "https://bj.lianjia.com/ershoufang/"
        if len(sys.argv)>=2:
            es_url = sys.argv[1]
        file_dt = '_'.join(es_url.split("/")[2:4]).replace(".lianjia.com", "") + "_" + str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f_%p'))
        urls=config(es_url)
        if urls.has_key("create_dt"):
            urls.pop("create_dt")
        if urls.has_key("shanghaizhoubian"):
            urls.pop("shanghaizhoubian")
        urls_name_list=urls.keys()
        import multiprocessing
        pool = multiprocessing.Pool(processes=20)
        from multiprocessing import Process, Lock
        for url_name in urls_name_list:
            search_sum=urls[url_name]["search_sum"]
            url_list=urls[url_name]["list"]
            exec_dict[url_name]={"search_sum":search_sum}
            for url in url_list:
                pool.apply_async(get_data, args=(url,url_name,search_sum,file_dt,0,), )
                # print "%s,info start:url:%s,url_name:%s" % (str(datetime.datetime.now()),url,url_name)
        pool.close()
        pool.join()
        res_sum = dataset_config(file_dt)
        print "*"*30,'info',"*"*30
        for res_sum_name in res_sum.keys():
            if sys.platform == 'linux2':
                res_sum[res_sum_name.decode("utf-8")] = res_sum[res_sum_name]
            else:
                res_sum[res_sum_name.decode("gbk")] = res_sum[res_sum_name]
        load_sum = 0
        down_sum = 0
        for data_key in urls.keys():
            if res_sum.has_key(data_key):
                print data_key, 'load data sum', urls[data_key]["search_sum"], 'down data sum', res_sum[data_key]
                load_sum += int(urls[data_key]["search_sum"])
                down_sum += int(res_sum[data_key])
            else:
                print data_key, 'load data sum', urls[data_key]["search_sum"]
                load_sum += int(urls[data_key]["search_sum"])
        end_dt = datetime.datetime.now()
        msg = 'start:' + str(start_dt) + ',' + 'end:' + str(end_dt) + ',execute:' + str(end_dt - start_dt), 'total:load_sum', load_sum, ',down_sum', down_sum
        print   "msg:", msg
    except Exception,e:
        print 'error',e
    print   "all end",str(datetime.datetime.now())

