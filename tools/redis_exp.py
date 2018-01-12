# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : redis_exp.py
'''
import os,sys,redis,json,re,datetime,string,random,logging
##create log dt/dir/name
logdt=datetime.datetime.now().strftime('%Y%m%d')
sep=os.sep
logdir=os.getcwd()+"%slog%s"  %(sep,sep)
datadir=os.getcwd()+"%sdata%s"  %(sep,sep)
if os.path.exists(logdir)==False:
    os.mkdir(logdir)
else:
    pass
if os.path.exists(datadir)==False:
    os.mkdir(datadir)
else:
    pass

logfile=logdir+os.path.split(os.path.realpath( sys.argv[0]))[-1].split('.')[0]+logdt+".log"
datafile=datadir+os.path.split(os.path.realpath( sys.argv[0]))[-1].split('.')[0]+logdt+".json"
# print logfile
##pro use inof mode
logging.basicConfig(level=logging.DEBUG,
                    format='"%(asctime)s","%(filename)s","%(module)s","%(funcName)s","%(lineno)d","%(thread)d","%(threadName)s","%(process)d","%(levelno)s","%(levelname)s","%(relativeCreated)d","%(name)s","%(message)s"',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=logfile,
                    filemode='a')

class redis_exp(object):
    def __init__(self):
        self.key_dict={}
    def save2json(self,filename, filedata):
        try:
            with open(filename, 'ab') as file:
                json.dump(filedata, file)
                file.write('\n')
        except Exception, e:
            logging.info(e)
    def conn(self,ip,port,pwd,db):
        try:
            conn = redis.Redis(host=ip, port=port, password=pwd, charset='utf-8', db=db)
            return conn
        except Exception,e:
            logging.info(e)

    def load_data(self,conn):

        keys = conn.keys()
        key_dict={}
        key_dict['start_dt'] = str(datetime.datetime.now())
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
        key_dict['end_dt'] = str(datetime.datetime.now())
        return  key_dict
    def start(self,ip,port,pwd,db,filename):
        self.key_dict['start_dt'] = str(datetime.datetime.now())
        if ip=='':
            ip='127.0.0.1'
        if port=='':
            port=6379
        if pwd=='':
            pwd=''
        if db=='':
            try:
                conn=self.conn(ip,int(port),pwd,db)
                dbs=filter(lambda x: re.findall(r'db\d+', x, re.S) != [], conn.info().keys())
            except Exception,e:
                msg='error is %s,info(ip:%s,port:%s,pwd:%s,db:%s)'%(e,ip, int(port), pwd, db)
                logging.info(msg)
                dbs=['0']
        else:
            dbs=list(db)
        for db in  dbs:
            try:
                db=str(db).replace('db','')
                conn = self.conn(ip, int(port), pwd, db)
                keys_data=self.load_data(conn)
                # print db,keys_data
                self.key_dict[db]=keys_data
            except Exception,e:
                msg='error is %s,info(ip:%s,port:%s,pwd:%s,db:%s)'%(e,ip, int(port), pwd, db)
                logging.info(msg)
        filedt=datetime.datetime.now().strftime('%Y%m%d')
        if filename=='':
            filename='ip_'+ip+'_'+str(port)+'_'+'_'.join(dbs)+'_'+filedt+'.json'
            filename =filedt + ".json"
        else:
            filename=filename
        self.key_dict['end_dt']=str(datetime.datetime.now())
        self.key_dict['filename'] = filename
        self.save2json(filename,self.key_dict)
if __name__ == '__main__':
    log_start_dt=datetime.datetime.now()
    log_start_dt_msg = 'start:' + str(log_start_dt)
    logging.info(log_start_dt_msg)
    ip='127.0.0.1'
    # ip='118.126.108.44'
    port=''
    pwd=''
    db=''
    filename='xxx'
    mm=redis_exp()
    mm.start(ip,port,pwd,db,filename)
    log_end_dt = datetime.datetime.now()
    msg = 'start:' + str(log_start_dt) + ',' + 'end:' + str(log_end_dt) + ',execute:' + str(log_end_dt - log_start_dt)
    logging.info(msg)
