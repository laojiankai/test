#coding:utf-8
#!usr/bin/python

import time

from drivers import chrome
from drivers.openBrowser import openChrome, closeChrome
from keywords.publicKey import *

#global browser
browser= chrome.chromeBrowser

def addModelOrder():

    openChrome()
    browser.switch_to_window(browser.window_handles[0])
    browser.find_element_by_xpath("html/body/div[2]/div/div[2]/ul/li[7]/a").click()
    browser.find_element_by_xpath("html/body/div[4]/div[1]/div/ul/li[4]/a").click()
    time.sleep(3)
    browser.find_element_by_xpath("html/body/div[4]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div[1]/div[3]/a").click()
    time.sleep(2)
    browser.find_element_by_xpath(".//*[@id='loftNewInput']/div[1]/div/input").send_keys(u"样本间布景申请" + getNowdate())
    time.sleep(2)
    browser.find_element_by_xpath(".//*[@id='loftNewInput']/div[2]/div/div/a/span[2]/b").click()
    browser.find_element_by_xpath(".//*[@id='select2-drop']/div/input").send_keys(u"中南世纪雅苑")
    browser.find_element_by_xpath(".//*[@id='select2-drop']/ul/li/div").click()
    time.sleep(2)
    browser.find_element_by_xpath(".//*[@id='loftNewInput']/div[3]/div/div/a/span").click()
    browser.find_element_by_xpath(".//*[@id='select2-drop']/div/input").send_keys(u"中南世纪雅苑C2户型")
    browser.find_element_by_xpath(".//*[@id='select2-drop']/ul/li/div").click()
    time.sleep(2)
    browser.find_element_by_xpath(".//*[@id='orderTime']/span/button").click()
    browser.find_element_by_xpath("html/body/div[6]/div[3]/table/tfoot/tr/th").click()

    browser.find_element_by_xpath(".//*[@id='reviewVoucher']/span/input[2]").send_keys("/Users/laojiankai/Documents/bug/WechatIMG1.jpeg")


    closeChrome()

if __name__ == '__main__':
    addModelOrder()



