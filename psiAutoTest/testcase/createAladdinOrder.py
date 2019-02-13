#coding:utf-8
#!usr/bin/python

#创建房产，并新增代客下单订单

import re
from drivers import *
from keywords import *
import logging

browser= chrome.chromeBrowser

def getOrderMess(orderNumTextStr):
    p = re.compile(r'：')
    return p.split(orderNumTextStr)[1]

def getOrderAmount(orderAmountTextStr):
    p = re.compile(r'\¥|\,')
    amount = p.split(orderAmountTextStr)
    return amount[1]+amount[2]


#aladdin代客下单
def createAladdinReplaceOrder(customerId,goodType):

    #openChrome()
    #测试用客户信息 手机号17777771111 客户ID：12448
    print "创建aladdin订单"
    logging.info("创建aladdin订单")
    #客户详情页
    houseUrl = u"https://boss.sit.ihomefnt.org/index.html#/customer-manage-detail/"
    browser.get(houseUrl+customerId)
    sleep(5)
    browser.refresh()
    sleep(5)

    #新增房产  所属项目、项目类型、户型名称
    projectName = u'虞城建业城'
    projectType = u'BBC'
    houseType = u'H'
    newHouse(projectName,projectType,houseType)
    sleep(5)

    #获取订单号
    orderNumText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[1]/div[1]").text
    #print orderNumText
    orderNumTextStr = orderNumText.encode('utf-8')
    orderNum = getOrderMess(orderNumTextStr)
    #print orderNum
    browser.refresh()
    sleep(3)

    #订单详情页地址URL
    orderUrl = "http://boss.sit.ihomefnt.org/index.html#/all-family-order-detail/" + orderNum

    #收取定金
    frontMoney = 1000
    receiveFrontMoney(frontMoney)
    #财务确认收取定金
    financeCheques(orderNum)

    #代客下单
    # 标准商品下单 根据sku添加商品 2677 2696 2699
    skuList1 = [2696,2699,148125,2699,28667]
    #定制商品下单
    skuList2 = [151077,151078]
    orderAmount = replaceCustomerCrearteOrder(orderUrl,goodType,skuList1,skuList2)

    #browser.refresh()
    #sleep(3)
    #收合同款
    receiveMoneyAmount = float(orderAmount)-float(frontMoney)
    receiveMoney(str(receiveMoneyAmount).decode('utf-8'))
    #财务确认收取合同款
    financeCheques(orderNum)

    #获取订单信息
    browser.get(orderUrl)
    #browser.get("http://boss.sit.ihomefnt.org/index.html#/all-family-order-detail/10238477")
    browser.refresh()
    sleep(3)
    '''
    showMoreText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/a").text
    #print showMoreText,type(showMoreText)
    if showMoreText == u'更多':
        #browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/a").click()
        button = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/a")
        browser.execute_script("arguments[0].click()",button)
        sleep(2)
    else:
        print u"没有找到下单人信息"
        logging.info(u"没有找到下单人信息")
    '''
    #订单号
    globalVariables.ord_orderNum = orderNum
    print "客户订单号：" + str(globalVariables.ord_orderNum)
    logging.info("客户订单号：" + str(globalVariables.ord_orderNum))
    #客户姓名
    globalVariables.ord_orderOwn = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/a").text
    print globalVariables.ord_orderOwn
    logging.info(globalVariables.ord_orderOwn)
    #下单人
    orderSalePersonText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[4]/div[1]").text
    orderSalePersonTextStr = orderSalePersonText.encode('utf-8')
    globalVariables.ord_orderSalePerson = getOrderMess(orderSalePersonTextStr)
    print globalVariables.ord_orderSalePerson
    logging.info(globalVariables.ord_orderSalePerson)

    #预期收获时间
    #globalVariables.ord_expectedArrivalTime = browser.find_element_by_xpath(".//*[@id='depositForm']/div/div[6]/div[2]/span").text

    return orderNum

#aladdin方案订单
def createAladdinProjectOrder(customerId):

    # openChrome()
    # 测试用客户信息 手机号17777771111 客户ID：12448
    print "创建aladdin订单"
    logging.info("创建aladdin订单")
    # 客户详情页
    houseUrl = u"http://boss.sit.ihomefnt.org/index.html#/customer-manage-detail/"
    browser.get(houseUrl + customerId)
    sleep(5)
    browser.refresh()
    sleep(5)

    # 新增房产  所属项目、项目类型、户型名称
    projectName = u'虞城建业城'
    projectType = u'BBC'
    houseType = u'H'
    newHouse(projectName, projectType, houseType)
    sleep(5)

    # 获取订单号
    orderNumText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[1]/div[1]").text
    # print orderNumText
    orderNumTextStr = orderNumText.encode('utf-8')
    orderNum = getOrderMess(orderNumTextStr)
    # print orderNum
    browser.refresh()
    sleep(3)

    # 订单详情页地址URL
    orderUrl = "http://boss.sit.ihomefnt.org/index.html#/all-family-order-detail/" + orderNum

    # 收取定金
    frontMoney = 1000
    receiveFrontMoney(frontMoney)
    # 财务确认收取定金
    financeCheques(orderNum)

    # 方案下单
    #没想好怎么完

    # browser.refresh()
    # sleep(3)
    # 收合同款
    receiveMoneyAmount = float(orderAmount) - float(frontMoney)
    receiveMoney(str(receiveMoneyAmount).decode('utf-8'))
    # 财务确认收取合同款
    financeCheques(orderNum)

    # 获取订单信息
    browser.get(orderUrl)
    # browser.get("http://boss.sit.ihomefnt.org/index.html#/all-family-order-detail/10238477")
    browser.refresh()
    sleep(3)
    showMoreText = browser.find_element_by_xpath(
        "html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/a").text
    # print showMoreText,type(showMoreText)
    if showMoreText == u'更多':
        # browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/a").click()
        button = browser.find_element_by_xpath(
            "html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[3]/a")
        browser.execute_script("arguments[0].click()", button)
        sleep(2)
    else:
        print u"没有找到下单人信息"
        logging.info(u"没有找到下单人信息")
    # 订单号
    globalVariables.ord_orderNum = orderNum
    print "客户订单号：" + str(globalVariables.ord_orderNum)
    logging.info("客户订单号：" + str(globalVariables.ord_orderNum))
    # 客户姓名
    globalVariables.ord_orderOwn = browser.find_element_by_xpath(
        "html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/span").text
    print globalVariables.ord_orderOwn
    logging.info(globalVariables.ord_orderOwn)
    # 下单人
    orderSalePersonText = browser.find_element_by_xpath(
        "html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div[2]/div[4]/div").text
    orderSalePersonTextStr = orderSalePersonText.encode('utf-8')
    globalVariables.ord_orderSalePerson = getOrderMess(orderSalePersonTextStr)
    print globalVariables.ord_orderSalePerson
    logging.info(globalVariables.ord_orderSalePerson)

    # 预期收获时间
    # globalVariables.ord_expectedArrivalTime = browser.find_element_by_xpath(".//*[@id='depositForm']/div/div[6]/div[2]/span").text

    return orderNum


if __name__ == '__main__':

    #customerId = u"12448"
    #createAladdinOrder(customerId)
    openChrome()
    closeChrome()
    sleep(3)
    openChrome()
    quitChrome()