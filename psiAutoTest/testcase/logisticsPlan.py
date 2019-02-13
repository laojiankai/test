#coding:utf-8
#!usr/bin/python

from keywords.publicKey import *
from drivers import *
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

browser= chromeBrowser

def getLogisticsPlanMessage(orderNum):

    #物流计划
    browser.get("http://boss.sit.ihomefnt.org/index.html#/logistics-plan")
    sleep(5)
    #清空搜索条件
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/button[2]").click()
    sleep(2)
    #采购订单号搜索
    browser.find_element_by_xpath(".//*[@id='purchaseOrderNum']").send_keys(orderNum)
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[3]/button[1]").click()
    #取客户订单号、采购订单号
    logisticsOrderNum = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/span[1]/span").text
    logsticsPurchaseNum = browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/span[1]").text
    #选择货物信息
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[1]/input").click()
    #创建物流订单
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[2]/a").click()
    #物流订单服务类型 三包
    browser.find_element_by_xpath(".//*[@id='uniform-serviceType']/span").click()
    #提交
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/ng-form/div[3]/div/div/div/div[1]/a[2]").click()
    sleep(5)


#if __name__ == '__main__':




