# -*- coding: utf-8 -*-

import scrapy
import json
import time
from bilibili.items import BilibiliItem

def Build_Link(np):
    #Link = 'https://api.bilibili.com/x/web-interface/newlist?rid=182&type=0&pn='\
    #       +str(np)+'&ps=50'
    Link = 'https://api.bilibili.com/x/web-interface/newlist?rid=182&type=1&pn=' \
           +str(np)+'&ps=50'
    return Link

class BilibiliLinkSpider(scrapy.Spider):
    name = 'bilibili_link'
    num= 0
    def start_requests(self):
        Link = Build_Link(self.num)
        yield scrapy.Request(url= Link,callback=self.parse,
                             meta={'num':self.num})
    def parse(self, response):
        if response.status == 200:
            text_data = json.loads(response.text)
            num=response.meta['num']
            item = BilibiliItem()
            if text_data['data']['archives']=='':
                pass
            else:
                for i in text_data['data']['archives']:
                    item['aid'] = i['aid']
                    item['videos'] = i['videos']
                    item['title'] = i['title']
                    item['pubdate'] = i['pubdate']
                    item['ctime'] = i['ctime']
                    item['desc']= i['desc']
                    item['duration'] = i['duration']
                    item['owner_mid'] = i['owner']['mid']
                    item['owner_name'] = i['owner']['name']
                    item['view'] = i['stat']['view']
                    item['danmaku'] = i['stat']['danmaku']
                    item['reply'] = i['stat']['reply']
                    item['favorite'] = i['stat']['favorite']
                    item['coin'] = i['stat']['coin']
                    item['share'] = i['stat']['share']
                    item['now_rank'] = i['stat']['now_rank']
                    item['history_rank'] = i['stat']['his_rank']
                    item['like'] = i['stat']['like']
                    item['dislike'] = i['stat']['dislike']
                    item['dynamic']= i['dynamic']
                    try:
                        item['cid'] = i['cid']
                    except:
                        item['cid']='None'
                    yield item
                if text_data['data']['page']['count']>(num*50):
                    num += 1
                    Link = Build_Link(num)
                    time.sleep(0.1)
                    yield scrapy.Request(url=Link, callback=self.parse,
                                         meta={'num': num})
