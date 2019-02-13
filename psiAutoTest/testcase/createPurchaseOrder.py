#coding:utf-8
#!usr/bin/python

from keywords import *
from drivers import *
import sys
import re
import logging

reload(sys)
sys.setdefaultencoding('utf-8')

browser= chromeBrowser

def getCompanyName(mess):
    r = re.compile('\(|\)')
    return r.split(mess)[0]

def createPurchaseOrder(orderNum):

    #采购计划
    browser.get("http://boss.sit.ihomefnt.org/index.html#/goods-purchase")
    sleep(3)

    while True:
        # 客户订单号查询
        browser.refresh()
        sleep(3)
        #采购计划搜索
        purchasePlanSearch(orderNum)
        #判断搜索结果 是否存在货物信息
        xpath = ".//*[@id='supplier']/ul/li[1]"
        if isElementExist(xpath):
            supplierText = browser.find_element_by_xpath(".//*[@id='supplier']/ul/li[1]").text
            print supplierText
            logging.info(supplierText)

            if supplierText:
                browser.find_element_by_xpath(".//*[@id='supplier']/ul/li[1]").click()
                sleep(2)
                #采购计划订单货物全选
                browser.find_element_by_xpath(".//*[@id='productTable']/div[2]/div/div[1]/div[1]/div/span/input").click()
                sleep(2)
                browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/a").click()
                sleep(3)
                purOrdName = createPurOrdName()
                browser.find_element_by_xpath(".//*[@id='generateOrderForm']/div/div[1]/div/input").clear()
                browser.find_element_by_xpath(".//*[@id='generateOrderForm']/div/div[1]/div/input").send_keys(purOrdName)
                #获取创建页面的客户订单号、货物数量、采购订单状态
                pur_orderNum = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[1]/tr[1]/td/strong").text
                goodNum = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[3]/table/tbody[2]/tr/td[6]/strong").text
                purOrderStatus = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/form/div/div/div[1]/span").text
                print pur_orderNum,goodNum,purOrderStatus
                logging.info(pur_orderNum,goodNum,purOrderStatus)
                #创建
                browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/form/div/div/div[2]/div[1]/button[2]").click()
                sleep(10)
            else:
                break
        else:
            print "采购计划列表没有找到客户订单号%s相关的货物信息，或相关货物都已完成采购"%orderNum
            logging.info("采购计划列表没有找到客户订单号%s相关的货物信息，或相关货物都已完成采购"%orderNum)
            break

    while True:
        #采购订单列表 采购订单派发订单
        browser.get("http://boss.sit.ihomefnt.org/index.html#/psi-purchase-orders/:statusId")
        sleep(5)
        browser.refresh()
        sleep(3)
        #重新加载页面
       # browser.switch_to_default_content()
        orderStatus = u"待备货"
        purchaseOrderListSearch(orderNum,orderStatus)

        xpath = ".//*[@id='sample_0']/tbody/tr/td[1]/span[1]"
        if isElementExist(xpath):

            #采购订单号
            globalVariables.purOrdNum = browser.find_element_by_xpath(".//*[@id='sample_0']/tbody/tr/td[1]/span[1]").text
            if globalVariables.purOrdNum:
                print globalVariables.purOrdNum
                logging.info(globalVariables.purOrdNum)

                #采购订单详情
                browser.find_element_by_xpath(".//*[@id='sample_0']/tbody/tr/td[1]/span[1]").click()
                sleep(5)
                print browser.window_handles
                #打开新页签后关闭原来的页签
                closeChrome()
                #browser.refresh()
                sleep(3)
                #切换采购订单详情页
                browser.switch_to_window(browser.window_handles[0])
                #browser.refresh()
                sleep(3)
                #采购单状态
                purchaseOrderStatus = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/form[1]/div[2]/div[1]/span").text
                print purchaseOrderStatus
                logging.info(purchaseOrderStatus)
                # 采购单送货类型
                deliverType = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/form[2]/div[2]/div[1]/span").text
                print deliverType
                logging.info(deliverType)

                if deliverType == u'艾佳派发物流':

                    #合同额
                    contractAmountText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/form[3]/table/tbody[1]/tr[1]/td/span[2]/strong[1]").text
                    contractAmount = getMoneyAmount(contractAmountText.encode('utf-8'))
                    print contractAmount
                    logging.info(contractAmount)
                    #实收金额
                    makeCollectionsAmountText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/form[3]/table/tbody[1]/tr[1]/td/span[2]/strong[2]").text
                    makeCollectionsAmount = getMoneyAmount(makeCollectionsAmountText.encode('utf-8'))
                    print makeCollectionsAmount
                    logging.info(makeCollectionsAmount)

                    #标准商品备货至物流计划
                    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/form[1]/div[3]/button[3]").click()
                    sleep(2)
                    #计划提货时间
                    browser.find_element_by_xpath(".//*[@id='orderTime']/span/button").click()
                    browser.find_element_by_xpath("html/body/div[6]/div[3]/table/thead/tr[1]/th[3]/i").click()
                    browser.find_element_by_xpath("html/body/div[6]/div[3]/table/tbody/tr[3]/td[5]").click()
                    browser.find_element_by_xpath("html/body/div[6]/div[2]/table/tbody/tr/td/span[11]").click()
                    browser.find_element_by_xpath("html/body/div[6]/div[1]/table/tbody/tr/td/span[3]").click()

                    #获取预期收获时间
                    deliveryTime = browser.find_element_by_xpath(".//*[@id='orderTime']/input").text
                    globalVariables.deliveryTime = deliveryTime
                    print globalVariables.deliveryTime
                    logging.info(globalVariables.deliveryTime)
                    #选择货物确认
                    sleep(2)
                    browser.find_element_by_xpath(".//*[@id='confirmSplit']/div[2]/ng-form/div/div[2]/table/tbody/tr[1]/th[1]/div/span/input").click()
                    browser.find_element_by_xpath(".//*[@id='confirmSplit']/div[2]/ng-form/div/div[3]/button[2]").click()
                    sleep(5)
                    #采购订单状态(待排单)
                    purOrderStatus2 = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/form[1]/div[2]/div[1]/span").text
                    print purOrderStatus2
                    logging.info(purOrderStatus2)

                elif deliverType == u'厂家承担送装':

                    contractAmountText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/form[3]/table/tbody[1]/tr[1]/td/span/strong[1]").text
                    #html/body/div[4]/div[2]/div/div/div[2]/div/div/form[3]/table/tbody[1]/tr[1]/td/span/strong[1]
                    contractAmount = getMoneyAmount(contractAmountText.encode('utf-8'))
                    print contractAmount
                    logging.info(contractAmount)
                    # 实收金额
                    makeCollectionsAmountText = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/form[3]/table/tbody[1]/tr[1]/td/span/strong[2]").text
                    makeCollectionsAmount = getMoneyAmount(makeCollectionsAmountText.encode('utf-8'))
                    print makeCollectionsAmount
                    logging.info(makeCollectionsAmount)

                    #厂家送装完成
                    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/div/div/form[1]/div[3]/button[3]").click()
                    sleep(3)
                    browser.find_element_by_xpath(".//*[@id='confirmSplitBySupplier']/div[2]/ng-form/div/div[2]/table/tbody/tr[1]/th[1]/div/span/input").click()
                    browser.find_element_by_xpath(".//*[@id='confirmSplitBySupplier']/div[2]/ng-form/div/div[3]/button[2]").click()
                    sleep(2)
                    browser.refresh()
                    sleep(3)
                    #采购订单状态(已完成)
                    purOrderStatus2 = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div/form[1]/div[2]/div[1]/span").text
                    print purOrderStatus2
                    logging.info(purOrderStatus2)
            else:
                break
        else:
            print "采购订单列表没有找到客户订单号%s相关的采购订单，或相关采购订单都已完成排单"%orderNum
            logging.info("采购订单列表没有找到客户订单号%s相关的采购订单，或相关采购订单都已完成排单"%orderNum)
            break

def getMoneyAmount(moneyAmountStr):
    r = re.compile(r'\¥|\,')
    moneyAmountList = r.split(moneyAmountStr)
    return moneyAmountList[1]+moneyAmountList[2]


if __name__ == '__main__':

    orderNum = u'10016714'
    createPurchaseOrder(orderNum)



