""" XPath元素定位
利用相对路径、绝对路径策略
"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 需求：打开注册A.html⻚页⾯面，完成以下操作
# 1).使⽤用绝对路径定位⽤户名输⼊框，并输入：admin
driver.find_element(By.XPATH,'/html/body/div/fieldset/form/p[1]/input').send_keys("admin")
# 2).暂停2秒
time.sleep(2)
# 3).使⽤相对路径定位密码输⼊框，并输入：123
# 注意: 使⽤相对路径时, 需要注意方法参数的内外引号嵌套问题
driver.find_element(By.XPATH,'//*[@id="passwordA"]').send_keys("123")

time.sleep(6)
driver.quit()