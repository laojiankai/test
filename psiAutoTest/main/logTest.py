#coding:utf-8
#!usr/bin/python
'''
import sys
# make a copy of original stdout route
stdout_backup = sys.stdout
# define the log file that receives your log info
log_file = open("../log/log.log", "a")
# redirect print output to log file
sys.stdout = log_file

print "Now all print info will be written to log.log"
# any command line that you will execute
log_file.close()
# restore the output to initial pattern
sys.stdout = stdout_backup

print "Now this will be presented on screen"
'''

from keywords.publicKey import *
from drivers import *
import sys
import requests
import json
import types

import logging
import logging.config
reload(sys)
sys.setdefaultencoding('utf-8')

#browser= chromeBrowser



#logging.config.fileConfig('../log/log.conf')
# create logger
#logger = logging.getLogger('simpleExample')

logging.basicConfig(filename='../log/log.log', level=logging.INFO)
def test():
    '''
    param1 = {
        "businessKey": "WL201709300002",
        "logisticsOrderNum": "2438746821",
        "caller": "YAJ",
        "token": "@#@%SDJHADJAGFAHAHJFGHAYJ",
        "uuid": "ADFNSDFIEKBFO",
        "orderStatus": "81",
        "rejectCause": "",
        "completeTime": "2017-11-29 10:00:05",
        "appointedCustomerList": [
            {
                "customerOrderNum": "YBJ20170928000001",
                "customerName": "董婳",
                "appointDoorTime": "2017-11-29 13:00:00",
                "updateTime": "2017-11-29 13:00:00"
            }
        ],
        "signCustomerList": [
            {
                "customerOrderNum": "YBJ20170928000001",
                "customerName": "董婳",
                "signTime": "2017-11-29 15:00:00",
                "signResourceAddress": "江苏南京市栖霞区 土城头路和天和路交汇处"
            }
        ]
    }

    #param2 = json.dumps(param1, sort_keys=True, ensure_ascii=False, indent=4)
    print type(param1)
    print param1.keys()
    print param1["appointedCustomerList"]
    print type(param1["appointedCustomerList"])
    print param1["appointedCustomerList"][0]
    print type(param1["appointedCustomerList"][0])
    print param1["appointedCustomerList"][0].keys()
    print param1["appointedCustomerList"][0]["customerName"] + ('\n')
    print type(param1["appointedCustomerList"][0]["customerName"])

    logging.info(param1["appointedCustomerList"][0].keys())
    '''
    url = "https://boss.sit.ihomefnt.org/psi-web/deliverCentre/purchasePlan/purchasePlanList/481/DC397F496AD3E0272A232152F1A3A82D"
    data = '''{pageNo: 1, pageSize: 30, userType: 1}'''
    response = requests.post(url,data=data)




if __name__ == '__main__':
    test()