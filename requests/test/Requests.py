# -*- coding: utf-8 -*-
import requests
import json
import types

import urllib
import urllib2

def use_requests_demo():
    response = requests.get(URL_IP)
    print '>>>response.Headers'
    print response.headers
    print '>>>response.text'
    print response.text

def use_requests_post(url,data):
    response2 = requests.post(url,json=data)
    print response2.status_code
    print response2.text
    return response2.text

def json2str(jsonList):
    str = json.loads(jsonList)
    key_list = str.keys()
    success = str[u"success"]
    print key_list
    print success


def http_post():

    jdata = json.dumps(data,encoding='utf-8')  # 对数据进行JSON格式化编码
    req = urllib2.Request(URL_IP2,jdata)  # 生成页面请求的完整数据
    response = urllib2.urlopen(req)  # 发送页面请求
    return response.read()

if __name__ == '__main__':
        URL_IP = 'http://httpbin.org/ip'
        URL_IP2 = 'http://192.168.1.31:10003/ihome-api/account/queryAjbAccountByUserId'
        #URL_IP2 = 'http://boss.sit.ihomefnt.org/cms-web/order/query/481/211D50534B109D60F2FC813E85B229AB'
        data1 = {"userId": 12201}
        #data1 = {"pageNo":1,"pageSize":30,"userType":1,"customerTel":"18888888031"}
        data = json.dumps(data1)
        json_text = '{"origin": "218.94.135.74"}'
        #use_requests_demo()
        #json_get()
        outJson = use_requests_post(URL_IP2, data1)
        json2str(outJson)

