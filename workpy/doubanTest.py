'''
@AUTHOR:图灵学院-惊蛰
@FILE:doubanTest.py
@DATE:2021/7/2
'''

import requests
from lxml import etree
import csv

url = 'https://movie.douban.com/top250?start=0&filter='

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }

response = requests.get(url=url,headers=headers)
#print(response.text)

data = etree.HTML(response.text)

movieItemList = data.xpath('//div[@class="info"]')

#电影信息列表
movieList = []

for moiveItem in movieItemList:
    #字典,保存每部电影的信息
    movieDict = {}

    title = moiveItem.xpath('div[@class="hd"]/a/span[@class="title"]/text()')
    otherTitle = moiveItem.xpath('div[@class="hd"]/a/span[@class="other"]/text()')
    link = moiveItem.xpath('div[@class="hd"]/a/@href')[0]
    star = moiveItem.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
    quote = moiveItem.xpath('div[@class="bd"]/p[@class="quote"]/span/text()')


    movieDict['title'] = ''.join(title+otherTitle)
    movieDict['url'] = link
    movieDict['star'] = star
    movieDict['quote'] = quote
    print(movieDict)
    movieList.append(movieDict)
#
#
#
# with open('doubanMoive.csv','w',encoding='utf-8',newline='') as f:
#     writer = csv.DictWriter(f,fieldnames=['title','star','quote','url'])
#     writer.writeheader()
#     for each in movieList:
#         writer.writerow(each)







