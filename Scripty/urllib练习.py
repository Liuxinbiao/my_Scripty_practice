#Urllib的操作演练

#关于urlopen

# import urllib.request
# response=urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

#关于超时的设置
# import urllib.request
# response=urllib.request.urlopen('http://httpbin.org/get', timeout=1)
# print(response.read())


#关于报错的演练
# import urllib.request
# import socket
# import urllib.request
# import urllib.error
# try:
#     response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')


#-------

#Request

#-------


#响应

#关于状态码及响应头

# import urllib.request
# response=urllib.request.urlopen('http://www.python.org')
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

#Request

#request对象能传给urlopen 与urlopen结果一样
# import urllib.request
# request=urllib.request.Request('https://python.org')
# response=urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))


#request的请求方式和heards参数及额外的参数
# from urllib import request,parse
# url='http://httpbin.org/post'
# heards={
#     'User-Agent':'Mozllla/4.0(compatible;MSIE 5.5;Windows NT',
#     'Host':'httpbin.org'
# }
# dict={
#     'name':'Germey'
# }
# data=bytes(parse.urlencode(dict),encoding='utf8')
# req=request.Request(url=url,data=data,headers=heards,method='POST')
# response=request.urlopen(req)
# print(response.read().decode('utf-8'))

#-------
#Handler
#-------

#代理（这是使用韩国代理 但是不会设置。没成功）
# import urllib.request
# proxy_handers=urllib.request.ProxyHandler({
#     'http':'http://127.0.0.11:9743',
#     'https':'https://127.0.0.11:9743'
# })
# opener=urllib.request.build_opener(proxy_handers)
# response=opener.open('http://httbin.org/get')
# print(response.read())

#cookie

# import http.cookiejar,urllib.request
# cookie=http.cookiejar.CookieJar()
# hander=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(hander)
# response=opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

#cookie 以TXT格式保存
# import http.cookiejar,urllib.request
# filename="Cookie.txt"
# cookie=http.cookiejar.MozillaCookieJar(filename)
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

#cookie 保存后读取
import http.cookiejar,urllib.request
cookie=http.cookiejar.LWPCookieJar()
cookie.load("Cookie.txt",ignore_discard=True,ignore_expires=True)
handler=urllib.request.HTTPCookieProcessor(cookie)
opener=urllib.request.build_opener(handler)
response=opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))

