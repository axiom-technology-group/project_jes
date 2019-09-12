# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import urllib
from bs4 import BeautifulSoup
# 导入随机模块
import lxml
import random
import requests
import threading
import time

# 导入data5u文件中的IPPOOL
#from data5u import IPPOOL
# 导入官方文档对应的HttpProxyMiddleware
#from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware

## 导入随机模块

# 导入data5u文件中的IPPOOL



import threading
import time
import requests
 
exec_count = 0 
def IPtimer():
    
    
    URL= 'http://http.tiqu.alicdns.com/getip3?num=5&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='


    res = requests.get(URL)
    
    global datalst
    
    datalst = res.text.split('\r\n')[:-1]

    datalst = datalst[:3]
    
    print(time.strftime('%Y-%m-%d %H:%M:%S'),datalst)
 
    global exec_count
    exec_count += 1
    # 15秒后停止定时器
    if exec_count < 15:
        threading.Timer(300, IPtimer).start()
        
        
IPtimer()


#get_datalist()


class MyproxiesSpiderMiddleware(object):
 
    def __init__(self,ip=''):

        self.ip=ip
       
    def process_request(self, request, spider):


        data = random.choice(datalst)
        print('the current ip is',data)
        request.meta["proxy"]="http://"+ data


class ProjectAug19SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProjectAug19DownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
