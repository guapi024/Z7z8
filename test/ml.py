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
                with open(filename+'_'+str(seq), 'ab') as obj:
                    time.sleep(int((100-seq)/50.00))
                    obj.write("test data %s\n" % data)
    except BaseException, e:
                print e
    print datetime.datetime.now(), 'test ok run  seq:%s' %seq

def run_lock(lock,filename,data,seq):
    lock.acquire()
    print datetime.datetime.now(), 'test start run  seq:%s' %seq
    try:
                with open(filename, 'ab') as obj:
                    time.sleep(int((100-seq)/50.00))
                    obj.write("test data %s\n" % data)
    except BaseException, e:
                print e
    print datetime.datetime.now(), 'test ok run  seq:%s' %seq
    lock.release()


# test
'''
if __name__ == '__main__':
    print 'start',datetime.datetime.now()
    start = time.time()
    from multiprocessing import Process, Lock
    lock = Lock()
    t = multiprocessing.Process(target=run_lock, args=(lock,filename, '1',1,), ).start()
    t = multiprocessing.Process(target=run_lock, args=(lock,filename, '2',2,), ).start()
    print "all done."
    end = time.time()
    print 'end', datetime.datetime.now()
    print str(round(end - start, 3)) + 's'
start 2017-12-13 10:09:24.078000
all done.
end 2017-12-13 10:09:24.115000
0.037s
2017-12-13 10:09:24.303000 test start run  seq:1
2017-12-13 10:09:25.306000 test ok run  seq:1
2017-12-13 10:09:25.307000 test start run  seq:2
2017-12-13 10:09:26.310000 test ok run  seq:2
'''

