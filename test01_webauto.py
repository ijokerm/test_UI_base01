"""web自动化基本代码"""
# 1.导入模块
from selenium import webdriver
import time

# 2.实例化浏览器对象
driver = webdriver.Chrome()
driver2 = webdriver.Firefox()
# 3.打开网页 --必须协议头
# driver.get("http://www.baidu.com")
driver2.get('http://www.baidu.com')
# 4.观察效果

time.sleep(5)
# 5.关闭页面
driver2.quit()

