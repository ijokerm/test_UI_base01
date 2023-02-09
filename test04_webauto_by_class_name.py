from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')
# 实现需求
# 需求：打开注册A.html⻚面，完成以下操作
# class_name ⽅法: 由于元素的 class 属性值可能存在重复, 必须确定其能够代表目标元素唯⼀性之后, ⽅可使⽤
# 注意
# 1. ⽅法名是 class_name, 但要找元素的 class 属性值
# 2. 如果元素的 class 属性值存在多个值, 在 class_name ⽅法使用时, 只能使用其中的任意一个
# 1).通过class_name定位电话号码A，并输⼊：18611111111
phone = driver.find_element(By.CLASS_NAME,'telA')
phone.send_keys("18611111111")
# 2).通过class_name定位电子邮箱A，并输入：123@qq.com
# mail = driver.find_element(By.CLASS_NAME,'emailA dzyxA')  错误样例
mail = driver.find_element(By.CLASS_NAME,'dzyxA')  # 正确样例
# mail = driver.find_element(By.CLASS_NAME,'emailA')  # 正确样例
mail.send_keys("123@qq.com")

time.sleep(6)
driver.quit()
