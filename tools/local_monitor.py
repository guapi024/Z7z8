# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : monitor.py
'''
import  os,sys,datetime,time,json,logging,platform,commands,multiprocessing


##dict
osinfo={}
cpu_count=multiprocessing.cpu_count()
##create log dt/dir/name
logdt=datetime.datetime.now().strftime('%Y%m%d')
sep=os.sep
logdir=os.getcwd()+"%slog%s"  %(sep,sep)
datadir=os.getcwd()+"%sdata%s"  %(sep,sep)
# print logdir
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
logging.basicConfig(level=logging.DEBUG,
                    format='"%(asctime)s","%(filename)s","%(module)s","%(funcName)s","%(lineno)d","%(thread)d","%(threadName)s","%(process)d","%(levelno)s","%(levelname)s","%(relativeCreated)d","%(name)s","%(message)s"',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=logfile,
                    filemode='a')
def disk():
    try:
        if os.name == "nt":
            import win32file
            disk_path_data = os.popen("wmic logicaldisk get name").read()
            disklist = disk_path_data.split()
            disklist.remove('Name')
            diskinfoall = {}
            for path in disklist:
                res_list = win32file.GetDiskFreeSpace(str(path + "\\"))
                disk_dict = {}
                res_list = win32file.GetDiskFreeSpace(path)
                disk_ava = res_list[0] * res_list[1] * res_list[2]
                disk_sum = res_list[0] * res_list[1] * res_list[3]
                disk_use = disk_sum - disk_ava
                disk_use_per = disk_use / (disk_sum * 1.0)
                disk_dict['disk_use'] = disk_use
                disk_dict['disk_ava'] = disk_ava
                disk_dict['disk_sum'] = disk_sum
                disk_dict['disk_use_per'] = disk_use_per
                diskinfoall[path] = disk_dict
        elif os.name == "posix":
            mount = commands.getoutput('mount -v')
            lines = mount.split('\n')
            mount_list = map(lambda line: line.split()[2], lines)
            mount_list_dit = ['/proc', '/sys', '/dev/pts', '/proc/sys/fs/binfmt_misc']
            for i in mount_list_dit:
                mount_list.remove(i)
            diskinfoall = {}
            for path in mount_list:
                diskinfo = os.statvfs(path)
                disk_dict = {}
                disk_use = (diskinfo.f_blocks - diskinfo.f_bfree) * diskinfo.f_bsize / 1024
                disk_ava = (diskinfo.f_bavail) * diskinfo.f_bsize / 1024
                disk_sum = (diskinfo.f_blocks) * diskinfo.f_bsize / 1024
                disk_use_per = (diskinfo.f_blocks - diskinfo.f_bfree) * 100.00 / \
                               (diskinfo.f_blocks - diskinfo.f_bfree + diskinfo.f_bavail) + 1
                if disk_use == 0:
                    disk_use_per = 0
                disk_dict['disk_use'] = disk_use
                disk_dict['disk_ava'] = disk_ava
                disk_dict['disk_sum'] = disk_sum
                disk_dict['disk_use_per'] = disk_use_per
                diskinfoall[path] = disk_dict
    except BaseException, e:
        msg='This Is Exception,(%s)' %e
        logging.info(msg)
    finally:
        return diskinfoall
def cpu():
    try:
        cpuinfo = {}
        cpu_count = multiprocessing.cpu_count()
        cpu_load = os.getloadavg()
        cpu_load1 = cpu_load[0]
        cpu_load5 = cpu_load[1]
        cpu_load15 = cpu_load[2]
        cpuinfo['cpu_count'] = cpu_count
        cpuinfo['cpu_load1'] = ('%.2f' % (cpu_load1))
        cpuinfo['cpu_load5'] = ('%.2f' % (cpu_load5))
        cpuinfo['cpu_load15'] = ('%.2f' % (cpu_load15))
    except BaseException, e:
        msg = 'This Is Exception,(%s)' % e
        logging.info(msg)
    finally:
        return cpuinfo
def mem():
    try:
        meminfo = {}
        mem_list = commands.getoutput('more /proc/meminfo')
        mem_list = mem_list.split('\n')
        # mount_list = map(lambda line: line.split()[2], lines)
        mem_list = map(lambda line: line.split()[0:2], mem_list)
        try:
            for memlist in mem_list:
                meminfo[memlist[0]] = memlist[1]
        except BaseException, e:
            meminfo={}
            msg = 'This Is Exception,(%s)' % e+str(mem_list)
            logging.info(msg)
    except BaseException, e:
        msg='This Is Exception,(%s)' %e
        logging.info(msg)
    finally:
        return meminfo
def net():
    try:
        netinfo={}
        def map_list_sum(net_e,net_s):
            i_dict = {}
            for i in    range(len(net_s)):
                if  net_e[i][0]==net_s[i][0]:
                    m_dict = {}
                    for m in    range(1,len(net_e[i])):
                        m_dict[str(net_e[i][0]+''+str(m))]=abs(int(net_e[i][m])/2.00-int(net_s[i][m])/2.00)
                    i_dict[net_e[i][0]]=m_dict
            return   i_dict
        net_s=commands.getoutput('more /proc/net/dev').split('\n')[2:]
        time.sleep(1)
        net_e=commands.getoutput('more /proc/net/dev').split('\n')[2:]
        net_e=map(lambda a:a.split(),net_e)
        net_s=map(lambda a:a.split(),net_s)
        netinfo = map_list_sum(net_e, net_s)
    except BaseException, e:
        msg = 'This Is Exception,(%s)' % e
        logging.info(msg)
    finally:
        return netinfo
def save2json(dt,lock,type):
    data={}
    lock.acquire()
    data['data'] = dt
    data['time']=str(datetime.datetime.now())
    data['type'] = type
    with open(datafile, 'ab') as file:
        json.dump(data, file)
        file.write('\n')
    lock.release()
def warining():
    pass

def cmd_type():
    monitor_type = {}
    monitor_type['disk'] = disk()
    monitor_type['net'] = net()
    monitor_type['cpu'] = cpu()
    return  monitor_type
if __name__ == '__main__':
    start_dt=datetime.datetime.now()
    msg = 'start:'+str(start_dt)
    logging.info(msg)
    from multiprocessing import Process, Lock
    lock = Lock()
    # for i in cmd_type():
    #     data=cmd_type()[i]
    #     t = multiprocessing.Process(target=save2json, args=(data, lock,i), ).start()
    pool = multiprocessing.Pool(processes=10)
    for i in range(0, 100):
        msg = "hello %d" % (i)
        res = pool.apply_async(save2json, args=(disk(),lock, 'disk',), )
        print  'start',res, i
    pool.close()
    pool.join()
    print "all done."
    end_dt=datetime.datetime.now()
    msg = 'end:'+str(end_dt)+',execute:'+str(end_dt - start_dt)
    logging.info(msg)

