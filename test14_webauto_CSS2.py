""" CSS定位策略 --层级选择器
"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')
# 需求：打开注册A.html⻚页⾯面，完成以下操作
# 1).使⽤用CSS定位方式中的层级选择器定位⽤户名输入框，并输入：admin
# 层级选择器
# ⽗子层级关系: ⽗层级策略>⼦层级策略
driver.find_element(By.CSS_SELECTOR,'#pa>input').send_keys("admin")
time.sleep(2)
# 祖辈后代层级关系: 祖辈策略 后代策略
driver.find_element(By.CSS_SELECTOR,'form [placeholder="请输入用户名"]').send_keys("admin")
# 注意：父子层级关系也可以使用空格连接
time.sleep(2)
driver.quit()