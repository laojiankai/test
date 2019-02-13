#coding:utf-8
#!usr/bin/python

import createCustomerOrder
from drivers.chrome import *
from drivers.variables import globalVariables
from keywords.publicKey import *
import re
import sys
import types
import logging

reload(sys)
sys.setdefaultencoding('utf-8')

browser= chromeBrowser

def getPurchasePlanMessage(orderNum):

    #采购计划
    browser.get("http://boss.sit.ihomefnt.org/index.html#/goods-purchase")
    sleep(5)

    #客户订单号查询
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/button[2]").click()
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[3]/input").send_keys(orderNum)
    browser.find_element_by_xpath(".//*[@id='searchBtn']").click()
    sleep(3)
    #软装公司信息
    xpath = ".//*[@id='supplier']/ul/li"
    if isElementExist(xpath):
        globalVariables.pur_softCompany = browser.find_element_by_xpath(".//*[@id='supplier']/ul/li").text
        print globalVariables.pur_softCompany
        logging.info(globalVariables.pur_softCompany)
        #货物总数
        globalVariables.pur_total = browser.find_element_by_xpath(".//*[@id='tabs']/li[1]/a").text
        print globalVariables.pur_total
        logging.info(globalVariables.pur_total)
        #客户订单信息
        globalVariables.pur_orderMessage = browser.find_element_by_xpath(".//*[@id='productTable']/div[2]/div/div[1]/div[2]/span[1]/a").text
        print globalVariables.pur_orderMessage
        logging.info(globalVariables.pur_orderMessage)
        #下单人
        globalVariables.pur_salePerson = browser.find_element_by_xpath(".//*[@id='productTable']/div[2]/div/div[1]/div[2]/span[2]").text
        print globalVariables.pur_salePerson
        logging.info(globalVariables.pur_salePerson)
        #客户姓名
        globalVariables.pur_orderOwn = browser.find_element_by_xpath(".//*[@id='productTable']/div[2]/div/div[1]/div[2]/span[3]").text
        print globalVariables.pur_orderOwn
        logging.info(globalVariables.pur_orderOwn)
        #预期收获时间
        globalVariables.pur_expectedArrivalTime = browser.find_element_by_xpath(".//*[@id='productTable']/div[2]/div/div[1]/div[2]/span[4]").text
        print globalVariables.pur_expectedArrivalTime
        logging.info(globalVariables.pur_expectedArrivalTime)
    else:
        print "待采购货物信息不存在，请检查订单是否同步了货物信息到待采购!"
        logging.info("待采购货物信息不存在，请检查订单是否同步了货物信息到待采购!")

