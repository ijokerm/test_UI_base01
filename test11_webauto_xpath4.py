""" XPath元素定位
利用层级与逻辑结合策略 //*[@id='p1']/input
"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A.html⻚页⾯面，完成以下操作
# 1).使⽤层级与逻辑结合策略定位，在test1并输入：admin
driver.find_element(By.XPATH,'//*[@id="p1"]/input').send_keys("admin")
# 2).暂停2秒
time.sleep(2)

# driver.find_element(By.XPATH,'//input[@name="user" and @class="login-test"]').send_keys("123@qq.com")

driver.quit()