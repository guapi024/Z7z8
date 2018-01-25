# -*- coding: utf-8 -*-
'''
__author__ : renou
'''

import random
import time

import scrapy


class lianjia_sh_Spider(scrapy.Spider):
    # import re
    # def res_data(url):
    #     import urllib2
    #     res = urllib2.urlopen(url)
    #     data = res.read()
    #     return data
    # urls = []
    # base_url = "http://sh.lianjia.com"
    # es_url = "http://sh.lianjia.com/ershoufang/"
    # import urllib2, re
    # from lxml import etree
    # data = res_data(es_url)
    # tree = etree.HTML(data)
    # for area in tree.xpath('//div[@class="level1"]/a'):
    #     area = area.xpath('./@href')
    #     if area != ['/ershoufang/'] and area != ['/ershoufang/shanghaizhoubian']:
    #         area_url = str(base_url + area[0])
    #         # print area_url
    #         # area_url = "http://sh.lianjia.com/ershoufang/chongming"
    #         data = res_data(area_url)
    #         tree = etree.HTML(data)
    #         for town in tree.xpath('//div[@class="level2-item"]/a'):
    #             town = town.xpath('./@href')
    #             if town != area:
    #                 town_url = str(base_url + town[0])
    #                 # print town_url
    #                 urls.append(town_url)
    # urls = list(set(urls))
    # import os
    # current_dir = os.getcwd()
    # data_dir = current_dir + os.sep + "data"
    # urls_name = data_dir + os.sep + "url.list"
    # if os.path.exists(urls_name):
    #     pass
    # else:
    #     fp = open(urls_name, "ab")
    #     for url_list in urls:
    #         fp.write(url_list)
    #         fp.write('\n')
    #     fp.close()
    name = "lianjia_sh"
    allowed_domains = ["sh.lianjia.com"]
    start_urls = ["http://sh.lianjia.com/ershoufang/baozhen/"]
    # start_urls=urls

    def parse(self, response):
        filename = response.url.split("/")[-2]
        ss=1
        search_result = response.xpath('//div[@class="search-result"]//span')
        search_result_sum = search_result.xpath('./text()').extract()[0]
        search_area_xp=response.xpath('//div[@class="location-child"]//div')
        search_area=search_area_xp.xpath('//div[@class="level1-item on"]//a').extract()
        search_town=""
        print   'xxxxx',search_area_xp
        for res in response.xpath('//ul[@class="js_fang_list"]//li'):
            ss += 1
            url= res.xpath('.//div[@class="info"]//a/@href').extract()[0]  ##url link /ershoufang/sh4702459.html
            url_uq=url
            # # title =地铁直达，低区出入方便，装修精美，满5年
            title=str(res.xpath('.//div[@class="info"]//a/@title').extract()).decode("unicode-escape")  ##title 地铁直达，低区出入方便，装修精美，满5年
            # # text =4室2厅 | 148.49平| 低区/20层| 朝南
            text=res.xpath('.//div[@class="info"]//span[@class="info-col row1-text"]/text()').extract()[1].replace("\t","").replace("\n","")  ##4室2厅 | 148.49平| 低区/20层| 朝南
            text = text.split("|")
            text_dict = {"text0":"","text1":"","text2":"","text3":""}
            for seq in range(len(text)):
                text_dict[str("text" + str(seq))] = text[seq]
            # # price =960 万
            price=res.xpath('.//div[@class="info"]//span[@class="total-price strong-num"]/text()').extract()[0].replace("\t","").replace("\n","")+res.xpath('.//div[@class="info"]//span[@class="unit"]/text()').extract()[0].replace("\t","").replace("\n","")  ##960 万
            # # xiaoqu = scrapy.Field()  ##span虹延小区
            xiaoqu=res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]//@title').extract()[0]
            # # xiaoqu_link = scrapy.Field()  ##/xiaoqu/5011000015991.html
            xiaoqu_link =res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/@href').extract()[0]
            # # area = scrapy.Field()  ## 长宁
            area=res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/text()').extract()[0]
            #
            # # area_link = scrapy.Field()  ##/ershoufang/changning/
            area_link=res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/@href').extract()[1]
            # # area_town = scrapy.Field()  ##泗泾
            area_town=res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/text()').extract()[1]
            # # area_town_link = scrapy.Field()  ##/ershoufang/sijing/
            area_town_link= res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/@href').extract()[2]
            # # create_time = scrapy.Field()  ##|2012年建
            create_time=  res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/text()').extract()[-1].replace("\t","").replace("\n","").replace("|","").replace(" ","").replace(u"年建","")
            # print res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/text()').extract()[-1].replace("\t","").replace("\n","").replace("|","").replace(" ","")
            # # price_minor = scrapy.Field()  ##单价31280元/平
            price_minor= res.xpath('.//div[@class="info"]//span[@class="info-col price-item minor"]/text()').extract()[0].replace("\t", "").replace("\n", "")
            tag= ','.join(res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract())
            # print res.xpath('.//div[@class="info"]//div[@class="info-col price-item main"]/span/text()').extract()
            ##title
            # print  res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract()[0]


            import datetime
            yield {
                'load_time':str(datetime.datetime.now()),
                'uq_url':url_uq,#'uq_url': u'sh4628068'
                'tag':tag, #"tag": "满五,有钥匙"
                'url':url,#= scrapy.Field()  ##url link /ershoufang/sh4702459.html
                'title':title,# = scrapy.Field()  ##title 地铁直达，低区出入方便，装修精美，满5年
                # 'text':text,# = scrapy.Field()  ##4室2厅 | 148.49平| 低区/20层| 朝南
                'price':price,# = scrapy.Field()  ##960 万
                'xiaoqu':xiaoqu,# = scrapy.Field()  ##span虹延小区
                'xiaoqu_link':xiaoqu_link,# = scrapy.Field()  ##/xiaoqu/5011000015991.html
                'area':area,# = scrapy.Field()  ## 长宁
                'area_link':area_link,# = scrapy.Field()  ##/ershoufang/changning/
                'area_town':area_town,# = scrapy.Field()  ##泗泾
                'area_town_link':area_town_link,# = scrapy.Field()  ##/ershoufang/sijing/
                'create_time':create_time,# = scrapy.Field()  ##|2012年建
                'price_minor':price_minor,#= scrapy.Field()  ##单价31280元/平
                'text0':text_dict["text0"],#4室2厅 | 148.49平| 低区/20层| 朝南
                'text1':text_dict["text1"],#4室2厅 | 148.49平| 低区/20层| 朝南
                'text2':text_dict["text2"],#4室2厅 | 148.49平| 低区/20层| 朝南
                'text3':text_dict["text3"],#4室2厅 | 148.49平| 低区/20层| 朝南
                'search_result_sum':search_result_sum,
            }
            url_dir=r'D:\pc\pc\note\Python\test\scrapy\tutorial\tutorial\\'+str(int(res.xpath('//span[@class="current"]/text()').extract()[0]))+".txt"
        try:
            end_page= res.xpath('//div[@class="c-pagination"]/a/text()').extract()[-1]##下一页
        except Exception,e:
            # print e
            end_page=u'error'
        start_page='http://sh.lianjia.com'

        if end_page==u'下一页'or end_page==u'\u4e0b\u4e00\u9875':
            print u'继续爬'
            now_page=int(res.xpath('//span[@class="current"]/text()').extract()[0])
            current_page=int(res.xpath('//span[@class="current"]/text()').extract()[0])+1
            page_url=res.xpath('//div[@class="c-pagination"]/a/@href').extract()[-1]
            print u'当前页',str(start_page)+str(page_url).replace(u"d"+str(current_page),u"d"+str(now_page))
            print u'下一页',str(start_page)+str(res.xpath('//div[@class="c-pagination"]/a/@href').extract()[-1])
            next_page=response.urljoin(str(start_page)+str(res.xpath('//div[@class="c-pagination"]/a/@href').extract()[-1]))
            print u'随机等待'

            # sleep_time=random.random()
            # time.sleep(sleep_time)
            # print u'随机等待',sleep_time
            # sleep_time=random.randint(1, 1)
            # for sleep_time_i in range(1,sleep_time):
            #     # print u'随机等待'
            #     print sleep_time-sleep_time_i
            #     time.sleep(1)
            # print u'0',sleep_time
            # yield scrapy.Request(next_page,callback=self.parse)
        else:
            print u'最后一页'




