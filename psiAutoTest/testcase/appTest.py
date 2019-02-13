#coding=UTF-8
'''
Create on 2015-4-16
python 2.7 for mac
@author: tangdongchu
'''
import os
import unittest
from selenium import webdriver
import time
#Appium环境配置
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class DpAppTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android' #设置平台
        desired_caps['platformVersion'] = '4.4' #系统版本
        desired_caps['deviceName'] = '93d1243b' #设备id
        desired_caps['autoLaunch'] = 'true' #是否自动启动
        desired_caps['app'] = PATH(
            'apk/Nova_7.2.0_debug.apk' #安装包路径，放在该py文件的目录下
        )
        desired_caps['appPackage'] = 'com.dianping.v1' #包名
        desired_caps['appActivity'] = 'com.dianping.main.guide.SplashScreenActivity' #启动的activity
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def tearDown(self):
        self.driver.quit() #case执行完退出
    def test_dpApp(self): #需要执行的case
        time.sleep(15)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'上海')]") #通过xpath找到定位框
        el.click() #点击定位框
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DpAppTests)

    unittest.TextTestRunner(verbosity=2).run(suite) #执行case集