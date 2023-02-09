# 导包
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# 实例化浏览器对象
driver = webdriver.Chrome()
# 打开网页
driver.get('file:///C:/Users/Cbear/Desktop/page/%E6%B3%A8%E5%86%8CA.html')
# 实现需求
# 需求：打开注册A.html⻚页⾯面，完成以下操作
# id ⽅方法: 通过目标元素的 id 属性值定位, 由于 id 值一般是唯⼀的,因此当元素存在 id 属性值时, 优先使用 id ⽅方法定位元素
# 1).使⽤用id定位，输⼊入⽤用户名：admin 输入方法：元素对象.send_keys('内容')
username = driver.find_element(By.ID,'userA')    # username是一个元素对象
username.send_keys('admin')

# 2).使⽤用id定位，输⼊入密码：123456
password = driver.find_element(By.ID,'passwordA')
password.send_keys('123456')
# 注意：selenium更新find_element_by_id(id)均用 find_elment(By.XX, “字段值”)方法替代 要导入from selenium.webdriver.common.by import By

# 展示效果
time.sleep(5)
# 关闭页面
driver.quit()