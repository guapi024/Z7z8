# -*- coding: utf-8 -*-
'''
__author__ : renou
'''

import random
import time

import scrapy


class lianjia_sh_Spider(scrapy.Spider):
    name = "lianjia_sh"
    allowed_domains = ["sh.lianjia.com"]
    start_urls = ["http://sh.lianjia.com/ershoufang/d01g100","http://sh.lianjia.com/ershoufang/gumei/g100"]
    def parse(self, response):
        filename = response.url.split("/")[-2]
        ss=1
        for res in response.xpath('//ul[@class="js_fang_list"]//li'):
            ss += 1
            url= res.xpath('.//div[@class="info"]//a/@href').extract()[0]  ##url link /ershoufang/sh4702459.html
            url_uq=url
            # # title =地铁直达，低区出入方便，装修精美，满5年
            title=str(res.xpath('.//div[@class="info"]//a/@title').extract()).decode("unicode-escape")  ##title 地铁直达，低区出入方便，装修精美，满5年
            # # text =4室2厅 | 148.49平| 低区/20层| 朝南
            text=res.xpath('.//div[@class="info"]//span[@class="info-col row1-text"]/text()').extract()[1].replace("\t","").replace("\n","")  ##4室2厅 | 148.49平| 低区/20层| 朝南
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
            # # tag1 = scrapy.Field()  ##满五
            tag1= res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract()[0]
            # # tag2 = scrapy.Field()  ##有钥匙
            tag2= res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract()[1]
            # # tag3 = scrapy.Field()  ##距离1号线共康路站316米
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
                'text':text,# = scrapy.Field()  ##4室2厅 | 148.49平| 低区/20层| 朝南
                'price':price,# = scrapy.Field()  ##960 万
                'xiaoqu':xiaoqu,# = scrapy.Field()  ##span虹延小区
                'xiaoqu_link':xiaoqu_link,# = scrapy.Field()  ##/xiaoqu/5011000015991.html
                'area':area,# = scrapy.Field()  ## 长宁
                'area_link':area_link,# = scrapy.Field()  ##/ershoufang/changning/
                'area_town':area_town,# = scrapy.Field()  ##泗泾
                'area_town_link':area_town_link,# = scrapy.Field()  ##/ershoufang/sijing/
                'create_time':create_time,# = scrapy.Field()  ##|2012年建
                'price_minor':price_minor,#= scrapy.Field()  ##单价31280元/平
                'text1':text.split("|")[0],
                'text2':text.split("|")[1],
                'text3':text.split("|")[-2],
                'text4':text.split("|")[-1],

            }
            url_dir=r'D:\pc\pc\note\Python\test\scrapy\tutorial\tutorial\\'+str(int(res.xpath('//span[@class="current"]/text()').extract()[0]))+".txt"
        end_page= res.xpath('//div[@class="c-pagination"]/a/text()').extract()[-1]##下一页
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
            sleep_time=random.randint(1, 1)
            for sleep_time_i in range(1,sleep_time):
                # print u'随机等待'
                print sleep_time-sleep_time_i
                time.sleep(1)
            print u'0',sleep_time
            # yield scrapy.Request(next_page,callback=self.parse)
        else:
            print u'最后一页'




