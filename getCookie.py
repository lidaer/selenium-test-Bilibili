from selenium import webdriver

options = webdriver.ChromeOptions()

options.binary_location = "E:\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)

driver.get('https://www.bilibili.com/')

'''
打开网页后直接登录
手动登录完成后在命令行内按回车，因为我用input阻塞了
等提示进程已结束，退出代码，可以看到同级目录下多出一个名为 jsoncookie.json的文件。里面存的是cookie
'''

driver.implicitly_wait(10)

input()
dictcookie = driver.get_cookies()
print('dictcookie:', dictcookie)
import json

jsoncookie = json.dumps(dictcookie)
print('jsoncookie:', jsoncookie)
with open('jsoncookie.json', 'w') as f:
    f.write(jsoncookie)
driver.close()