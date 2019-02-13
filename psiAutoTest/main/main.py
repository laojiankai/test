#coding:utf-8
#!usr/bin/python
from testcase import *
import sys
import logging

if __name__ == '__main__':

    # logging.config.fileConfig('../log/log.conf')
    # create logger
    # logger = logging.getLogger('simpleExample')

    logging.basicConfig(filename='../log/log.log', level=logging.INFO)

    # make a copy of original stdout route
    #stdout_backup = sys.stdout
    # define the log file that receives your log info
    #log_file = open("../log/log.log", "a")
    # redirect print output to log file
    #sys.stdout = log_file


    customerId = u"6714"
    orderNum = ''

    expectedSoftCompany1 = u'深圳兴利家具有限公司'
    expectedGoodTotal1 = u'16'

    expectedSoftCompany2 = u'河南双友家俱实业有限公司'
    expectedGoodTotal2 = u'4'

    #下单类型 1 标准商品下单 2 定制品下单
    goodTypelist = [1]

    openChrome()
    for goodType in goodTypelist:
        if goodType ==1:
            print "testcase 1"
            logging.info("testcase 1")
            #testCase1 标准商品下单
            #标准商品代客下单
            orderNum = createAladdinReplaceOrder(customerId,goodType)
            #增减项
            #orderIncrementItem(orderNum,goodType)
            #交付
            deliverFlow(orderNum)
            #采购计划货物信息校验
            #checkPurchaseOrdMassage(orderNum,expectedSoftCompany1,expectedGoodTotal1)
            #创建采购订单
            #createPurchaseOrder(orderNum)
            #创建物流订单
            #createLogisticsOrder(orderNum)
            #物流订单供应商状态回调
            #logisticsOrderCallBack()
            #检查物流、采购、客户订单状态是否已完成
            #checkStandardOrderStatus(orderNum)

        elif goodType ==2:
            print "testcase 2"
            logging.info("testcase 2")
            #定制品代客下单
            #orderNum = createAladdinReplaceOrder(customerId,goodType)
            #orderIncrementItem(orderNum,goodType)
            #采购计划货物信息校验
            #checkPurchaseOrdMassage(orderNum,expectedSoftCompany2,expectedGoodTotal2)
            #创建采购订单及厂家送装完成
            #createPurchaseOrder(orderNum)
            #检查采购、客户订单状态是否已完成
            #checkCustomMadeOrderStatus(orderNum)

        else:
            print "用例执行结束"
            logging.info("用例执行结束")
            break

    quitChrome()

    # any command line that you will execute
    #log_file.close()
    # restore the output to initial pattern
    #sys.stdout = stdout_backup