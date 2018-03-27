# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Item,Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id=Field()
    name=Field()
    avatar_url=Field()
    answer_count=Field()
    articles_count=Field()
    employments=Field()
    follower_count=Field()
    gender=Field()
    headline=Field()
    is_advertiser=Field()
    is_blocking=Field()
    is_followed=Field()
    is_following=Field()
    url=Field()
    url_token=Field()
    is_end=Field()
    is_start=Field()


