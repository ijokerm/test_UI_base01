from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')
# tag_name --通过标签名来定位
# HTML本质就是标签组成的，每一种标签在页面都可能有多个，因此不方便精确定位
# 实现需求
# 需求：打开注册A.html⻚页⾯面，完成以下操作
# tag_name ⽅方法: 由于⻚⾯内可能存在⼤量重复的标签名, 因此必须确定其能够代表目标元素唯⼀性之后, 方可使⽤
# 注意: 由于标签名的重复性过⾼高, ⼀般做精确定位时, 都不会选择 tag_name方法
# 1).使⽤用tag_name定位⽤用户名输⼊入框，并输⼊入：admin

# username = driver.find_element(By.TAG_NAME,'input')
# username.send_keys('admin')
# 说明: 如果目标元素对象在后续的代码中只使⽤一次, 也可以直接在定位元素结束后, 直接调⽤输入方法实现操作
driver.find_element(By.TAG_NAME,'input').send_keys('admin')

time.sleep(6)
driver.quit()