def checkPurchaseOrdMassage(orderNum,expectedSoftCompany,expectedGoodTotal):

    #先获取采购计划的订单、货物相关信息
    getPurchasePlanMessage(orderNum)

    pur_orderNum = getOrderNum(globalVariables.pur_orderMessage)
    if pur_orderNum == globalVariables.ord_orderNum:
        print "pur_orderNum == ord_orderNum"
        logging.info("pur_orderNum == ord_orderNum")
    else:
        print "pur_orderNum:" + pur_orderNum + "!== ord_orderNum:" + globalVariables.ord_orderNum
        logging.info("pur_orderNum:" + pur_orderNum + "!== ord_orderNum:" + globalVariables.ord_orderNum)

    salePerson = getSalePerson(globalVariables.pur_salePerson)
    if salePerson == globalVariables.ord_orderSalePerson:
        print "salePerson == ord_orderSalePerson"
        logging.info("salePerson == ord_orderSalePerson")
    else:
        print "salePerson:" + salePerson + "!== ord_orderSalePerson:" + globalVariables.ord_orderSalePerson
        logging.info("salePerson:" + salePerson + "!== ord_orderSalePerson:" + globalVariables.ord_orderSalePerson)

    orderOwn = getOrderOwn(globalVariables.pur_orderOwn)
    if orderOwn == globalVariables.ord_orderOwn:
        print "orderOwn == ord_orderOwn"
        logging.info("orderOwn == ord_orderOwn")
    else:
        print "orderOwn:" + orderOwn + "!== ord_orderOwn:" + globalVariables.ord_orderOwn
        logging.info("orderOwn:" + orderOwn + "!== ord_orderOwn:" + globalVariables.ord_orderOwn)
    #expectedArrivalTime = getExpectedArrivalTime(globalVariables.pur_expectedArrivalTime)
    #print globalVariables.ord_expectedArrivalTime
    #print type(globalVariables.ord_expectedArrivalTime)
    #ord_expectedArrivalTime = createCustomerOrder.getOrdExpectedArrivalTime(globalVariables.ord_expectedArrivalTime)
    #if expectedArrivalTime == ord_expectedArrivalTime:
    #    print u"预期收获时间" + expectedArrivalTime +"success"
    #else:
    #    print u"预期收获时间与时间结果不一致"

    #将softCompany由<type 'unicode'>转化为<type 'str'>
    pur_softCompany = globalVariables.pur_softCompany.encode('utf-8')
    softCompany =  getSoftCpmpany(pur_softCompany)
    softCompany = unicode(softCompany,'utf-8')
    if softCompany == expectedSoftCompany:
        print u"软装公司为:" + softCompany + "success"
        logging.info(u"软装公司为:" + softCompany + "success")
    else:
        print u"软装公司为:" + softCompany + u"与预期结果不一致"
        logging.info(u"软装公司为:" + softCompany + u"与预期结果不一致")

    pur_total = globalVariables.pur_total.encode('utf-8')
    goodtotal =  getGoodTotal(pur_total)
    goodtotal = goodtotal.decode('utf-8')
    print goodtotal
    logging.info(goodtotal)
    if goodtotal == expectedGoodTotal:
        print u"货物数量为:" + goodtotal + " success"
        logging.info(u"货物数量为:" + goodtotal + " success")
    else:
        print u"货物数量为:" + goodtotal + u"与预期结果不一致"
        logging.info(u"货物数量为:" + goodtotal + u"与预期结果不一致")

def getSoftCpmpany(pur_softCompany):

    p = re.compile(r'\(|\)')  # 根据左右括号拆分字符串
    print p.split(pur_softCompany)[0]
    logging.info(p.split(pur_softCompany)[0])
    return p.split(pur_softCompany)[0]

def getGoodTotal(pur_total):

    p = re.compile(r'\（|\）')  # 根据中文左右括号拆分字符串
    return p.split(pur_total)[1]

def getOrderNum(pur_ordermessage):

    p = re.compile(r'\s')
    return p.split(pur_ordermessage)[1]

def getSalePerson(pur_salePerson):

    p = re.compile(r':')
    return p.split(pur_salePerson)[1]

def getOrderOwn(pur_orderOwn):

    p = re.compile(r':')
    return p.split(pur_orderOwn)[1]

def getExpectedArrivalTime(pur_expectedArrivalTime):

    p = re.compile(r':')
    return p.split(pur_expectedArrivalTime)[1]

if __name__ == '__main__':

    #.//*[@id='commitMoney']/div[2]/div/div[2]/div/ng-form/div/div[3]/div[1]/div[1]/select
    #广州酷漫居动漫科技有限公司(2)
    #全部（2）
    #客户订单(客服BOSS代客下单) 1371030869
    #下单人:劳建凯
    #客户姓名:测试031
    #期望收货时间:2017年09月29日

    expectedSoftCompany = u'广州酷漫居动漫科技有限公司'
    expectedGoodTotal = u'2'

    createCustomerOrder.createCustomerOrder()
    print globalVariables.ord_orderNum
    getPurchasePlanMessage(globalVariables.ord_orderNum)
    checkPurchaseOrdMassage(expectedSoftCompany,expectedGoodTotal)


