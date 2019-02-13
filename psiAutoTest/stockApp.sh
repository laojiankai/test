#!/bin/bash

tomcat_name=$1
#job_name= $1

dateNow=`date +%Y%m%d`

sequence='270'
sequence2=$((sequence+1))
echo $sequence2
stockAppVersion="$dateNow$sequence2"
echo $stockAppVersion

search_filter=""

replace_list='{
    "details": [
        {
            "file_name": "StockModule.js",
            "rename": false,
            "items": [
                {
                    "old_value": "StockApp.version=.*",
                    "new_value": "StockApp.version= '\'$stockAppVersion\''"
                }
            ]
        }
    ]

}'
