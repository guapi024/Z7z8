# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : monitor.py
'''
import  os,sys,datetime,time,json,logging,platform,commands,multiprocessing
import requests
import ConfigParser


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
##pro use inof mode
logging.basicConfig(level=logging.DEBUG,
                    format='"%(asctime)s","%(filename)s","%(module)s","%(funcName)s","%(lineno)d","%(thread)d","%(threadName)s","%(process)d","%(levelno)s","%(levelname)s","%(relativeCreated)d","%(name)s","%(message)s"',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=logfile,
                    filemode='a')

class os_monitor(object):
    def disk(self):
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
    def cpu(self):
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
    def mem(self):
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
    def net(self):
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
    def cmd_type(self):
        monitor_type = {}
        monitor_type['disk'] = self.disk()
        monitor_type['net'] = self.net()
        monitor_type['cpu'] = self.cpu()
        return monitor_type
class db_monitor(object):
    pass
class tools(object):
    def save2json(dt, type, seq):
        print   type, seq, datetime.datetime.now(), 'start'
        time.sleep(int((100 - seq) / 50.00))
        data = {}
        # lock.acquire()
        data['data'] = dt
        data['time'] = str(datetime.datetime.now())
        data['type'] = type
        data['seq'] = seq
        with open(datafile, 'ab') as file:
            json.dump(data, file)
            file.write('\n')
        # lock.release()
        print   type, seq, datetime.datetime.now(), 'end'
    def warining(self):
        pass
class send_wechat(object):
    def __init__(self):
        pass
    def load_conf(self,finename):
        if finename=='':
            finename='conf.ini'
        ini_dict = {}
        try:
            cnf = ConfigParser.SafeConfigParser()
            cnf.read(finename)
            cs = cnf.sections()
            for i in cs:
                ci = cnf.items(i)
                ini_dict[i] = dict(ci)
        except ConfigParser.ParsingError, e:
            print u"error is %s" % e
        finally:
            return ini_dict
    def update_conf(self,finename,cs,ci,data):
        if finename=='':
            finename='conf.ini'
        cnf = ConfigParser.SafeConfigParser()
        cnf.read(finename)
        cnf.set(cs, ci,data)
        cnf.write(open(finename, "w"))
    def get_token(self,corpid, corpsecret):
        try:
            wx_url_get = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
            wx_login = {'corpid': corpid,
                        'corpsecret': corpsecret}
            wx_get = requests.get(url=wx_url_get, params=wx_login)
            return json.loads(wx_get.text)['access_token']
        except Exception, e:
            return json.loads(wx_get.text)['errmsg']
    def post_msg(self,token, msg):
        try:
            msg = json.dumps(msg, ensure_ascii=False)
            wx_url_post = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % (token)
            wx_post = requests.post(wx_url_post, data=msg)
            return wx_post.text

        except Exception, e:
            print  'error is ', e, token
    def msg(self,data,msgdata,msgtype):
        msg={}
        msg['touser'] = data['touser']
        msg['toparty'] = data['toparty']
        msg['totag'] = data['totag']
        msg['agentid'] = data['agentid']
        msg['safe'] = data['safe']
        msg['msgtype'] = msgtype
        if  msgtype=='text':
            msg['text']=msgdata
        if  msgtype=='other':
            msg['other']='other '
        return msg
    def start(self,cnf,msgdata,msgtype):
        wechat_cnf=self.load_conf(cnf)['wechat']
        # print wechat_cnf
        access_token=wechat_cnf['access_token']
        if  access_token:
            access_token=access_token
        else:
            access_token=self.get_token(wechat_cnf['corpid'],wechat_cnf['corpsecret'])
        msgdata=self.msg(wechat_cnf,msgdata,msgtype)
        # print msgdata
        res_post_msg=self.post_msg(access_token,msgdata)
        res_post_msg=json.loads(res_post_msg)['errmsg']
        if  res_post_msg!='ok':
            access_token = self.get_token(wechat_cnf['corpid'], wechat_cnf['corpsecret'])
            self.update_conf(cnf,'wechat','access_token',access_token)

def test_sleep(data):
    # time.sleep(data)
    msg='%s sleep'%data
    logging.info(msg)
    time.sleep(int((100 - data) / 50.00))
    # print int((100 - data) / 50.00)
    msg='%s end'%data
    logging.info(msg)
def start():
    pool = multiprocessing.Pool(processes=10)
    from multiprocessing import Process, Lock
    lock = Lock()
    # for i in range(0, 100):
    #     msg = "hello %d" % (i)
    #     logging.info(msg+'start')
    #     # for x in cmd_type():
    #     res = pool.apply_async(test_sleep, args=(i,), )
        # print  res.successful()
        # print  res.ready()
    sw = send_wechat()
    confpath = 'conf.ini'
    msgdata={}
    msgdata= {"content": "title:title\nerror:\ntest111"}
    msgtype='text'
    for i in range(10):
        dt=str(datetime.datetime.now())
        msgdata['content']=str(i)+msgdata['content']
        # sw.start(confpath,msgdata,msgtype)
        ss=sw.start(confpath,msgdata,msgtype)
        res=pool.apply_async(ss,)
        print res
    pool.close()
    pool.join()

    # ts=tools()
    # om=os_monitor()
    # dm=db_monitor()
    # sw=send_wechat()
    # try:
    #     confpath = 'conf.ini'
    #     msgdata={}
    #     msgdata= {"content": "title:title\nerror:\ntest111"}
    #     msgtype='text'
    #     sw.start(confpath,msgdata,msgtype)
    # except Exception,e:
    #     print logging.info(e)



if __name__ == '__main__':
    start_dt = datetime.datetime.now()
    msg = 'start:' + str(start_dt)
    logging.info(msg)
    start()
    print 'all end'
    end_dt = datetime.datetime.now()
    msg = 'start:' + str(start_dt)+','+'end:' + str(end_dt) + ',execute:' + str(end_dt - start_dt)
    logging.info(msg)
