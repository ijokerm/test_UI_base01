""" 元素定位 --name"""
from time import time, sleep

# 导包
from  selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器对象
driver = webdriver.Chrome()
driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')
# 使用name定位元素 name属性值不具备唯一性，可能存在重复。必须要保证唯一性才能使用
# 当元素中的name值相同 无法保证唯一性的话 默认只会获取第一个符合要求特征对应的元素
# 定义元素时尽量保证其特征值的唯一性
username = driver.find_element(By.NAME,'AAA')
username.send_keys('admin')
password = driver.find_element(By.NAME,'AAA')
password.send_keys('1234567')
# 展示效果
sleep(6)
# 关闭页面
driver.quit()