# -*- coding: utf-8 -*-


import scrapy
import sys

from scrapy.exceptions import DropItem

sys.path.append(r'C:\Users\刘新彪\Scripty')
sys.path.append(r'C:\Users\刘新彪\Scripty\Scripty')
from items import ScriptyItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes=response.css('.quote')#用quote来接受这个区块（所有内容）
        for quote in quotes:#下面是把区块进行进一步分解。。/迭代关系
            item=ScriptyItem()
            text=quote.css('.text::text').extract_first()#scrapy独有的。（::）是把选择器选择的对象以文本格式输出   #这是只把选择器里的第一个输出出来
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()#此处的tags下标签数是含有多个。这跟之前的区别就是把所有都打印出来，而前面的就是只打印一个
            item['text']=text
            item['author']=author
            item['tags']=tags
            yield item#把item生成出来

            next=response.css('.pager .next a::attr(href)').extract_first()#翻页的作用
            url=response.urljoin(next)#生成一个完整的url
            yield  scrapy.Request(url=url, callback=self.parse)#callback是回掉函数，递归调用自己

class TextPipeline(object):
    def __init__(self):
        self.limit=50
        #如果爬取结果长度大于50就把后面换成省略号
    def process_item(self, item, spider):
        if item('text'):
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip()+'...'
                return item
        else:
            return  DropItem('Missing Text')







