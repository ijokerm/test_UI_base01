""" 定位一组元素的方法
了解find_elements()
"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# elements = driver.find_elements(By.NAME,'userA')
# print(elements,type(elements))
# 注意：find_elements(),执行的返回结果是列表数据类型，里面的数据是多个元素对象 --试用于一个元素对象对应多个值的情况
# 可以通过列表的下标获取某个确定元素，再执行操作 --tag_name
elements = driver.find_elements(By.TAG_NAME,'input')
elements[2].send_keys("13800000002")
elements[3].send_keys("123@qq.com")


time.sleep(6)
driver.quit()