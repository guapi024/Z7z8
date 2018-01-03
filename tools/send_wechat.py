# -*- coding: utf-8 -*-
'''
__author__ : renou
__file_name__ : send_wechat.py 
'''

import json
import requests
import ConfigParser

class main(object):

    def __init__(self):
        pass


    def load_conf(self,data):
        ini_dict = {}
        try:
            cnf = ConfigParser.SafeConfigParser()
            cnf.read(data)
            cs = cnf.sections()
            for i in cs:
                ci = cnf.items(i)
                ini_dict[i] = dict(ci)
        except ConfigParser.ParsingError, e:
            print u"error is %s" % e
        finally:
            return ini_dict

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
        print token,msg
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
            msg['content']=msgdata
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
        print msgdata







if __name__ == '__main__':
    ss = main()
    confpath = 'conf.ini'
    msgdata='test 123 '
    msgtype='text'
    ss.start(confpath,msgdata,msgtype)