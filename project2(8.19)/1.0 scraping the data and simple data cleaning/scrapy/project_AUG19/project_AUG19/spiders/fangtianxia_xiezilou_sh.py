# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from project_AUG19.items import fangtianxia_xiezilouItem
from scrapy import Selector
from fake_useragent import UserAgent
import re
from scrapy.http import Request
from urllib import parse
import scrapy


class LianjiaershoubjSpider(CrawlSpider):
    name = 'fangtianxiaxieziloush'
    allowed_domains = ['sh.office.fang.com']
    start_urls = ['https://sh.office.fang.com/shou/house/i31/']
    ua = UserAgent()
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36'}

    #rules = [Rule(LinkExtractor(allow=r'cd.lianjia.com/chengjiao/pg'),follow=True),
    #Rule(LinkExtractor(allow=r'chengjiao/\d+'), callback='parse_item', follow=False),
    #Rule(LinkExtractor(allow=r'chengjiao/CD\d+'), callback='parse_item', follow=False),
    #Rule(LinkExtractor(allow=r'chengjiao/CDQY\d+'), callback='parse_item', follow=False),
    
    
    #]
    # Rule(LinkExtractor(allow=r' /content/'), callback='parse_item', follow=False),


    def parse(self, response):
        
        URLs = []
        url = 'https://sh.office.fang.com/shou/house/'
        #lst = ["k260","j260-k2100","j2100-k2150","j2150-k2200","j2200-k2300","j2300-k2500","j2500-k2800","j2800-k21000","j21000-k22000","k22000"]

        jump = 2000

        for i in range(4000,10000,jump):

        

            URLs.append(url + 'j2'+ str(i) + '-' +'j2' +str(i + jump) + "-i31" + "/")


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

            totallink = 'https://sh.office.fang.com'+ str(link)
            
            yield scrapy.Request(totallink, callback=self.parse_item)



    

    def parse_item(self, response):
      
        item = fangtianxia_xiezilouItem()

        print(response.url)

       
        item["url"] = response.url 

        item["titile"] = response.xpath('//h1/text()').extract_first().strip()

        item["total_price_10K"] = response.xpath('//span[@class = "red20b"]/text()').extract_first()

        item["price_perunit"] = response.xpath('//dt[@class = "gray6 zongjia1"]/text()').extract()[2].strip()

        item["jianzhumianji"] = response.xpath('//dd[@class = "gray6"]/span/text()').extract_first()

        item["suozailouceng"] = response.xpath('//div[@class = "inforTxt"]/dl[2]//dd/text()').extract()[1]

        item["zhuangxiu"] = response.xpath('//div[@class = "inforTxt"]/dl[2]//dd/text()').extract()[-3].strip()

        item["building_type"] = response.xpath('//div[@class = "inforTxt"]/dl[2]//dd/text()').extract()[-1].strip()


        cont = response.xpath('//div[@class = "inforTxt"]/dl[2]//span/text()').extract()[3]
        contlst = cont.split('：')
        try:
            item["service_price"] = contlst[1]
        except:
            item["service_price"] = 'null'

        cont2 = response.xpath('//div[@class = "inforTxt"]/dl[2]//span/text()').extract()[5]
        contlst2 = cont2.split('：')
        try:
            item["dengji"] = contlst2[1]
        except:
            item["dengji"] = 'null'


        item["xzl_content"] = ''.join(response.xpath('//*[@id="house_des"]/ul/li/div[2]/div/text()').extract())

        item["loupan_content"] = response.xpath('//*[@id="hsmPro-pos"]/div[2]/dl//span/text()').extract_first()

        cont3 = response.xpath('//p[@class = "gray9"]/span[3]/text()').extract()[0]
        contlst3 = cont3.split('：')

        try:
            item["release_date"] = contlst3[1]
        except:
            item["release_date"] = "null"

        try:
            item["loupandizhi"] = response.xpath('//div[@class = "bread"]/p//text()').extract()
        except:
            item["loupandizhi"] = "null"

    

        








        yield item
