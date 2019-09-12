# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from project_AUG19.items import fangtianxia_shangquanItem
from scrapy import Selector
from fake_useragent import UserAgent
import re
from scrapy.http import Request
from urllib import parse
import scrapy
import random


class LianjiaershoubjSpider(CrawlSpider):
    name = 'fangtianxiashangquansz'
    allowed_domains = ['sz.shop.fang.com']
    start_urls = ['https://sz.shop.fang.com/shou/house/i31/']
    ua = UserAgent()
    headers={'User-Agent':str(ua.random)
    
        }

    #rules = [Rule(LinkExtractor(allow=r'cd.lianjia.com/chengjiao/pg'),follow=True),
    #Rule(LinkExtractor(allow=r'chengjiao/\d+'), callback='parse_item', follow=False),
    #Rule(LinkExtractor(allow=r'chengjiao/CD\d+'), callback='parse_item', follow=False),
    #Rule(LinkExtractor(allow=r'chengjiao/CDQY\d+'), callback='parse_item', follow=False),
    
    
    #]
    # Rule(LinkExtractor(allow=r' /content/'), callback='parse_item', follow=False),

    

    def parse(self, response):

        lst = ["d250",]
        #lst = ["c50-d2100"]
        #lst = ["c2100-d2150",]
        #lst = ["c2200-d2300",]
        #lst = ["c2300-d2500",]
        #lst = ["c2500-d2800",]
        #lst = ["c2800-d21000",]
        #lst = ["c21000"]

        urlstring = 'https://sz.shop.fang.com/shou/house/' 

        URLs = []
        for i in lst:
            URLs.append(urlstring + i + "-i31/")

        for url in URLs:
            yield scrapy.Request(url,callback=self.parse_big)



    def parse_big(self, response):
        url = str(response.url)
        #string1 = url.split('i3')[0]
        string1 = url.split('i3')[0][:-1]

        try:
            num = int(response.xpath('//*[@id="PageControl1_hlk_last"]/@href').extract_first().split('i3')[1][:-1])

            totalURLs = []

            for i in range(1,num+1):

                totalURLs.append(string1 + '-i3' + str(i) + "/")        


            for i in range(len(totalURLs)):

                    #continue
                yield scrapy.Request(totalURLs[i],callback=self.parse_small)

        except:
            yield scrapy.Request(url, callback=self.parse_small)




    def parse_small(self, response):
        for link in response.xpath("//dt[@class = 'floatl']//a/@href").extract():

            totallink = 'https://sz.shop.fang.com'+ str(link)
            
            yield scrapy.Request(totallink, callback=self.parse_item)
       
        
    

    def parse_item(self, response):
      
        item = fangtianxia_shangquanItem()
        print(response.url)

        item["titile"] = response.xpath('//h1[@class = "cont_tit"]/text()').extract_first()

        item["location"] = response.xpath('//div[@class = "tel_area"]/p[2]//a/text()').extract()

        item["total_price"] = response.xpath('//ul[@class = "clearfix"]/li[1]/span/text()').extract_first()

        item["service_price"] = response.xpath('//ul[@class = "clearfix"]/li[2]/span/text()').extract_first()

        item["jianzhumianji"] = response.xpath('//ul[@class = "clearfix"]/li[3]/span/text()').extract_first()

        item["floor"] = response.xpath('//ul[@class = "clearfix"]/li[4]/span/text()').extract_first()

        item["loupandizhi"] = response.xpath('//ul[@class = "clearfix"]/li[10]/span/text()').extract_first()

        


        

        item["function_list"] = response.xpath('//div[@class = "clearfix"]//dd/text()').extract()

        item["release_date"] = response.xpath('//span[@class = "time"]/text()').extract()[1]

        if '米' in response.xpath('//ul[@class = "clearfix"]/li[11]/span/text()').extract_first():

            item["miankuan"] = response.xpath('//ul[@class = "clearfix"]/li[11]/span/text()').extract_first()

            item["shifoufenge"] = response.xpath('//ul[@class = "clearfix"]/li[7]/span/text()').extract_first()

            item["shihejingying"] = response.xpath('//ul[@class = "clearfix"]/li[8]/span/text()').extract_first()

            item["loupanmingcheng"] = response.xpath('//ul[@class = "clearfix"]/li[9]/span/text()').extract_first()

            item["shangpu_type"] = response.xpath('//ul[@class = "clearfix"]/li[6]/span/text()').extract_first()

            item["zhuangxiu"] = response.xpath('//ul[@class = "clearfix"]/li[5]/span/text()').extract_first()

            item["jinshen"] = response.xpath('//ul[@class = "clearfix"]/li[12]/span/text()').extract_first()

            item["cenggao"] = response.xpath('//ul[@class = "clearfix"]/li[13]/span/text()').extract_first()

        else:
            item["miankuan"] = response.xpath('//ul[@class = "clearfix"]/li[12]/span/text()').extract_first()

            item["shifoufenge"] = response.xpath('//ul[@class = "clearfix"]/li[8]/span/text()').extract_first()

            item["shihejingying"] = response.xpath('//ul[@class = "clearfix"]/li[9]/span/text()').extract_first()

            item["loupanmingcheng"] = response.xpath('//ul[@class = "clearfix"]/li[10]/span/text()').extract_first()

            item["shangpu_type"] = response.xpath('//ul[@class = "clearfix"]/li[7]/span/text()').extract_first()

            item["zhuangxiu"] = response.xpath('//ul[@class = "clearfix"]/li[6]/span/text()').extract_first()

            item["jinshen"] = response.xpath('//ul[@class = "clearfix"]/li[13]/span/text()').extract_first()

            item["cenggao"] = response.xpath('//ul[@class = "clearfix"]/li[14]/span/text()').extract_first()






        #getting the url
        item["url"] = response.url 




        yield item
