#!/usr/bin/python
# -*- coding: UTF-8 -*-

#auto:laojiankai

import sys
import MySQLdb
#import types
import paramiko


def getData(sql):
    cursor.execute(sql)
    # 使用 fetchall() 方法获取全部数据。
    data = cursor.fetchall()
    return data

def delOrdInv(data):
    if data:
        print "开始删除进销存数据..."
        #删除进销存货物信息
        for d in data:
            # 根据订单id删除进销存中的待采购货物信息
            cursor.execute("select DISTINCT order_id from psi.t_purchase_detail where order_id = %s", d)
            d2 = cursor.fetchall()
            if d2:
                for d3 in d2:
                    cursor.execute("delete from psi.t_purchase_detail where order_id = %s", d3)
                    db.commit()

            #删除采购订单
            cursor.execute("select DISTINCT purchase_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data2 = cursor.fetchall()
            if data2:
                for s in data2:
                    cursor.execute("select id from psi.t_purchase_order where id = %s",s)
                    s2 = cursor.fetchall()
                    if s2:
                        #删除采购订单数据
                        cursor.execute("delete from psi.t_purchase_order where id = %s", s2)
                        db.commit()

                    cursor.execute("select DISTINCT purchase_order_id from psi.t_purchase_order_detail where purchase_order_id = %s", s)
                    s3 = cursor.fetchall()
                    if s3:
                        for s4 in s3:
                            #删除采购订单中的货物数据
                            cursor.execute("delete from psi.t_purchase_order_detail where purchase_order_id = %s", s4)
                        db.commit()

            #删除干线运输单
            cursor.execute("select DISTINCT linehault_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data3 = cursor.fetchall()
            if data3:
                for s in data3:
                    cursor.execute("select id from psi.t_line_haul where id = %s", s)
                    s2 = cursor.fetchall()
                    if s2:
                        cursor.execute("delete from psi.t_line_haul where id = %s",s2)
                        db.commit()

            #删除入库单信息
            cursor.execute("select stockin_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data4 = cursor.fetchall()
            if data4:
                for s in data4:
                    cursor.execute("select id from psi.t_stockin where id = %s", s)
                    s2 = cursor.fetchall()
                    if s2:
                        cursor.execute("delete from psi.t_stockin where id = %s", s2)
                        db.commit()

            #删除送货安装单信息
            cursor.execute("select DISTINCT delivery_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data5 = cursor.fetchall()
            if data5:
                for s in data5:
                    cursor.execute("select id from psi.t_delivery_order where id = %s", s)
                    s2 = cursor.fetchall()
                    if s2:
                        cursor.execute("delete from psi.t_delivery_order where id = %s", s2)
                        db.commit()

            #删除出库单信息
            cursor.execute("select DISTINCT stockout_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data6 = cursor.fetchall()
            if data6:
                for s in data6:
                    cursor.execute("select id from psi.t_stockout where id = %s",s)
                    s2 = cursor.fetchall()
                    if s2:
                        cursor.execute("delete from psi.t_stockout where id = %s", s2)
                        db.commit()

            #删除调拨单信息
            cursor.execute("select transfer_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data7 = cursor.fetchall()
            if data7:
                for s in data7:
                    cursor.execute("select id from psi.t_transfer_order_info where id = %s", s)
                    s2 = cursor.fetchall()
                    if s2:
                        cursor.execute("delete from psi.t_transfer_order_info where id = %s", s2)
                        db.commit()

            #删除关联关系psi.t_uid_ru_op
            cursor.execute("select id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data9 = cursor.fetchall()
            if data9:
                for s in data9:
                    cursor.execute("delete from psi.t_uid_ru_op where id = %s",s)
                    db.commit()
        print "进销存数据删除成功"
        print "开始删除物流订单数据..."
        #删除物流订单
        for d in data:
            cursor.execute("select DISTINCT wl_order_id from psi.t_logistics_order_cargos where order_id = %s", d)
            data8 = cursor.fetchall()
            if data8:
                for s in data8:
                    #删除物流订单数据
                    cursor.execute("select id from psi.t_logistics_order_info where id = %s",s)
                    s2 = cursor.fetchall()
                    if s2:
                        cursor.execute("delete from psi.t_logistics_order_info where id = %s",s2)
                        db.commit()

                    cursor.execute("select DISTINCT wl_order_id from psi.t_logistics_order_price_detail where wl_order_id = %s", s)
                    s3 = cursor.fetchall()
                    if s3:
                        #删除物流订单价格项
                        cursor.execute("delete from psi.t_logistics_order_price_detail where wl_order_id = %s", s3)
                        db.commit()

                    cursor.execute("select DISTINCT wl_order_id from psi.t_logistics_status_time_record where wl_order_id = %s",s)
                    s4 = cursor.fetchall()
                    if s4:
                        #删除物流订单状态记录信息
                        cursor.execute("delete from psi.t_logistics_status_time_record where wl_order_id = %s", s4)
                        db.commit()

                    cursor.execute("delete from psi.t_logistics_order_cargos  where wl_order_id = %s", s)
                    db.commit()
        print "物流订单删除结束"
        print "进销存数据删除结束"
    else:
        print "准备删除的进销存数据不存在..."

def delCusOrd(data):
    if data:
        print "开始删除订单数据..."
        # 删除订单信息
        for d in data:
            # 删除订单详情表t_order_detail中的测试数据
            cursor.execute("select DISTINCT fid_order from oms.t_order_detail where fid_order = %s", d)
            d2 = cursor.fetchall()
            if d2:
                cursor.execute("update oms.t_order_detail set delete_flag = 1 where fid_order = %s", d2)
                db.commit()

            # 删除订单信息
            cursor.execute("update oms.t_order set delete_flag = 1 where order_id = %s", d)
            db.commit()
        print"订单数据删除成功"
    else:
        print "准备删除的订单数据不存在..."

def delModelOrd(data):
    if data:
        print "开始删除样本单订单数据..."
        # 删除样本间订单信息
        for d in data:
            # 删除样本间订单详情表t_purchase_loft_order_detail中的测试数据
            cursor.execute("select idt_order_detail from oms.t_purchase_loft_order_detail where fid_order = %s", d)
            d2 = cursor.fetchall()
            if d2:
                for s in d2:
                    cursor.execute("delete from oms.t_purchase_loft_order_detail where idt_order_detail = %s", s)
                    db.commit()
            # 删除样本间订单信息
            cursor.execute("delete from oms.t_purchase_loft_order where idt_order = %s", d)
            db.commit()

def judeg(inputList):
    for i in inputList:
        cursor.execute("select order_id from oms.t_order where order_num = %s", i.split())
        result = cursor.fetchall()
        if result:
            print "开始删除订单ID:",i,"相关的进销存及订单数据......"
            delOrdInv(result)
            delCusOrd(result)
        else:
            cursor.execute("select order_id from oms.t_order where mobile = %s", i.split())
            result2 = cursor.fetchall()
            if result2:
                print "开始删除手机号:",i,"相关的进销存及订单数据......"
                delOrdInv(result2)
                delCusOrd(result2)
            else:
                cursor.execute("select idt_order from oms.t_purchase_loft_order where order_num = %s", i.split())
                result3 = cursor.fetchall()
                if result3:
                    print "开始删除样本间订单:",i,"相关的进销存及订单数据......"
                    delOrdInv(result3)
                    delModelOrd(result3)
                else:
                    cursor.execute("select idt_order from oms.t_purchase_loft_order where mobile = %s", i.split())
                    result4 = cursor.fetchall()
                    if result4:
                        print "开始删除手机号:",i,"相关的进销存及样本间订单数据......"
                        delOrdInv(result4)
                        delModelOrd(result4)
                    else:
                        print "未找到与",i,"相关要删除订单及进销存信息"

def connect():
    hostname = '121.196.205.228'
    port = 2525
    username = 'root'
    password = 'vr*$fz%3#1zl6jd#'
    execmd = "free"
    sshclient_execmd(hostname, port, username, password, execmd)

def sshclient_execmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command(execmd)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.

    #print stdout.read()
    #s.close()

def getOrderMessage():
    inputList = sys.argv[1:]
    return inputList

if __name__ == '__main__':
    #offline 22
    host = '192.168.1.22'
    PORT = '3306'
    user = 'root'
    passwd = 'aijia1234567'
    #database = 'oms'

    #读取要删除订单的订单号或客户手机号 输入参数以空格隔开s
    inputList = sys.argv[1:]
    #inputList = [('188888888',),('177777777',)]


    #筛选查询订单表t_order中的测试数据
    #sql = "select order_id from oms.t_order where order_id = 8180"

    #ssh = paramiko.SSHClient()
    #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #ssh.connect(hostname=hostname, port=port, username=username, password=password)

    # 打开数据库连接
    db = MySQLdb.connect(host, user, passwd)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    #judeg(inputList)
    #db.commit()