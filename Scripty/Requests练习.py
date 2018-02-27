#---Requests

#get 请求
# import requests
# response=requests.get('http://httpbin.org/get')
# print(response.text)

#带参数的get请求(也可以理解为传值)
# import requests
# response=requests.get("http://httpbin.org/get?name=germey&age=22")
# print(response.text)
# #------------------(另一种带参数方法)
# import requests
# data={
#     'name':'germey',
#     'age':22
# }
# response=requests.get("http://httpbin.org/get",params=data)
# print(response.text)

#解析json
# import requests,json
# response=requests.get("http://httpbin.org/get")
# print(type(response.text))
# print(response.json())
# print(type(response.json()))

#获取二进制数据
# import requests
# respones=requests.get("https://www.baidu.com/img/baidu_jgylogo3.gif")
# print(type(respones.text),type(respones.content))
# print(respones.text)
# print(respones.content)
#-----------
# import requests
# respones=requests.get("https://www.baidu.com/img/baidu_jgylogo3.gif")
# with open('baidu_jgylogo3.gif','wb')as f:
#     f.write(respones.content)
#     f.close()

#添加headers
# import requests
# headers={
#     'Use-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
# }
# response=requests.get('https://www.zhihu.com/explore',headers=headers)
# print(response.text)

#post 请求(与get方法一样)
# import requests
# data={'name':'germey','age':'22'}
# headers={
#     'Use-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
# }
# response=requests.post("http://httpbin.org/post",data=data,headers=headers)
# print(response.json())


#--------------

#相应

#--------------

#response属性
# import requests
# response=requests.get('http://www.jianshu.com')
# print(type(response.status_code),response.status_code)
# print(type(response.headers),response.headers)
# print(type(response.cookies),response.cookies)
# print(type(response.url),response.url)
# print(type(response.history),response.history)

#状态码判断
# import requests
# response=requests.get('http://www.jianshu.com')
# exit()if not response.status_code==requests.codes.ok else print("Requests Successful")
#另一种方法
# import requests
# response=requests.get('http://www.jianshu.com')
# exit()if not response.status_code==200 else print("Requests Successful")


#-------------

#高级操作

#--------------


#文件上传
# import requests
# files={'file':open('baidu_jgylogo3.gif','rb')}
# response=requests.post('http://httpbin.org/post',files=files)
# print(response.text)

#获取cookie
# import requests
# response=requests.get('http://www.baidu.com')
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key+"="+ value)


#会话维持（模拟登陆）
#可理解为两个浏览器分别请求
# import requests
# requests.get('http://httpbin.org/coolies/set/number/123456789')
# response=requests.get('http://httpbin.org/cookies')
# print(response.text)
#可理解为一个浏览器两次请求
# import requests
# s=requests.session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# response=s.get('http://httpbin.org/cookies')
# print(response.text)

#在没有维持登陆的情况下(是没有cookies)
# import requests
# response=requests.get('http://httpbin.org/get')
# print(response.text)

#证书验证
# import requests
# response=requests.get('http://www.12306.cn')
# print(response.status_code)
#解决方法
# import requests
# response=requests.get('http://www.12306.cn',verify=False)
#urllib.disable_warnings    #为了消除警告信息
# print(response.status_code)


#代理设置
# import requests
# proxies={
#     'http':'http://127.0.0.1:9743',
#     'https':'https://127.0.0.1:9743'
#     #自己所使用的代理一致
# }
# response=requests.get('https://www.taobao.com',proxies=proxies)
# print(response.status_code)
#需要用户名跟密码的情况
# import requests
# proxies={
#     'http':'http://user:password@127.0.0.1:9743',
# }
# response=requests.get('https://www.taobao.com',proxies=proxies)
# print(response.status_code)


#超时设置
# import requests
# from requests.exceptions import ReadTimeout
# try:
#     response = requests.get('http://httpbin.org/get', timeout=0.5)
#     print(response.status_code)
# except ReadTimeout:
#     print('timeout')

#认证信息
# import requests
# from requests.auth import HTTPBasicAuth
# r=requests.get('http://120.27.34.24:9001',auth=HTTPBasicAuth('user','123'))
# print(r.status_code)
#另一中方法
# import requests
# r=requests.get('http://120.27.34.24:9001',auth=('user','123'))
# print(r.status_code)