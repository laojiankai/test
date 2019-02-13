#coding:utf-8
#!usr/bin/python

import logging
import re
from keywords.publicKey import *


browser = chrome.chromeBrowser

def getOrderAmount(orderAmountTextStr):
    p = re.compile(r'\¥|\,')
    amount = p.split(orderAmountTextStr)
    return amount[1]+amount[2]

#aladdin新增房产
def newHouse(projectName,projectType,houseType):

    browser.find_element_by_xpath("html/body/div[4]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/a[2]/button").click()
    sleep(3)
    #browser.current_window_handle
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/ng-form/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a/span[2]/b").click()
    browser.find_element_by_xpath("html/body/div[9]/div/input").send_keys(projectName)
    browser.find_element_by_xpath("html/body/div[9]/ul/li/div").click()
    sleep(1)
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/ng-form/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a/span[2]/b").click()
    browser.find_element_by_xpath("html/body/div[9]/div/input").send_keys(projectType)
    browser.find_element_by_xpath("html/body/div[9]/ul/li/div").click()
    sleep(1)
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/ng-form/div[1]/div[2]/div[3]/div[1]/div[1]/input").send_keys(randomNO(1,100))
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/ng-form/div[1]/div[2]/div[4]/div/div/input").send_keys(randomNO(1,50))
    sleep(2)
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/ng-form/div/div[3]/div/div/div/div/a/span[2]/b").click()
    browser.find_element_by_xpath("html/body/div[9]/div/input").send_keys(houseType)
    browser.find_element_by_xpath("html/body/div[9]/ul/li/div").click()
    sleep(1)
    button = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/ng-form/div[2]/div/div/div/div/button[2]")
    browser.execute_script("arguments[0].click()",button)
    #browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/ng-form/div[2]/div/div/div/div/button[2]").click()

#aladdin订单收定金
def receiveFrontMoney(frontMoney):

    #frontMoney = 1000
    #订单详情页 收取定金按钮
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/button[3]").click()
    sleep(2)
    browser.find_element_by_xpath(".//*[@money-type='2']/div[1]/div[2]/div[1]/div[2]/ng-form/div[1]/div[1]/input").send_keys(frontMoney)
    #收据编号
    browser.find_element_by_xpath(".//*[@money-type='2']/div[1]/div[2]/div[1]/div[2]/ng-form/div[1]/div[2]/input").send_keys(u"SJ1000")
    browser.find_element_by_xpath(".//*[@money-type='2']/div[1]/div[2]/div[1]/div[2]/ng-form/div[2]/div/div/a/span[2]/b").click()
    sleep(1)
    browser.find_element_by_xpath(".//*[@id='select2-drop']/ul/li/div").click()
    browser.find_element_by_xpath(".//*[@money-type='2']/div[1]/div[2]/div[1]/div[2]/ng-form/div[3]/div/textarea").send_keys(u"收定金1000")
    browser.find_element_by_xpath(".//*[@money-type='2']/div[1]/div[2]/div/div[3]/button[2]").click()

