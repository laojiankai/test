#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector
#import  sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

def queryPurchaseTestData():

    #筛选采购计划中测试数据
    cursor.execute("SELECT id FROM psi.t_purchase_detail where cargo_name like '%测试%' and status !=  '-1'")
    d1 = cursor.fetchall()
    if d1:
        dataList1 = []
        for d in d1:
            dataList1.append(d[0])
        print "采购计划主表t_purchase_detail中测试数据ID：",dataList1
    else:
        print "采购计划中未查询到需要删除的测试数据！"

    #查询采购订单测试数据
    cursor.execute("SELECT distinct order_num FROM psi.t_purchase_order where order_name like '%测试%'")
    d2 = cursor.fetchall()
    if d2:
        dataList2 = []
        for d in d2:
            dataList2.append(d[0].encode('utf8'))
        print "采购订单主表t_purchase_order中测试数据订单号：",dataList2
    else:
        print "采购中为查询到需要删除的测试订单数据"

    cursor.execute("SELECT distinct order_id  FROM aladdin_dms.t_deliver_cargo where cargo_name like '%测试%'")
    d3 = cursor.fetchall()
    if d3:
        dataList3 = []
        for d in d3:
            dataList3.append(d[0])
        print "交付中心主表t_deliver中包含测试商品的订单号：",dataList3
    else:
        print "交付中心没有查询到包含测试商品信息的订单信息"


if __name__ == '__main__':

    config = {
        'host': '192.168.1.32',
        'user': 'root',
        'password': 'aijia1234567',
        'charset': 'utf8'
    }
    # 打开数据库连接
    try:
        cnn = mysql.connector.connect(**config)
    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
    cursor = cnn.cursor()
    try:
        queryPurchaseTestData()
    except mysql.connector.Error as e:
        print('query error!{}'.format(e))
    finally:
        cursor.close()
        cnn.close()
