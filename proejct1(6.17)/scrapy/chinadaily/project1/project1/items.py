# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import codecs
import json
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class chinadailyItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()

class chinadailyItem(scrapy.Item):

    title = scrapy.Field()
    url=scrapy.Field()
    publishtime=scrapy.Field()
    source=scrapy.Field()
    content=scrapy.Field()
    column_1=scrapy.Field()
    column_2=scrapy.Field()

class chinadailyenItem(scrapy.Item):

    title = scrapy.Field()
    url=scrapy.Field()
    publishtime=scrapy.Field()
    source=scrapy.Field()
    content=scrapy.Field()
    column_1=scrapy.Field()
    column_2=scrapy.Field()

    
