#coding:utf-8
#!usr/bin/python

#增减项下单并确认收款

import logging
import re
from drivers import *
from keywords import *

browser= chrome.chromeBrowser

def randomNO(m,n):
    #print random.randint(1, 100)
    return random.randint(m, n)

def getOrderMess(orderNumTextStr):
    p = re.compile(r'：')
    return p.split(orderNumTextStr)[1]

def getOrderAmount(orderAmountTextStr):
    p = re.compile(r'\¥|\,')
    amount = p.split(orderAmountTextStr)
    return amount[1]+amount[2]


def orderIncrementItem(orderNum,goodType):

    #openChrome()
    #测试用客户信息 手机号17777771111 客户ID：12448
    print "创建订单增减项"
    logging.info("创建订单增减项")

    orderUrl = u"http://boss.sit.ihomefnt.org/index.html#/all-family-order-detail/"
    browser.get(orderUrl+orderNum)
    sleep(10)
    #browser.refresh()
    #sleep(2)
    #打开增减项添加页面
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/button[3]").click()
    sleep(2)
    browser.find_element_by_xpath(".//*[@id='increaseOrDecrease']/div[2]/div/div[2]/a[1]").click()
    sleep(3)

    # 增减项下单 标准货物根据sku添加商品 2677 2696 2699
    skuId1 = [2677,2696,2699,148125,2699,28667]
    #增减项下单 定制商品
    skuId2 = [151077,151078]

    if goodType == 1:
        skuId = skuId1
    elif goodType == 2:
        skuId = skuId2

    for sku in skuId:
        inputText = browser.find_element_by_xpath(".//*[@id='orderSupplement']/div/div/div[2]/ng-form/div[4]/div[2]/div[1]/div/input")
        inputButton = browser.find_element_by_xpath(".//*[@id='orderSupplement']/div/div/div[2]/ng-form/div[4]/div[2]/div[1]/div/button[1]")
        inputText.clear()
        inputText.send_keys(sku)
        inputButton.click()
        sleep(3)

    #增减项原因
    browser.find_element_by_xpath(".//*[@id='orderSupplement']/div/div/div[2]/ng-form/div[3]/div[2]/div/div/textarea").send_keys(orderNum)
    #保存
    button = browser.find_element_by_xpath(".//*[@id='orderSupplement']/div/div/div[2]/ng-form/div[5]/div/button")
    browser.execute_script("arguments[0].click()",button)
    sleep(5)

    #收款
    contractAmountText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[4]/div[2]/div[1]/div[1]/div[1]/span").text
    receivedAmountText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[4]/div[2]/div[1]/div[1]/div[2]/span").text
    contractAmountTextStr = contractAmountText.encode('utf-8')
    receivedAmountTextStr = receivedAmountText.encode('utf-8')
    contractAmount = getOrderAmount(contractAmountTextStr)
    receivedAmount = getOrderAmount(receivedAmountTextStr)
    receivableAmountnNum = float(contractAmount)-float(receivedAmount)
    receivableAmount = str(receivableAmountnNum).decode('utf-8')
    print receivableAmount
    logging.info(receivableAmount)

    #收合同款
    receiveMoney(receivableAmount)
    #财务确认收取合同款
    financeCheques(orderNum)


if __name__ == '__main__':

    orderNum = u"10016622"

    orderIncrementItem(orderNum)