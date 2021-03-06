#!/usr/bin/python
# -*- coding: UTF-8 -*-
#auto:laojiankai
import MySQLdb
#import types

host = '192.168.1.22'
PORT = '3306'
user = 'root'
passwd = 'aijia1234567'
database = 'oms'

# 打开数据库连接
db = MySQLdb.connect(host,user,passwd)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
#筛选查询样本间订单表t_purchase_loft_order中的测试数据
#sql2 = "select idt_order from oms.t_purchase_loft_orde where fid_admin = 481"
sql2 = "select idt_order from oms.t_purchase_loft_order where idt_order in (13,19)"
cursor.execute(sql2)
# 使用 fetchall() 方法获取全部数据。
data = cursor.fetchall()

if data:
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

        # 删除关联关系psi.t_uid_ru_op
        cursor.execute("select id from psi.t_uid_ru_op where sale_order_id = %s", d)
        data9 = cursor.fetchall()
        if data9:
            for s in data9:
                cursor.execute("delete from psi.t_uid_ru_op where id = %s", s)
                db.commit()

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

    #删除订单信息
    for d in data:
        #删除订单详情表t_purchase_loft_order_detail中的测试数据
        cursor.execute("select idt_order_detail from oms.t_purchase_loft_order_detail where fid_order = %s", d)
        d2 = cursor.fetchall()
        if d2:
            for s in d2:
                cursor.execute("delete from oms.t_purchase_loft_order_detail where idt_order_detail = %s", s)
                db.commit()

        #删除样本间订单信息
        cursor.execute("delete from oms.t_purchase_loft_order where idt_order = %s",d)
        db.commit()

# 关闭数据库连接
db.close()