#--------------
#Selenium
#-------------


#声明浏览器对象
#from selenium import webdriver
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")#这是webdriver所在位置


#访问页面
# from selenium import webdriver
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()



#----------------
#查找元素
#----------------



#单个元素
# from selenium import webdriver
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.taobao.com')
# input_first=browser.find_element_by_id('q')
# input_second=browser.find_element_by_css_selector('#q')
# input_third=browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first,input_third,input_second)
# browser.close()
#另一个方法
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.taobao.com')
# input_first=browser.find_element(By.ID,'q')
# print(input_first)
# browser.close()


#多个元素

# from selenium import webdriver
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.taobao.com')
# lis=browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# browser.close()



#元素交互操作
# from selenium import webdriver
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.taobao.com')
# input=browser.find_element_by_id('q')
# input.send_keys('iphone')
# input.clear()
# input.send_keys('ipad')
# button=browser.find_element_by_class_name('bin-search')
# button.click()



#交互动作
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# url='http://www.runoob.com/try/try/php?filename=jqueryul-apl-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source=browser.find_element_by_css_selector('#draggable')
# target=browser.find_element_by_css_selector('#droppable')
# actions=ActionChains(browser)
# actions.drag_and_drop(source,target)
# actions.perform()


#执行JavaScript
# from selenium import webdriver
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Botton")')




#------------------
#获取元素信息
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.zhihu.com/explore')
# logo=browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))


#获取文本值
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.zhihu.com/explore')
# input=browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)#文本
# print(input.id)#获取ID
# print(input.location)#获取位置
# print(input.tag_name)#获取标签名
# print(input.size)#获取大小



#Frame#切换父/子元素
# import time
# from selenium.common.exceptions import NoSuchElementException
# from selenium import webdriver
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# url='http://www.runoob.com/try/try.php?filename=jqueryul-apl-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source=browser.find_element_by_css_selector('#draggbale')
# print(source)
# try:
#     logo=browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('No Logo')
# browser.switch_to.parent_frame()
# logo=browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)



#--------------
#等待
#-------------

#隐式等待
# from selenium import webdriver
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.zhihu.com/explore')
# input=browser.find_element_by_class_name('zu-top-add-question')
# print(input)

#显式等待
#指定等待条件，制定等待时间，判断条件成立就立即返回，条件不成立就继续等待，知道等待到最长时间的时间
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.taobao.com/')
# wait=WebDriverWait(browser,10)
# input=wait.until(EC.presence_of_all_elements_located((By.ID,'q')))#传入条件
# button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'bin-search')))
# print(input,button)
# title_is 标题是某内容
# title_contains 标题包含内容
# presence_of_element_located 元素加载出，传入定位元组
# visibility_of_element_located 元素可见，传入定位元组
#

# 前进和后退
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

#cookies
# from selenium import webdriver
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())


#选项卡管理#切换网页
# from selenium import webdriver
# import time
# browser=webdriver.Edge("D:\python\Scripts\MicrosoftWebDriver.exe")
# browser.get('https://www.baidu.com/')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('http://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')