# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from project_AUG19.items import fangtianxia_xiezilourentItem
from scrapy import Selector
from fake_useragent import UserAgent
import re
from scrapy.http import Request
from urllib import parse
import scrapy
import numpy as np


class LianjiaershoubjSpider(CrawlSpider):
    name = 'fangtianxiaxiezilougzrent'
    allowed_domains = ['gz.office.fang.com']
    start_urls = ['https://gz.office.fang.com/zu/house/i31/']
    ua = UserAgent()
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36'}

    #rules = [Rule(LinkExtractor(allow=r'gz.lianjia.com/chengjiao/pg'),follow=True),
    #Rule(LinkExtractor(allow=r'chengjiao/\d+'), callback='parse_item', follow=False),
    #Rule(LinkExtractor(allow=r'chengjiao/gz\d+'), callback='parse_item', follow=False),
    #Rule(LinkExtractor(allow=r'chengjiao/gzQY\d+'), callback='parse_item', follow=False),
    
    
    #]
    # Rule(LinkExtractor(allow=r' /content/'), callback='parse_item', follow=False),


    def parse(self, response):
        
        URLs = ['https://gz.office.fang.com/zu/house/c1150-i31/']
        url = 'https://gz.office.fang.com/zu/house/'
        #lst = ["k260","j260-k2100","j2100-k2150","j2150-k2200","j2200-k2300","j2300-k2500","j2500-k2800","j2800-k21000","j21000-k22000","k22000"]

        jump = 10

        #c12-d13-i32

        for i in range(0,150,jump):

        

            URLs.append(url + 'c1'+ str(i) + '-' +'d1' +str(i + jump) + "-i31" + "/")


        for url in URLs:
            yield scrapy.Request(url,callback=self.parse_big)


 
    def parse_big(self, response):
        url = str(response.url)
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
    
        for link in response.xpath("//p[@class = 'title']//a/@href").extract():

            totallink = 'https://gz.office.fang.com'+ str(link)
            
            yield scrapy.Request(totallink, callback=self.parse_item)



    

    def parse_item(self, response):
      
        item = fangtianxia_xiezilourentItem()

        print(response.url)

       
        item["url"] = response.url 

        item["titile"] = response.xpath('//h1/text()').extract_first().strip()

        item["total_price_10K_permonth"] = response.xpath('//span[@class = "red20b"]/text()').extract_first()


        item["price_perunit"] = response.xpath('//*[@style="font-size: 16px; color: #f30; font-family: Arial; padding-left: 62px;"]//text()').extract_first()

        
        item["chuzumianji"] = response.xpath('//dd[@class = "gray6"]/span/text()').extract_first().split('：')[-1]


        

        
        num = len(response.xpath('//div[@class = "inforTxt"]/dl[2]//dd').extract())
        lst = response.xpath('//div[@class = "inforTxt"]/dl[2]//dd//text()').extract()
        lst1 = []

        for i in lst:
            i = i.strip()
            i = i.replace('\r\n','')
            i = i.replace(' ','')
            i = i.replace('：','')
            if len(i) > 1:
                lst1.append(i)

        temp = ['floor','service_price','xiezilou_level','zhuangxiu','building_type','building_year']

        for i in temp:
            item[i] = np.nan

        for i in lst1:
            
            if '共' in i:
                item['floor'] = i

            elif '平米·月' in i:
                item['service_price'] = i

            elif '级' in i:
                item['xiezilou_level'] = i[1:]

            elif '装' in i or '毛' in i:
                item['zhuangxiu'] = i

            elif '楼' in i:
                item['building_type'] = i

            elif '年' in i:
                item['building_year'] = i



        lst_loc = response.xpath('//div[@class = "bread"]/p//a/text()').extract()[3:]

        item['loupandizhi'] = lst_loc

        item["xzl_content"] = ''.join(response.xpath('//*[@class="fyms_modify"]//text()').extract())

        item["loupan_content"] = ''.join(response.xpath('//*[@class="leftBox"]//dl[@class="mt10"]//text()').extract())


        temp = response.xpath('//*[@class="title"]//span[@class = "mr10"]/text()').extract()[-1]

        temp = temp.split('发布时间：')[-1].replace('(','')

        item['release_date'] = temp




        yield item
