# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from project1.items import chinadailyItemLoader,chinadailyItem
from scrapy import Selector
import re
from scrapy.http import Request
from urllib import parse



class ChinadailySpider(CrawlSpider):
    name = 'chinadaily'
    allowed_domains = ['chinadaily.com.cn']
    start_urls = ['https://cn.chinadaily.com.cn']
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'china.chinadaily.com.cn',
        'If-Modified-Since': 'Mon, 24 Jun 2019 22:08:00 GMT',
        'Referer':'http://cn.chinadaily.com.cn/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36'
        }
               
    rules = [Rule(LinkExtractor(allow=r'/a/.*'), callback='parse_item', follow=False),
    Rule(LinkExtractor(allow=r'cn.chinadaily.com.cn/',deny=("www","content")), follow=True),
   ]
        # Rule(LinkExtractor(allow=r' /content/'), callback='parse_item', follow=False),


    

    def parse_item(self, response):
      
        item = chinadailyItem()
        print(response.url)

        #getting the publishtime
        item["publishtime"] = response.xpath("//*[@class='fenx']/div[2]/text()").extract()
        #item_loader.add_xpath("publishtime", "//*[@class='fenx']/div[2]/text()")

        #getting the title
        item["title"] = response.xpath("//*[@class='dabiaoti']/text()").extract_first().strip()
        #item_loader.add_xpath("title", "//*[@class='dabiaoti']/text()")

        #getting the source
        item["source"] = response.xpath("//*[@class='fenx']/div[1]/text()").extract_first().strip()
        #item_loader.add_xpath("source", "//*[@class='fenx']/div[1]/text()")

        #getting the conetent
        content_list = response.xpath('//*[@class="article"]/p/text()').extract()
        item["content"] = " ".join(content_list)
        #item_loader.add_xpath("content", '//*[@id="Content"]/text()')

        #getting the column1
    
        item["column_1"] = response.xpath('//*[@class="da-bre"]/a[1]/text()').extract_first().strip()
        #item_loader.add_xpath("column","/html/body/div[2]/div/div[3]/div[2]/a[1]/text()")

        #getting the column2
        item["column_2"] = response.xpath('//*[@class="da-bre"]/a[2]/text()').extract_first().strip().split(">")[-1].strip()

        #getting the url
        item["url"] = response.url 




        #bbs_item = item_loader.load_item()
        yield item
        #yield bbs_item

'''
    def md5(self.url):
    	import hashlib
    	obj = hashlib.md5()
    	obj.update(bytes)
    	return obj.hexdigest()

'''

        
