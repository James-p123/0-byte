import requests
import json
from lxml import etree

url = 'https://exam.mshengedu.com/exam/test/user/union/result/report HTTP/1.1'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    "authorization":"135247a24b6549baaf25b1999692f004",
    "Referer":"https://exam.mshengedu.com/examPC/",
    "Cookie":"acw_tc=2f6a1fce16524622127393516eb19e3f100099d283171a2069712a97eb4a13"

    ''' "Host": "exam.mshengedu.com",
    "Connection": "keep-alive",
    "Content-Length":"16",
    "sec-ch-ua":"Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101",
    "version": "v2.8.7",
    "sec-ch-ua-mobile": "?0", 
    
    "Content-Type":"application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    
    "sec-ch-ua-platform": "Windows",
    "Origin": "https://exam.mshengedu.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
     '''
}

data = {
    "id":"4184942"   
}

res = requests.post(url, headers=headers, data=data)

html = etree.HTML(res.content)


pat = html.xpath('//data/sublist/div/span[@class="question-type-name"]/text()')


print (html)

