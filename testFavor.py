import json
import time

from selenium import webdriver

options = webdriver.ChromeOptions()

options.binary_location = "E:\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)

driver.get('https://www.bilibili.com/')
# 删除本次打开网页时的所有cookie
driver.delete_all_cookies()
with open('jsoncookie.json', 'r') as f:
    ListCookies = json.loads(f.read())
# 将jsoncookie.json里的cookie写入本次打开的浏览器中。
for cookie in ListCookies:
    driver.add_cookie({
        'domain': '.bilibili.com',
        'name': cookie['name'],
        'value': cookie['value'],
        'path': '/',
        'expires': None,
        'httponly': False,
    })
driver.get('https://www.bilibili.com/')

# 开始计时
start=time.time()

# 生成当前页面快照并保存
driver.save_screenshot("./png/favor/1.png")

# 点击首页第一个视频
driver.find_element_by_xpath('//*[@id="i_cecream"]/main/section[1]/div[1]/div[2]/div[2]/a').click()

driver.switch_to.window(driver.window_handles[-1])  # 跳转到不同页面下的新页面.

time.sleep(1.1)  # 延长时间确保能捕捉到.

# 生成当前页面快照并保存
driver.save_screenshot("./png/favor/2.png")

# 点赞
driver.find_element_by_xpath('//*[@id="arc_toolbar_report"]/div[1]/span[1]').click()

time.sleep(0.1)

# 生成当前页面快照并保存
driver.save_screenshot("./png/favor/3.png")

end=time.time()

# 打印出测试花费的时间
print(end-start)