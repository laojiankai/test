# coding=utf-8

from appium import webdriver

desired_caps = {

                'platformName': 'Android',

                'deviceName': 'HWLLD-H2',

                'platformVersion': '8.0.0',

                # apk包名

                'appPackage': 'com.ihomefnt',

                # apk的launcherActivity

                'appActivity': 'com.ihomefnt.ui.activity.SplashActivity'



                }

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