'''
if __name__ == '__main__':
    print 'start',datetime.datetime.now()
    start = time.time()
    for i in range(1,100,2):
        multiprocessing.Process(target=run, args=(filename, '1',i,), ).start()
        multiprocessing.Process(target=run, args=(filename, '1', i+1,), ).start()
    print "all done."
    end = time.time()
    print 'end', datetime.datetime.now()
    print str(round(end - start, 3)) + 's'
start 2017-12-13 10:04:15.625000
2017-12-13 10:04:16.087000 test start run  seq:2
2017-12-13 10:04:16.270000 test start run  seq:4
2017-12-13 10:04:16.291000 test start run  seq:1
2017-12-13 10:04:16.330000 test start run  seq:3
2017-12-13 10:04:17.096000 test ok run  seq:2
2017-12-13 10:04:17.273000 test ok run  seq:4
2017-12-13 10:04:17.300000 test ok run  seq:1
2017-12-13 10:04:17.337000 test ok run  seq:3
all done.
end 2017-12-13 10:04:18.353000
2.728s
2017-12-13 10:04:19.549000 test start run  seq:5
2017-12-13 10:04:20.554000 test ok run  seq:5
2017-12-13 10:04:21.388000 test start run  seq:7
2017-12-13 10:04:21.557000 test start run  seq:8
2017-12-13 10:04:21.568000 test start run  seq:6
2017-12-13 10:04:21.750000 test start run  seq:9
2017-12-13 10:04:21.788000 test start run  seq:15
2017-12-13 10:04:21.810000 test start run  seq:11
2017-12-13 10:04:21.813000 test start run  seq:10
2017-12-13 10:04:22.398000 test ok run  seq:7
2017-12-13 10:04:22.563000 test ok run  seq:8
2017-12-13 10:04:22.575000 test ok run  seq:6
2017-12-13 10:04:22.757000 test ok run  seq:9
2017-12-13 10:04:22.793000 test ok run  seq:15
2017-12-13 10:04:22.803000 test start run  seq:13
2017-12-13 10:04:22.818000 test ok run  seq:10
2017-12-13 10:04:22.839000 test ok run  seq:11
2017-12-13 10:04:23.807000 test ok run  seq:13
2017-12-13 10:04:24.567000 test start run  seq:55
2017-12-13 10:04:24.569000 test ok run  seq:55
2017-12-13 10:04:24.727000 test start run  seq:71
2017-12-13 10:04:24.730000 test ok run  seq:71
2017-12-13 10:04:24.745000 test start run  seq:47
2017-12-13 10:04:24.757000 test start run  seq:87
2017-12-13 10:04:24.763000 test ok run  seq:87
2017-12-13 10:04:24.898000 test start run  seq:97
2017-12-13 10:04:24.904000 test ok run  seq:97
2017-12-13 10:04:24.928000 test start run  seq:94
2017-12-13 10:04:24.932000 test ok run  seq:94
2017-12-13 10:04:24.999000 test start run  seq:16
2017-12-13 10:04:25.076000 test start run  seq:48
2017-12-13 10:04:25.079000 test start run  seq:29
2017-12-13 10:04:25.208000 test start run  seq:45
2017-12-13 10:04:25.222000 test start run  seq:53
2017-12-13 10:04:25.224000 test start run  seq:76
2017-12-13 10:04:25.228000 test ok run  seq:53
2017-12-13 10:04:25.228000 test ok run  seq:76
2017-12-13 10:04:25.252000 test start run  seq:89
2017-12-13 10:04:25.257000 test ok run  seq:89
2017-12-13 10:04:25.346000 test start run  seq:25
2017-12-13 10:04:25.348000 test start run  seq:33
2017-12-13 10:04:25.437000 test start run  seq:92
2017-12-13 10:04:25.440000 test ok run  seq:92
2017-12-13 10:04:25.461000 test start run  seq:85
2017-12-13 10:04:25.466000 test start run  seq:57
2017-12-13 10:04:25.467000 test ok run  seq:85
2017-12-13 10:04:25.471000 test ok run  seq:57
2017-12-13 10:04:25.543000 test start run  seq:17
2017-12-13 10:04:25.602000 test start run  seq:69
2017-12-13 10:04:25.603000 test start run  seq:26
2017-12-13 10:04:25.607000 test ok run  seq:69
2017-12-13 10:04:25.631000 test start run  seq:67
2017-12-13 10:04:25.639000 test ok run  seq:67
2017-12-13 10:04:25.656000 test start run  seq:51
2017-12-13 10:04:25.662000 test ok run  seq:51
2017-12-13 10:04:25.723000 test start run  seq:21
2017-12-13 10:04:25.745000 test start run  seq:27
2017-12-13 10:04:25.751000 test start run  seq:19
2017-12-13 10:04:25.751000 test ok run  seq:47
2017-12-13 10:04:25.784000 test start run  seq:46
2017-12-13 10:04:25.827000 test start run  seq:86
2017-12-13 10:04:25.833000 test ok run  seq:86
2017-12-13 10:04:25.839000 test start run  seq:58
2017-12-13 10:04:25.851000 test start run  seq:34
2017-12-13 10:04:25.854000 test ok run  seq:58
2017-12-13 10:04:25.894000 test start run  seq:52
2017-12-13 10:04:25.898000 test ok run  seq:52
2017-12-13 10:04:25.932000 test start run  seq:18
2017-12-13 10:04:25.980000 test start run  seq:83
2017-12-13 10:04:25.983000 test ok run  seq:83
2017-12-13 10:04:25.987000 test start run  seq:22
2017-12-13 10:04:26.017000 test ok run  seq:16
2017-12-13 10:04:26.021000 test start run  seq:28
2017-12-13 10:04:26.063000 test start run  seq:59
2017-12-13 10:04:26.066000 test ok run  seq:59
2017-12-13 10:04:26.075000 test start run  seq:63
2017-12-13 10:04:26.081000 test ok run  seq:48
2017-12-13 10:04:26.083000 test ok run  seq:63
2017-12-13 10:04:26.088000 test ok run  seq:29
2017-12-13 10:04:26.097000 test start run  seq:79
2017-12-13 10:04:26.098000 test ok run  seq:79
2017-12-13 10:04:26.136000 test start run  seq:23
2017-12-13 10:04:26.158000 test start run  seq:31
2017-12-13 10:04:26.184000 test start run  seq:91
2017-12-13 10:04:26.189000 test ok run  seq:91
2017-12-13 10:04:26.193000 test start run  seq:43
2017-12-13 10:04:26.214000 test ok run  seq:45
2017-12-13 10:04:26.226000 test start run  seq:99
2017-12-13 10:04:26.230000 test ok run  seq:99
2017-12-13 10:04:26.232000 test start run  seq:38
2017-12-13 10:04:26.262000 test start run  seq:14
2017-12-13 10:04:26.267000 test start run  seq:39
2017-12-13 10:04:26.272000 test start run  seq:82
2017-12-13 10:04:26.303000 test start run  seq:75
2017-12-13 10:04:26.320000 test ok run  seq:82
2017-12-13 10:04:26.353000 test ok run  seq:75
2017-12-13 10:04:26.363000 test ok run  seq:25
2017-12-13 10:04:26.370000 test ok run  seq:33
2017-12-13 10:04:26.561000 test start run  seq:42
2017-12-13 10:04:26.570000 test ok run  seq:17
2017-12-13 10:04:26.585000 test start run  seq:36
2017-12-13 10:04:26.599000 test start run  seq:61
2017-12-13 10:04:26.683000 test ok run  seq:61
2017-12-13 10:04:26.687000 test ok run  seq:26
2017-12-13 10:04:26.739000 test ok run  seq:21
2017-12-13 10:04:26.756000 test start run  seq:95
2017-12-13 10:04:26.771000 test start run  seq:90
2017-12-13 10:04:26.783000 test start run  seq:81
2017-12-13 10:04:26.834000 test ok run  seq:27
2017-12-13 10:04:26.835000 test ok run  seq:19
2017-12-13 10:04:26.837000 test ok run  seq:95
2017-12-13 10:04:26.838000 test ok run  seq:81
2017-12-13 10:04:26.840000 test ok run  seq:90
2017-12-13 10:04:26.853000 test ok run  seq:46
2017-12-13 10:04:26.872000 test ok run  seq:34
2017-12-13 10:04:26.913000 test start run  seq:65
2017-12-13 10:04:26.914000 test start run  seq:35
2017-12-13 10:04:26.922000 test start run  seq:96
2017-12-13 10:04:26.948000 test start run  seq:98
2017-12-13 10:04:26.975000 test ok run  seq:65
2017-12-13 10:04:26.979000 test ok run  seq:18
2017-12-13 10:04:26.979000 test ok run  seq:96
2017-12-13 10:04:26.985000 test ok run  seq:98
2017-12-13 10:04:27.013000 test ok run  seq:22
2017-12-13 10:04:27.026000 test start run  seq:40
2017-12-13 10:04:27.050000 test ok run  seq:28
2017-12-13 10:04:27.065000 test start run  seq:77
2017-12-13 10:04:27.069000 test start run  seq:49
2017-12-13 10:04:27.082000 test start run  seq:72
2017-12-13 10:04:27.090000 test start run  seq:73
2017-12-13 10:04:27.092000 test start run  seq:12
2017-12-13 10:04:27.093000 test start run  seq:78
2017-12-13 10:04:27.100000 test start run  seq:37
2017-12-13 10:04:27.104000 test start run  seq:80
2017-12-13 10:04:27.114000 test ok run  seq:77
2017-12-13 10:04:27.115000 test start run  seq:41
2017-12-13 10:04:27.120000 test ok run  seq:73
2017-12-13 10:04:27.120000 test ok run  seq:78
2017-12-13 10:04:27.123000 test ok run  seq:72
2017-12-13 10:04:27.127000 test ok run  seq:80
2017-12-13 10:04:27.151000 test start run  seq:50
2017-12-13 10:04:27.154000 test ok run  seq:23
2017-12-13 10:04:27.161000 test start run  seq:93
2017-12-13 10:04:27.170000 test start run  seq:24
2017-12-13 10:04:27.175000 test start run  seq:54
2017-12-13 10:04:27.194000 test ok run  seq:31
2017-12-13 10:04:27.195000 test ok run  seq:93
2017-12-13 10:04:27.202000 test ok run  seq:43
2017-12-13 10:04:27.204000 test ok run  seq:54
2017-12-13 10:04:27.204000 test start run  seq:30
2017-12-13 10:04:27.207000 test start run  seq:32
2017-12-13 10:04:27.216000 test start run  seq:64
2017-12-13 10:04:27.217000 test start run  seq:70
2017-12-13 10:04:27.220000 test start run  seq:62
2017-12-13 10:04:27.221000 test start run  seq:66
2017-12-13 10:04:27.224000 test start run  seq:68
2017-12-13 10:04:27.226000 test ok run  seq:64
2017-12-13 10:04:27.226000 test start run  seq:74
2017-12-13 10:04:27.228000 test ok run  seq:70
2017-12-13 10:04:27.229000 test start run  seq:60
2017-12-13 10:04:27.231000 test ok run  seq:66
2017-12-13 10:04:27.236000 test ok run  seq:38
2017-12-13 10:04:27.236000 test ok run  seq:62
2017-12-13 10:04:27.238000 test ok run  seq:74
2017-12-13 10:04:27.242000 test start run  seq:84
2017-12-13 10:04:27.243000 test ok run  seq:60
2017-12-13 10:04:27.252000 test start run  seq:44
2017-12-13 10:04:27.259000 test start run  seq:20
2017-12-13 10:04:27.261000 test ok run  seq:84
2017-12-13 10:04:27.263000 test ok run  seq:68
2017-12-13 10:04:27.266000 test ok run  seq:14
2017-12-13 10:04:27.272000 test ok run  seq:39
2017-12-13 10:04:27.283000 test start run  seq:56
2017-12-13 10:04:27.285000 test start run  seq:88
2017-12-13 10:04:27.287000 test ok run  seq:56
2017-12-13 10:04:27.289000 test ok run  seq:88
2017-12-13 10:04:27.293000 test start run  seq:100
2017-12-13 10:04:27.296000 test ok run  seq:100
2017-12-13 10:04:27.566000 test ok run  seq:42
2017-12-13 10:04:27.616000 test ok run  seq:36
2017-12-13 10:04:27.921000 test ok run  seq:35
2017-12-13 10:04:28.029000 test ok run  seq:40
2017-12-13 10:04:28.072000 test ok run  seq:49
2017-12-13 10:04:28.093000 test ok run  seq:12
2017-12-13 10:04:28.102000 test ok run  seq:37
2017-12-13 10:04:28.117000 test ok run  seq:41
2017-12-13 10:04:28.153000 test ok run  seq:50
2017-12-13 10:04:28.173000 test ok run  seq:24
2017-12-13 10:04:28.206000 test ok run  seq:30
2017-12-13 10:04:28.210000 test ok run  seq:32
2017-12-13 10:04:28.265000 test ok run  seq:44
2017-12-13 10:04:28.270000 test ok run  seq:20

Process finished with exit code 0
'''



