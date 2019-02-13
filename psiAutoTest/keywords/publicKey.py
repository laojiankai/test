#coding:utf-8
#!usr/bin/python

import logging
from drivers import *

#货物当前日期
def getNowdate():
    nowTime = time.localtime(time.time())
    nowDate = time.strftime('%Y%m%d%H%M',nowTime)
    print nowDate
    logging.info(nowDate)
    return nowDate

def sleep(s):
    return time.sleep(s)

#生成采购订单名称
def createPurOrdName():
    str = u"软装代客下单采购"
    purOrdName = str + getNowdate()
    return purOrdName

#根据xpath判断标签是否存在
def isElementExist(xpath):
    try:
        browser.find_element_by_xpath(xpath)
        return True
    except:
        return False

#生成m,n之间的随机整数
def randomNO(m,n):
    #print random.randint(1, 100)
    return random.randint(m, n)