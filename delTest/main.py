#!/usr/bin/python
# -*- coding: UTF-8 -*-

#auto:laojiankai
import paramiko
from delCustomerOrder2 import *
import MySQLdb

def sshclient_execmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command(execmd)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.

    print stdout.read()

    s.close()


def connect():
    hostname = '121.196.205.228'
    port = 2525
    username = 'root'
    password = 'vr*$fz%3#1zl6jd#'
    execmd = "free"
    sshclient_execmd(hostname, port, username, password, execmd)

def conMysql():
    #offline 22
    host = '192.168.1.22'
    PORT = '3306'
    user = 'root'
    passwd = 'aijia1234567'
    #database = 'oms'
    db = MySQLdb.connect(host, user, passwd)
    cursor = db.cursor()
    #getOrderMessage()
    #judeg(getOrderMessage())
    db.commit()

if __name__ == "__main__":
    #connect()
    #judeg(getOrderMessage())
    #db = MySQLdb.connect(host, user, passwd)
    # 使用cursor()方法获取操作游标
    #cursor = db.cursor()
    #getOrderMessage()
    #judeg(getOrderMessage())
    #db.commit()
    conMysql()