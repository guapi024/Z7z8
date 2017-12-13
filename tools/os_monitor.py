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
if platform.system()=="Windows":
    datadir=os.getcwd()+"\\data"+"\\"
else:
    datadir = os.getcwd() + "/data" + "/"

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
                    datefmt='%Y%m%d%H%M%S',
                    filename=logfile,
                    filemode='a')
# logging.debug('This is debug message')
msg='start '
logging.info(msg)
msg=''
# logging.warning('This is warning message')

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

def mail(receivers,info,sub,filename,partname):

    import smtplib, sys, os
    from email.mime.text import MIMEText ##
    from email.header import Header##
    from email.mime.multipart import MIMEMultipart  ##发送附件
    # from email.mime.image import MIMEImage  ##照片
    mail_host = 'smtp.qq.com'
    mail_user = '289010426@qq.com'
    mail_pass = 'svmyfirdorgxbjfa'
    sender = mail_user  # '289010426@qq.com'
    receivers = receivers #['243362276@qq.com']
    # receivers =  ['243362276@qq.com','hanchengliang@chinazyjr.com']
    message = MIMEMultipart()
    file_str = ''
    with open(filename, 'rt') as ff:
        for line in filter(None, ff):
            # print '<p>',line,'</p>'
            line = str('<p>' + line + '</p>')
            file_str += ''.join(line)

    mail_msg = """
    <p>log info:</p>
    <p>%s</p>
    <p>file name:</p>%s
    <p>file con start</p>
    <p>%s</p>
    <p>file con end</p>
     <!--<p><a href="http://www.renouh.com">链接</a></p>-->
    <p>ps:\n附件</p>
    """ % (info,filename, file_str)

    message.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    # message.attach(MIMEText(mail_msg, 'plain', 'utf-8'))
    att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="%s"' % filename
    message.attach(att1)
    ##循环发送所有文件
    # for root, dirs, files in os.walk(os.getcwd()):
    #     # print files
    #     for file in files:
    #         # print file
    #         if (file[-3:] == 'log' and file != partname):  ##and os.path.join(root,file)!=fileone): 绝对路径
    #             # print file
    #             att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
    #             att1["Content-Type"] = 'application/octet-stream'
    #             att1["Content-Disposition"] = 'attachment; filename="%s"' % file
    #             message.attach(att1)
    # message['From'] = mail_user  # Header("测试发件人", 'utf-8')
    message['From'] = 'from '
    message['To'] = 'to'
    subject = "%s" % sub
    message['Subject'] = sub
    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mail_host, 465)  # 25 为SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print u"sen mail ok"
    except smtplib.SMTPException, e:
        print u"error send mail fail is %s" % e


receivers=['289010426@qq.com',]
info='info'
sub='mail title'.upper()
filename='os_monitor20171205.log'

# print  mail(receivers,info,sub,filename,filename)
dirname=r'D:\pc\pc\note\Python\github\Z7z8\tools'
filetype='*log'

path=dirname+os.sep
for filename in os.listdir(path):
    if  os.path.isfile(path+filename):
            # print path+filename,filename
            print  filename

# for root, dirs, files in os.walk(path):
#     print files
    # # print files
    # for file in files:
    #     # print file
    #     if (file[-3:] == 'log' and file != partname):  ##and os.path.join(root,file)!=fileone): 绝对路径
    #         # print file
    #         att1 = MIMEText(open(file, 'rb').read(), 'base64', 'utf-8')
    #         att1["Content-Type"] = 'application/octet-stream'
    #         att1["Content-Disposition"] = 'attachment; filename="%s"' % file
    #         message.attach(att1)



# if __name__ == '__main__':
#
#     # filedata=disk()
#     start = time.time()
#     print 'start',datetime.datetime.now()
#
#     from multiprocessing import Process, Lock
#     lock = Lock()
#     # t = multiprocessing.Process(target=runx, args=(lock,datafile, '1',1,), ).start()
#     # t = multiprocessing.Process(target=runy, args=(lock,datafile, '1',1,), ).start()
#     end = time.time()
#     print 'end',datetime.datetime.now()
#     print str(round(end - start, 3)) + 's'