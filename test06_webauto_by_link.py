from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')

# 实现需求
# 需求：打开注册A.html⻚页⾯面，完成以下操作
# 1).使⽤用link_text定位(访问 新浪 网站)超链接，并点击
# driver.find_element(By.LINK_TEXT,'访问 新浪 网站').click()

# link_text 方法: 该方法只针对超链接元素(a 标签), 并且需要输入超链接的全部文本信息
# 点击⽅方法: 元素对象.click() 输入超链接的部分文本信息

driver.find_element(By.PARTIAL_LINK_TEXT,'访问').click()
# 注意: 虽然是只传入部分⽂文本信息, 但是需要确定其唯一性, 方可以使⽤


time.sleep(6)
driver.quit()