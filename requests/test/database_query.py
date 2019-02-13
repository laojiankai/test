# -*- coding: utf-8 -*-
import MySQLdb
import types

# 打开数据库连接
db = MySQLdb.connect("192.168.1.32","root","aijia1234567","cms" )
sql = 'select password,sessionid from cms.t_admin where username = "testqa032";'
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute(sql)

# 使用 fetchone() 方法获取一条数据库
data = cursor.fetchone()
for d in data:
    print d

print "password : %s,%s" % data

cursor.close()
# 关闭数据库连接
db.close()