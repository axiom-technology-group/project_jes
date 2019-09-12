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

class ProjectAug19ItemLoader(ItemLoader):
    #自定义itemloader
    default_output_processor = TakeFirst()

class ProjectAug19Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class lianjia_ershoufangItem(scrapy.Item):
    url=scrapy.Field()

    headline =scrapy.Field()

    house_location=scrapy.Field()

    house_price_tenK=scrapy.Field()

    house_price_perunit=scrapy.Field()

    sell_date=scrapy.Field()

    house_website_traffic=scrapy.Field()

    Housing_type=scrapy.Field()

    floor=scrapy.Field()

    Built_up_area=scrapy.Field()

    Huxing_structure=scrapy.Field()

    Cover_area=scrapy.Field()

    Architectural_Types=scrapy.Field()

    House_orientation=scrapy.Field()

    Completion_date=scrapy.Field()

    Decoration=scrapy.Field()

    building_structure=scrapy.Field()

    Heating_mode=scrapy.Field()

    household_ratio_perstair=scrapy.Field()

    Equipped_with_elevators=scrapy.Field()

    Years_of_Property_Rights=scrapy.Field()

    Years_of_housing=scrapy.Field()

    Transaction_Ownership=scrapy.Field()

    House_use=scrapy.Field()

    Ownership_of_housing=scrapy.Field()

class fangtianxia_shangquanItem(scrapy.Item):
    url=scrapy.Field()

    titile=scrapy.Field()

    location=scrapy.Field()

    total_price=scrapy.Field()

    service_price=scrapy.Field()

    jianzhumianji=scrapy.Field()

    floor=scrapy.Field()

    zhuangxiu=scrapy.Field()

    shangpu_type=scrapy.Field()

    shifoufenge=scrapy.Field()

    shihejingying=scrapy.Field()

    loupanmingcheng=scrapy.Field()

    loupandizhi=scrapy.Field()

    miankuan=scrapy.Field()

    jinshen=scrapy.Field()

    cenggao=scrapy.Field()

    function_list=scrapy.Field()

    release_date=scrapy.Field()

    


class fangtianxia_xiezilouItem(scrapy.Item):

    url=scrapy.Field()

    titile=scrapy.Field()

    total_price_10K=scrapy.Field()

    price_perunit=scrapy.Field()

    jianzhumianji=scrapy.Field()

    suozailouceng=scrapy.Field()

    zhuangxiu=scrapy.Field()

    building_type=scrapy.Field()

    service_price=scrapy.Field()

    dengji=scrapy.Field()

    xzl_content=scrapy.Field()

    loupan_content=scrapy.Field()

    release_date=scrapy.Field()

    loupandizhi = scrapy.Field()


class gangjiwang_shangpuItem(scrapy.Item):

    url=scrapy.Field()

    titile=scrapy.Field()

    location=scrapy.Field()

    total_price_10K=scrapy.Field()

    service_price=scrapy.Field()

    jianzhumianji=scrapy.Field()

    floor=scrapy.Field()

    zhuangxiu=scrapy.Field()

    shangpu_type=scrapy.Field()

    shifoufenge=scrapy.Field()

    shihejingying=scrapy.Field()

    loupanmingcheng=scrapy.Field()

    loupandizhi=scrapy.Field()

    miankuan=scrapy.Field()

    jinshen=scrapy.Field()

    cenggao=scrapy.Field()

    function_list=scrapy.Field()

    release_date=scrapy.Field()


class lianjia_ershoufangrentItemloc(scrapy.Item):
    url=scrapy.Field()
    location=scrapy.Field()

class lianjia_ershoufangrentItem(scrapy.Item):
    url=scrapy.Field()

    sell_date=scrapy.Field()

    headline=scrapy.Field()

    house_website_traffic=scrapy.Field()

    rental_pirce=scrapy.Field()

    tags=scrapy.Field()

    chuzufangshi=scrapy.Field()

    Huxing_structure=scrapy.Field()

    Built_up_area=scrapy.Field()

    chaoxiang=scrapy.Field()

    ruzhu=scrapy.Field()

    rental_duration=scrapy.Field()

    visiting_time=scrapy.Field()

    floor=scrapy.Field()

    have_elvator=scrapy.Field()

    have_parkingspace=scrapy.Field()

    yongshui=scrapy.Field()

    yongdian=scrapy.Field()

    ranqi=scrapy.Field()

    warming_system=scrapy.Field()
    
    function_list=scrapy.Field()


class fangtianxia_xiezilourentItem(scrapy.Item):

    url=scrapy.Field()

    titile=scrapy.Field()

    total_price_10K_permonth=scrapy.Field()

    price_perunit=scrapy.Field()

    chuzumianji=scrapy.Field()

    floor=scrapy.Field()

    service_price=scrapy.Field()

    xiezilou_level=scrapy.Field()

    zhuangxiu=scrapy.Field()

    building_type=scrapy.Field()

    building_year=scrapy.Field()

    loupandizhi=scrapy.Field()

    xzl_content=scrapy.Field()

    loupan_content=scrapy.Field()

    release_date=scrapy.Field()

    


class fangtianxia_shangquanrentItem(scrapy.Item):
    titile = scrapy.Field()

    location= scrapy.Field()

    zhuanrangfei= scrapy.Field()

    rental_price= scrapy.Field()

    pay_method= scrapy.Field()

    jianzhumianji= scrapy.Field()

    shiyongmianji= scrapy.Field()

    shengyuzuqi= scrapy.Field()

    zhuanrangfangshi= scrapy.Field()

    floor= scrapy.Field()

    elvator_number= scrapy.Field()

    zhuangxiu= scrapy.Field()

    building_type= scrapy.Field()

    shifoufenge= scrapy.Field()

    shihejingying= scrapy.Field()

    loupanmingcheng= scrapy.Field()

    loupandizhi= scrapy.Field()

    miankuan= scrapy.Field()

    jinshen= scrapy.Field()

    cenggao= scrapy.Field()

    function_list= scrapy.Field()

    url= scrapy.Field()

    release_date=scrapy.Field()

    service_price=scrapy.Field()
















