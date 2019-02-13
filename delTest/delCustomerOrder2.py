#!/usr/bin/python
# -*- coding: UTF-8 -*-

#auto:laojiankai

import sys
import MySQLdb
import  types

#from main import *

def getData(sql):
    cursor.execute(sql)
    # 使用 fetchall() 方法获取全部数据。
    data = cursor.fetchall()
    return data

def printOrdInv(data):
    if data:
        #print "开始删除进销存数据..."
        #删除进销存货物信息
        for d in data:
            #print d
            # 根据订单id删除进销存中的待采购货物信息
            cursor.execute("select DISTINCT order_id from psi.t_purchase_detail where order_id = %s", d)
            d2 = cursor.fetchall()
            if d2:
                print "带采购货物订单ID：", d2
                #for d3 in d2:
                #    cursor.execute("delete from psi.t_purchase_detail where order_id = %s", d3)
                #   db.commit()

            #删除采购订单
            cursor.execute("select DISTINCT purchase_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data2 = cursor.fetchall()
            if data2:
                for s in data2:
                    cursor.execute("select id from psi.t_purchase_order where id = %s",s)
                    s2 = cursor.fetchall()
                    if s2:
                        print "采购订单ID：",s2
                        #删除采购订单数据
                        #cursor.execute("delete from psi.t_purchase_order where id = %s", s2)
                        #db.commit()

                    cursor.execute("select DISTINCT purchase_order_id from psi.t_purchase_order_detail where purchase_order_id = %s", s)
                    s3 = cursor.fetchall()
                    if s3:
                        for s4 in s3:
                            print "采购订单货物关联订单ID：",s4
                            #删除采购订单中的货物数据
                            #cursor.execute("delete from psi.t_purchase_order_detail where purchase_order_id = %s", s4)
                            #db.commit()

            #删除干线运输单
            cursor.execute("select DISTINCT linehault_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data3 = cursor.fetchall()
            if data3:
                for s in data3:
                    cursor.execute("select id from psi.t_line_haul where id = %s", s)
                    s2 = cursor.fetchall()
                    if s2:
                        print "干线运输单ID：",s2
                        #cursor.execute("delete from psi.t_line_haul where id = %s",s2)
                        #db.commit()

            #删除入库单信息
            cursor.execute("select DISTINCT stockin_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data4 = cursor.fetchall()
            if data4:
                for s in data4:
                    cursor.execute("select id from psi.t_stockin where id = %s", s)
                    s2 = cursor.fetchall()
                    if s2:
                        print "入库单ID：",s2
                        #cursor.execute("delete from psi.t_stockin where id = %s", s2)
                        #db.commit()

            #删除送货安装单信息
            cursor.execute("select DISTINCT delivery_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data5 = cursor.fetchall()
            if data5:
                for s in data5:
                    cursor.execute("select id from psi.t_delivery_order where id = %s", s)
                    s2 = cursor.fetchall()
                    if s2:
                        print "送货安装单ID：",s2
                        #cursor.execute("delete from psi.t_delivery_order where id = %s", s2)
                        #db.commit()

            #删除出库单信息
            cursor.execute("select DISTINCT stockout_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data6 = cursor.fetchall()
            if data6:
                for s in data6:
                    cursor.execute("select id from psi.t_stockout where id = %s",s)
                    s2 = cursor.fetchall()
                    if s2:
                        print "出库单ID：",s2
                        #cursor.execute("delete from psi.t_stockout where id = %s", s2)
                        #db.commit()

            #删除调拨单信息
            cursor.execute("select DISTINCT transfer_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data7 = cursor.fetchall()
            if data7:
                for s in data7:
                    cursor.execute("select id from psi.t_transfer_order_info where id = %s", s)
                    s2 = cursor.fetchall()
                    if s2:
                        print "调拨单ID：",s2
                        #cursor.execute("delete from psi.t_transfer_order_info where id = %s", s2)
                        #db.commit()

            #删除关联关系psi.t_uid_ru_op
            cursor.execute("select id from psi.t_uid_ru_op where sale_order_id = %s", d)
            data9 = cursor.fetchall()
            if data9:
                print "关联关系表t_uid_ru_op：",data9
                #for s in data9:
                    #cursor.execute("delete from psi.t_uid_ru_op where id = %s",s)
                    #db.commit()

        #print "进销存数据删除成功"
        #print "开始删除物流订单数据..."
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
                        print "物流订单ID：",s2
                        #cursor.execute("delete from psi.t_logistics_order_info where id = %s",s2)
                        #db.commit()

                    cursor.execute("select DISTINCT wl_order_id from psi.t_logistics_order_price_detail where wl_order_id = %s", s)
                    s3 = cursor.fetchall()
                    if s3:
                        print "物流订单价格项：",s3
                        #删除物流订单价格项
                        #cursor.execute("delete from psi.t_logistics_order_price_detail where wl_order_id = %s", s3)
                        #db.commit()

                    cursor.execute("select DISTINCT wl_order_id from psi.t_logistics_status_time_record where wl_order_id = %s",s)
                    s4 = cursor.fetchall()
                    if s4:
                        print "物流订单状态记录信息ID：",s4
                        #删除物流订单状态记录信息
                        #cursor.execute("delete from psi.t_logistics_status_time_record where wl_order_id = %s", s4)
                        #db.commit()
                    print "物流计划ID：",s
                    #cursor.execute("delete from psi.t_logistics_order_cargos  where wl_order_id = %s", s)
                    #db.commit()
    else:
        print "准备删除的进销存数据不存在..."

def printCusOrd(data):
    if data:
        #print "开始删除订单数据..."
        # 删除订单信息
        for d in data:
            # 删除订单详情表t_order_detail中的测试数据
            cursor.execute("select DISTINCT fid_order from oms.t_order_detail where fid_order = %s", d)
            d2 = cursor.fetchall()
            if d2:
                print "客户订单货物详情ID：",d2
                #cursor.execute("update oms.t_order_detail set delete_flag = 1 where fid_order = %s", d2)
                #db.commit()

            # 删除订单信息
            print "客户订单ID：",d
            #cursor.execute("update oms.t_order set delete_flag = 1 where order_id = %s", d)
            #db.commit()
        #print"订单数据删除成功"
    else:
        print "准备删除的订单数据不存在..."

def printModelOrd(data):
    if data:
        #print "开始删除样本单订单数据..."
        # 删除样本间订单信息
        for d in data:
            # 删除样本间订单详情表t_purchase_loft_order_detail中的测试数据
            cursor.execute("select idt_order_detail from oms.t_purchase_loft_order_detail where fid_order = %s", d)
            d2 = cursor.fetchall()
            if d2:
                print "样本间订单货物ID：",d2
                #for s in d2:
                    #cursor.execute("delete from oms.t_purchase_loft_order_detail where idt_order_detail = %s", s)
                    #db.commit()
            # 删除样本间订单信息
            print "样本间订单ID：",d
            #cursor.execute("delete from oms.t_purchase_loft_order where idt_order = %s", d)
            #db.commit()

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
            cursor.execute("select DISTINCT stockin_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
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
            cursor.execute("select DISTINCT transfer_order_id from psi.t_uid_ru_op where sale_order_id = %s", d)
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

def delAladdinOrder(orderNum):
    if orderNum:
        for num in orderNum:
            cursor.execute("select id from aladdin_order.t_add_bags_order_info where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("update aladdin_order.t_add_bags_order_info set del_flag = 1 where id = %s", d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_aladdin_master_order where id = %s;", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("update aladdin_order.t_aladdin_master_order set del_flag = 1 where id = %s", d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_hard_order_info where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("select id from aladdin_order.t_hard_order_room where hard_order_id = %s", d2)
                    d3 = cursor.fetchall()
                    if d3:
                        for d4 in d3:
                            cursor.execute("update aladdin_order.t_hard_order_room set del_flag = 1 where id = %s", d4)
                            db.commit()
                    cursor.execute("update aladdin_order.t_hard_order_info where order_num = %s", d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_room_product_detail where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("update aladdin_order.t_room_product_detail set del_flag = 1 where id = %s", d2)
                    db.commit()

            cursor.execute("select id from  aladdin_order.t_snapshot_cargo_info where order_num = %s",num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("select id from aladdin_order.t_snapshot_package_info where cargo_info_id = %s", d2)
                    d3 = cursor.fetchall()
                    if d3:
                        for d4 in d3:
                            cursor.execute("update aladdin_order.t_snapshot_package_info set del_flag = 1 where id = %s", d4)
                            db.commit()
                    cursor.execute("update aladdin_order.t_snapshot_cargo_info set del_flag = 1 where id = %s", d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_snapshot_cargo_info_curtained where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("update aladdin_order.t_snapshot_cargo_info_curtained set del_flag = 1 where order_num = %s", d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_snapshot_order_customer_info where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("update aladdin_order.t_snapshot_order_customer_info set del_flag = 1 where order_num = %s",d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_snapshot_room_detail_info where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("update aladdin_order.t_snapshot_room_detail_info set del_flag = 1 where order_num = %s",d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_snapshot_room_pictures where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("update aladdin_order.t_snapshot_room_pictures set del_flag = 1 where order_num = %s",d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_snapshot_room_product_detail where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("update aladdin_order.t_snapshot_room_product_detail set del_flag = 1 where order_num = %s",d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_snapshot_solution_detail where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("update aladdin_order.t_snapshot_solution_detail set del_flag = 1 where order_num = %s",d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_customer_building_account where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute(
                        "update aladdin_order.t_customer_building_account set del_flag = 1 where order_num = %s", d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_customer_contact where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute(
                        "update aladdin_order.t_customer_contact set del_flag = 1 where order_num = %s", d2)
                    db.commit()

            cursor.execute("select id from aladdin_order.t_customer_transaction_bill where order_num = %s", num)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("update aladdin_order.t_customer_transaction_bill set del_flag = 1 where order_num = %s",d2)
                    db.commit()

def delAladdinCustomer(mobile):

    if mobile:
        for tel in mobile:
            cursor.execute("select DISTINCT user_id from aladdin_order.t_customer_base_info where mobile = %s", tel)
            d1 = cursor.fetchall()
            if d1:
                for d2 in d1:
                    cursor.execute("select id from aladdin_order.t_customer_house_info where user_id = %s", d2)
                    d3 = cursor.fetchall()
                    if d3:
                        for d4 in d3:
                            cursor.execute("update aladdin_order.t_customer_house_info set del_flag = 1 where id = %s", d4)
                            db.commit()

                    cursor.execute("select id from aladdin_order.t_customer_house_info_ext where user_id = %s", d2)
                    d3 = cursor.fetchall()
                    if d3:
                        for d4 in d3:
                            cursor.execute("update aladdin_order.t_customer_house_info_ext set id = %s", d4)
                            db.commit()
                    cursor.execute("update aladdin_order.t_customer_base_info set del_flag = 1 where user_id = %s", d2)

#aladdin_order.t_customer_transaction_bill
def printOrder(inputList):

    for i in inputList:
        cursor.execute("select order_id from oms.t_order where order_num = %s", i.split())
        result = cursor.fetchall()
        if result:
            print "开始删除订单ID:",i,"相关的进销存及订单数据......"
            printOrdInv(result)
            printCusOrd(result)
        else:
            cursor.execute("select order_id from oms.t_order where customer_tel = %s", i.split())
            result2 = cursor.fetchall()
            if result2:
                print "开始删除手机号:",i,"相关的进销存及订单数据......"
                printOrdInv(result2)
                printCusOrd(result2)
            else:
                cursor.execute("select idt_order from oms.t_purchase_loft_order where order_num = %s", i.split())
                result3 = cursor.fetchall()
                if result3:
                    print "开始删除样本间订单:",i,"相关的进销存及订单数据......"
                    printOrdInv(result3)
                    printModelOrd(result3)
                else:
                   print "未找到与",i,"相关要删除订单及进销存信息"

def delOrder2num(inputList):

    for i in inputList:
        cursor.execute("select order_id from oms.t_order where order_num = %s", i.split())
        result = cursor.fetchall()
        if result:
            print "开始删除订单ID:",i,"相关的进销存及订单数据......"
            delOrdInv(result)
            delCusOrd(result)
        else:
            cursor.execute("select idt_order from oms.t_purchase_loft_order where order_num = %s", i.split())
            result2 = cursor.fetchall()
            if result2:
                print "开始删除样本间订单:",i,"相关的进销存及订单数据......"
                delOrdInv(result2)
                delModelOrd(result2)
            else:
                cursor.execute("select id from aladdin_order.t_aladdin_master_order where id = %s",i.split())
                result3 = cursor.fetchall()
                if result3:
                    print "开始删除大订单订单信息。。。。。。"
                    delAladdinOrder(result3)
                else:
                    print "未找到与",i,"相关要删除订单及进销存信息"

def delorder2mobile(inputList):
    for i in inputList:
        cursor.execute("select order_id from oms.t_order where customer_tel = %s", i.split())
        result = cursor.fetchall()
        if result:
            print "开始删除手机号:",i,"相关的进销存及订单数据......"
            delOrdInv(result)
            delCusOrd(result)
        else:
            cursor.execute("select distinct mobile from aladdin_order.t_customer_base_info where mobile = %s",i.split())
            result4 = cursor.fetchall()
            if result4:
                print "开始删除大订单客户信息。。。。。。"
                delAladdinCustomer(result4)
            else:
                print "未找到与",i,"相关要删除订单及进销存信息"

def judeg(operateType):

    #print type(operateType)
    if operateType == str(1):
        printOrder(inputList)

    elif operateType == str(2):
        delOrder2num(inputList)

    elif operateType == str(3):
        delorder2mobile(inputList)

    else:
        print '''您输入的参数有误，请重新输入！，参数格数: operateType [ordernum／mobile，]
                operateType  1 查询输入要删除的订单数据   2 根据订单号orderNum执行删除 3 根据手机号执行删除'''



if __name__ == '__main__':
    #offline 22
    host = '192.168.1.32'
    PORT = '3306'
    user = 'root'
    passwd = 'aijia1234567'
    #database = 'oms'

    #筛选查询订单表t_order中的测试数据
    #sql = "SELECT order_id FROM oms.t_order where customer_tel like '18888888%' and order_type in (9,10);"
    # 打开数据库连接
    db = MySQLdb.connect(host, user, passwd)
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    if len(sys.argv) < 4:
        print '''您输入的参数有误，请重新输入！，参数格数: operateType [ordernum／mobile，]
                operateType  1 查询输入要删除的订单数据   2 根据订单号orderNum执行删除 3 根据手机号执行删除'''
    else:
        operateType = sys.argv[1]
        inputList = sys.argv[2:]

        judeg(operateType)

    db.commit()
