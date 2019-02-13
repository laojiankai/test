#coding:utf-8
#!usr/bin/python

import sys
import requests
import time
'''
from userMessage import *


reload(sys)
sys.setdefaultencoding('utf-8')

headers = {'content-type': 'application/json', 'Zeus-Context-Service-Path': 'Zeus-Context-Service-Path'}

def sendlogsmsV2(mobile):
    sendlogsmsV2_url = "http://192.168.1.253:10003/ihome-api/verification/sendSmsCode"
    #sendlogsmsV2_url = "http://boss.sit.ihomefnt.org/ihome-api/verification/sendSmsCode"
    sendlogsmsV2_param = {
                            "ip": "172.16.2.83",
                            "mobile": "%d" %mobile,
                            "type": 2
                        }

    print sendlogsmsV2_param

    response = requests.post(sendlogsmsV2_url, json=sendlogsmsV2_param, headers=headers)
    try:
        if response.status_code == 200:
            print response.text
            print response.json()
    except:
        print "短信验证码发送失败"

def login(mobile,smsCode):
    #newvalidelogsms_url = "http://192.168.1.247:10031/o2o-api/account/newvalidelogsms"
    newvalidelogsms_url = "http://api.sit.ihomefnt.org/account/newvalidelogsms"
    newvalidelogsms_param = {
                                "mobile": "%d" %mobile,
                                "appVersion": "5.0.0",
                                "osType": 1,
                                "location": "南京",
                                "deviceType": "iPhone 7",
                                "width": 750,
                                "parterValue": 100,
                                "sms": "%s" %smsCode,
                                "systemVersion": "11.4.1",
                                "deviceToken": "0BB73E7B-534E-458A-A044-E46E469BC34E",
                                "login": 1
                            }
    print newvalidelogsms_param

    response = requests.post(newvalidelogsms_url, json=newvalidelogsms_param, headers=headers)
    if response.status_code == 200:
        print response.text
        print response.json()


def addCustomer(mobile):
    #新增客户
    #userId = getUserId(mobile)
    addCustomer_url = "https://boss.sit.ihomefnt.org/aladdin-order/customer/addCustomer"
    addCustomer_param = {
                "mobile": "%d" %mobile,
                "name": "阿斯顿",
                "gender": "1",
                "openingBank": "",
                "operatorId": 539,
                "sessionId": "1"
            }
    print addCustomer_param
    response = requests.post(addCustomer_url, json=addCustomer_param, headers=headers)
    if response.status_code == 200:
        print response.text + ('\n')
        print response.json()
    else:
        print response.text + ('\n')
        print response.json()


def saveHouseProperty(mobile):

    customerId = getCustomerId(mobile)
    print mobile,customerId
    #创建全品价订单
    saveHouseProperty_url = "https://boss.sit.ihomefnt.org/aladdin-order/houseProperty/saveHouseProperty"
    saveHouseProperty_param = {
                "customerBaseInfoParamDto": {
                    "customerName": "阿斯顿",
                    "customerId": "%s" %customerId,
                    "mobile": "%d" %mobile
                },
                "housePropertyInfoParamDto": {
                    "adviser": 539,
                    "buildingId": 291,
                    "zoneId": 457,
                    "housingNum": "1",
                    "unitNum": "1",
                    "roomNum": "3402",
                    "area": 90,
                    "shortLayoutInfo": "2室2厅1厨1卫1阳台",
                    "layoutName": "A",
                    "layoutId": 1495,
                    "expectedSubmitData": 1543766400000,
                    "layoutRoom": "2",
                    "layoutLiving": "2",
                    "layoutKitchen": "1",
                    "layoutStorage": "0",
                    "layoutCloak": "0",
                    "layoutBalcony": "1",
                    "companyId": 8
                },
                "housePropertyInfoExtParamDto": {
                    "deliverStatus": 2,
                    "deliverTime": "2018-12-03"
                },
                "expectTimeStr": "2019-03-03",
                "orderSaleType": 1,
                "preContractAmount": 200000,
                "operatorId": 539,
                "sessionId": "1"
            }
    print saveHouseProperty_param

    response = requests.post(saveHouseProperty_url, json=saveHouseProperty_param, headers=headers)
    if response.status_code == 200:
        print response.text
        print response.json()
    else:
        print response.text
        print response.json()

def handleEarnestMoney(mobile):
    #收意向金
    userId = getUserId(mobile)
    orderNum,houseId = getOrderIdAndHouseId(userId)
    handleEarnestMoney_url = "https://boss.sit.ihomefnt.org/aladdin-order/transaction/handleEarnestMoney"
    handleEarnestMoney_param = {
                                    "payType": 24,
                                    "transtionAmount": "1999",
                                    "remark": "意向金",
                                    "orderNum": "%s" %orderNum ,
                                    "userId": "%s" %userId ,
                                    "operatorId": 539,
                                    "sessionId": "1"
                                }
    print handleEarnestMoney_param

    response = requests.post(handleEarnestMoney_url, json=handleEarnestMoney_param, headers=headers)
    if response.status_code == 200:
        print response.text
        print response.json()
        confirmFund(mobile,0)
    else:
        print response.text
        print response.json()


def updateHouseProperty(mobile):
    #更新房产信息
    userId = getUserId(mobile)
    customerId = getCustomerId(mobile)
    orderId,houseId = getOrderIdAndHouseId(userId)
    updateHouseProperty_url = "https://boss.sit.ihomefnt.org/aladdin-order/houseProperty/updateHouseProperty"
    updateHouseProperty_param = {
                                    "houseId": "%s" %houseId,
                                    "orderId": "%s" %orderId,
                                    "customerBaseInfoParamDto": {
                                        "customerId": "%s" %customerId,
                                        "customerName": "阿斯顿"
                                    },
                                    "expectTimeStr": "2019-03-03",
                                    "housePropertyInfoParamDto": {
                                        "adviser": 539,
                                        "buildingId": 291,
                                        "zoneId": 457,
                                        "housingNum": "1",
                                        "unitNum": "1",
                                        "roomNum": "3402",
                                        "layoutId": 1495
                                    },
                                    "housePropertyInfoExtParamDto": {
                                        "deliverTime": "2018-12-03"
                                    },
                                    "operatorId": 539,
                                    "sessionId": "1"
                                }
    print updateHouseProperty_param

    response = requests.post(updateHouseProperty_url, json=updateHouseProperty_param, headers=headers)
    if response.status_code == 200:
        print response.text
        print response.json()
    else:
        print response.text
        print response.json()

def handleDepositMoney(mobile,money="1999"):
    #收定金
    userId = getUserId(mobile)
    orderNum,houseId = getOrderIdAndHouseId(userId)
    handleDepositMoney_url = "https://boss.sit.ihomefnt.org/aladdin-order/transaction/handleDepositMoney"
    handleDepositMoney_param = {
                                    "payType": 24,
                                    "transtionAmount": "%s" %money,
                                    "remark": "阿萨德撒打算",
                                    "orderNum": "%s" %orderNum,
                                    "userId": "%s" %userId,
                                    "operatorId": 539,
                                    "sessionId": "1"
                                }
    print handleDepositMoney_param

    response = requests.post(handleDepositMoney_url, json=handleDepositMoney_param, headers=headers)
    if response.status_code == 200:
        print response.text
        print response.json()
        confirmFund(mobile,1)
    else:
        print response.text
        print response.json()

def handleMoney(mobile,money="1999"):
        #收合同款
        userId = getUserId(mobile)
        orderNum, houseId = getOrderIdAndHouseId(userId)
        handleMoney_url = "https://boss.sit.ihomefnt.org/aladdin-order/transaction/handleMoney"
        handleMoney_param = {
                                "payNo": "%s" %orderNum,
                                "transtionAmount": "%s" %money,
                                "remark": "%s" %orderNum,
                                "payType": 24,
                                "operatorId": 539,
                                "sessionId": "1",
                                "orderNum": "%s" %orderNum,
                                "userId": "%s" %userId,
                                "orderStatus": 16
                            }
        print handleMoney_param
        response = requests.post(handleMoney_url,json=handleMoney_param,headers=headers)
        if response.status_code == 200:
            print response.text
            print response.json()
            confirmFund(mobile, 2)
        else:
            print response.text
            print response.json()

def commitDesignDemand(mobile):
    #选风格
    smsCode = getSmsCode(mobile)
    time.sleep(2)
    login(mobile,smsCode)
    userId = getUserId(mobile)
    accessToken = getAccessToken(userId)
    orderId,houseId = getOrderIdAndHouseId(userId)
    commitDesignDemand_url = "http://api.sit.ihomefnt.org/personalneed/commitDesignDemand"
    commitDesignDemand_param = {
                                    "location": "南京",
                                    "osType": 1,
                                    "appVersion": "5.0.0",
                                    "width": 750,
                                    "parterValue": 100,
                                    "accessToken": "%s" %accessToken,
                                    "deviceToken": "0BB73E7B-534E-458A-A044-E46E469BC34E",
                                    "mobileNum": "%d" %mobile,
                                    "budget": "34万",
                                    "remark": "Adffggh",
                                    "dnaId": 268,
                                    "orderId": "%s" %orderId
                                }
    print commitDesignDemand_param

    response = requests.post(commitDesignDemand_url, json=commitDesignDemand_param, headers=headers)
    if response.status_code == 200:
        print response.text
        print response.json()
    else:
        print response.text
        print response.json()

def createFamilyOrder(mobile):
    #创建订单
    userId = getUserId(mobile)
    accessToken = getAccessToken(userId)
    orderId,houseId = getOrderIdAndHouseId(userId)
    #createFamilyOrder_url = "http://192.168.1.31:10031/o2o-api/programOrder/v5/createFamilyOrder"
    createFamilyOrder_url = "http://api.sit.ihomefnt.org/programOrder/v5/createFamilyOrder"
    createFamilyOrder_param = {
                                    "location": "南京",
                                    "osType": 1,
                                    "appVersion": "5.0.0",
                                    "width": 750,
                                    "parterValue": 100,
                                    "accessToken": "%s" %accessToken,
                                    "deviceToken": "0BB73E7B-534E-458A-A044-E46E469BC34E",
                                    "mobileNum": "%d" %mobile,
                                    "orderId": "%s" %orderId,
                                    "houseId": "%s" %houseId,
                                    "roomIds": [24110, 24111, 24112, 24113, 24114, 24115, 24116],
                                    "opType": "1",
                                    "source": 0,
                                    "roomEffectImageDtos": [{
                                        "roomId": 24110,
                                        "pictureUrls": ["http://dr-3d.ihomefnt.com/1533371067413-2-b2ba866747294b50a4348009396c3c25.png?imageView2/2/w/375"]
                                    }, {
                                        "roomId": 24111,
                                        "pictureUrls": ["http://dr-3d.ihomefnt.com/1533371508285-2-d8f17d90dae1efe27769b7a06871f848.png?imageView2/2/w/375"]
                                    }, {
                                        "roomId": 24112,
                                        "pictureUrls": ["http://dr-3d.ihomefnt.com/1533373406727-2-89a008fa49fbb0e62975034253903a6a.png?imageView2/2/w/375"]
                                    }, {
                                        "roomId": 24113,
                                        "pictureUrls": ["http://dr-3d.ihomefnt.com/1533370503335-2-cc97560c1640ac5abe33210766537856.png?imageView2/2/w/375"]
                                    }, {
                                        "roomId": 24114,
                                        "pictureUrls": ["http://dr-3d.ihomefnt.com/1533377779109-2-53a4cdc24c5e99d2ad26bd335e404d86.png?imageView2/2/w/375"]
                                    }, {
                                        "roomId": 24115,
                                        "pictureUrls": ["http://dr-3d.ihomefnt.com/1533375130356-2-cdb1764c8a3e87046bee016e0f21b402.png?imageView2/2/w/375"]
                                    }, {
                                        "roomId": 24116,
                                        "pictureUrls": ["http://dr-3d.ihomefnt.com/1533375967906-2-d3f614e875ab6cf86c42822ad9944c30.png?imageView2/2/w/375"]
                                    }],
                                    "hardAddBagProducts": [],
                                    "replaceProductDtos": [],
                                    "replaceHardProductDtos": [{
                                        "roomId": 24110,
                                        "replaceHardProductDtoList": [],
                                        "addHardProductDtoList": []
                                    }, {
                                        "roomId": 24111,
                                        "replaceHardProductDtoList": [],
                                        "addHardProductDtoList": []
                                    }, {
                                        "roomId": 24112,
                                        "replaceHardProductDtoList": [],
                                        "addHardProductDtoList": []
                                    }, {
                                        "roomId": 24113,
                                        "replaceHardProductDtoList": [],
                                        "addHardProductDtoList": []
                                    }, {
                                        "roomId": 24114,
                                        "replaceHardProductDtoList": [],
                                        "addHardProductDtoList": []
                                    }, {
                                        "roomId": 24115,
                                        "replaceHardProductDtoList": [],
                                        "addHardProductDtoList": []
                                    }, {
                                        "roomId": 24116,
                                        "replaceHardProductDtoList": [],
                                        "addHardProductDtoList": []
                                    }]
                                }
    print createFamilyOrder_param

    response = requests.post(createFamilyOrder_url, json=createFamilyOrder_param, headers=headers)
    if response.status_code == 200:
        print response.text
        print response.json()
    else:
        print response.text
        print response.json()

def cancelOrderProgram(mobile):

    userId = getUserId(mobile)
    accessToken = getAccessToken(userId)
    orderId,houseId = getOrderIdAndHouseId(userId)
    #cancelOrderProgram_url = "http://192.168.1.31:10031/o2o-api/programOrder/cancelOrderProgram"
    cancelOrderProgram_url = "http://api.sit.ihomefnt.org/programOrder/cancelOrderProgram"
    cancelOrderProgram_param = {
                                    "location": "南京",
                                    "osType": 1,
                                    "appVersion": "5.0.0",
                                    "width": 750,
                                    "parterValue": 100,
                                    "accessToken": "%s" %accessToken ,
                                    "deviceToken": "0BB73E7B-534E-458A-A044-E46E469BC34E",
                                    "mobileNum": "%d" %mobile,
                                    "orderId": "%s" %orderId,
                                    "opType": "1"
                                }
    print cancelOrderProgram_param

    response = requests.post(cancelOrderProgram_url, json=cancelOrderProgram_param, headers=headers)
    if response.status_code == 200:
        print response.text
        print response.json()

def confirmFund(mobile,i):
    #确认收款
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    typeList = ["意向金","定金","合同款"]
    userId = getUserId(mobile)
    applyId = getApplyId(userId)
    confirmFund_url = "https://boss.sit.ihomefnt.org/finalkeeper-web/front/receiptApply/confirmFund"
    confirmFund_param = {
                            "userId": 539,
                            "applyId": "%s" %applyId,
                            "remark": "%s" %typeList[i],
                            "bankAccount": 2,
                            "actualPayTime": "%s 00:00:00" %today,
                            "payTimeStr": "%s 00:00:00" %today,
                            "actualAmount": 2999
                        }
    print confirmFund_param
    time.sleep(2)
    response = requests.post(confirmFund_url, json=confirmFund_param, headers=headers)
    if response.status_code == 200:
        print response.text
        print response.json()
    else:
        print response.text
        print response.json()






if __name__ == '__main__':
    #for mobile in range(15500000076,15500000077):
        #print mobile

        #新增客户
        #addCustomer(mobile)
        #新增全品家
        #saveHouseProperty(mobile)
        #收意向金及确认
        #handleEarnestMoney(mobile)
        #更新房产信息--该接口是允许客户收订单时更新客户房产信息
        #updateHouseProperty(mobile)
        #收定金及确认
        #handleDepositMoney(mobile,"40000")
        #确认定金
        #confirmFund(mobile, 1)
        #选风格
        #commitDesignDemand(mobile)
        #创建订单
        #createFamilyOrder(mobile)
        #取消订单
        #cancelOrderProgram(mobile)
        #收合同款
        #handleMoney(mobile,"181511")
'''
postData = {
            "action": "hqyzm",
            "sjh": 18652957980,
            "yzmYwlb": 02
            }

response = requests.post('http://95598.gx.csg.cn/kh/yhzc.do', postData)
print response.text