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
driver.save_screenshot("./png/comment/1.png")

# 点击首页第一个视频
driver.find_element_by_xpath('//*[@id="i_cecream"]/main/section[1]/div[1]/div[2]/div[2]/a').click()

driver.switch_to.window(driver.window_handles[-1])  # 跳转到不同页面下的新页面.

time.sleep(1.5)  # 延长时间确保能捕捉到.

# 生成当前页面快照并保存
driver.save_screenshot("./png/comment/2.png")



# 开始计时
start=time.time()

# 评论
# 输入对应的搜索内容.
for i in range(10):
    # 抓取评论区域
    search_content = driver.find_element_by_xpath('//*[@id="comment"]/div/div/div/div[2]/div[1]/div/div/div[2]/textarea')
    # 填充评论
    search_content.send_keys("selenium自动测试b站评论第 " + str(i) +"次")
    # 点击发布
    driver.find_element_by_xpath('//*[@id="comment"]/div/div/div/div[2]/div[1]/div/div/div[3]').click()
    time.sleep(1)  # 防止频繁发送
    # 生成当前页面快照并保存
    driver.save_screenshot("./png/comment/test/"+str(i)+".png")

time.sleep(0.1)

# 生成当前页面快照并保存
driver.save_screenshot("./png/comment/3.png")

end=time.time()

# 打印出测试花费的时间
print(end-start)