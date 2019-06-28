# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from project1.items import chinadailyItemLoader,chinadailyenItem
from scrapy import Selector
import re
from scrapy.http import Request
from urllib import parse



class ChinadailyEnSpider(CrawlSpider):
    name = 'chinadailyen'
    allowed_domains = ['www.chinadaily.com.cn']
    start_urls = ['http://www.chinadaily.com.cn']
    headers={'authority': 'www.chinadaily.com.cn',
    'method': 'GET',
	'path': '/a/201906/25/WS5d11c6b7a3103dbf1432a1e8.html',
	'scheme': 'https',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
	'cache-control': 'max-age=0',
	'cookie': '7NSx_98ef_saltkey=Ia21ZBnR; 7NSx_98ef_lastvisit=1560825038; 7NSx_98ef_lastact=1561454806%09api.php%09chinadaily',
	'if-modified-since': 'Tue, 25 Jun 2019 07:07:32 GMT',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    year_list = tuple()
    for i in range(2000,2017):
        year_list += (str(i),)
    rules = [Rule(LinkExtractor(allow=r'/a/.*'), callback='parse_item', follow=True),
    Rule(LinkExtractor(allow=r'www.chinadaily.com.cn/',deny=year_list), follow=True),
   ]
        # Rule(LinkExtractor(allow=r' /content/'), callback='parse_item', follow=False),


    

    def parse_item(self, response):
      
        item = chinadailyenItem()
        print(response.url)

        s = response.xpath('//*[@class="info_l"]/text()').extract()[0].strip()
        s1 = s.split('Updated:')

        #getting the publishtime
        item["publishtime"] = s1[1].strip()
        #item_loader.add_xpath("publishtime", "//*[@class='fenx']/div[2]/text()")

        #getting the title
        item["title"] = response.xpath('//h1/text()').extract_first().strip()
        #item_loader.add_xpath("title", "//*[@class='dabiaoti']/text()")

        #getting the source
        item["source"] = s1[0].replace(" |\n","").strip()
        #item_loader.add_xpath("source", "//*[@class='fenx']/div[1]/text()")

        #getting the conetent
        content_list = response.xpath('//*[@id="Content"]/p/text()').extract()
        item["content"] = " ".join(content_list)
        #item_loader.add_xpath("content", '//*[@id="Content"]/text()')

        #getting the column
        item["column_1"] = response.xpath('//*[@id="bread-nav1"]/li[2]/a/text()').extract_first().strip()
        #item_loader.add_xpath("column","/html/body/div[2]/div/div[3]/div[2]/a[1]/text()")


        item["column_2"] = response.xpath('//*[@id="bread-nav1"]/li[3]/a/text()').extract_first().strip()        

        #getting the url
        item["url"] = response.url 



        #bbs_item = item_loader.load_item()
        yield item
