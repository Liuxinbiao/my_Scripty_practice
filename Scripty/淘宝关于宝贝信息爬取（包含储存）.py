import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
from config import *
import pymongo



brower = webdriver.Chrome()
wait = WebDriverWait(brower, 10)
client=pymongo.MongoClient(MONGO_URL)
db=client[MONGO_DB]


def search():
    try:
        brower.get('https://www.taobao.com')
        input = wait.until(  # 设置等待时间 #在网速较慢还有浏览器出现问题就会出现TIMEOUT
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#q'))  # 判断加载是否成功  #'#q'是选择搜索框
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        # element_to_be_clickable 按钮为可点击 #css选择器为“搜索”按钮
        brower.find_element_by_id("q").send_keys('美食')
        # 根据ID选择具体位置（搜索输入框）输入美食
        submit.click()
        total = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_products()
        # css为总共一百页的
        return brower.find_element_by_class_name("total").text
        # 根据class选择总共的页数
    except TimeoutException:
        return search()  # 在TIMEOUT出现后再次请求


def next_page(page_number):
    try:
        input = wait.until(  # 设置等待时间 #在网速较慢还有浏览器出现问题就会出现TIMEOUT
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))  # 判断加载是否成功  #css选择器为第（）页
        )
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))  # css为确定按钮
        brower.find_element_by_css_selector("#mainsrp-pager > div > div > div > div.form > input").clear()
        # css把第（）页清零
        brower.find_element_by_css_selector("#mainsrp-pager > div > div > div > div.form > input").send_keys(
            page_number)
        # css选择器输入数字的文本框
        submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        # 判断翻页是否成功 #css选择器为高亮
        get_products()
    except TimeoutException:
        next_page(page_number)  # 出错后再次尝试


def get_products():
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    # 先判断是否加载完成，然后定位到item（）
    html = brower.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    # 调用items 可以得到所有选择内容
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),  # 选择item标签下的img标签 定位到src
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('location').text()
        }
    print(product)
    save_to_monge(product)
def save_to_monge(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print("储存到MONGODB成功，",result)
    except Exception:
        print("储存到MONGODB错误",result)

def main():
    total = search()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2, total + 1):  # 如果翻页的话要从第二页开始
        next_page(i)
    brower.close()


if __name__ == '__main__':
    main()

