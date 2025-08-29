import requests
import json


headers = {
    "content-type": "application/json;charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
}
my_data = {"userName": "18924211642", "passwd": "jp669338", "type": "pass"}

params = json.dumps(my_data)

res = requests.post('https://study.mshengedu.com/study/sys/login/webPassLogin&redirect_url=https:%2F%2Fstudypc.mshiedu.com/#/home%2F', headers=headers, data=params)

# print(res.cookies)
# print(res.text)

url_1 = "https://exam.mshengedu.com/exam/test/user/answer/details"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=utf-8",
    "authorization": "391e7408335b470faa7c1d1b275432a3",
    "version": "v2.8.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
}

data =  "{\"examUserId\":\"4184942\"}"

res_1 = requests.post(url_1, headers=headers, data=data)
