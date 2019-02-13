#coding:utf-8
#!usr/bin/python

from keywords import *
from drivers import *
import sys
import logging

reload(sys)
sys.setdefaultencoding('utf-8')

browser= chromeBrowser

def __checkWlOrderStatus__(orderNum):

    #校验物流订单状态
    logisticsOrderListUrl = "http://boss.sit.ihomefnt.org/index.html#/logistics-order-list"
    browser.get(logisticsOrderListUrl)
    sleep(5)
    logisticsOrderListSearch(orderNum)

    i = 1
    while True:
        trXpath = ".//*[@id='sample_1']/tbody/tr[%s]" %i
        if isElementExist(trXpath):
            statusTdXpath = ".//*[@id='sample_1']/tbody/tr[%s]/td[8]" %i
            wlOrderTdXpath = ".//*[@id='sample_1']/tbody/tr[%s]/td[1]/div/div[1]/strong" %i
            logisticsOrderStatus = browser.find_element_by_xpath(statusTdXpath).text
            wlOrderNum = browser.find_element_by_xpath(wlOrderTdXpath).text
            if logisticsOrderStatus == u"已签收":
                print "物流订单%s状态正确" %wlOrderNum
                logging.info("物流订单%s状态正确" %wlOrderNum)
            else:
                print "###物流订单%s状态为%s,与完结状态不一致" %wlOrderNum %logisticsOrderStatus
                logging.info("###物流订单%s状态为%s,与完结状态不一致" %wlOrderNum %logisticsOrderStatus)
            sleep(3)
            i = i + 1
        else:
            break

def __checkPurchaseOrderStatus__(orderNum):
    #校验采购订单状态
    purchaseOrderListUrl = "http://boss.sit.ihomefnt.org/index.html#/psi-purchase-orders/:statusId"
    browser.get(purchaseOrderListUrl)
    sleep(5)
    purchaseOrderListSearch(orderNum,orderStatus=u"请选择")
    #检查列表订单状态
    i = 1
    while True:
        trXpath = "//*[@id='sample_0']/tbody/tr[%s]" %i
        if isElementExist(trXpath):
            statusTdXpath = "//*[@id='sample_0']/tbody/tr[%s]/td[8]" %i
            purchaseOrderNumTdXpath = ".//*[@id='sample_0']/tbody/tr[%s]/td[1]/span[1]" %i
            purchaseOrderStatus = browser.find_element_by_xpath(statusTdXpath).text
            purchaseOrderNum = browser.find_element_by_xpath(purchaseOrderNumTdXpath).text
            if purchaseOrderStatus == u"已完成":
                print "采购订单%s状态正确" %purchaseOrderNum
                logging.info("采购订单%s状态正确" %purchaseOrderNum)
            else:
                print "###采购订单%s状态为%s,与完结状态不一致" %purchaseOrderNum %purchaseOrderStatus
                logging.info("###采购订单%s状态为%s,与完结状态不一致" %purchaseOrderNum %purchaseOrderStatus)
            sleep(3)
            i = i + 1
        else:
            break

def __checkAladdinOrderStatus__(orderNum):
    #校验客户订单状态
    aladdinOrderListUrl = "http://boss.sit.ihomefnt.org/index.html#/all-family-order-list"
    browser.get(aladdinOrderListUrl)
    sleep(5)
    aladdinOrderListSearch(orderNum)
    while True:
        trXpath = ".//*[ @ id ='sample_1']/tbody/tr"
        if isElementExist(trXpath):
            statusTdXpath = ".//*[ @ id ='sample_1']/tbody/tr/td[7]"
            aladdinOrderStatus = browser.find_element_by_xpath(statusTdXpath).text

            if aladdinOrderStatus == u"已完成":
                print "客户订单%s状态正确" %orderNum
                logging.info("客户订单%s状态正确" %orderNum)
            else:
                print "###客户订单%s状态为%s，与完结状态不一致" %orderNum %aladdinOrderStatus
                logging.info("###客户订单%s状态为%s，与完结状态不一致" %orderNum %aladdinOrderStatus)
            sleep(3)
        else:
            break
#订单
def checkCustomMadeOrderStatus(orderNum):
    __checkPurchaseOrderStatus__(orderNum)
    __checkAladdinOrderStatus__(orderNum)

def checkStandardOrderStatus(orderNum):
    __checkWlOrderStatus__(orderNum)
    __checkPurchaseOrderStatus__(orderNum)
    __checkAladdinOrderStatus__(orderNum)


#if __name__ == '__main__':




