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
import numpy as np


class LianjiaershoubjSpider(CrawlSpider):
    name = 'fangtianxiashangquancd'
    allowed_domains = ['cd.shop.fang.com']
    start_urls = ['https://cd.shop.fang.com/shou/house/i31/']
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
    
        for link in response.xpath("//dt[@class = 'floatl']//a/@href").extract():

            totallink = 'https://cd.shop.fang.com'+ str(link)
            
            yield scrapy.Request(totallink, callback=self.parse_item)

        
       
        
        '''                    

        URLs = []
        url = 'https://cd.shop.fang.com/shou/house/'
        for i in range(1,101):
            lst = ["d220","c220-d250","c250-d2100","c2100-d2150","c2150-d2200","c2200-d2300","c2300-d2500","c2500-d2800","c2800"]
            for t in range(len(lst)):
                j = random.randint(0,len(lst)-1)
                URLs.append(url + str(lst[j]) + "-i3" + str(i) + "/")
                lst = lst[:j]+lst[j+1:]
        '''
        URLs = []
        url = 'https://cd.shop.fang.com/shou/house/'
        
        lst = ["d220","c220-d250","c250-d2100","c2100-d2150","c2150-d2200","c2200-d2300","c2300-d2500","c2500-d2800","c2800"]
        for t in range(len(lst)):
            j = random.randint(0,len(lst)-1)
            
            for i in range(1,101):
                URLs.append(url + str(lst[j]) + "-i3" + str(i) + "/")
            lst = lst[:j]+lst[j+1:]



        for i in range(len(URLs)):

                #continue
            yield scrapy.Request(URLs[i],callback=self.parse)


    

    def parse_item(self, response):
      
        item = fangtianxia_shangquanItem()
        print(response.url)

        item["titile"] = response.xpath('//h1[@class = "cont_tit"]/text()').extract_first()

        item["location"] = response.xpath('//div[@class = "tel_area"]/p[2]//a/text()').extract()

        num = len(response.xpath('//ul[@class = "clearfix"]//li/b/text()').extract())

        item = {}

        for i in ["zhuanrangfei","rental_price","pay_method","jianzhumianji","shiyongmianji","shengyuzuqi","zhuanrangfangshi",
        "floor","zhuangxiu","building_type","shifoufenge","shihejingying","loupanmingcheng","loupandizhi","miankuan","jinsheni",
        "cenggao"]:
            item[i] = np.nan

        for i in range(1,num+1):

            if response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '转让费':
                item["zhuanrangfei"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '租金':
                item["rental_price"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '支付方式':
                item["pay_method"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '建筑面积':
                item["jianzhumianji"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '使用面积':
                item["shiyongmianji"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '剩余租期':
                item["shengyuzuqi"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '转让方式':
                item["zhuanrangfangshi"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '所在楼层':
                item["floor"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '装修':
                item["zhuangxiu"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '类型':
                item["building_type"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '是否分割':
                item["shifoufenge"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '适合经营':
                item["shihejingying"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '楼盘名称':
                item["loupanmingcheng"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '楼盘地址':
                item["loupandizhi"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '面宽':
                item["miankuan"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '进深':
                item["jinsheni"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

            elif response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/b/text()').extract()[0].replace('\xa0','') == '层高':
                item["cenggao"] = response.xpath('//ul[@class = "clearfix"]/li['+str(i)+']/span/text()').extract_first()

        item["function_list"] = response.xpath('//div[@class = "clearfix"]//dd/text()').extract()


        item["url"] = response.url 




        yield item
