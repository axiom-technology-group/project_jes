# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from selenium import webdriver
from project_AUG19.items import fangtianxia_shangquanrentItem
from scrapy import Selector
from fake_useragent import UserAgent
import re
from scrapy.http import Request
from urllib import parse
import scrapy
import random
import numpy as np


class LianjiaershoubjSpider(CrawlSpider):
    name = 'fangtianxiashangquangzrent'
    allowed_domains = ['gz.shop.fang.com']
    start_urls = ['https://gz.shop.fang.com/zu/house/i31/']
    ua = UserAgent()
    headers={'User-Agent':str(ua.random)
    
        }

    def parse(self, response):

        lst = ["d220","c20-d2100","c2100-d2150","c2200-d2300","c2300-d2500","c2500-d2800","c2800-d21000","c21000"]

        urlstring = 'https://gz.shop.fang.com/zu/house/' 

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

            totallink = 'https://gz.shop.fang.com'+ str(link)
            
            yield scrapy.Request(totallink, callback=self.parse_item)
       
        


    

    def parse_item(self, response):
      
        item = fangtianxia_shangquanrentItem()
        print(response.url)

        item["titile"] = response.xpath('//h1[@class = "cont_tit"]/text()').extract_first()

        item["location"] = response.xpath('//div[@class = "tel_area"]/p[2]//a/text()').extract()

        lstbox1 = response.xpath('//ul[@class = "clearfix"]//li/span/text()').extract()
        lstbox2 = response.xpath('//ul[@class = "clearfix"]//li/b/text()').extract()

        item = {}

        for i in ["zhuanrangfei","rental_price","pay_method","jianzhumianji","shiyongmianji","shengyuzuqi","zhuanrangfangshi",
        "floor","zhuangxiu","building_type","shifoufenge","shihejingying","loupanmingcheng","loupandizhi","miankuan","jinshen",
        "cenggao","elvator_number","service_price"]:
            item[i] = np.nan
        num = min(len(lstbox1),len(lstbox2))

        for i in range(0,num):

            if lstbox2[i].replace('\xa0','') == '转让费':
                item["zhuanrangfei"] = lstbox1[i]

            elif  lstbox2[i].replace('\xa0','') == '租金':
                item["rental_price"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '支付方式':
                item["pay_method"] = lstbox1[i]

            elif '建筑面积' in lstbox2[i].replace('\xa0',''):
                item["jianzhumianji"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '使用面积':
                item["shiyongmianji"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '剩余租期':
                item["shengyuzuqi"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '转让方式':
                item["zhuanrangfangshi"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '所在楼层':
                item["floor"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '电梯数量':
                item["elvator_number"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '装修':
                item["zhuangxiu"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '类型':
                item["building_type"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '是否分割':
                item["shifoufenge"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '适合经营':
                item["shihejingying"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '楼盘名称':
                item["loupanmingcheng"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '楼盘地址':
                item["loupandizhi"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '面宽':
                item["miankuan"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '进深':
                item["jinshen"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '层高':
                item["cenggao"] = lstbox1[i]

            elif lstbox2[i].replace('\xa0','') == '物业费':
                item["service_price"] = lstbox1[i]

        item["function_list"] = response.xpath('//div[@class = "clearfix"]//dd/text()').extract()

        item["release_date"] = response.xpath('//span[@class = "time"]//text()').extract()[1]

        item["url"] = response.url 




        yield item
