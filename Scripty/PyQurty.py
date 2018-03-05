#-------------------
#PyQuery
#-------------------

#
# html = '''
# <div>
#    <ul>
#       <li class="item-0">first item</li>
#       <li dass="item-1'href="link2.html">second item</a></li>
#       <li class="item-0 active"><a href="link3.html>span class=bold">third item</span></a></li>
#       <li class="item-1 active"<a href='link4.html">fourth item/a></li>
#       <li class="item-0"><a href="link5.html>fifth item</a></li>
#    <ul>
# </div>
# '''

# 字符串初始化
#
# doc=pq(html)
# # print(doc('li'))#（如选择class使用. 选择item时使用#item ）


#url初始化
# from pyquery import PyQuery as pq
# doc=pq(url='http://www.baidu.com')
# print(doc('head'))




# html = '''
# <div class="wrap">
#    <div id="container">
#       <ul class="list">
#           <li class="item-0">first item</li>
#           <li dass="item-1'href="link2.html">second item</a></li>
#           <li class="item-0 active"><a href="link3.html>span class=bold">third item</span></a></li>
#           <li class="item-1 active"<a href='link4.html">fourth item/a></li>
#           <li class="item-0"><a href="link5.html>fifth item</a></li>
#       </ul>
#    </div>
# </div>
# '''
#-----------
#基本CSS选择器
#-----------

# from pyquery import PyQuery as pq
# doc=pq(html)
# print(doc('#container .list li'))#查找ID为container class为list 的li标签


#查找元素

#子元素
# from pyquery import PyQuery as pq
# doc=pq(html)
# item=doc('.list')
# print(type(item))
# print(item)
# lis=item.find('li')
# print(type(lis))
# print(lis)
#另一种方法
# from pyquery import PyQuery as pq
# doc=pq(html)
# item=doc('.list')
# lis=item.children('.active')
# print(lis)

#父元素
# from pyquery import PyQuery as pq
# doc=pq(html)
# items=doc('.list')
# container=items.parent()
# print(type(container))
# print(container)


#查找祖先节点
# from pyquery import PyQuery as pq
# doc=pq(html)
# items=doc('.list')
# parents=items.parents()
# print(type(parents))
# print(parents)
# #另一种方法
# from pyquery import PyQuery as pq
# doc=pq(html)
# items=doc('.list')
# parent=items.parents('.wrap')
# print(parent)


#兄弟元素
# from pyquery import PyQuery as pq
# doc=pq(html)
# li=doc('.list .item-0.active')
# print(li.siblings())
#其他方法
# from pyquery import PyQuery as pq
# doc=pq(html)
# li=doc('.list .item-0.active')
# print(li.siblings('.active'))




#---------------
#遍历
#-------------


# html = '''
# <div class="wrap">
#    <div id="container">
#       <ul class="list">
#           <li class="item-0">first item</li>
#           <li dass="item-1><a href="link2.html">second item</a></li>
#           <li class="item-0 active"><a href="link3.html">span class="bold">third item</span></a></li>
#           <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#           <li class="item-0"><a href="link5.html>fifth item</a></li>
#       </ul>
#    </div>
# </div>
'''
#单个元素
# from pyquery import PyQuery as pq
# doc=pq(html)
# li=doc('.item-0.active')
# print(li)
#另一个方法
# from pyquery import PyQuery as pq
# doc=pq(html)
# li=doc('.item-0.active')
# lis=doc('li').items()
# print(type(lis))
# for li in lis:
#     print(li)



#----------------
#获取信息
#------------

# html = '''
# <div class="wrap">
#    <div id="container">
#       <ul class="list">
#           <li class="item-0">first item</li>
#           <li dass="item-1><a href="link2.html">second item</a></li>
#           <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#           <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#           <li class="item-0"><a href="link5.html>fifth item</a></li>
#       </ul>
#    </div>
# </div>
'''
#获取属性
# from pyquery import PyQuery as pq
# doc=pq(html)
# a=doc('.item-0.active a')
# print(a)
# print(a.attr('href'))
# print(a.attr.href)


#获取文本
# from pyquery import PyQuery as pq
# doc=pq(html)
# a=doc('.item-0.active a')
# print(a)
# print(a.text())


#获取HTML
# from pyquery import PyQuery as pq
# doc=pq(html)
# a=doc('.item-0.active')
# print(a)
# print(a.html())


#----------------
#DOM操作
#------------


# html = '''
# <div class="wrap">
#    <div id="container">
#       <ul class="list">
#           <li class="item-0">first item</li>
#           <li dass="item-1><a href="link2.html">second item</a></li>
#           <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#           <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#           <li class="item-0"><a href="link5.html>fifth item</a></li>
#       </ul>
#    </div>
# </div>
# '''
#addClass 和removeClass(动态修改）
# from pyquery import PyQuery as pq
# doc=pq(html)
# li=doc('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class('.active')
# print(li)


#attr和css(动态属性修改)
# from pyquery import PyQuery as pq
# doc=pq(html)
# li=doc('.item-0.active')
# print(li)
# li.attr('name','link')
# print(li)
# li.css('font-size','14px')
# print(li)


#remove
# html='''
# <div class="wrap">
#    Hello.World
#    <p>This is a paragraph.</p>
# <div>
# '''
# from pyquery import PyQuery as pq
# doc=pq(html)
# wrap=doc('.wrap')
# print(wrap.text())
# wrap.find('p').remove()
# print(wrap.text())





#-----------------
#伪装选择器
#---------------

html = '''
<div class="wrap">
   <div id="container">
      <ul class="list">
          <li class="item-0">first item</li>
          <li dass="item-1><a href="link2.html">second item</a></li>
          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
          <li class="item-1 active"><a href="link4.html">fourth item</a></li> 
          <li class="item-0"><a href="link5.html>fifth item</a></li>
      </ul>
   </div>
</div>
'''
from pyquery import PyQuery as pq
doc=pq(html)
li=doc('li:first-child')
print(li)#获取第一个标签
li=doc('li:last-child')
print(li)
#获取最后一个标签
li=doc('li:nth-child(3)')
print(li)
#获取第三个标签（从1开始的）
li=doc('li:gt(2)')
print(li)
#获取比二大标签（从零开始的）
li=doc('li:nth-child(2n)')
print(li)
#获取二的倍数的
li=doc('li:contains(second)')
print(li)
#查找文本中含有second的
