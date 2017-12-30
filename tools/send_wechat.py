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

    def get_token(corpid, corpsecret):
        try:
            wx_url_get = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
            wx_login = {'corpid': corpid,
                        'corpsecret': corpsecret}
            wx_get = requests.get(url=wx_url_get, params=wx_login)
            return json.loads(wx_get.text)['access_token']
        except Exception, e:
            return json.loads(wx_get.text)['errmsg']

    def post_msg(token, msg):
        try:
            msg = json.dumps(msg, ensure_ascii=False)
            wx_url_post = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % (token)
            wx_post = requests.post(wx_url_post, data=msg)
            return wx_post.text
        except Exception, e:
            print  'error is ', e, token

ss=main()
confpath='conf.ini'
print ss.load_conf(confpath)

# if __name__ == '__main__':