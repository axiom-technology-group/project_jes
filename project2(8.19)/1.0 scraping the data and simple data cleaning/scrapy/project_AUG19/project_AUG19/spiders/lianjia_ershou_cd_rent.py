# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from project_AUG19.items import lianjia_ershoufangrentItem
from scrapy import Selector
import re
from scrapy.http import Request
from urllib import parse
import scrapy
import pandas as pd

class LianjiaershouSpider(CrawlSpider):
    name = 'lianjiaershourentcd'
    allowed_domains = ['cd.lianjia.com']
    start_urls = ['https://cd.lianjia.com/zufang/pg1']
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

    
    '''
    def parse(self, response):



        
        lst = []
        for i in range(1,6):
            #change this value down below!!!!!!!!!!!!!!!!!!!!!!!

            jump = 30
            for j in range(450,1500,jump):
            #for j in range(96,98,jump):
                #lst.append('lc'+str(i)+'ba'+str(j)+'ea'+str(j+jump))

                for k in range(1,3):
                    lst.append('ie'+str(k)+'lc'+str(i)+'ba'+str(j)+'ea'+str(j+jump))

        urlstring = 'https://bj.lianjia.com/zufang/pg1' 

        URLs = ['',]
        #for i in lst:
            #URLs.append(urlstring + i)
        for url in URLs:
            yield scrapy.Request(url,callback=self.parse_big)


    def parse_big(self, response):
        url = str(response.url)
        string1 = url.split('pg1')[0]
        string2 = url.split('pg1')[1]

        num = int(response.xpath('//div[@class="total fl"]/span/text()').extract_first().strip())//30 +1

        totalURLs = []

        for i in range(1,num+1):

            totalURLs.append(string1 + 'pg' + str(i) + string2)        


        for i in range(len(totalURLs)):

                #continue
            yield scrapy.Request(totalURLs[i],callback=self.parse_small)
    '''


    def parse(self, response):


        lst = ['brp55000']
        jump = 100
        for j in range(0,55000,jump):
 
            lst.append('brp'+ str(j) + 'erp' + str(j+jump))


        urlstring = 'https://cd.lianjia.com/zufang/pg1' 

        URLs = []
        for i in lst:
            URLs.append(urlstring + i)
        for url in URLs:
            yield scrapy.Request(url,callback=self.parse_big)


    def parse_big(self, response):
        
        url = str(response.url)
        string1 = url.split('pg1')[0]
        string2 = url.split('pg1')[1]

        num = int(response.xpath('//*[@id="content"]/div[1]/p/span[1]/text()').extract_first().strip())//30 +1

        totalURLs = []

        for i in range(1,num+1):

            totalURLs.append(string1 + 'pg' + str(i) + string2)        


        for i in range(len(totalURLs)):

                #continue
            yield scrapy.Request(totalURLs[i],callback=self.parse_small)




    def parse_small(self, response):


        locationlstraw = response.xpath("//*[@class = 'content__list--item--des']//a/text()").extract()
        locationlst = []
        for i in range(0,len(locationlstraw),3):
            
            string = locationlstraw[i] + ',' + locationlstraw[i+1]+ ',' + locationlstraw[i+2]
            
            locationlst.append(string)

        print(locationlst)



        placelinkraw = response.xpath("//div[@class = 'content__list']//p[@class='content__list--item--title twoline']//a[@target='_blank']//@href").extract()
        placelink = []
        for link in placelinkraw:
            placelink.append('https://cd.lianjia.com' + link)

        print(placelink)


        for j in range(0,len(placelink)):


            yield scrapy.Request(placelink[j], callback=self.parse_item)

    

    def parse_item(self, response):
      
        item = lianjia_ershoufangrentItem()

        item['sell_date'] = response.xpath('//*[@class="content__subtitle"]/text()').extract()[1].replace('房源上架时间','').strip()

        
        #标题
        item["headline"] = response.xpath('//p[@class = "content__title"]/text()').extract_first()

        item["house_website_traffic"]= response.xpath('//*[@class="content__subtitle"]/i/text()').extract()[0].replace('人浏览','').strip()


        #房屋成交价
        item["rental_pirce"] = response.xpath('//*[@class="content__aside--title"]/span/text()').extract_first()

        item["tags"] = response.xpath('//*[@class="content__aside--tags"]//i/text()').extract()

        lst = response.xpath('//*[@class="content__article__table"]//span/text()').extract()

        item["chuzufangshi"] = lst[0] 

        item["Huxing_structure"] = lst[1]

        item["Built_up_area"] = lst[2]

        item["chaoxiang"] = lst[3]

        lst2 = response.xpath('//*[@class="fl oneline"]/text()').extract()

        for i in lst2:

            temp = i.split('：')
            if temp[0] == '入住':
                item['ruzhu'] = temp[1]
            elif temp[0] == '租期':
                item['rental_duration'] = temp[1]
            elif temp[0] == '看房':
                item['visiting_time'] = temp[1]
            elif temp[0] == '楼层':
                item['floor'] = temp[1]
            elif temp[0] == '电梯':
                item['have_elvator'] = temp[1]
            elif temp[0] == '车位':
                item['have_parkingspace'] = temp[1]
            elif temp[0] == '用水':
                item['yongshui'] = temp[1]
            elif temp[0] == '用电':
                item['yongdian'] = temp[1]
            elif temp[0] == '燃气':
                item['ranqi'] = temp[1]
            elif temp[0] == '采暖':
                item['warming_system'] = temp[1]


        lst3 = []
        for j in response.xpath('//*[@class="content__article__info2"]//*[@class="fl oneline  "]/text()').extract():
            if len(j.strip())>=1:
                lst3.append(j.strip())

        item["function_list"] = lst3
   

        #getting the url
        item["url"] = response.url 


        yield item
