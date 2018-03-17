# 1 抓取索引页内容
# 2代理设置
# 3 经数据到数据库
# 4分析详情页内容

from urllib.parse import urlencode
import requests
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq

base_url='http://weixin.sogou.com/weixin?'
#需要加入cookies位置登陆的状态才能观看全部内容
headers={
    'Cookie': 'CXID=183CFDDD8E510FB843BFB779CACAECC0; SUID=C0438FD35D68860A5AA392CB000955F2; ad=Hlllllllll2zoiaalllllV$6WTDlllll1cdRZlllll9llllljCxlw@@@@@@@@@@@; IPLOC=CN1302; SUV=1521005950708264; ABTEST=0|1521005956|v1; SNUID=6FEC207CAFABC8F66511EC18AF0AFA30; weixinIndexVisited=1; ppinf=5|1521006377|1522215977|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxMDg6JUVGJUJBJUFEJUU1JUI5JUI2JUU3JThCJUEwJUU3JThCJUEwJUU0JUJBJUIyJUU0JUJBJTg2JUU0JUJEJUEwJUU0JUI4JTgwJUU1JThGJUEzJUVGJUJBJUFEJUU1JUE0JUE3JUU1JUJEJUFBfGNydDoxMDoxNTIxMDA2Mzc3fHJlZm5pY2s6MTA4OiVFRiVCQSVBRCVFNSVCOSVCNiVFNyU4QiVBMCVFNyU4QiVBMCVFNCVCQSVCMiVFNCVCQSU4NiVFNCVCRCVBMCVFNCVCOCU4MCVFNSU4RiVBMyVFRiVCQSVBRCVFNSVBNCVBNyVFNSVCRCVBQXx1c2VyaWQ6NDQ6bzl0Mmx1QjRIOGlRNDZCb1lmcm5Rd3dvajM5SUB3ZWl4aW4uc29odS5jb218; pprdig=srPGLDq6EXTz3tigHXLmcahSyf_wqBvjX-POxGPdafKrQezrxxb4lH504tI0maSIcFT9kKQRTzPHYM7oCl-sGunqumJ-EOar3GMXgcLLRoU5QdSuP4MtzliTyVaN5DpwQaDyruAyNWnIiQegV9QK86hCRSgTztjdaT5bW5QOCrY; sgid=14-34046819-AVqotymYBIUMERbNXM6rickA; SMYUV=1521177399452680; ppmdig=1521177412000000b8cd5b79abd2149fa3b091cbbf3dacae; JSESSIONID=aaaeucYgllHb_-YttHOiw; sct=3',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
}

keyword="风景"
proxy_pool_url='http://127.0.0.1:5000/get'
proxy=None#更改一次代理就全局生效，如果不把peoxy设成参数的话，那就会代理一直传
Max_count=5
def get_proxy():
    try:
         response=requests.get(proxy_pool_url)
         if response.status_code==200:
             return response.text
         return None
    except ConnectionError:
        return None

def get_html(url,count=1):
    """需要代理"""
    global proxy
    if count>=Max_count:
        print("Tries Too Many Counts")
        return None
    #当此时到达最大值后就结束
    try:
        if proxy:
            proxies={
                'http':'http://'+proxy
            }#有代理的话就设置成有代理的参数请求，没有代理的话就用正正常的请求
        response=requests.get(url,allow_redirects=False,headers=headers,proxy=proxies)#allow_redirects是跳转界面
        if response.status_code==200:
            return response.text
        if response.status_code==302:
            #need proxy
            print("302")
            proxy=get_proxy()
            if proxy:
                print("Use Proxy",proxy)
                count+=1
                return get_html(url,count)
            else:
                print("GET proxy Failer")
                return None#当get_proxy 失败了。就是所有ip都用不来哦了，爬取就结束了
    except ConnectionError as e :
        print("Error Occurred",e.args)#打印错误信息
        proxy=get_proxy()
        count+=1
        return get_html(url)

def get_index(keyword,page):#构造请求参数 2指的是文章
    """索引页的抓取"""
    data={
        'query':keyword,
        'type':2,
        'page':page
    }
    queries=urlencode(data)#把字典进行编码，变成get请求参数
    url=base_url+queries#做url拼接 ，把完整的URL拼出来
    html=get_html(url)
    return html

def parse_index(html):
    doc=pq(html)
    items=doc('.new-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')#这是把超链接拿过来

def get_detail(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except ConnectionError:
        return None
def parse_detail(html):
    doc=pq(html)
    title=doc('.rich_media_title').text()
    content=doc('rich_media_content ').text()
    date=doc('#post-date').text()
    wechat=doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
    return {
        'title':title,
        'content':content,
        'date':date,
        'wechat':wechat
    }

def main():
    for page in range(1,101):
        html=get_index(keyword,page)
        if html:
            article_urls=parse_index(html)
            for article_url in article_urls:
                article_html=get_detail(article_url)
                if article_html:
                    article_data=parse_detail(article_html)
                    print(article_data)


if __name__ == '__main__':
    main()