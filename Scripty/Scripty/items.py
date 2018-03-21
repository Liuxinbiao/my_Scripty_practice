# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScriptyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text=scrapy.Field()
    author=scrapy.Field()
    tags=scrapy.Field()
    #全部定义成Field这个变量随之定义一个Item，这个Item在爬取完后进行赋值

