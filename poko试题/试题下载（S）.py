# poko 试题下载

#引入selenium库中的 webdriver 模块
from selenium import webdriver
#引入time库
import time

# 创建 chrome 参数对象
opt = webdriver.ChromeOptions()  
# 设置无头浏览器
opt.headless = True  
# 创建 chrome 无界面对象
driver = webdriver.Chrome(options=opt)  

#打开谷歌浏览器
driver = webdriver.Chrome()
#打开智慧树学习平台
driver.get('https://studypc.mshiedu.com/#/phoneLogin/passLogin')
'''
考虑到网页打开的速度取决于每个人的电脑和网速，使用time库sleep()方法，让程序睡眠5秒
'''
time.sleep(5)
#在主页面点击登录按钮，进入登录页面

driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[2]/div/div[1]').click()
#输入账号和密码
driver.find_element_by_xpath('//*[@id="userName"]').send_keys('18924211642')
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys('jp669338')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[2]/div[2]/label/span/input').click()
#点击登录按钮
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[1]/div[2]/div[3]/button').click()