'''
##test1
if __name__ == '__main__':
    print 'start',datetime.datetime.now()
    start = time.time()
    pool = multiprocessing.Pool(processes=40)
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


#
# start 2017-12-13 09:44:54.509000
# start <multiprocessing.pool.ApplyResult object at 0x029A4270> 0
# start <multiprocessing.pool.ApplyResult object at 0x029A42D0> 1
# start <multiprocessing.pool.ApplyResult object at 0x029A4330> 2
# start <multiprocessing.pool.ApplyResult object at 0x029A4390> 3
# start <multiprocessing.pool.ApplyResult object at 0x029A43F0> 4
# start <multiprocessing.pool.ApplyResult object at 0x029A4450> 5
# start <multiprocessing.pool.ApplyResult object at 0x029A44B0> 6
# start <multiprocessing.pool.ApplyResult object at 0x029A4510> 7
# start <multiprocessing.pool.ApplyResult object at 0x029A4550> 8
# start <multiprocessing.pool.ApplyResult object at 0x029A4590> 9
# start <multiprocessing.pool.ApplyResult object at 0x029A45D0> 10
# start <multiprocessing.pool.ApplyResult object at 0x029A4610> 11
# start <multiprocessing.pool.ApplyResult object at 0x029A4650> 12
# start <multiprocessing.pool.ApplyResult object at 0x029A4690> 13
# start <multiprocessing.pool.ApplyResult object at 0x029A46D0> 14
# start <multiprocessing.pool.ApplyResult object at 0x029A4710> 15
# start <multiprocessing.pool.ApplyResult object at 0x029A4750> 16
# start <multiprocessing.pool.ApplyResult object at 0x029A42B0> 17
# start <multiprocessing.pool.ApplyResult object at 0x029A47B0> 18
# start <multiprocessing.pool.ApplyResult object at 0x029A47F0> 19
# start <multiprocessing.pool.ApplyResult object at 0x029A4830> 20
# start <multiprocessing.pool.ApplyResult object at 0x029A4870> 21
# start <multiprocessing.pool.ApplyResult object at 0x029A48B0> 22
# start <multiprocessing.pool.ApplyResult object at 0x029A48F0> 23
# start <multiprocessing.pool.ApplyResult object at 0x029A4930> 24
# start <multiprocessing.pool.ApplyResult object at 0x029A4970> 25
# start <multiprocessing.pool.ApplyResult object at 0x029A49B0> 26
# start <multiprocessing.pool.ApplyResult object at 0x029A49F0> 27
# start <multiprocessing.pool.ApplyResult object at 0x029A4A30> 28
# start <multiprocessing.pool.ApplyResult object at 0x029A4A70> 29
# start <multiprocessing.pool.ApplyResult object at 0x029A4AB0> 30
# start <multiprocessing.pool.ApplyResult object at 0x029A4AF0> 31
# start <multiprocessing.pool.ApplyResult object at 0x029A4B30> 32
# start <multiprocessing.pool.ApplyResult object at 0x029A4B70> 33
# start <multiprocessing.pool.ApplyResult object at 0x029A4BB0> 34
# start <multiprocessing.pool.ApplyResult object at 0x029A4BF0> 35
# start <multiprocessing.pool.ApplyResult object at 0x029A4C30> 36
# start <multiprocessing.pool.ApplyResult object at 0x029A4C70> 37
# start <multiprocessing.pool.ApplyResult object at 0x029A4CB0> 38
# start <multiprocessing.pool.ApplyResult object at 0x029A4CF0> 39
# start <multiprocessing.pool.ApplyResult object at 0x029A4D30> 40
# start <multiprocessing.pool.ApplyResult object at 0x029A4D70> 41
# start <multiprocessing.pool.ApplyResult object at 0x029A4DB0> 42
# start <multiprocessing.pool.ApplyResult object at 0x029A4DF0> 43
# start <multiprocessing.pool.ApplyResult object at 0x029A4E30> 44
# start <multiprocessing.pool.ApplyResult object at 0x029A4E70> 45
# start <multiprocessing.pool.ApplyResult object at 0x029A4EB0> 46
# start <multiprocessing.pool.ApplyResult object at 0x029A4EF0> 47
# start <multiprocessing.pool.ApplyResult object at 0x029A4F30> 48
# start <multiprocessing.pool.ApplyResult object at 0x029A4F70> 49
# start <multiprocessing.pool.ApplyResult object at 0x029A4FB0> 50
# start <multiprocessing.pool.ApplyResult object at 0x029A4FF0> 51
# start <multiprocessing.pool.ApplyResult object at 0x029AC050> 52
# start <multiprocessing.pool.ApplyResult object at 0x029AC090> 53
# start <multiprocessing.pool.ApplyResult object at 0x029AC0D0> 54
# start <multiprocessing.pool.ApplyResult object at 0x029AC110> 55
# start <multiprocessing.pool.ApplyResult object at 0x029AC150> 56
# start <multiprocessing.pool.ApplyResult object at 0x029AC190> 57
# start <multiprocessing.pool.ApplyResult object at 0x029AC1D0> 58
# start <multiprocessing.pool.ApplyResult object at 0x029AC230> 59
# start <multiprocessing.pool.ApplyResult object at 0x029AC290> 60
# start <multiprocessing.pool.ApplyResult object at 0x029AC2F0> 61
# start <multiprocessing.pool.ApplyResult object at 0x029AC350> 62
# start <multiprocessing.pool.ApplyResult object at 0x029AC3B0> 63
# start <multiprocessing.pool.ApplyResult object at 0x029AC410> 64
# start <multiprocessing.pool.ApplyResult object at 0x029AC470> 65
# start <multiprocessing.pool.ApplyResult object at 0x029AC4D0> 66
# start <multiprocessing.pool.ApplyResult object at 0x029AC530> 67
# start <multiprocessing.pool.ApplyResult object at 0x029AC590> 68
# start <multiprocessing.pool.ApplyResult object at 0x029AC5F0> 69
# start <multiprocessing.pool.ApplyResult object at 0x029AC650> 70
# start <multiprocessing.pool.ApplyResult object at 0x029AC6B0> 71
# start <multiprocessing.pool.ApplyResult object at 0x029AC710> 72
# start <multiprocessing.pool.ApplyResult object at 0x029AC770> 73
# start <multiprocessing.pool.ApplyResult object at 0x029AC7D0> 74
# start <multiprocessing.pool.ApplyResult object at 0x029AC830> 75
# start <multiprocessing.pool.ApplyResult object at 0x029AC890> 76
# start <multiprocessing.pool.ApplyResult object at 0x029AC8F0> 77
# start <multiprocessing.pool.ApplyResult object at 0x029AC950> 78
# start <multiprocessing.pool.ApplyResult object at 0x029AC9B0> 79
# start <multiprocessing.pool.ApplyResult object at 0x029ACA10> 80
# start <multiprocessing.pool.ApplyResult object at 0x029ACA70> 81
# start <multiprocessing.pool.ApplyResult object at 0x029ACAD0> 82
# start <multiprocessing.pool.ApplyResult object at 0x029ACB30> 83
# start <multiprocessing.pool.ApplyResult object at 0x029ACB90> 84
# start <multiprocessing.pool.ApplyResult object at 0x029ACBF0> 85
# start <multiprocessing.pool.ApplyResult object at 0x029ACC50> 86
# start <multiprocessing.pool.ApplyResult object at 0x029ACCB0> 87
# start <multiprocessing.pool.ApplyResult object at 0x029ACD10> 88
# start <multiprocessing.pool.ApplyResult object at 0x029ACD70> 89
# start <multiprocessing.pool.ApplyResult object at 0x029ACDD0> 90
# start <multiprocessing.pool.ApplyResult object at 0x029ACE30> 91
# start <multiprocessing.pool.ApplyResult object at 0x029ACE90> 92
# start <multiprocessing.pool.ApplyResult object at 0x029ACEF0> 93
# start <multiprocessing.pool.ApplyResult object at 0x029ACF50> 94
# start <multiprocessing.pool.ApplyResult object at 0x029ACFB0> 95
# start <multiprocessing.pool.ApplyResult object at 0x02A27030> 96
# start <multiprocessing.pool.ApplyResult object at 0x02A27090> 97
# start <multiprocessing.pool.ApplyResult object at 0x02A270F0> 98
# start <multiprocessing.pool.ApplyResult object at 0x02A27150> 99
# 2017-12-13 09:44:54.880000 test start run  seq:0
# 2017-12-13 09:44:54.882000 test start run  seq:1
# 2017-12-13 09:44:54.888000 test start run  seq:2
# 2017-12-13 09:44:55.886000 test ok run  seq:1
# 2017-12-13 09:44:55.886000 test start run  seq:3
# 2017-12-13 09:44:55.891000 test ok run  seq:2
# 2017-12-13 09:44:55.891000 test start run  seq:4
# 2017-12-13 09:44:56.882000 test ok run  seq:0
# 2017-12-13 09:44:56.882000 test start run  seq:5
# 2017-12-13 09:44:56.888000 test ok run  seq:3
# 2017-12-13 09:44:56.888000 test start run  seq:6
# 2017-12-13 09:44:56.893000 test ok run  seq:4
# 2017-12-13 09:44:56.893000 test start run  seq:7
# 2017-12-13 09:44:57.888000 test ok run  seq:5
# 2017-12-13 09:44:57.888000 test start run  seq:8
# 2017-12-13 09:44:57.897000 test ok run  seq:6
# 2017-12-13 09:44:57.897000 test start run  seq:9
# 2017-12-13 09:44:57.900000 test ok run  seq:7
# 2017-12-13 09:44:57.900000 test start run  seq:10
# 2017-12-13 09:44:58.895000 test ok run  seq:8
# 2017-12-13 09:44:58.895000 test start run  seq:11
# 2017-12-13 09:44:58.915000 test ok run  seq:10
# 2017-12-13 09:44:58.915000 test start run  seq:12
# 2017-12-13 09:44:58.919000 test ok run  seq:9
# 2017-12-13 09:44:58.919000 test start run  seq:13
# 2017-12-13 09:44:59.901000 test ok run  seq:11
# 2017-12-13 09:44:59.901000 test start run  seq:14
# 2017-12-13 09:44:59.919000 test ok run  seq:12
# 2017-12-13 09:44:59.919000 test start run  seq:15
# 2017-12-13 09:44:59.931000 test ok run  seq:13
# 2017-12-13 09:44:59.931000 test start run  seq:16
# 2017-12-13 09:45:00.904000 test ok run  seq:14
# 2017-12-13 09:45:00.905000 test start run  seq:17
# 2017-12-13 09:45:00.923000 test ok run  seq:15
# 2017-12-13 09:45:00.923000 test start run  seq:18
# 2017-12-13 09:45:00.943000 test ok run  seq:16
# 2017-12-13 09:45:00.943000 test start run  seq:19
# 2017-12-13 09:45:01.909000 test ok run  seq:17
# 2017-12-13 09:45:01.909000 test start run  seq:20
# 2017-12-13 09:45:01.931000 test ok run  seq:18
# 2017-12-13 09:45:01.931000 test start run  seq:21
# 2017-12-13 09:45:01.948000 test ok run  seq:19
# 2017-12-13 09:45:01.948000 test start run  seq:22
# 2017-12-13 09:45:02.917000 test ok run  seq:20
# 2017-12-13 09:45:02.917000 test start run  seq:23
# 2017-12-13 09:45:02.940000 test ok run  seq:21
# 2017-12-13 09:45:02.940000 test start run  seq:24
# 2017-12-13 09:45:02.954000 test ok run  seq:22
# 2017-12-13 09:45:02.954000 test start run  seq:25
# 2017-12-13 09:45:03.925000 test ok run  seq:23
# 2017-12-13 09:45:03.925000 test start run  seq:26
# 2017-12-13 09:45:03.945000 test ok run  seq:24
# 2017-12-13 09:45:03.945000 test start run  seq:27
# 2017-12-13 09:45:03.960000 test ok run  seq:25
# 2017-12-13 09:45:03.961000 test start run  seq:28
# 2017-12-13 09:45:04.930000 test ok run  seq:26
# 2017-12-13 09:45:04.930000 test start run  seq:29
# 2017-12-13 09:45:04.951000 test ok run  seq:27
# 2017-12-13 09:45:04.951000 test start run  seq:30
# 2017-12-13 09:45:04.965000 test ok run  seq:28
# 2017-12-13 09:45:04.965000 test start run  seq:31
# 2017-12-13 09:45:05.934000 test ok run  seq:29
# 2017-12-13 09:45:05.934000 test start run  seq:32
# 2017-12-13 09:45:05.963000 test ok run  seq:30
# 2017-12-13 09:45:05.963000 test start run  seq:33
# 2017-12-13 09:45:05.970000 test ok run  seq:31
# 2017-12-13 09:45:05.970000 test start run  seq:34
# 2017-12-13 09:45:06.939000 test ok run  seq:32
# 2017-12-13 09:45:06.939000 test start run  seq:35
# 2017-12-13 09:45:06.978000 test ok run  seq:34
# 2017-12-13 09:45:06.978000 test start run  seq:36
# 2017-12-13 09:45:06.981000 test ok run  seq:33
# 2017-12-13 09:45:06.981000 test start run  seq:37
# 2017-12-13 09:45:07.942000 test ok run  seq:35
# 2017-12-13 09:45:07.942000 test start run  seq:38
# 2017-12-13 09:45:07.981000 test ok run  seq:36
# 2017-12-13 09:45:07.981000 test start run  seq:39
# 2017-12-13 09:45:08.010000 test ok run  seq:37
# 2017-12-13 09:45:08.010000 test start run  seq:40
# 2017-12-13 09:45:08.948000 test ok run  seq:38
# 2017-12-13 09:45:08.949000 test start run  seq:41
# 2017-12-13 09:45:08.987000 test ok run  seq:39
# 2017-12-13 09:45:08.987000 test start run  seq:42
# 2017-12-13 09:45:09.013000 test ok run  seq:40
# 2017-12-13 09:45:09.013000 test start run  seq:43
# 2017-12-13 09:45:09.958000 test ok run  seq:41
# 2017-12-13 09:45:09.958000 test start run  seq:44
# 2017-12-13 09:45:09.994000 test ok run  seq:42
# 2017-12-13 09:45:09.994000 test start run  seq:45
# 2017-12-13 09:45:10.040000 test ok run  seq:43
# 2017-12-13 09:45:10.040000 test start run  seq:46
# 2017-12-13 09:45:10.963000 test ok run  seq:44
# 2017-12-13 09:45:10.963000 test start run  seq:47
# 2017-12-13 09:45:11.002000 test ok run  seq:45
# 2017-12-13 09:45:11.002000 test start run  seq:48
# 2017-12-13 09:45:11.044000 test ok run  seq:46
# 2017-12-13 09:45:11.044000 test start run  seq:49
# 2017-12-13 09:45:11.966000 test ok run  seq:47
# 2017-12-13 09:45:11.966000 test start run  seq:50
# 2017-12-13 09:45:12.006000 test ok run  seq:48
# 2017-12-13 09:45:12.006000 test start run  seq:51
# 2017-12-13 09:45:12.010000 test ok run  seq:51
# 2017-12-13 09:45:12.010000 test start run  seq:52
# 2017-12-13 09:45:12.014000 test ok run  seq:52
# 2017-12-13 09:45:12.014000 test start run  seq:53
# 2017-12-13 09:45:12.017000 test ok run  seq:53
# 2017-12-13 09:45:12.017000 test start run  seq:54
# 2017-12-13 09:45:12.021000 test ok run  seq:54
# 2017-12-13 09:45:12.022000 test start run  seq:55
# 2017-12-13 09:45:12.026000 test ok run  seq:55
# 2017-12-13 09:45:12.026000 test start run  seq:56
# 2017-12-13 09:45:12.029000 test ok run  seq:56
# 2017-12-13 09:45:12.029000 test start run  seq:57
# 2017-12-13 09:45:12.034000 test ok run  seq:57
# 2017-12-13 09:45:12.034000 test start run  seq:58
# 2017-12-13 09:45:12.037000 test ok run  seq:58
# 2017-12-13 09:45:12.037000 test start run  seq:59
# 2017-12-13 09:45:12.042000 test ok run  seq:59
# 2017-12-13 09:45:12.042000 test start run  seq:60
# 2017-12-13 09:45:12.046000 test ok run  seq:60
# 2017-12-13 09:45:12.046000 test start run  seq:61
# 2017-12-13 09:45:12.046000 test ok run  seq:49
# 2017-12-13 09:45:12.046000 test start run  seq:62
# 2017-12-13 09:45:12.050000 test ok run  seq:62
# 2017-12-13 09:45:12.050000 test start run  seq:63
# 2017-12-13 09:45:12.056000 test ok run  seq:63
# 2017-12-13 09:45:12.056000 test start run  seq:64
# 2017-12-13 09:45:12.059000 test ok run  seq:61
# 2017-12-13 09:45:12.059000 test start run  seq:65
# 2017-12-13 09:45:12.065000 test ok run  seq:64
# 2017-12-13 09:45:12.065000 test start run  seq:66
# 2017-12-13 09:45:12.066000 test ok run  seq:65
# 2017-12-13 09:45:12.066000 test start run  seq:67
# 2017-12-13 09:45:12.069000 test ok run  seq:66
# 2017-12-13 09:45:12.069000 test start run  seq:68
# 2017-12-13 09:45:12.072000 test ok run  seq:68
# 2017-12-13 09:45:12.072000 test start run  seq:69
# 2017-12-13 09:45:12.074000 test ok run  seq:67
# 2017-12-13 09:45:12.074000 test start run  seq:70
# 2017-12-13 09:45:12.075000 test ok run  seq:69
# 2017-12-13 09:45:12.075000 test start run  seq:71
# 2017-12-13 09:45:12.082000 test ok run  seq:70
# 2017-12-13 09:45:12.083000 test start run  seq:72
# 2017-12-13 09:45:12.083000 test ok run  seq:71
# 2017-12-13 09:45:12.083000 test start run  seq:73
# 2017-12-13 09:45:12.087000 test ok run  seq:73
# 2017-12-13 09:45:12.087000 test start run  seq:74
# 2017-12-13 09:45:12.088000 test ok run  seq:72
# 2017-12-13 09:45:12.088000 test start run  seq:75
# 2017-12-13 09:45:12.091000 test ok run  seq:74
# 2017-12-13 09:45:12.091000 test start run  seq:76
# 2017-12-13 09:45:12.096000 test ok run  seq:76
# 2017-12-13 09:45:12.096000 test start run  seq:77
# 2017-12-13 09:45:12.096000 test ok run  seq:75
# 2017-12-13 09:45:12.096000 test start run  seq:78
# 2017-12-13 09:45:12.104000 test ok run  seq:78
# 2017-12-13 09:45:12.104000 test start run  seq:79
# 2017-12-13 09:45:12.105000 test ok run  seq:77
# 2017-12-13 09:45:12.105000 test start run  seq:80
# 2017-12-13 09:45:12.109000 test ok run  seq:80
# 2017-12-13 09:45:12.110000 test start run  seq:81
# 2017-12-13 09:45:12.113000 test ok run  seq:79
# 2017-12-13 09:45:12.113000 test start run  seq:82
# 2017-12-13 09:45:12.115000 test ok run  seq:81
# 2017-12-13 09:45:12.116000 test start run  seq:83
# 2017-12-13 09:45:12.118000 test ok run  seq:82
# 2017-12-13 09:45:12.118000 test start run  seq:84
# 2017-12-13 09:45:12.121000 test ok run  seq:83
# 2017-12-13 09:45:12.121000 test start run  seq:85
# 2017-12-13 09:45:12.124000 test ok run  seq:84
# 2017-12-13 09:45:12.124000 test start run  seq:86
# 2017-12-13 09:45:12.128000 test ok run  seq:85
# 2017-12-13 09:45:12.128000 test start run  seq:87
# 2017-12-13 09:45:12.131000 test ok run  seq:86
# 2017-12-13 09:45:12.131000 test start run  seq:88
# 2017-12-13 09:45:12.134000 test ok run  seq:87
# 2017-12-13 09:45:12.134000 test start run  seq:89
# 2017-12-13 09:45:12.137000 test ok run  seq:88
# 2017-12-13 09:45:12.137000 test start run  seq:90
# 2017-12-13 09:45:12.140000 test ok run  seq:89
# 2017-12-13 09:45:12.140000 test start run  seq:91
# 2017-12-13 09:45:12.144000 test ok run  seq:90
# 2017-12-13 09:45:12.144000 test start run  seq:92
# 2017-12-13 09:45:12.147000 test ok run  seq:91
# 2017-12-13 09:45:12.147000 test start run  seq:93
# 2017-12-13 09:45:12.150000 test ok run  seq:92
# 2017-12-13 09:45:12.150000 test start run  seq:94
# 2017-12-13 09:45:12.153000 test ok run  seq:93
# 2017-12-13 09:45:12.153000 test start run  seq:95
# 2017-12-13 09:45:12.155000 test ok run  seq:94
# 2017-12-13 09:45:12.155000 test start run  seq:96
# 2017-12-13 09:45:12.158000 test ok run  seq:95
# 2017-12-13 09:45:12.158000 test start run  seq:97
# 2017-12-13 09:45:12.161000 test ok run  seq:96
# 2017-12-13 09:45:12.161000 test start run  seq:98
# 2017-12-13 09:45:12.163000 test ok run  seq:97
# 2017-12-13 09:45:12.163000 test start run  seq:99
# 2017-12-13 09:45:12.165000 test ok run  seq:98
# 2017-12-13 09:45:12.166000 test ok run  seq:99
# 2017-12-13 09:45:12.968000 test ok run  seq:50
# all done.
# end 2017-12-13 09:45:13.099000
# 18.59s
#
# Process finished with exit code 0
'''