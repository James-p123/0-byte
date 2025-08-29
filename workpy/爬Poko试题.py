# from http import cookies
# from tkinter.messagebox import QUESTION
from bs4 import BeautifulSoup
import requests
# from lxml import html
# import json
import re

# s *session_requests
# s = requests.session()
#创建 session 对象。这个对象会允许我们保存所有的登录会话请求。

# 发送一个 POST 请求给登录的 url,若存在验证码，
# 用 result = session_requests.post(login_url, data = payload, headers = dict(referer=login_url)) 
# 是不行的
# response_captcha = requests_session.get(url=url_login, cookies=cookies)
# response1 = requests.get(url_login) # 未登陆
# response2 = requests_session.get(url_login) # 已登陆，因为之前拿到了Response Cookie！ 
# response3 = requests_session.get(url_results) # 已登陆，因为之前拿到了Response Cookie！

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}

cookies = {'Cookie': 'acw_tc=2f6a1fec16506415357095962ed161af1719658f8d7368ce540ff507d2dd09'}

# url_list = ['https://exam.mshengedu.com/examPC/#/exam/wrongAnalysis?testUserId=4185166&status=3','https://exam.mshengedu.com/examPC/#/exam/examAnalysis?questionType=1&testUserId=4185166&status=','url3',...]
#for url in url_list:
#    res = requests.get(url)
#    if res.status_code !=200
#    continue
# 通常当url较多时，排除掉无法连接的

# url *login_url
url = 'https://exam.mshengedu.com/examPC/#/exam/examAnalysis?token=d533de3dff6d46dcbe716ef62e2e485f&testUserId=4184942&subjectId=1010000000001132&originOrgType=0'

# tree = html.fromstring(result.text)
# authenticity_token = list(set(tree.xpath("//input[@name=‘csrfmiddlewaretoken’]/@value")))[0]
#用 lxml 和 xpath 提取在登录时使用的 csrf 标记。也可以使用正则表达式或者其他的一些方法来提取这些数据。


# r *result
r = requests.get(url, headers = headers, cookies = cookies)

# r.encoding = r.apparent_encoding
#这样就不用担心乱码
list_all = []
     #创建列表

bs = BeautifulSoup(r.text,'html.parser')
    
x = 1
x in range (34)
datas = re.findall( 'div','id =' + str(x))

for data in datas:    
    q = datas.findall('div', class_ = 'question-type-name').find_all('span'.text)
    a = datas.findall('div', class_ = 'option_list').find_all('span'.text)
    e = datas.findall('div', class_ = 'topic_box').find_all('span'.text)
  
            
    print(list_all[q,a,e])