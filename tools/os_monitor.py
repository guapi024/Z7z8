# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : os_monitor.py
'''
import  os,sys,datetime,time,json,logging,platform,commands,multiprocessing


##dict
osinfo={}
cpu_count=multiprocessing.cpu_count()


##create log dt/dir/name
logdt=datetime.datetime.now().strftime('%Y%m%d')
if platform.system()=="Windows":
    logdir=os.getcwd()+"\\log"+"\\"
else:
    logdir = os.getcwd() + "/log" + "/"
# print logdir
if os.path.exists(logdir)==False:
    os.mkdir(logdir)
else:
    pass
logfile=logdir+os.path.split(os.path.realpath( sys.argv[0]))[-1].split('.')[0]+logdt+".log"
# print logfile
logging.basicConfig(level=logging.DEBUG,
                    format='"%(asctime)s","%(filename)s","%(module)s","%(funcName)s","%(lineno)d","%(thread)d","%(threadName)s","%(process)d","%(levelno)s","%(levelname)s","%(relativeCreated)d","%(name)s","%(message)s"',
                    datefmt='%Y%m%d%H%M%S',
                    filename=logfile,
                    filemode='a')
# logging.debug('This is debug message')
# logging.info('This is info message')
# logging.warning('This is warning message')


if  os.name=="nt":
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
    osinfo['disk'] = diskinfoall
elif    os.name=="posix":
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
        disk_use = (diskinfo.f_blocks - diskinfo.f_bfree) * diskinfo.f_bsize / 1024  # "磁盘使用"
        disk_ava = (diskinfo.f_bavail) * diskinfo.f_bsize / 1024  # "磁盘可用"
        disk_sum = (diskinfo.f_blocks) * diskinfo.f_bsize / 1024  # "磁盘总计"
        disk_use_per = (diskinfo.f_blocks - diskinfo.f_bfree) * 100.00 / \
                       (diskinfo.f_blocks - diskinfo.f_bfree + diskinfo.f_bavail) + 1  # "磁盘使用百分比"
        ## 过滤数据
        if disk_use == 0:
            disk_use_per = 0
        disk_dict['disk_use'] = disk_use
        disk_dict['disk_ava'] = disk_ava
        disk_dict['disk_sum'] = disk_sum
        disk_dict['disk_use_per'] = disk_use_per
        diskinfoall[path] = disk_dict
    osinfo['disk'] = diskinfoall


print osinfo


cpuinfo={}
cpu_count=multiprocessing.cpu_count()
cpu_load=os.getloadavg()
cpu_load1=cpu_load[0]
cpu_load5=cpu_load[1]
cpu_load15=cpu_load[2]
cpuinfo['cpu_count']=cpu_count
cpuinfo['cpu_load1']=('%.2f' %(cpu_load1))
cpuinfo['cpu_load5']=('%.2f' %(cpu_load5))
cpuinfo['cpu_load15']=('%.2f' %(cpu_load15))
print   cpuinfo


disk_path_data = os.popen("more /proc/meminfo").read()
commands.getoutput('more /proc/meminfo')

import commands
mem_list = commands.getoutput('more /proc/meminfo')
mem_list = mem_list.split('\n')
# mount_list = map(lambda line: line.split()[2], lines)
mem_list = map(lambda line: line.split()[0:2], mem_list)
meminfo={}
for memlist in mem_list:
    meminfo[memlist[0]]=memlist[1]
    print memlist[0],memlist[1]
osinfo['mem']=meminfo

import commands,time
net_s=commands.getoutput('more /proc/net/dev').split('\n')[2:]
time.sleep(1)
net_e=commands.getoutput('more /proc/net/dev').split('\n')[2:]
for net_s_list in net_s:
    print   net_s_list.split()
for net_e_list in net_e:
    print   net_e_list.split()

