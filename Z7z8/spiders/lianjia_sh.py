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
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        # "http://www.renouh.com/"
        "http://sh.lianjia.com/ershoufang/d97g100",
        # "http://sh.lianjia.com/ershoufang/pg99",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
    #     filename = response.url.split(".")[-2]
    #     with open(filename, 'wb') as f:
    #          f.write(response.body)
        # print  response.body
        # for sel in response.xpath('//ul/li'):
        #     title = sel.xpath('a/text()').extract()
        #     link = sel.xpath('a/@href').extract()
        #     desc = sel.xpath('text()').extract()
        #     print title, link, desc

    # def parse(self, response):
    #     for res in response.xpath("//ul[@class='js_fang_list']//li"):
        ss=1
        for res in response.xpath('//ul[@class="js_fang_list"]//li'):

            # title = res.xpath('a/text()').extract()
            # link = res.xpath('a/@href').extract()
            # desc = res.xpath('text()').extract()
            # print  sel.extract(),i,'****************'
            # x= sel.extract()
            # info=res.extract()
            # test_1 = res.xpath("//div[@class='prop-title']//@href").extract()
            # test_3 = res.xpath("//div[@class='prop-title']//@href").extract()
            # test1=res.xpath('//a/@href').extract()
            # print  info,'******1'
            # print  (test1),'test1'
            # print  res,ss
            # print  res.xpath('a/@href').extract() ##url
            ##[u'/ershoufang/sh4603489.html']
            # print  res.xpath('.//div[@class="info"]//a/@href').extract()##link
            ##[u'/ershoufang/sh4860904.html', u'/xiaoqu/5011000013836.html', u'/ershoufang/yangpu/', u'/ershoufang/zhongyuan1/']
            # print  str(res.xpath('.//div[@class="info"]//a/@title').extract()).decode("unicode-escape")##title
            ##[u'厨卫全明，卧室带阳台，地铁直达，楼层好']
            # print res.xpath('.//div[@class="info"]//span[@class="info-col row1-text"]/text()').extract()[1].replace("\t","").replace("\n","")
            ##2室2厅 | 80.44平| 高区/6层| 朝南
            # print res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/text()').extract()[3].replace("\t", "").replace("\n", "").replace("|","")
            # area_name=res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/text()').extract()
            # print  area_name[0],area_name[1]
            ##宝山 杨行
            # area_link = res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/@href').extract()
            # print 'xiaoqu',area_link[0],area_link[1],area_link[2]
            ##/xiaoqu/5011000012404.html /ershoufang/baoshan/ /ershoufang/yanghang/
            # print res.xpath('.//div[@class="info"]//span[@class="total-price strong-num"]/text()').extract()[0].replace("\t","").replace("\n","")
            # print res.xpath('.//div[@class="info"]//span[@class="unit"]/text()').extract()[0].replace("\t","").replace("\n","")
            # print res.xpath('.//div[@class="info"]//span[@class="info-col price-item minor"]/text()').extract()[0].replace("\t","").replace("\n","")
            # tag=res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract()
            # print  tag[0],tag[1],tag[2]
            # new= res.xpath('.//div[@class="info"]//span[@class="c-prop-tag c-prop-tag--blue"]/text()').extract()
            # print  new
            # print res.xpath('.//img')
            # print res.xpath('.//img/@onerror').extract()
            # print res.xpath('.//img/@src').extract()
            # print res.xpath('.//img/@data-img-real').extract()
            # print res.xpath('.//img/@data-original').extract()
            # print res.xpath('.//img/@data-img-layout').extract()
            # print res.xpath('.//img/@alt').extract()

            ss += 1
        # end_page=res.xpath('//div[@class="c-pagination"]/a/@gahref').extract()
        # print  end_page,type(end_page)
        # print res.xpath('//div[@class="c-pagination"]/a/text()').extract()
        ##下一页 u'\u4e0b\u4e00\u9875'
        # print  response.xpath('//ul[@class="js_fang_list"]//li')
            # data1=str(sel.extract())+'\n'
            # self.into_file(filename,data1)
        # filename = response.url.split(".")[-2].replace("/","_")
        # for sel in response.xpath('//ul/li'):
        #     item = TutorialItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['desc'] = sel.xpath('text()').extract()
        #     self.into_file(filename,item)
        #     yield item

            # url =/ershoufang/sh4702459.html
            # print res.xpath('.//div[@class="info"]//a/@href').extract()[0]  ##url link /ershoufang/sh4702459.html
            # # title =地铁直达，低区出入方便，装修精美，满5年
            # print str(res.xpath('.//div[@class="info"]//a/@title').extract()).decode("unicode-escape")  ##title 地铁直达，低区出入方便，装修精美，满5年
            # # text =4室2厅 | 148.49平| 低区/20层| 朝南
            # print res.xpath('.//div[@class="info"]//span[@class="info-col row1-text"]/text()').extract()[1].replace("\t","").replace("\n","")  ##4室2厅 | 148.49平| 低区/20层| 朝南
            # # price =960 万
            # print res.xpath('.//div[@class="info"]//span[@class="total-price strong-num"]/text()').extract()[0].replace("\t","").replace("\n","")+res.xpath('.//div[@class="info"]//span[@class="unit"]/text()').extract()[0].replace("\t","").replace("\n","")  ##960 万
            # # xiaoqu = scrapy.Field()  ##span虹延小区
            # print res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]//@title').extract()[0]
            # # xiaoqu_link = scrapy.Field()  ##/xiaoqu/5011000015991.html
            # print res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/@href').extract()[0]
            # # area = scrapy.Field()  ## 长宁
            # print  res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/text()').extract()[0]
            #
            # # area_link = scrapy.Field()  ##/ershoufang/changning/
            # print  res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/@href').extract()[1]
            # # area_town = scrapy.Field()  ##泗泾
            # print  res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/text()').extract()[1]
            # # area_town_link = scrapy.Field()  ##/ershoufang/sijing/
            # print  res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/a/@href').extract()[2]
            # # create_time = scrapy.Field()  ##|2012年建
            # print  res.xpath('.//div[@class="info"]//span[@class="info-col row2-text"]/text()').extract()[3].replace("\t","").replace("\n","").replace("|","").replace(" ","")
            # # price_minor = scrapy.Field()  ##单价31280元/平
            # print res.xpath('.//div[@class="info"]//span[@class="info-col price-item minor"]/text()').extract()[0].replace("\t", "").replace("\n", "")
            # # tag1 = scrapy.Field()  ##满五
            # print res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract()[0]
            # # tag2 = scrapy.Field()  ##有钥匙
            # print res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract()[1]
            # # tag3 = scrapy.Field()  ##距离1号线共康路站316米
            # print ','.join(res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract())
            # print res.xpath('.//div[@class="info"]//div[@class="info-col price-item main"]/span/text()').extract()
            ##title
            # print  res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract()[0]
            yield {
                'uq_url': res.xpath('.//div[@class="info"]//a/@href').extract()[0].split(".")[-2].split("/")[-1],#'uq_url': u'sh4628068'
                'tag':','.join(res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract()),
                'tag1': res.xpath('.//div[@class="info"]//span[@class="c-prop-tag2"]/text()').extract()[0],
            }
            url_dir=r'D:\pc\pc\note\Python\test\scrapy\tutorial\tutorial\\'+str(int(res.xpath('//span[@class="current"]/text()').extract()[0]))+".txt"

            # self.into_file(url_dir,res.xpath('.//div[@class="info"]//a/@href').extract()[0].split(".")[-2].split("/")[-1])

        end_page= res.xpath('//div[@class="c-pagination"]/a/text()').extract()[-1]##下一页
        # print  res.xpath('//span[@class="current"]/text()').extract() ##当前页
        # print res.xpath('//div[@class="c-pagination"]/a/@href').extract()[-1]##下一页链接
        start_page='http://sh.lianjia.com'

        if end_page==u'下一页'or end_page==u'\u4e0b\u4e00\u9875':
            print u'继续爬'
            now_page=int(res.xpath('//span[@class="current"]/text()').extract()[0])
            current_page=int(res.xpath('//span[@class="current"]/text()').extract()[0])+1
            page_url=res.xpath('//div[@class="c-pagination"]/a/@href').extract()[-1]
            print u'当前页',str(start_page)+str(page_url).replace(u"d"+str(current_page),u"d"+str(now_page))
            print u'下一页',str(start_page)+str(res.xpath('//div[@class="c-pagination"]/a/@href').extract()[-1])
            next_page=response.urljoin(str(start_page)+str(res.xpath('//div[@class="c-pagination"]/a/@href').extract()[-1]))
            # print   next_page,'next_page'
            # next_page="http://sh.lianjia.com/ershoufang/d91g100"
            ##random
            print u'随机等待'
            sleep_time=random.randint(1, 1)
            for sleep_time_i in range(1,sleep_time):
                # print u'随机等待'
                print sleep_time-sleep_time_i,
                time.sleep(1)
            print u'0'
            # yield scrapy.Request(next_page,callback=self.parse)
        else:
            print u'最后一页'




'''

cd D:\pc\pc\note\Python\test\github\Z7z8
D:
scrapy crawl lianjia_sh

'''