#aladdin代客下单
def replaceCustomerCrearteOrder(orderUrl,goodType,skuList1,skuList2):

    #orderUrl = "http://boss.sit.ihomefnt.org/index.html#/all-family-order-detail/" + orderNum
    # orderUrl = "http://boss.sit.ihomefnt.org/index.html#/all-family-order-detail/10238458"
    browser.get(orderUrl)
    sleep(5)
    browser.refresh()
    sleep(5)
    #判断定金状态是否为"已确认收款"
    payTypeXpath = ".//*[@id='payListTable']/tbody/tr[1]/td[9]"
    judgeConfrimPay(payTypeXpath)
    #待客下单
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/a[2]").click()
    sleep(3)
    # browser.refresh()
    # sleep(3)

    if goodType == 1:
        skuId = skuList1
    elif goodType == 2:
        skuId = skuList2

    # 代客下单页sku搜索输入框及加入清单按钮
    inputText = browser.find_element_by_xpath(".//*[@id='signingContract']/div/div/div[2]/ng-form/div[4]/div[2]/div/div/input")
    inputButton = browser.find_element_by_xpath(".//*[@id='signingContract']/div/div/div[2]/ng-form/div[4]/div[2]/div/div/button[1]")

    for sku in skuId:
        inputText.clear()
        inputText.send_keys(sku)
        sleep(1)
        #inputButton.click()
        browser.execute_script("arguments[0].click()",inputButton)
        sleep(3)

    # 获取货物总金额
    orderAmountText = browser.find_element_by_xpath(".//*[@id='signingContract']/div/div/div[2]/ng-form/div[4]/div[2]/table/tfoot/tr/td[4]/strong").text
    orderAmountTextStr = orderAmountText.encode('utf-8')
    orderAmount = getOrderAmount(orderAmountTextStr)
    print orderAmount
    logging.info(orderAmount)
    # 软装金额
    orderAmountInput = browser.find_element_by_xpath(".//*[@id='signingContract']/div/div/div[2]/ng-form/div[3]/div[2]/div/div/div/div[2]/div/input")
    orderAmountInput.clear()
    orderAmountInput.send_keys(orderAmount)
    sleep(2)
    #交房日期
    browser.find_element_by_xpath("//*[@id='orderTime']/span/button").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[11]/div[3]/table/thead/tr[1]/th[3]").click()
    sleep(1)
    browser.find_element_by_xpath("/html/body/div[11]/div[3]/table/thead/tr[1]/th[3]").click()
    browser.find_element_by_xpath("/html/body/div[11]/div[3]/table/tbody/tr[3]/td[5]").click()
    # 保存订单
    button = browser.find_element_by_xpath(".//*[@id='signingContract']/div/div/div[2]/ng-form/div[5]/div/button")
    browser.execute_script("arguments[0].click()", button)
    sleep(10)
    return orderAmount

#订单收合同款
def receiveMoney(receivemonyAmount):
    #收合同款
    #browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/button[2]").click()
    button = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/button[2]")
    browser.execute_script("arguments[0].click()",button)
    sleep(2)
    browser.find_element_by_xpath(".//*[@money-type='3']/div[1]/div[2]/div[1]/div[2]/ng-form/div[1]/div[1]/input").send_keys(receivemonyAmount)
    browser.find_element_by_xpath(".//*[@money-type='3']/div[1]/div[2]/div[1]/div[2]/ng-form/div[1]/div[2]/input").send_keys(u"SHTK10000")
    browser.find_element_by_xpath(".//*[@money-type='3']/div[1]/div[2]/div[1]/div[2]/ng-form/div[2]/div/div/a/span[2]/b").click()
    browser.find_element_by_xpath(".//*[@id='select2-drop']/ul/li/div").click()
    browser.find_element_by_xpath(".//*[@money-type='3']/div[1]/div[2]/div[1]/div[2]/ng-form/div[3]/div/textarea").send_keys(u"收合同款")
    browser.find_element_by_xpath(".//*[@money-type='3']/div[1]/div[2]/div/div[3]/button[2]").click()

#财务确认收款
def financeCheques(orderNum):
    #财务确认收款
    financeChequesUrl="http://boss.sit.ihomefnt.org/index.html#/account-order-collect/5"
    browser.get(financeChequesUrl)
    sleep(5)
    browser.refresh()
    sleep(5)
    #根据订单号搜索
    #清空搜索条件
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[3]/div/button[2]").click()
    #订单号搜索
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[1]/div[3]/input").send_keys(orderNum)
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/form/div[3]/div/button[1]").click()
    sleep(2)

    #确认收款
    xpath = ".//*[@id='sample_collect']/tbody/tr/td[11]/a[2]"
    if isElementExist(xpath):
        browser.find_element_by_xpath(xpath).click()
        sleep(3)
        browser.find_element_by_xpath(".//*[@operator-type='1']/div/div[2]/div/div[2]/ng-form/div[7]/div/textarea").send_keys(u"财务确认收款")
        browser.find_element_by_xpath(".//*[@id='confirmCollect']/div[2]/div/div[3]/button[2]").click()

