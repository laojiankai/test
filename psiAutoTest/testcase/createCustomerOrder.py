#coding:utf-8
#!usr/bin/python

import logging
import time
import types
import re
from drivers import chrome
from drivers.openBrowser import openChrome
from selenium.webdriver.support.select import Select
from drivers.variables import globalVariables
from keywords.publicKey import *

browser= chrome.chromeBrowser

#客户订单已经迁移到大订单，废弃不再使用
def createCustomerOrder():

    openChrome()
    #软装代客下单
    print "创建软装订单代客下单"
    logging.info("创建软装订单代客下单")
    browser.get("http://boss.sit.ihomefnt.org/index.html#/valet-order-detail/")
    sleep(2)
    '''
    browser.switch_to_window(browser.window_handles[0])
    #电商
    browser.find_element_by_xpath("html/body/div[2]/div/div[2]/ul/li[7]/a").click()
    #客户订单
    browser.find_element_by_xpath("html/body/div[4]/div[1]/div/ul/li[3]/a").click()
    time.sleep(2)
    #软装订单
    browser.find_element_by_xpath("html/body/div[4]/div[1]/div/ul/li[3]/ul/li[1]/a").click()
    time.sleep(3)
    #browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div[3]/div/a").click()
    time.sleep(3)
    '''
    browser.find_element_by_xpath(".//*[@id='valetOrderForm']/div/div[2]/div[1]/input").send_keys("18888888031")
    sleep(3)
    #添加商品
    browser.find_element_by_xpath(".//*[@id='addGoodsForm']/div/input").send_keys("144795")
    browser.find_element_by_xpath(".//*[@id='addGoodsForm']/div/span[2]").click()
    browser.find_element_by_xpath(".//*[@id='addGoodsForm']/div/input").clear()
    sleep(2)
    browser.find_element_by_xpath(".//*[@id='addGoodsForm']/div/input").send_keys("5002020")
    browser.find_element_by_xpath(".//*[@id='addGoodsForm']/div/span[2]").click()
    sleep(2)
    browser.find_element_by_xpath(".//*[@id='valetOrderForm']/div/div[7]/div/div/input").send_keys("10000")
    sleep(2)
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div/a[1]").click()
    sleep(5)

    '''
    ##test############
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/input").send_keys("1371030869")
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[2]/input").send_keys("18888888031")
    browser.find_element_by_id("searchBtn").click()
    time.sleep(2)
    browser.find_element_by_xpath(".//*[@id='sample_1_wrapper']/div[2]/table/tbody/tr/td[1]").click()
    time.sleep(3)
    ##test############
    '''
    #收款
    print "收款"
    logging.info("收款")
    browser.find_element_by_xpath(".//*[@id='depositForm']/div/div[1]/div[2]/div[2]/button").click()
    sleep(3)
    #browser.switch_to.alert()
    browser.find_element_by_xpath(".//*[@id='commitMoney']/div[2]/div/div[2]/div/ng-form/div/div[3]/div[1]/div[1]/select").click()
    s = browser.find_element_by_xpath(".//*[@id='commitMoney']/div[2]/div/div[2]/div/ng-form/div/div[3]/div[1]/div[1]/select")
    Select(s).select_by_visible_text("首付款")
    browser.find_element_by_xpath(".//*[@id='commitMoney']/div[2]/div/div[2]/div/ng-form/div/div[3]/div[2]/div[1]/div/input").send_keys("6000")

    browser.find_element_by_xpath(".//*[@id='commitMoney']/div[2]/div/div[2]/div/ng-form/div/div[3]/div[3]/div/select").click()
    s = browser.find_element_by_xpath(".//*[@id='commitMoney']/div[2]/div/div[2]/div/ng-form/div/div[3]/div[3]/div/select")
    Select(s).select_by_visible_text("现金支付")
    sleep(2)
    browser.find_element_by_xpath(".//*[@id='commitMoney']/div[2]/div/div[3]/button[2]").click()

    sleep(3)
    #确认收款
    print "确认收款"
    logging.info("确认收款")
    browser.find_element_by_xpath(".//*[@id='depositForm']/div/div[13]/div/table/tbody/tr[2]/td[7]/div/button[1]").click()
    sleep(2)
    browser.find_element_by_xpath(".//*[@id='confirmMoney']/div[2]/div/div[3]/button[2]").click()
    sleep(2)
    comfirmText = browser.find_element_by_xpath(".//*[@id='depositForm']/div/div[13]/div/table/tbody/tr[2]/td[7]/span").text
    print comfirmText
    print type(comfirmText)
    print "订单创建成功，货物已同步到采购计划"
    logging.info("订单创建成功，货物已同步到采购计划")
    #订单号
    globalVariables.ord_orderNum = browser.find_element_by_xpath(".//*[@id='depositForm']/div/div[2]/div[2]/span").text
    print "客户订单号：" + str(globalVariables.ord_orderNum)
    logging.info("客户订单号：" + str(globalVariables.ord_orderNum))
    #客户姓名
    globalVariables.ord_orderOwn = browser.find_element_by_xpath(".//*[@id='depositForm']/div/div[3]/div[1]/span/a").text
    #下单人
    globalVariables.ord_orderSalePerson = browser.find_element_by_xpath(".//*[@id='depositForm']/div/div[4]/div[2]/span").text
    #预期收获时间
    globalVariables.ord_expectedArrivalTime = browser.find_element_by_xpath(".//*[@id='depositForm']/div/div[6]/div[2]/span").text

def getOrdExpectedArrivalTime(ord_expectedArrivalTime):
    p= re.compile(r'-|\s')
    year = p.split(ord_expectedArrivalTime)[0]
    month = p.split(ord_expectedArrivalTime)[1]
    day = p.split(ord_expectedArrivalTime)[2]
    print year + '年' + month + '月' + day + '日'
    logging.info(year + '年' + month + '月' + day + '日')
    return year + '年' + month + '月' + day + '日'

#if __name__ == '__main__':

    #ord_expectedArrivalTime = '2017-09-29 00:00:00'
    #print getOrdExpectedArrivalTime(ord_expectedArrivalTime)

