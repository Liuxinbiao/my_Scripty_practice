# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem




class TextPipeline(object):
    def __init__(self):
        self.limit=50
        #如果爬取结果长度大于50就把后面换成省略号
    # def process_item(self, item, spider):
    #     if item('text'):
    #         if len(item['text']) > self.limit:
    #             item['text'] = item['text'][0:self.limit].rstrip()+'...'
    #             return item
    #     else:
    #         return  DropItem('Missing Text')


class MongoPipeline(object):
    def __init__(self,mongo_url,mongo_db):
        self.mongo_url=mongo_url
        self.mongo_db=mongo_db
    @classmethod#classMehtod是一个类方法
    def from_crawler(cls,crawler):
        return cls(#构造函数的调用
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB')
            #把mongo_url和mongo_db当成参数传给MongoPipeline
        )
    def open_spider(self,spider):#这是在爬虫启动时要进行的一个操作
        self.client=pymongo.MongoClient(self.mongo_url)
        self.db=self.client[self.mongo_db]
    def process_item(self,item,spider):
        """把item储存到MONGODB中"""
        self.db['quote'].insert(dict(item))
        return item
    def close_spider(self,spider):
        """把MONGODB关闭"""
        self.client.close()
