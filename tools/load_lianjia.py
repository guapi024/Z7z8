# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : get_urls.py
'''
import urllib2,re,os,datetime,json,time
from lxml import etree

exec_dict={}
def res_data(url):
    agents = []
    import random
    agent_one=random.choice(agents)
    timeout=10
    # request_headers={ 'User-Agent':agent_one}
    # print   request_headers
    # res = urllib2.urlopen(url,timeout=timeout)
    # data = res.read()
    # print "status",url,res.getcode()
    # req = urllib2.Request(url)
    # req.add_header('User-Agent',agent_one)
    try:
        request_headers = {'User-Agent': agent_one}
        request = urllib2.Request(url, None, request_headers)
        response = urllib2.urlopen(request,timeout=timeout)
        print "Url: %s\t%s" % (url, response.getcode())
        data = response.read()
        # print data
        return data
    except urllib2.URLError as e:
        if hasattr(e, 'code'):
            print "Url: %s\t%s" % (url, e.code)
        elif hasattr(e, 'reason'):
            print "Url: %s\t%s" % (url, 'error')
    except:
        pass
    finally:
        if response:
            response.close()

def get_urls(es_url):
    urls = {}
    es_rep = es_url.split("/")[-2]
    base_url = es_url.replace("/" + es_rep + "/", "")
    es_url_type = es_url.split("/")[-2]
    data = res_data(es_url)
    tree = etree.HTML(data)
    for area in tree.xpath('//div[@class="level1"]/a'):
        area_sum = {}
        area = area.xpath('./@href')
        if area[0] != "/"+es_url_type+"/" and area != ['/ershoufang/shanghaizhoubian'] and es_url_type in area[0] :
            area_url = str(base_url + area[0])
            data = res_data(area_url)
            tree = etree.HTML(data)
            search_result = tree.xpath('//div[@class="search-result"]//span/text()')
            town_urls = []
            for town in tree.xpath('//div[@class="level2-item"]/a'):
                town = town.xpath('./@href')
                if town != area:
                    town_url = str(base_url + town[0])
                    town_urls.append(town_url)
            area_sum["search_sum"]=search_result[0]
            area_sum["list"]=town_urls
        urls[area[0].split("/")[-1]]=area_sum
    if urls.has_key(""):
            urls.pop("")
    # print urls
    return  urls
def load_urls(filename):
    with open(filename, 'r') as fb:
        urls = json.load(fb)
    return  urls
def save_json(data,filename):
    fp = open(filename, "ab")
    fp.write(json.dumps(data, ensure_ascii=False))
    fp.close()
def save_csv(data,filename):
    # print filename,'1'
    current_dir = os.getcwd()
    data_dir = current_dir+os.sep + "data"+os.sep
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

def get_data(url,url_name,sum):
    data=res_data(url)
    tree = etree.HTML(data)
    info_dict={}
    seq_sum_i=0
    start_page=url[0:(10+len('lianjia.com'))]
    #  = tree.xpath('//div[@class="search-result"]//span')
    search_result=tree.xpath('//div[@class="search-result"]//span/text()')[0]
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
    filename=str(datetime.datetime.now().strftime( '%Y_%m_%d' ))+"_"+url.split("/")[1]+"_"+area_link.split("/")[-2]+"_"+area_town_link.split("/")[-2]+".csv"
        # print   filename
    save_csv(info_dict, filename)
    print next_page, 'next'
    get_data(next_page, url_name, sum)

def config(url):
    es_url_type = es_url.split("/")[-2]
    current_dir = os.getcwd()
    data_dir = current_dir + os.sep + "data"
    if os.path.exists(data_dir):
        pass
    else:
        os.mkdir(data_dir)
    filename = data_dir + os.sep + es_url_type + ".list"
    if os.path.exists(filename):
        urls = load_urls(filename)
    else:
        urls = get_urls(es_url)
        save_json(urls, filename)
    return urls
if __name__ == '__main__':
    try:
        es_url = "http://su.lianjia.com/ershoufang/"
        urls=config(es_url)
        urls_name_list=urls.keys()
        if "" in  urls_name_list:
            urls_name_list.remove("")
        import multiprocessing
        pool = multiprocessing.Pool(processes=20)
        from multiprocessing import Process, Lock
        for url_name in urls_name_list:
            search_sum=urls[url_name]["search_sum"]
            url_list=urls[url_name]["list"]
            exec_dict[url_name]={"search_sum":search_sum}
            # print   exec_dict
            for url in url_list:
                pool.apply_async(get_data, args=(url,url_name,search_sum), )
                print url, url_name, search_sum
        pool.close()
        pool.join()
    except Exception,e:
        print e





# if os.path.exists(urls_name):
#         pass
# else:
#
# fp=open(urls_name)
# urls=fp.readlines()
#

