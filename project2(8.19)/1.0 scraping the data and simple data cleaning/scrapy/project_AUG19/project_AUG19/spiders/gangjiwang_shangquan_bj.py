# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
import random
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from project_AUG19.items import gangjiwang_shangpuItem
from scrapy import Selector
from fake_useragent import UserAgent
import re
from scrapy.http import Request
from urllib import parse
import scrapy
from multiprocessing import Pool
import urllib.request
import urllib.parse

class LianjiaershoubjSpider(CrawlSpider):
    name = 'ganjiwangshangquanbj'
    allowed_domains = ['cd.ganji.com']
    start_urls = ['http://cd.ganji.com/shangpucs/pn1/']
    ua = UserAgent()
    headers={'User-Agent':str(ua.random)
    
        }

    #rules = [Rule(LinkExtractor(allow=r'cd.lianjia.com/chengjiao/pg'),follow=True),
    #Rule(LinkExtractor(allow=r'chengjiao/\d+'), callback='parse_item', follow=False),
    #Rule(LinkExtractor(allow=r'chengjiao/CD\d+'), callback='parse_item', follow=False),
    #Rule(LinkExtractor(allow=r'chengjiao/CDQY\d+'), callback='parse_item', follow=False),
    
#proxy_pool = [{'HTTP':'111.155.116.215:8123'}]
    
    #]
    # Rule(LinkExtractor(allow=r' /content/'), callback='parse_item', follow=False),

   
    # 获取IP的API接口


    

    def parse(self, response):


    
        for link in response.xpath('//div[@class="f-list js-tips-list"]//dd[@class="dd-item title"]/a/@href').extract()[-35:]:

            fulllink = "http:" +str(link)




            #proxy_addr = random.choice([{'HTTP':'180.118.86.86:9000'},{'HTTP':'61.183.233.6:54896'},{'HTTP':'219.159.38.209:56210'},{'HTTP':'112.85.150.234:9999'},{'HTTP':'58.22.214.124:9000'}])

                                                                                                        

            yield scrapy.Request(fulllink, callback=self.parse_item,)

        
        url = 'http://cd.ganji.com/shangpucs/'

        URLs = []

        for i in range(1,71):
            
            URLs.append(url + "pn" + str(i) + "/")


        for i in range(len(URLs)):


                #continue
            yield scrapy.Request(URLs[i],callback=self.parse)


        '//ul[@class="er-list-two f-clear" ]/li/span[2]'
       
        


    

    def parse_item(self, response):
      
        item = gangjiwang_shangpuItem()
        print(response.url)

        item["titile"] = response.xpath('//p[@class = "card-title"]/i/text()').extract_first()

        try:
            item["location"] = response.xpath('//ul[@class="er-list-two f-clear" ]/li/span[2]/text()').extract_first().strip()
        except:
            item["location"] = 'null'

        try:
            item["total_price_10K"] = response.xpath('//*[@class = "er-card-pay"]/div/span[1]/text()').extract_first()
        except:
            item["total_price_10K"] = 'null'

        item["service_price"] = 'null'

        item["jianzhumianji"] = response.xpath('//*[@class = "er-list f-clear"]/li[1]/span[2]/text()').extract_first()

        item["floor"] = response.xpath('//*[@class = "er-list f-clear"]/li[7]/span[2]/text()').extract_first().strip()

        item["zhuangxiu"] = 'null'

        item["shangpu_type"] = response.xpath('//*[@class = "er-list f-clear"]/li[6]/span[2]/text()').extract_first()

        item["shifoufenge"] = 'null'

        item["shihejingying"] = 'null'

        item["loupanmingcheng"] = 'null'

        item["loupandizhi"] = response.xpath('//*[@class = "er-list f-clear"]/li[9]/span[2]/text()').extract_first().strip()

        item["miankuan"] = response.xpath('//*[@class = "er-list f-clear"]/li[2]/span[2]/text()').extract_first()

        item["jinshen"] = response.xpath('//*[@class = "er-list f-clear"]/li[3]/span[2]/text()').extract_first()

        item["cenggao"] = response.xpath('//*[@class = "er-list f-clear"]/li[5]/span[2]/text()').extract_first()

        lst = []
        for i in [i.strip() for i in response.xpath('//*[@id="js-house-peizhi"]/ul//p/text()').extract()]:
            if len(i)>=1:
                lst.append(i)
        
        lstfunc = []
        count = -1
        for j in response.xpath('//*[@id="js-house-peizhi"]/ul//@src').extract():
            count += 1

            if 'gray' not in j.lower():
                lstfunc.append(lst[count])



        item["function_list"] = lstfunc

        try:
            item["release_date"] = response.xpath('//*[@class="card-status-left f-fl"]//li/text()').extract_first()
        except:
            item["release_date"] = "null"






        #getting the url
        item["url"] = response.url 




        yield item


'''
    # 获取IP的API接口
apiUrl = "http://api.ip.data5u.com/dynamic/get.html?order=" + order;

f = urllib.request.urlopen(apiUrl)
f.read().decode('utf-8')

'''
