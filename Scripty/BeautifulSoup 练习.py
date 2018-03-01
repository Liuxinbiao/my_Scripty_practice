#BeautifulSoup

# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their r
# <a href="http://example.com/elsleo class="sister" Id= IInkl"><!- Elsie ->.
# <a href="http://example.com/lacie" class="sister" ld="link2">Lacie</a> and
# <a href="http://example.com/tilliem class="sister" ld="link3">TIIIie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

#--------------
#标签选择器
#------------


#基本使用
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.prettify())
# print(soup.title.string)


#选择元素
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.title)
# print(type(soup.title))
# print(soup.head)
# print(soup.p)#只会打印第一个标签


#获取标签名称
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.title.name)


# #获取属性
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.p.attrs['name'])
# print(soup.p['name'])

#获取内容
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.p.string)

#嵌套结构
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.head.title.string)


html = """
<html>
  <head>
    <title>The Dormouse's story</title>
  <head>
  <body>
    <p class="story"
       Once upon a time there were three little sisters;and their names were
       <a href="http://example.com/elsleo class="sister" Id= IInkl"><!- Elsie ->.
         <span>Elsie</span>
        </a>
        <a href="http://example.com/lacie" class="sister" ld="link2">Lacie</a>
        and
        <a href="http://example.com/tilliem class="sister" ld="link3">TIIIie</a>
        and they lived at the bottom of a well.</p>
       <p class="story">Once upon a time there were three little sisters; and their r
       <p class="story">...</p>
"""
#子节点和子孙节点
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.p.contents)
#另一种方法    ###.children 属于迭代器
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.p.children)
# for i,child in enumerate(soup.p.children):# in enumerate 会返回索引和内容
#     print(i,child)
#另一种方法 #获取搜友子孙节点#把span节点也打印出来了（span为p的孙子的儿子）
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.p.descendants)
# for i,child in enumerate(soup.p.descendants):#这也是属于迭代器
#     print(i,child)

#父节点
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.p.parent)

#祖父节点
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(list(enumerate(soup.p.parents)))

#兄弟节点
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(list(enumerate(soup.a.next_siblings)))
# print(list(enumerate(soup.a.previous_siblings)))



#-----------------------
#标准选择器
#可根据标签名、属性、内容来查找文档
#-----------------------
html='''
<div class="panel">
   <div class="panel-heading">
     <h4>Hello</h4>
   </div>
   <div class="panel-body">
      <ul class="list" id="list-1">
         <li class="element">Foo</li>
         <li class="element">Bar</li>
         <li class="element">Jay</li>
      </ul>
      <ul class="list list-small" ld="list-2">
         <li class="element">Foo</li>
         <li class="element">Bar</ll>
      </ul>
   </div>
</div>
'''
#根据标签名来查找
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.find_all('ul'))
# print(type(soup.find_all('ul')[0]))
#另一种方法(以嵌套的方法来查找)
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# for ul in soup.find_all('ul'):
#     print(ul.find_all('li'))

#attrs用法
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.find_all(attrs={"id":"list-1"}))
# print(soup.find_all(attrs={"class":"list"}))
# print(soup.find_all(attrs={"class":"list list-small"}))
#另一种方法
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.find_all(id='list-1'))
# print(soup.find_all(class_="element"))# 当需要查找class时需要在后面添加下划线

#find（name,attrs,recursive,text）
#find 时返回一个元素 find_all是返回多个元素
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.find('ul'))
# print(type(soup.find('ul')))
# print(soup.find('li'))


#---------------
#CSS选择器
#---------------


html='''
<div class="panel">
   <div class="panel-heading">
     <h4>Hello</h4>
   </div>
   <div class="panel-body">
      <ul class="list" id="list-1">
         <li class="element">Foo</li>
         <li class="element">Bar</li>
         <li class="element">Jay</li>
      </ul>
      <ul class="list list-small" id="list-2">
         <li class="element">Foo</li>
         <li class="element">Bar</ll>
      </ul>
   </div>
</div>
'''
#select用法
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))# ul 和li 标签不需要加.
# print(soup.select('#list-1 .element'))#在选择id 时要加#号
#另一种方法
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# for ul in soup.select('ul'):
#     print(ul.select('li'))

#获取属性
# from bs4 import BeautifulSoup
# soup=BeautifulSoup(html,'lxml')
# for ul in soup.select('ul'):
#     print(ul['id'])
#     print(ul.attrs['id'])

#获取内容
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
for li in soup.select('li'):
    print(li.get_text())