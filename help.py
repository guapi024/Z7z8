# -*- coding: utf-8 -*-
'''
__author__ : renou
'''
#scrapy
# http://scrapy-chs.readthedocs.io/zh_CN/0.24/

import  os
import platform
import  Z7z8.items
print dir(Z7z8.items),type(dir(Z7z8.items))


current_dir=os.getcwd()


##cmd

print  "cd ",os.getcwd()
ps=platform.system()
pl=platform.architecture()
if ps=='Windows':
    print os.getcwd().split(":")[0]+":"
sc_name=['lianjia_sh']
for sc_name in sc_name:
    print "scrapy crawl %s" %sc_name


