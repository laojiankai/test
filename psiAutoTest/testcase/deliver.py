#coding:utf-8
#!usr/bin/python

#创建房产，并新增代客下单订单

import re
from drivers import *
from keywords import *
import logging

browser= chrome.chromeBrowser

#交付中心流程
def deliverFlow(orderNum):

    #openChrome()
    #待交付订单分配交付负责人
    projectDJFUrl = u"http://boss.sit.ihomefnt.org/index.html#/projectDJF"
    browser.get(projectDJFUrl)
    sleep(3)
    #browser.refresh()
    #sleep(5)
    #待交付根据客户订单号查询
    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/form/div[3]/div[3]/button[2]").click()
    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/form/div[1]/div[1]/input").send_keys(orderNum)
    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/form/div[3]/div[3]/button[1]").click()
    sleep(2)
    browser.find_element_by_xpath("//*[@id='sample_1']/tbody/tr/td[1]/input").click()
    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/button").click()
    sleep(2)
    browser.find_element_by_xpath("//*[@id='confirmBtn']").click()
    #待排期分配艾管家
    projectDpqUrl = u"http://boss.sit.ihomefnt.org/#/projectDpq"
    browser.get(projectDpqUrl)
    sleep(3)
    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/form/div[3]/div[5]/button[2]").click()
    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/form/div[1]/div[1]/input").send_keys(orderNum)
    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/form/div[3]/div[5]/button[1]").click()
    sleep(2)
    browser.find_element_by_xpath("//*[@id='tabs']/li[2]/a").click()
    browser.find_element_by_xpath("//*[@id='sample_1']/tbody/tr/td[1]/input").click()
    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/button").click()
    browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div/form/div/div[2]/div/div/a/span[2]/b")





if __name__ == '__main__':

    orderNum = u"10019525"
    deliverFlow(orderNum)