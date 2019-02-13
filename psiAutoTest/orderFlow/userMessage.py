#coding:utf-8
#!usr/bin/python

import MySQLdb
import re
from customerOrder import *

def mysql_select(sql):
    #连接数据库
    host = '192.168.1.32'
    PORT = '3306'
    user = 'root'
    passwd = 'aijia1234567'

    #sql = "SELECT id FROM aladdin_order.t_customer_base_info where mobile in ('15500000004')"

    db = MySQLdb.connect(host, user, passwd, charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    cursor.execute(sql)
    list = cursor.fetchall()
    db.close()
    #print list
    return list

def mysql_update(sql):
    #连接数据库
    host = '192.168.1.32'
    PORT = '3306'
    user = 'root'
    passwd = 'aijia1234567'
    #sql = "SELECT id FROM aladdin_order.t_customer_base_info where mobile in ('15500000004')"
    db = MySQLdb.connect(host, user, passwd, charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    cursor.execute(sql)
    db.close()
    print "账号密码更新成功"


def sqltuple2list(tuple):
    list = []
    list2 = []
    p = re.compile('\(|, |\)|Decimal\(\'|\'\)|L\,|L\)')
    p2 = re.compile('u\'|\'')
    for tup in tuple:
        q = p.split(str(tup))
        for str1 in q:
            if str1:
                list.append(str1)
        for str2 in list:
            if str2 == 'Decimal':
                continue
            elif str2.startswith('u'):
                list2.append(p2.split(str2)[1])
            elif str2 == 'None':
                list2.append('')
            else:
                list2.append(str2)
    return list2

def getUserId(mobile):
    sql0 = "select id from users.t_user where mobile= %d" %mobile
    print sql0
    list0 = mysql_select(sql0)
    userIdList = sqltuple2list(list0)
    userId = userIdList[0]
    print "userId: ", userId
    return userId

def getCustomerId(mobile):
    sql1 = "SELECT id FROM aladdin_order.t_customer_base_info where mobile = %d" %mobile
    list1 = mysql_select(sql1)
    customerIdList = sqltuple2list(list1)
    customerId = customerIdList[0]
    print "customerId:", customerId
    return customerId

def getOrderIdAndHouseId(userId):
    sql2 = "SELECT id,house_id FROM aladdin_order.t_aladdin_master_order where user_id= %s" % userId
    list2 = mysql_select(sql2)
    orderIdAndHouseIdList = sqltuple2list(list2)
    orderId = orderIdAndHouseIdList[0]
    houseId = orderIdAndHouseIdList[1]
    print "orderId:", orderId, "  houseId:", houseId
    return orderId , houseId

def getApplyId(userId):
    try:
        for i in range(1,3):
            sql3 = "SELECT id FROM finalkeeper.ar_receipt_apply where user_id =%s order by id desc limit 1" % userId
            list3 = mysql_select(sql3)
            applyIdList = sqltuple2list(list3)
            applyId = applyIdList[0]
            if applyId:
                print "applyId:", applyId
                break
            else:
                time.sleep(3)
                continue
        return applyId
    except:
        time.sleep(10)
        sql3 = "SELECT id FROM finalkeeper.ar_receipt_apply where user_id =%s" % userId
        list3 = mysql_select(sql3)
        applyIdList = sqltuple2list(list3)
        applyId = applyIdList[0]
        print "applyId:", applyId
        return applyId


def getSmsCode(mobile):
    sendlogsmsV2(mobile)
    time.sleep(1)
    sql5 = "SELECT sms_code FROM users.t_verification where mobile = %d order by id desc limit 1" % mobile
    list5 = mysql_select(sql5)
    smsCodeList = sqltuple2list(list5)
    smsCode = smsCodeList[0]
    print "smsCode:", smsCode
    #修改账号密码
    sql6 = "update users.t_user set password = 'e10adc3949ba59abbe56e057f20f883e' where mobile = '%s'" %mobile
    mysql_update(sql6)
    return smsCode

def getAccessToken(userId):
    sql4 = "SELECT access_token FROM users.t_auth where user_id =%s" % userId
    list4 = mysql_select(sql4)
    accessTokenList = sqltuple2list(list4)
    accessToken = accessTokenList[0]
    print "accessToken:", accessToken
    return accessToken


if __name__ == '__main__':

    userId =1
    #mobile = 15500000004
    #customerId= 96436
    #orderId = 10069967
    #houseId = 64109
    #applyId = 34882
    #accessToken = "1A54D6197A899B68A319B33F742B89F2"
    #根据手机号查询customerIdl
