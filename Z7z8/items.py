# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Z7Z8Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class lianjia_ershoufang(scrapy.Item):
    uq_url = scrapy.Field() ##唯一标识
    url=scrapy.Field()##url link /ershoufang/sh4702459.html
    title=scrapy.Field()##title 地铁直达，低区出入方便，装修精美，满5年
    text=scrapy.Field()##4室2厅 | 148.49平| 低区/20层| 朝南
    price=scrapy.Field()##960 万
    xiaoqu=scrapy.Field()##span虹延小区
    xiaoqu_link=scrapy.Field()##/xiaoqu/5011000015991.html
    area=scrapy.Field()## 长宁
    area_link=scrapy.Field()##/ershoufang/changning/
    area_town=scrapy.Field()##泗泾
    area_town_link = scrapy.Field()##/ershoufang/sijing/
    create_time=scrapy.Field()##|2012年建
    price_minor=scrapy.Field()##单价31280元/平
    tag1=scrapy.Field()##满五
    tag2=scrapy.Field()##有钥匙
    tag3=scrapy.Field()##距离1号线共康路站316米