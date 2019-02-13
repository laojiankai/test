#coding:utf-8
#!usr/bin/python

from drivers import chrome
#from drivers import  firefox
#from pymouse import PyMouse
import time

global browser

browser = chrome.chromeBrowser
#打开浏览器
def openChrome():

    browser.get("http://boss.sit.ihomefnt.org/index.html#/dashboard.html")
    browser.maximize_window()
    browser.find_element_by_id("username").send_keys("laojiankai")
    browser.find_element_by_id("password").send_keys("123456")
    browser.find_element_by_id("loginBtn").click()
    time.sleep(5)

'''
def openfirefox():
    browser = firefox.firefoxBrowser
    browser.get("http://boss.sit.ihomefnt.org/index.html#/dashboard.html")
    browser.maximize_window()
    browser.find_element_by_id("username").send_keys("laojiankai")
    browser.find_element_by_id("password").send_keys("123456")
    browser.find_element_by_id("loginBtn").click()
'''

'''
def Pymouse():

    m = PyMouse()
    m.position()  # gets mouse current position coordinates
    m.move(100, 100)
    m.click(200, 200)  # the third argument "1" represents the mouse button
    m.press(300, 0)  # mouse button press
    m.release(0, 100)
'''
#关闭当前页签
def closeChrome():
    browser.close()

#关闭浏览器
def quitChrome():
    browser.quit()