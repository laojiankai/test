#coding:utf-8
#!usr/bin/python

from keywords.publicKey import *
from drivers import *
import sys
import requests
import json
import types
import logging

reload(sys)
sys.setdefaultencoding('utf-8')

#browser= chromeBrowser

def logisticsOrderCallBack():

    #回调地址
    callBackUrl = "http://192.168.1.32:10028/alien-web/logistics/status/invoke"

    businessKey = globalVariables.logsticsOrderNum
    completeTime = globalVariables.completeTime
    #customerOrderNum = globalVariables.ord_orderNum
    #customerOrderOwn = globalVariables.ord_orderOwn
    customerOrderNum = globalVariables.pur_orderNum
    customerOrderOwn = globalVariables.pur_orderOwn
    appointDoorTime = globalVariables.appointDoorTime
    updateTime = globalVariables.updateTime
    signTime = globalVariables.signTime
    signResourceAddress = globalVariables.signResourceAddress
    if globalVariables.companyName == u"日日顺":
        caller = u"RRS"
    elif globalVariables.companyName == u"蚁安居":
        caller = u"YAJ"


    orderStatusList = [30,40,50,60,71,81]
    for orderStatus in orderStatusList:
    #params = {"businessKey":"%s"%businessKey,"logisticsOrderNum":"2438746821","caller":"YAJ","token":"@#@%SDJHADJAGFAHAHJFGHAYJ","uuid":"ADFNSDFIEKBFO","orderStatus":30,"rejectCause":"","completeTime":"%s"%completeTime,"appointedCustomerList":[{"customerOrderNum":"%s"%,"customerName":"曾维平","appointDoorTime":"2017-08-24 10:00:05","updateTime":"2017-08-24 10:30:05"}],"signCustomerList":[{"customerOrderNum":"10074365","customerName":"测试1111","signTime":"2017-08-24 15:40:05","signResourceAddress":"河南商丘市虞城县 虞城建业城 25栋2501"}]}

        param = {
              "businessKey": "%s"%businessKey,
              "logisticsOrderNum": "2438746821",
              "caller": "%s"%caller,
              "token": "@#@%SDJHADJAGFAHAHJFGHAYJ",
              "uuid": "ADFNSDFIEKBFO",
              "orderStatus": "%s"%orderStatus,
              "rejectCause": "",
              "completeTime": "%s"%completeTime,
              "appointedCustomerList": [
                {
                  "customerOrderNum": "%s"%customerOrderNum,
                  "customerName": "%s"%customerOrderOwn,
                  "appointDoorTime": "%s"%appointDoorTime,
                  "updateTime": "%s"%updateTime
                }
              ],
              "signCustomerList": [
                {
                  "customerOrderNum": "%s"%customerOrderNum,
                  "customerName": "%s"%customerOrderOwn,
                  "signTime": "%s"%signTime,
                  "signResourceAddress": "%s"%signResourceAddress
                }
              ]
            }
        '''
        param = {
            "businessKey": "WL201709300002",
            "logisticsOrderNum": "2438746821",
            "caller": "YAJ",
            "token": "@#@%SDJHADJAGFAHAHJFGHAYJ",
            "uuid": "ADFNSDFIEKBFO",
            "orderStatus": "81",
            "rejectCause": "",
            "completeTime": "2017-11-29 10:00:05",
            "appointedCustomerList": [
                {
                    "customerOrderNum": "YBJ20170928000001",
                    "customerName": "董婳",
                    "appointDoorTime": "2017-11-29 13:00:00",
                    "updateTime": "2017-11-29 13:00:00"
                }
            ],
            "signCustomerList": [
                {
                    "customerOrderNum": "YBJ20170928000001",
                    "customerName": "董婳",
                    "signTime": "2017-11-29 15:00:00",
                    "signResourceAddress": "江苏南京市栖霞区 土城头路和天和路交汇处"
                }
            ]
        }
        '''
        #print "########", json.dumps(param, sort_keys=True, ensure_ascii=False, indent=4)

        response2 = requests.post(callBackUrl,json=param)
        if response2.status_code == 200:
            print "orderStatus：" + param["orderStatus"]
            print "statusCode: " + str(response2.status_code)
            print response2.text + ('\n')
            logging.info("orderStatus：" + param["orderStatus"])
            logging.info("statusCode: " + str(response2.status_code))
            logging.info(response2.text + ('\n'))

            #print response2.json()
            #print json.dumps(response2.json(), sort_keys=True, ensure_ascii=False, indent=4)
            sleep(2)
            browser.refresh()
            sleep(3)
        else:
            print "orderStatus：" + param["orderStatus"]
            print "statusCode: " + str(response2.status_code)
            print response2.text + ('\n')
            logging.info("orderStatus：" + param["orderStatus"])
            logging.info("statusCode: " + str(response2.status_code))
            logging.info(response2.text + ('\n'))
            #print response2.json()
            #print json.dumps(response2.json(), sort_keys=True, ensure_ascii=False, indent=4)
            break




if __name__ == '__main__':
    logisticsOrderCallBack()