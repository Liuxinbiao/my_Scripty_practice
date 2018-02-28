#________________________
#正则表达式
#_______________________


# re.match

# #常规匹配
# import re
# content='Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())

#泛式搜索
# import re
# content='Hello 123 4567 World_This is a Regex Demo'
# result=re.match('^Hello.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())


#匹配目标
# import re
# content='Hello 1234567 World_This is a Regex Demo'
# result=re.match('^Hello\s(\d+)\s.*Demo$',content)
# print(result)
# print(result.group())
# print(result.span())
# print(result.group(1))#想打印出这些数字 第一个括号就对应着group（1）

#贪婪模式
# import re
# content='Hello 1234567 World_This is a Regex Demo'
# result=re.match('^He.*?(\d+).*Demo$',content)
# print(result)
# print(result.group(1))
# print(result.span())
# #有？就为非贪婪模式


#匹配模式
# import re
# content="""Hello 1234567 World_This
#          is a Regex Demo"""
# result=re.match('^He.*?(\d+).*Demo$',content,re.S)
# print(result.group(1))
#在遇到换行符时使用re.S可以时正则表达时正常运行


#遇到转义字符时
# import re
# content='price is $5.00'
# result=re.match('price is \$5\.00',content)
# print(result)
#使用但斜杠就可以解决




#Re.search

#为re.match与re.search对比
# import re
# content='Extra srtings Hello 1234567 Word_This is a Regex Demo Extra strings'
# result=re.match('Hello.*?(\d+).*Demo$',content)
# print(result)

# import re
# content='Extra srtings Hello 1234567 Word_This is a Regex Demo Extra strings'
# result=re.search('Hello.*?(\d+).*Demo',content)
# print(result)

#re.match从从字符串开头开始查询的 re.search时只要符合就可以打印出来



#Re.findall
#可以把所有符合条件的都打印出来



#Re.sub
# import re
# content='Extra srtings Hello 1234567 Word_This is a Regex Demo Extra strings'
# content=re.sub('\d+','',content)
# print(content)#第一个时想要替换的字符 第二个时替换为的字符 第三个时传入字符串
#另一种替换
# import re
# content='Extra srtings Hello 1234567 Word_This is a Regex Demo Extra strings'
# content=re.sub('\d+','text',content)
# print(content)
#在原来基础上进行替换
# import re
# content='Extra srtings Hello 1234567 Word_This is a Regex Demo Extra strings'
# content=re.sub('(\d+)',r'\1 789',content)
# print(content)
#\1 是为了把被替换的字符拿出来



#Re compile
# import re
# content=""""Extra srtings Hello 1234567 Word_This is a Regex
#  Demo Extra strings"""
# pattern=re.compile('Hello.*Demo',re.S)
# result1=re.search(pattern,content)
# print(result1)
# result=re.search('Hello.*Demo',content,re.S)
# print(result)

#Re.compile可以理解为把正则表达式保存下来




#实际操作

import requests,re
content=requests.get('https://book.douban.com/').text
pattern=re.compile('<li.*?cover.*?title="(.*?)".*?href="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
# pattern2=re.compile('<li.*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
results=re.findall(pattern,content)
print(results)
for result in results:
    url,name,author,date=result
    author=re.sub('\s','',author)
    date=re.sub('\s','',date)
    print(url,name,author,date)

