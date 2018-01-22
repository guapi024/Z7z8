# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  os,datetime,csv,time,json
class Z7Z8Pipeline(object):
    def process_item(self, item, spider):
        return item

# import pymysql as db
# class BooksPipeline(object):
#     def __init__(self):
#         self.con=db.connect(user="root",passwd="123",host="localhost",db="python",charset="utf8")
#         self.cur=self.con.cursor()
#         self.cur.execute('drop table douban_books')
#         self.cur.execute("create table douban_books(id int auto_increment primary key,book_name varchar(200),book_star varchar(244),book_pl varchar(244),book_author varchar(200),book_publish varchar(200),book_date varchar(200),book_price varchar(200))")
#     def process_item(self, item, spider):
#         self.cur.execute("insert into douban_books(id,book_name,book_star,book_pl,book_author,book_publish,book_date,book_price) values(NULL,%s,%s,%s,%s,%s,%s,%s)",(item['book_name'],item['book_star'],item['book_pl'],item['book_author'],item['book_publish'],item['book_date'],item['book_price']))
#         self.con.commit()
#         return item
#

#
# from scrapy.conf import settings
# #from scrapy import log
# import pymongo
# from openpyxl import Workbook
#
# class LagouPipeline(object):
#     def __init__(self):
#         self.server = settings['MONGODB_SERVER']
#         self.port = settings['MONGODB_PORT']
#         self.db = settings['MONGODB_DB']
#         self.tab = settings['MONGODB_COLLECTION']
#         connection = pymongo.MongoClient(self.server, self.port)
#         db = connection[self.db]
#         self.collection = db[self.tab]
#
#     def process_item(self, item, spider):
#         self.collection.insert(dict(item))
# #        log.msg('Item written to MongoDB database %s/%s' % (self.db, self.tab), level=log.DEBUG, spider=spider)
#         return item
#
# # #保存到xlsx

class save_file(object):
    def __init__(self):
        pass
    def to_txt(self,data,filename):
        # try:
        #     file = open(filename, 'ab')
        #     if len(data)==0:
        #         pass
        #     else:
        #         data_dist={}
        #         for i in data:
        #             data_dist[i]=data[i]
        #         data=json.dumps(data_dist,ensure_ascii=False)
        #         print  data
        # except Exception, e:
        #     print e
        # finally:
        #     file.close()
        # print  filename
        # print  data,type(data)
        # print json.dumps(data, encoding='UTF-8', ensure_ascii=False)
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        lst = data
        # lst=','.join(data.values())
        fp = open(filename, "ab")
        fp.write(json.dumps(lst, ensure_ascii=False))
        fp.write('\n')
        fp.close()
    def to_csv(self,data,filename):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')
        lst = '"' + '","'.join(data.values()) + '"'
        key_name=','.join(data.keys())
        if os.path.exists(filename):
            pass
        else:
            fp = open(filename, "ab")
            fp.write(key_name)
            fp.write('\n')
            fp.close()
        # lst=','.join(data.values())
        fp = open(filename, "ab")
        fp.write(lst)
        fp.write('\n')
        fp.close()
    def process_item(self, item, spider):
        current_dir = os.getcwd()
        data_dir = current_dir + "\\" + "data"
        if os.path.exists(data_dir):
            pass
        else:
            os.mkdir(data_dir)
        line=item
        file_name=datetime.datetime.now().strftime( '%Y_%m_%d' )
        # file_name=datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f_%p')
        # self.to_txt(line,data_dir+"\\"+file_name+".csv")
        self.to_csv(line, data_dir + "\\" + file_name + ".csv")
        return item



