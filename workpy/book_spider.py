'''
@AUTHOR:图灵学院-惊蛰
@FILE:book_spider.py
@DATE:2022/4/8
'''

#发起网络访问的工具库
import requests
from lxml import etree  #数据转换

#资源地址  第一个目的地
url = 'http://www.xqb5.org/rank/'

#字典  请求头/伪装头  网景  火狐
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}

#发起访问，获取数据
response = requests.get(url=url,headers=headers)
#print(response.text)

#数据转换  xpath解析数据  RE
data = etree.HTML(response.text)
# #
#拿到所有的小说详情地址  //   @ 定位符  指定条件
book_info_list = data.xpath('//div[@class="item"]')
#print(book_info_list)
# #
for book_info in book_info_list:
    page_id = book_info.xpath('div[@class="image"]/a/@href')[0]
    #print(page_id)
    #将每一部小说的路径拼接到主域名下面
    url = url[0:19] + page_id
    #print(url)
    #获取详情页面
    response = requests.get(url=url,headers=headers)
    info_page = etree.HTML(response.text)
    download_url = info_page.xpath('//div[@class="readbtn"]/a/@href')[2]
    print(download_url)
    #拼接下载的链接
    download_url = url[0:19] + download_url
    print(download_url)
    #拿到小说得名字
    book_name = download_url.split('=')[2]
    #print(book_name)
    #
    #对下载的链接进行访问
    boo_txt = requests.get(url=download_url,headers=headers)
    #文件I/O读写
    with open('book/%s.txt'%book_name,'w',encoding='utf-8') as f:
        f.write(boo_txt.text)
    print('《%s》 下载完成！'%book_name)
