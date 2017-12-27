# -*- coding: utf-8 -*-
'''
__author__ : renou
'''
#scrapy
# http://scrapy-chs.readthedocs.io/zh_CN/0.24/

import  os
import platform
current_dir=os.getcwd()

print  "cd ",os.getcwd()
ps=platform.system()
pl=platform.architecture()
if ps=='Windows':
    print os.getcwd().split(":")[0]+":"
sc_name=['lianjia_sh']
for sc_name in sc_name:
    print "scrapy crawl %s" %sc_name


import datetime
start_dt=datetime.datetime.now()
end_dt=datetime.datetime.now()
print   end_dt-start_dt
