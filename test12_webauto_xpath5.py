""" XPath元素定位--延伸
//*[text()="xxx"]                      文本内容是xxx元素 （全部）
//*[contains(@attribute,'xxx')]        属性中含有xxx元素
//*[starts-with(@attribute,'xxx')]    属性以xxx开头的元素
"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')
driver.find_element(By.XPATH,'//input[contains(@id,"pass")]').send_keys("123@qq.com")
time.sleep(2)
# 需求：打开注册A.html⻚页⾯面，完成以下操作
# 1).//*[text()="xxx"] ：通过文本信息定位目标元素，要求全部文本内容
driver.find_element(By.XPATH,"//*[text()='访问 新浪 网站']").click()
# 2).//*[contains(@attribute,'xxx')] 通过给定属性的部分内容进行元素定位

# 暂停2秒
time.sleep(2)


driver.quit()