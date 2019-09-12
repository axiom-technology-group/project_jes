# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from project_AUG19.items import lianjia_ershoufangrentItemloc
from scrapy import Selector
import re
from scrapy.http import Request
from urllib import parse
import scrapy
import pandas as pd

class LianjiaershouSpider(CrawlSpider):
    name = 'lianjiaershourentbjloc'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['https://bj.lianjia.com/zufang/pg1']
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

    
    
    def parse(self, response):
        
        lst = ['brp55000']
        jump = 500
        for j in range(0,55000,jump):
 
            lst.append('brp'+ str(j) + 'erp' + str(j+jump))


        urlstring = 'https://bj.lianjia.com/zufang/pg1' 

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



        locationlinkraw = response.xpath("//div[@class = 'content__list']//p[@class='content__list--item--title twoline']//a[@target='_blank']//@href").extract()
        locationlink = []
        for link in locationlinkraw:
            locationlink.append('https://bj.lianjia.com' + link)

        print(locationlink)


        for j in range(0,len(locationlink)):

            #location = locationlst[j]

            item = lianjia_ershoufangrentItemloc()

            item["location"] = locationlst[j]

            item["url"] = locationlink[j] 

            yield item

            
            #yield scrapy.Request(locationlink[j], callback=self.parse_item)

    

    #def parse_item(self, response):
      
        #item = lianjia_ershoufangrentItem()

        #item["location"] = 'j'

        
        #标题
        #item["headline"] = response.xpath('//div[@class = "wrapper"]/text()').extract_first()

        #房屋位置
        #item["house_location"] = response.xpath('/html/body/section[1]/div[1]//a/text()').extract()

        #房屋成交价
        #item["house_price_tenK"] = response.xpath('//*[@class = "dealTotalPrice"]/i/text()').extract_first()

        #房屋成交价每平米
        #item["house_price_perunit"] = response.xpath('//*[@class = "price"]/b/text()').extract_first()

        #房屋售出日期
        #item["sell_date"] = response.xpath('//div[@class = "wrapper"]/span/text()').extract_first()

        #房屋网站的访问量
        #item["house_website_traffic"] = response.xpath('//div[@class ="msg"]/span[6]/label/text()').extract_first()

        #房屋户型
        #item["Housing_type"] = response.xpath('//div[@class = "content"]/ul/li/text()').extract_first().strip()

        #所在楼层
        #item["floor"] = response.xpath('//div[@class = "content"]/ul/li[2]/text()').extract_first().strip()

        #建筑面积
        #item["Built_up_area"] = response.xpath('//div[@class = "content"]/ul/li[3]/text()').extract_first().strip()

        #户型结构
        #item["Huxing_structure"] = response.xpath('//div[@class = "content"]/ul/li[4]/text()').extract_first().strip()

        #套内面积
        #item["Cover_area"] = response.xpath('//div[@class = "content"]/ul/li[5]/text()').extract_first().strip()

        #建筑类型
        #item["Architectural_Types"] = response.xpath('//div[@class = "content"]/ul/li[6]/text()').extract_first().strip()

        #房屋朝向
        #item["House_orientation"] = response.xpath('//div[@class = "content"]/ul/li[7]/text()').extract_first().strip()

        #建成年代
        #item["Completion_date"] = response.xpath('//div[@class = "content"]/ul/li[8]/text()').extract_first().strip()

        #装修情况
        #item["Decoration"] = response.xpath('//div[@class = "content"]/ul/li[9]/text()').extract_first().strip()

        #建筑结构
        #item["building_structure"] = response.xpath('//div[@class = "content"]/ul/li[10]/text()').extract_first().strip()

        #供暖方式
        #item["Heating_mode"] = response.xpath('//div[@class = "content"]/ul/li[11]/text()').extract_first().strip()

        #鹈鹕比例
        #item["household_ratio_perstair"] = response.xpath('//div[@class = "content"]/ul/li[12]/text()').extract_first().strip()

        #配备电梯
        #item["Equipped_with_elevators"] = response.xpath('//div[@class = "content"]/ul/li[14]/text()').extract_first().strip()

        #产权年限
        #item["Years_of_Property_Rights"] = response.xpath('//div[@class = "content"]/ul/li[13]/text()').extract_first().strip()

        #房屋年限
        #item["Years_of_housing"] = response.xpath('//div[@class = "transaction"]/div/ul/li[5]/text()').extract_first().strip()

        #交易权属
        #item["Transaction_Ownership"] = response.xpath('//div[@class = "transaction"]/div/ul/li[2]/text()').extract_first().strip()

        #房屋用途
        #item["House_use"] = response.xpath('//div[@class = "transaction"]/div/ul/li[4]/text()').extract_first().strip()

        #房权所属
        #item["Ownership_of_housing"] = response.xpath('//div[@class = "transaction"]/div/ul/li[6]/text()').extract_first().strip()      

        #getting the url
        #item["url"] = response.url 


        #yield item
