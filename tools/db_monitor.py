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
path='test_db.ini'
ini_dict=cnf(path)


q='select * from mysql.user'
for i in (ini_dict):
    # print i,ini_dict[i]
    name=ini_dict[i]['name']
    ip = ini_dict[i]['ip']
    port=int(ini_dict[i]['port'])
    user=ini_dict[i]['user']
    pwd=ini_dict[i]['pwd']
    db=ini_dict[i]['db']
    print name,ip,port,user,pwd,db
    try:

        print name,'start conn'
        conn = MySQLdb.connect(host=ip, port=port, user=user, passwd=pwd,db=db,connect_timeout=10)
        cur = conn.cursor()
        cur.execute(q)
        resdata = cur.fetchall()
        print 'rowcount',cur.rowcount
        print resdata,'resdata'
        # print cur.description,'description'

    except conn.Error, e:
        print 'conn error is:%s' % e
    finally:
        while conn.ping():
            conn.close()
            print name, 'close conn'

print 'ok'
# =cnf.options(cs[0])
# info={}

# for i in co:
#     print i,cnf.get(cs[0],i)
#     info[i]=cnf.get(cs[0],i)
#     i=cnf.get(cs[0],i)
# h=info['hostip']
# P=int(info['port'])
# u=info['user']
# p=info['pwd']
q='select * from mysql.user'
# try:
#     mysql_connect = MySQLdb.connect(host=h, port=P, user=u, passwd=p, connect_timeout=10)
#     cur = mysql_connect.cursor()
#     cur.execute(q)
#     resdata = cur.fetchall()
#     print resdata#,cur.description
# except Exception, e:
#     print 'connect error is:%s' % e
def conn(data):
    pass
def is_live(ini_dict):
    for i in (ini_dict):
        # print i,ini_dict[i]
        name = ini_dict[i]['name']
        ip = ini_dict[i]['ip']
        port = int(ini_dict[i]['port'])
        user = ini_dict[i]['user']
        pwd = ini_dict[i]['pwd']
        db = ini_dict[i]['db']
        print name, ip, port, user, pwd, db
        try:
            print name, 'start conn'
            conn = MySQLdb.connect(host=ip, port=port, user=user, passwd=pwd, db=db, connect_timeout=10)
            cur = conn.cursor()
            cur.execute(q)
            resdata = cur.fetchall()
            print resdata  # ,cur.description
        except Exception, e:
            print 'conn error is:%s' % e
        finally:
            while conn.ping():
                conn.close()
                print name, 'close conn'

def slave_check():
    pass

