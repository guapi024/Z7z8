# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : ml.py
'''

import  multiprocessing
import thread
import datetime,time,os,platform,sys
##TEST

if platform.system()=="Windows":
    datadir=os.getcwd()+"\\data"+"\\"
else:
    datadir = os.getcwd() + "/data" + "/"
dt=  datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
filename=datadir+''+os.path.basename(__file__)+'_'+dt+'.log'

def run(filename,data,seq):
    print datetime.datetime.now(), 'test start run  seq:%s' %seq
    try:
                with open(filename, 'ab') as obj:
                    time.sleep(int((100-seq)/100.00))
                    obj.write("test data %s\n" % data)
    except BaseException, e:
                print e
    print datetime.datetime.now(), 'test ok run  seq:%s' %seq


##test1
if __name__ == '__main__':
    print 'start',datetime.datetime.now()
    start = time.time()
    pool = multiprocessing.Pool(processes=3)
    for i in range(0, 100):
        msg = "hello %d" % (i)
        res = pool.apply_async(run, args=(filename, msg, i,), )
        print  'start',res, i
    pool.close()
    pool.join()
    print "all done."
    end = time.time()
    print 'end', datetime.datetime.now()
    print str(round(end - start, 3)) + 's'
# start 2017-12-11 11:41:24.639000
# start <multiprocessing.pool.ApplyResult object at 0x02D031F0> 0
# start <multiprocessing.pool.ApplyResult object at 0x02D03250> 1
# start <multiprocessing.pool.ApplyResult object at 0x02D03290> 2
# start <multiprocessing.pool.ApplyResult object at 0x02D032D0> 3
# start <multiprocessing.pool.ApplyResult object at 0x02D03310> 4
# start <multiprocessing.pool.ApplyResult object at 0x02D03350> 5
# start <multiprocessing.pool.ApplyResult object at 0x02D03390> 6
# start <multiprocessing.pool.ApplyResult object at 0x02D033D0> 7
# start <multiprocessing.pool.ApplyResult object at 0x02D03410> 8
# start <multiprocessing.pool.ApplyResult object at 0x02D03450> 9
# start <multiprocessing.pool.ApplyResult object at 0x02D03490> 10
# 2017-12-11 11:41:24.922000 test start run  seq:0
# 2017-12-11 11:41:24.924000 test start run  seq:1
# 2017-12-11 11:41:24.925000 test ok run  seq:1
# 2017-12-11 11:41:24.925000 test start run  seq:2
# 2017-12-11 11:41:24.925000 test ok run  seq:2
# 2017-12-11 11:41:24.925000 test start run  seq:3
# 2017-12-11 11:41:24.926000 test ok run  seq:3
# 2017-12-11 11:41:24.926000 test start run  seq:4
# 2017-12-11 11:41:24.926000 test ok run  seq:4
# 2017-12-11 11:41:24.926000 test start run  seq:5
# 2017-12-11 11:41:24.927000 test ok run  seq:5
# 2017-12-11 11:41:24.927000 test start run  seq:6
# 2017-12-11 11:41:24.927000 test ok run  seq:6
# 2017-12-11 11:41:24.927000 test start run  seq:7
# 2017-12-11 11:41:24.928000 test ok run  seq:7
# 2017-12-11 11:41:24.928000 test start run  seq:8
# 2017-12-11 11:41:24.928000 test ok run  seq:8
# 2017-12-11 11:41:24.929000 test start run  seq:9
# 2017-12-11 11:41:24.929000 test ok run  seq:9
# 2017-12-11 11:41:24.929000 test start run  seq:10
# 2017-12-11 11:41:24.929000 test ok run  seq:10
# 2017-12-11 11:41:25.923000 test ok run  seq:0
# all done.
# end 2017-12-11 11:41:26.040000
# 1.401s



