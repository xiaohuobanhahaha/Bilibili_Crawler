# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class BilibiliPipeline(object):
    def open_spider(self,spider):
        self.out = open("Bilibili_Info.csv", "w")
        self.writer = csv.writer(self.out)
        self.writer.writerow(['aid', 'videos', 'title', 'pubdate',
                              'ctime', 'desc', 'duration', 'owner_mid',
                              'owner_name','view', 'danmaku', 'reply',
                              'favorite', 'coin','share', 'now_rank',
                              'history_rank', 'like','dislike','dynamic',
                              'cid'])
    def process_item(self, item, spider):
        self.writer.writerow([item['aid'], item['videos'], item['title'], item['pubdate'],
                              item['ctime'], item['desc'], item['duration'], item['owner_mid'],
                              item['owner_name'],item['view'], item['danmaku'], item['reply'],
                              item['favorite'], item['coin'],item['share'], item['now_rank'],
                              item['history_rank'], item['like'],item['dislike'], item['dynamic'],
                              item['cid']])
        return item
    def close_spider(self,spider):
        self.out.close()