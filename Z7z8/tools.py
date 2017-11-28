# -*- coding: utf-8 -*-
'''
__author__ : renou
'''
import  os
import  json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

filename=r"D:\pc\pc\note\Python\github\Z7z8\Z7z8\data\2017_11_27.txt"
data={'tag': u'\u6ee1\u4e94,\u6709\u94a5\u5319', 'tag1': u'\u6ee1\u4e94', 'uq_url': u'sh4617612'}
lst = data
fp = open(filename, "ab")
fp.write(json.dumps(lst, ensure_ascii=False))
fp.write('\n')
fp.close()

#
# ##python 3
# file = open('test.json','w',encoding='utf-8')
# data1 = {'name':'john',"age":12}
# data2 = {'name':'merry',"age":13}
# data = [data1,data2]
# print(data)
# json.dump(data,file,ensure_ascii=False)
# file.close()
# file = open('test.json','r',encoding='utf-8')
# s = json.load(file)
# print (s[0]['name'])
