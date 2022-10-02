# 导入 webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()

options.binary_location = "E:\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)


start = time.time()

"""测试基本的搜索内容."""
for i in range(10):
        driver.get("https://www.bilibili.com/")

        # 输入对应的搜索内容.
        search_content = driver.find_element_by_class_name("nav-search-input")
        search_content.send_keys("老番茄" + str(i))

        # 点击搜索.
        search_button = driver.find_element_by_class_name("nav-search-btn")
        search_button.click()

        driver.switch_to.window(driver.window_handles[-1])  # 跳转到不同页面下的新页面.

        try:
                element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div[2]/a/div/div[1]/picture/source')))
        finally: # 搜索结果加载出图片后再进行截图
                # 生成当前页面快照并保存
                driver.save_screenshot("./png/search/b" + str(i) + ".png")

end = time.time()

# 打印出测试花费的时间
print(end - start)
