#coding:utf-8
#!usr/bin/python

#创建房产，并新增代客下单订单


from keywords import *


browser= chrome.chromeBrowser

#交付中心流程
def getLoginCookies():

    #openChrome()
    bossUrl = u"https://boss.sit.ihomefnt.org/login.html"
    browser.get(bossUrl)
    sleep(3)
    browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/form/div[1]/div/div/input").send_keys("laojiankai")
    browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/form/div[2]/div/div/input").send_keys("123456")
    browser.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/form/div[3]/div/button/span").click()
    sleep(3)
    cookies = browser.get_cookies()
    print cookies

if __name__ == '__main__':
    getLoginCookies()

    #//*[@id="username"]
    #//*[@id="password"]
    #//*[@id="loginBtn"]