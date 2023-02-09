""" XPath元素定位
利用元素属性策略 //input[@属性='user']
"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A.html⻚页⾯面，完成以下操作
# 1).使⽤元素属性策略定位⽤户名输⼊框，并输入：admin
driver.find_element(By.XPATH,'//input[@placeholder="请输入用户名"]').send_keys("admin")
# 2).暂停2秒
time.sleep(2)
# 注意: 使⽤元素属性策略定位，目标属性和属性值可能存在多个相同特征的元素，需要注意唯一性
# 注意: 与 class_name ⽅法不同的是, 如果使⽤具有多个值的 class 属性,则需要传入全部的属性值!
driver.find_element(By.XPATH,'//input[@class="emailA dzyxA"]').send_keys("123@qq.com")


time.sleep(6)
driver.quit()