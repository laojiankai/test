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

def wankeyun():

    openChrome()
    #软装代客下单
    browser.get("https://item.jd.com/4993751.html")
    sleep(2)
    browser.refresh()


if __name__ == '__main__':

    wankeyun()

