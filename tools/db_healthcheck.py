# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : db_monitor.py
'''

import MySQLdb
import ConfigParser

def cnf(path):
    ini_dict={}
    try:
        cnf=ConfigParser.SafeConfigParser()
        cnf.read(path)
        cs=cnf.sections()
        for i in cs:
            ci=cnf.items(i)
            ini_dict[i]=dict(ci)
    except ConfigParser.ParsingError,e:
        print u"error is %s" %e

    finally:
        return ini_dict

def conn(data,sql):
    resdata=()
    rowcount=()
    description=()
    name=data['name']
    ip = data['ip']
    port=int(data['port'])
    user=data['user']
    pwd=data['pwd']
    db=data['db']
    conn = MySQLdb.connect(host=ip, port=port, user=user, passwd=pwd,db=db,connect_timeout=10)
    try:
        cur = conn.cursor()
        cur.execute(sql)
        resdata = cur.fetchall()
        rowcount=cur.rowcount
        description=cur.description
        return resdata,rowcount,description
    except Exception, e:
        # print 'conn error is:%s' % e
        return e,'error','error'
    finally:
        # print conn.ping()
        if conn.ping():
            conn.close()
            # print name, 'close conn'
        return  resdata,rowcount,description
def live_check(data):
    try:
        for i in (data):
            # print i,ini_dict[i]
            sql='select 1'
            res,rc,desc=conn(data[i],sql)
            if int(res[0][0]) ==1:
                print data[i]['ip'],'is','ok'
    except Exception,e:
        print data[i]['ip'],'is',e
    finally:
        print 'end'
def slave_check(data):
    try:
        for i in (data):
            # print i,ini_dict[i]
            sql='show slave status'
            res,rc,desc=conn(data[i],sql)

            if rc==0:
                print data[i]['ip'], 'is master'
                print 'pass'

                sql='show processlist'
            else:
                print data[i]['ip'], 'is slave'
                desc=map(lambda x: x[0],desc)
                res=list(res[0])
                dict_res=dict(zip(desc,res))
                print dict_res['Last_IO_Errno']
                print dict_res['Last_SQL_Errno']
                print dict_res['Last_Error']
                print dict_res['Last_SQL_Error']
    except Exception,e:
        print data[i]['ip'],'is',e
    finally:
        print 'end'

path='test_db.ini'
ini_dict=cnf(path)
# live_check(ini_dict)
slave_check(ini_dict)

