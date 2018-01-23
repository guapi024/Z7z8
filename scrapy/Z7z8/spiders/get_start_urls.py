# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : get_start_urls.py
'''
#
# urls=[]
# base_url="http://sh.lianjia.com"
# es_url="http://sh.lianjia.com/ershoufang/"
# import urllib2,re
# from lxml import etree
# def res_data(url):
#     res=urllib2.urlopen(url)
#     data=res.read()
#     return data
# data=res_data(es_url)
# tree=etree.HTML(data)
# for area in tree.xpath('//div[@class="level1"]/a'):
#     area=area.xpath('./@href')
#     if area!=['/ershoufang/'] and area!=['/ershoufang/shanghaizhoubian']:
#         area_url=str(base_url+area[0])
#         # print area_url
#         area_url = "http://sh.lianjia.com/ershoufang/chongming"
#         data = res_data(area_url)
#         tree = etree.HTML(data)
#         for town in tree.xpath('//div[@class="level2-item"]/a'):
#             town = town.xpath('./@href')
#             if town != area:
#                 town_url = str(base_url + town[0])
#                 # print town_url
#                 urls.append(town_url)
# urls=list(set(urls))
# print urls