#判断订单是否确认收款
def judgeConfrimPay(payTypeXpath):
    i = 1
    while True:
        if isElementExist(payTypeXpath):
            payTypeText = browser.find_element_by_xpath(payTypeXpath).text
            if payTypeText == u"已确认收款":
                break
            else:
                browser.refresh()
                sleep(3)
        else:
            browser.refresh()
            sleep(3)
        i=i+1
        if i>3:
            print "订单没有确认定金，代客下单失败!"
            logging.info("订单没有确认定金，代客下单失败!")
            break

#物流计划搜索
def logisticsPlanSearch(PurchaseOrderNum):

    #根据采购订单号搜索
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/button[2]").click()
    #根据采购订单号搜索
    browser.find_element_by_xpath(".//*[@id='purchaseOrderNum']").send_keys(PurchaseOrderNum)
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/button[1]").click()
    sleep(3)

#物流订单列表查询
def logisticsOrderListSearch(orderNum):
    # 清空搜索条件
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div/form/div[4]/button[2]").click()
    # 根据客户订单号搜索
    browser.find_element_by_xpath(".//*[@id='customerOrderNum']").send_keys(orderNum)
    # browser.find_element_by_xpath(".//*[@id='customerOrderNum']").send_keys(u'YBJ20170710000006')
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div/form/div[4]/button[1]").click()
    sleep(3)

#采购计划货物查询
def purchasePlanSearch(orderNum):
    #根据客户订单好查询
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/button[2]").click()      #清空搜索列表
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[3]/input").send_keys(orderNum)
    browser.find_element_by_xpath(".//*[@id='searchBtn']").click()
    sleep(3)

#采购订单列表查询
def purchaseOrderListSearch(orderNum,orderStatus):
    # 全部列表
    #browser.find_element_by_xpath(".//*[@id='tabs']/li[1]/a").click()
    button = browser.find_element_by_xpath(".//*[@id='tabs']/li[1]/a")
    browser.execute_script("arguments[0].click()",button)
    sleep(3)
    # 清空搜索条件
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/div[3]/button[2]").click()
    # 采购单名称搜索
    # browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/input").send_keys(purOrdName)
    # 根据客户订单号和单据状态搜索
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/input").send_keys(orderNum)
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[4]/div/a/span[2]/b").click()
    sleep(1)
    browser.find_element_by_xpath("html/body/div[9]/div/input").send_keys(orderStatus)
    sleep(1)
    browser.find_element_by_xpath("html/body/div[9]/ul/li/div/span").click()
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/div[3]/button[1]").click()
    sleep(2)

#aladdin订单列表查询
def aladdinOrderListSearch(orderNum):
    resetXpath = "/html/body/div[4]/div[2]/div/div/div[2]/div/form/div/div[4]/div/div/div/button[2]"
    searchXpath = "/html/body/div[4]/div[2]/div/div/div[2]/div/form/div/div[4]/div/div/div/button[1]"
    aladdinOrderNumInputXpath = "/html/body/div[4]/div[2]/div/div/div[2]/div/form/div/div[1]/div[1]/div/div/input"
    browser.find_element_by_xpath(resetXpath).click()
    sleep(1)
    browser.find_element_by_xpath(aladdinOrderNumInputXpath).send_keys(orderNum)
    sleep(1)
    browser.find_element_by_xpath(searchXpath).click()


'''
#判断是否还存在未采购的货物信息
i = 1
supplierList =[]
while True:
    supplier = browser.find_element_by_xpath(".//*[@id='supplier']/ul/li[%s]"%i)
    if len(supplier) == 1:
        supplierText = browser.find_element_by_xpath(".//*[@id='supplier']/ul/li[%s]"%i).text
        if supplierText:
            supplierTextStr = supplierText.encode('utf-8')
            supplier = getCompanyName(supplierTextStr)
            #print supplier
            supplierList.append(supplier)
            i=i+1
        else:
            break
        print supplierList
    else:
        break
'''