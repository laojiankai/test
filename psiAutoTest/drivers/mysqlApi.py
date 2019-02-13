#coding:utf-8
#!usr/bin/python

#import MySQLdb
import random
import time

'''
def mysqlDB():
    # 打开数据库连接
    db = MySQLdb.connect("192.168.1.32","root","aijia1234567","test" )
    #buildingNo= (randomNO(1,50),randomNO(51,100)
    L = [random(1,50),random(51,100)]
    sqlInsert = "insert into test.building(buildingNo,roomNo)VALUES (%s,%s)"
    sqlGet = "select id,buildingNo,roomNo from test.building order by id desc limit 1;"
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute(sqlInsert,L)
    db.commit()
    time.sleep(2)
    cursor.execute(sqlGet)
    # 使用 fetchone() 方法获取一条数据库
    id = cursor.fetchone()

    cursor.close()
    # 关闭数据库连接
    db.close()

    return id[1],id[2]

if __name__ == '__main__':
    mysqlDB()
    print  buildingNO
    #print randomNO(51,100)
'''