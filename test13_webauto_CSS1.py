""" CSS定位策略 --前四种
id选择器
class选择器
元素选择器 --标签选择器
属性选择器
"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')
# 需求：打开注册A.html⻚页⾯面，完成以下操作
# 1).使⽤CSS定位⽅式中id选择器定位用户名输⼊入框，并输入：admin
# 语法: #id属性值
driver.find_element(By.CSS_SELECTOR,'#userA').send_keys("admin")
# 2).使⽤用CSS定位⽅式中属性选择器定位密码输入框，并输⼊：123456
# 语法 1: [属性名="属性值"]
# 语法 2: 标签名[属性名="属性值"]
driver.find_element(By.CSS_SELECTOR,'input[placeholder="请输入用户名"]').send_keys("123456")
#  3).使⽤用CSS定位⽅式中class选择器定位电话号码输⼊入框，并输⼊入：18600000000
# 语法: .class属性值
driver.find_element(By.CSS_SELECTOR,'.telA').send_keys("18600000000")
time.sleep(3)
# 4).使⽤CSS定位方式中元素选择器定位注册按钮，并点击
# 说明: 元素选择器又名标签选择器
# 语法: 标签名
driver.find_element(By.CSS_SELECTOR,'button').click()

# 属性选择器注意点 与 class_name ⽅法不同的是, 如果使⽤具有多个值的 class 属性,则需要传入全部的属性值!
driver.find_element(By.CSS_SELECTOR,'[class="emailA dzyxA"]')
# class选择器注意点：如果元素的 class 属性值存在多个值, 在 class_name ⽅法使用时, 只能使用其中的任意一个
driver.find_element(By.CSS_SELECTOR,'.emailA')

time.sleep(6)
driver.quit()