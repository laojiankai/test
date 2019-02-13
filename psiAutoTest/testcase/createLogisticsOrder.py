#coding:utf-8
#!usr/bin/python

import logging
import re
import sys
from keywords import *
from drivers import *
from testcase.logisticsCallBack import logisticsOrderCallBack

reload(sys)
sys.setdefaultencoding('utf-8')

browser= chromeBrowser

def getTakeDeliveryTime(takeDeliveryTimeTextStr):
    p = re.compile(r'：')
    return p.split(takeDeliveryTimeTextStr)[1]

def getOrderOwn(orderOwnMess):
    p = re.compile(r'：')
    return p.split(orderOwnMess)[0]

def getCompanyName(compantNameMess):
    p = re.compile(r'：|\¥')
    return p.split(compantNameMess)[0]
#def searchForPurchase():
    

def createLogisticsOrder(orderNum):

    #globalVariables.purOrdNum = purOrdNum
    globalVariables.pur_orderNum = orderNum

    #物流计划创建物流订单
    logisticsPlanUrl = "http://boss.sit.ihomefnt.org/index.html#/logistics-plan"
    browser.get(logisticsPlanUrl)
    sleep(5)
    browser.refresh()
    sleep(5)
    #根据采购订单号查询物流计划列表
    logisticsPlanSearch(globalVariables.purOrdNum)
    #选择货物信息_选择对应采购订单下的所有货物
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/input").click()

    #创建物流订单
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/a").click()
    sleep(10)
    #物流订单服务类型 三包
    browser.find_element_by_xpath(".//*[@id='uniform-serviceType']/span").click()
    #提交
    button = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/ng-form/div[3]/div/div/div/div[1]/a[2]")
    browser.execute_script("arguments[0].click()",button)
    sleep(5)

    #物流订单列表
    logisticsOrderListUrl = "http://boss.sit.ihomefnt.org/index.html#/logistics-order-list"
    browser.get(logisticsOrderListUrl)
    sleep(20)
    logisticsOrderListSearch(orderNum)
    #物流订单号
    logsticsOrderNum = browser.find_element_by_xpath(".//*[@id='sample_1']/tbody/tr/td[1]/div/div[1]/strong").text
    globalVariables.logsticsOrderNum = logsticsOrderNum
    print globalVariables.logsticsOrderNum
    logging.info(globalVariables.logsticsOrderNum)
    #进入物流订单详情
    browser.find_element_by_xpath(".//*[@id='sample_1']/tbody/tr/td[1]/div/div[1]/strong").click()
    sleep(10)
    #print browser.window_handles
    #打开新页签之后关闭之前的页签
    closeChrome()
    sleep(2)
    #切换到当前页签
    browser.switch_to_window(browser.window_handles[0])
    #物流订单详情货物信息
    #客户订单号
    #browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/strong/div[5]/div/div[2]/table/tbody/tr[1]/td/span[1]/strong").text
    #客户姓名
    orderOwnMess = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/strong/div[5]/div/div[2]/table/tbody/tr[1]/td/span[2]").text
    orderOwnMessStr = orderOwnMess.encode('utf-8')
    globalVariables.pur_orderOwn = getOrderOwn(orderOwnMessStr)
    print globalVariables.pur_orderOwn
    logging.info(globalVariables.pur_orderOwn)

    #收获时间
    takeDeliveryTimeText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/strong/div[5]/div/div[2]/table/tbody/tr[1]/td/span[4]").text
    #收获地址
    signResourceAddressText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/strong/div[5]/div/div[2]/table/tbody/tr[1]/td/span[3]").text
    takeDeliveryTimeTextStr = takeDeliveryTimeText.encode('utf-8')
    takeDeliveryTime = getTakeDeliveryTime(takeDeliveryTimeTextStr)
    globalVariables.completeTime = takeDeliveryTime + u" " + u"10:00:05"
    globalVariables.appointDoorTime = takeDeliveryTime + u" "+ u"13:00:00"
    globalVariables.updateTime = globalVariables.appointDoorTime
    globalVariables.signTime = takeDeliveryTime + u" " + u"15:00:00"
    globalVariables.signResourceAddress = signResourceAddressText
    print globalVariables.completeTime,globalVariables.appointDoorTime,globalVariables.updateTime,globalVariables.signTime,globalVariables.signResourceAddress
    logging.info(globalVariables.completeTime,globalVariables.appointDoorTime,globalVariables.updateTime,globalVariables.signTime,globalVariables.signResourceAddress)
    #派发订单
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/button[3]").click()
    sleep(10)

    #选择物流供应商，存在多家可配送供应商时默认选择第一条
    xpath = ".//*[@id='logisticsCompanyForm']/div[2]/div/span"
    if isElementExist(xpath):
        logisticsCompanyText = browser.find_element_by_xpath(".//*[@id='logisticsCompanyForm']/div[2]/div/span").text
        logisticsCompanyTextStr = logisticsCompanyText.encode('utf-8')
        companyName = getCompanyName(logisticsCompanyTextStr)
        globalVariables.companyName = companyName
        #print type(companyName)
    else:
        print "没有找到可派单的物流供应商"
        logging.info("没有找到可派单的物流供应商")

    browser.find_element_by_xpath(".//*[@id='s2id_autogen3']/a/span[2]/b").click()
    browser.find_element_by_xpath(".//*[@id='s2id_autogen4_search']").send_keys(companyName.decode('utf-8'))
    sleep(2)
    browser.find_element_by_xpath(".//*[@id='select2-drop']/ul/li/div").click()
    browser.find_element_by_xpath(".//*[@id='confirmDistributeBtn']").click()
    sleep(3)
    browser.refresh()
    sleep(3)



if __name__ == '__main__':

    orderNum = u'10016697'
    purOrdNum = u'CG1506569905249481'
    createLogisticsOrder(orderNum)
    logisticsOrderCallBack()
