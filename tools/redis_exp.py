# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : redis_exp.py
'''
import redis,json,re
import string,random
import  re
import datetime,sys
def save2json(filename,filedata):
    try:
        with open(filename, 'ab') as file:
            json.dump(filedata, file)
            file.write('\n')
    except Exception,e:
        print e









class redis_exp(object):
    def __init__(self):
        self.key_dict={}
    def save2json(self,filename, filedata):
        try:
            with open(filename, 'ab') as file:
                json.dump(filedata, file)
                file.write('\n')
        except Exception, e:
            print e
    def conn(self,ip,port,pwd,db):
        conn = redis.Redis(host=ip, port=port, password=pwd, charset='utf-8', db=db)
        # print conn.info()
        return conn
    def load_data(self,conn):
        keys = conn.keys()
        conn_info = conn.info()
        yy = map(lambda x: re.findall(r'db\d+', x, re.S), conn_info.keys())
        print filter(lambda x: re.findall(r'db\d+', x, re.S) != [], conn_info.keys())
        key_dict=self.key_dict
        for key in keys:
            try:
                k = str(key)
                if conn.type(k) == 'string':
                    key_dict[conn.type(k) + '_' + k] = conn.get(k)
                if conn.type(k) == 'hash':
                    key_dict[conn.type(k) + '_' + k] = conn.hgetall(k)
                if conn.type(k) == 'list':
                    key_dict[conn.type(k) + '_' + k] = conn.lrange(k, 0, -1)
                if conn.type(k) == 'set':
                    key_dict[conn.type(k) + '_' + k] = str(conn.smembers(k))
                if conn.type(k) == 'zset':
                    key_dict[conn.type(k) + '_' + k] = conn.zrange(k, 0, -1, withscores=True)
                if key_dict.has_key('sum_' + conn.type(k)):
                    key_dict['sum_' + conn.type(k)] = key_dict['sum_' + conn.type(k)] + 1
                else:
                    key_dict['sum_' + conn.type(k)] = 1
            except redis.ResponseError, e:
                key_dict['error' + str(key)] = e
        return  key_dict
    def start(self,ip,port,pwd,db):
        if port=='':
            port=6379
        if pwd=='':
            pwd=''
        if db=='':
            conn=self.conn(ip,int(port),pwd,db)
            dbs=filter(lambda x: re.findall(r'db\d+', x, re.S) != [], conn.info().keys())
        for db in  dbs:
            try:
                db=str(db).replace('db','')
                # print db,type(db),str(db).replace('db','')
                conn = self.conn(ip, int(port), pwd, db)
                keys_data=self.load_data(conn)
                print keys_data
            except Exception,e:
                print e


        logdt=datetime.datetime.now().strftime('%Y%m%d')
        filename =logdt + ".json"
        print logdt
        # print   key_dict
        # print save2json(filename,key_dict)
if __name__ == '__main__':
    ip='127.0.0.1'
    port=''
    pwd=''
    db=''
    mm=redis_exp()
    mm.start(ip,port,pwd,db)
