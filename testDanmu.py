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

# 生成当前页面快照并保存
driver.save_screenshot("./png/danmu/1.png")

# 点击首页第一个视频
driver.find_element_by_xpath('//*[@id="i_cecream"]/main/section[1]/div[1]/div[2]/div[2]/a').click()

driver.switch_to.window(driver.window_handles[-1])  # 跳转到不同页面下的新页面.

time.sleep(2)  # 延长时间确保能捕捉到.

# 生成当前页面快照并保存
driver.save_screenshot("./png/danmu/2.png")



# 开始计时
start=time.time()

# 评论
# 输入对应的搜索内容.
for i in range(10):
    # 抓取弹幕区域
    search_content = driver.find_element_by_xpath('//*[@id="bilibili-player"]/div/div/div[1]/div[2]/div/div[2]/div[3]/div[1]/input')
    # 填充弹幕
    search_content.send_keys("selenium自动测试b站弹幕第 " + str(i) +"次")
    # 点击发布
    driver.find_element_by_xpath('//*[@id="bilibili-player"]/div/div/div[1]/div[2]/div/div[2]/div[3]/div[2]').click()
    time.sleep(2.5)
    # 生成当前页面快照并保存
    driver.save_screenshot("./png/danmu/test/"+str(i)+".png")
    time.sleep(2.5)  # b站发布一个弹幕后要过5秒

time.sleep(0.1)

# 生成当前页面快照并保存
driver.save_screenshot("./png/danmu/3.png")

end=time.time()

# 打印出测试花费的时间
print(end-start)