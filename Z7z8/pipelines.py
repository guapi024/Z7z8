# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import  os,datetime,csv,time
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

class save_json(object):
    def __init__(self):
        pass
    def to_txt(self,data,filename):
        try:
            file = open(filename, 'ab')
            if len(data)==0:
                pass
            else:
                # print data
                file.writelines(str(data)+ '\n')
                xx= data['tag1']
                print xx,file.write(xx)
        except Exception, e:
            print e
        finally:
            file.close()


    def process_item(self, item, spider):
        current_dir = os.getcwd()
        data_dir = current_dir + "\\" + "data"
        # print  data_dir
        if os.path.exists(data_dir):
            pass
        else:
            os.mkdir(data_dir)
        line = [item['uq_url']]
        line=item
        # print line,"url"
        file_name=datetime.datetime.now().strftime( '%Y_%m_%d' )
        self.to_txt(line,data_dir+"\\"+file_name+".txt")

        return item

##test
# test=save_json()
# item={'uq_url':u'sh4637210'}
# test.process_item(item,'')

#
# file_name=datetime.datetime.now().strftime( '%Y_%m_%d_%H_%M_%S_%f' )
# file_name=datetime.datetime.now().strftime( '%Y_%m_%d' )
# print   file_name


