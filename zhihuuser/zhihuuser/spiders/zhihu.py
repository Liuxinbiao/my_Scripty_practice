# -*- coding: utf-8 -*-
import json
from scrapy import Spider,Request
from zhihuuser.items import UserItem
class ZhihuSpider(Spider):
    #follow是user所关注的人
    #follower是关注user的人

    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    start_user='excited-vczh'
    #这是某个人的详细信息和关注信息的
    user_url='https://www.zhihu.com/api/v4/members/{user}?include={include}'#用户的URL #user_query就是include的内容
    user_query='allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    #下面是user所关注详细信息和关注信息
    follow_url='https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follow_query='data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    #下面是user的粉丝
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        """第一个url是个人信息，第二个url是用户的关注信息"""
        #url='https://www.zhihu.com/api/v4/members/chen-piao-piao-31?include=allow_message%2Cis_followed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
        #url='https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20'
        #用户的详细信息
        yield Request(self.user_url.format(user=self.start_user,include=self.user_query),self.parse_user)#parse_user是回掉函数作用是：解析用户的方法
        yield Request(self.follow_url.format(user=self.start_user,include=self.follow_query, offset=0,limit=20),callback=self.parse_follows)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0, limit=20),callback=self.parse_followers)

    def parse_user(self, response):
        """用户的详细信息（第一个与关注列表）"""
        result=json.loads(response.text)
        item=UserItem()
        for field in item.fields:#一次对field进行赋值
            if field in result.keys():#如果field是result的键名的话就进行赋值
                item[field]=result.get(field)
        yield item  #yield item 把item成功获取，下一步就进行parse_follows进行下一步进行

        yield Request(self.follow_url.format(user=result.get('url=token'),include=self.follow_query,limit=20,offset=0),self.parse_follows)
        yield Request(self.followers_url.format(user=result.get('url=token'), include=self.followers_query, limit=20, offset=0),self.parse_followers)

    def parse_follows(self, response):
        """这个函数目的是处理关注列表的（user所关注的"""
        results=json.loads(response.text)#把result转换成json格式

        if 'data' in results.keys():
            for result in results.get('data'):#拿到关注列表的信息并进行遍历
                yield Request(self.user_url.format(user=result.get('url_token'),include=self.user_query),self.parse_user)#把关注列表的url_token构造一个新的请求

        if 'paging' in results.keys() and results.get('paging').get('is_end')==False:#进行翻页操作
            next_page=results.get('paging').get('next')
            yield Request(next_page,self.parse_follows)#回掉函数就是回掉自己

    def parse_followers(self, response):
        """这个函数目的是处理关注列表的（粉丝）"""
        results = json.loads(response.text)  # 把result转换成json格式

        if 'data' in results.keys():
            for result in results.get('data'):  # 拿到关注列表的信息并进行遍历
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)  # 把关注列表的url_token构造一个新的请求

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:  # 进行翻页操作
            next_page = results.get('paging').get('next')
            yield Request(next_page, self.parse_followers)  # 回掉函数就是回掉自己


