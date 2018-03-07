#目标站点流程框架

#1.抓取但也内容
#2.正则表达式分析
#3.保存至文件


#爬取猫眼电影实战

import requests
from requests.exceptions import RequestException
import re
import json
def get_one_page(url):
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)
        if response.status_code==200:
            return response.text
            return NameError
    except RequestException:
        return None
def parse_one_page(html):
    pattern=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                       +'.*?>(.*?)</a>.*?star"(.*?)</p>.*?releasetime">(.*?)</p>'
                       +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    print(items)
    for item in items:#for的遍历
        #生成一个字典
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],#.strip去除空格
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }
def write_to_file(content):
    with open('result2.txt', 'a', encoding='utf-8') as f:
        #数据转换成json格式的字符串
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        print(item)
    write_to_file(item)
if __name__ == '__main__':
    for i in range(10):
        main(i*10)
