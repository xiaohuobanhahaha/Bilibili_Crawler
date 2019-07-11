# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BilibiliItem(scrapy.Item):
    aid = scrapy.Field()
    videos= scrapy.Field()
    title= scrapy.Field()
    pubdate= scrapy.Field()
    ctime= scrapy.Field()
    desc= scrapy.Field()
    duration= scrapy.Field()
    owner_mid = scrapy.Field()
    owner_name = scrapy.Field()
    view= scrapy.Field()
    danmaku = scrapy.Field()
    reply= scrapy.Field()
    favorite= scrapy.Field()
    coin= scrapy.Field()
    share= scrapy.Field()
    now_rank = scrapy.Field()
    history_rank = scrapy.Field()
    like= scrapy.Field()
    dislike= scrapy.Field()
    dynamic = scrapy.Field()
    cid = scrapy.Field()