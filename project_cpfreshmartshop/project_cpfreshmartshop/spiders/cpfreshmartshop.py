import scrapy,traceback
from project_cpfreshmartshop.items import ProjectCpfreshmartshopItem

class CpfreshmartshopSpider(scrapy.Spider):
    name = 'cpfreshmartshop'
    allowed_domains = ['cpfreshmartshop.com']
    start_urls=['https://cpfreshmartshop.com/en/shop',
    'https://cpfreshmartshop.com/en/egg-product',
    'https://cpfreshmartshop.com/en/festival-product',
    'https://cpfreshmartshop.com/en/chicken',
    'https://cpfreshmartshop.com/en/pork',
    'https://cpfreshmartshop.com/en/beef',
    'https://cpfreshmartshop.com/en/duck',
    'https://cpfreshmartshop.com/en/seafood',
    'https://cpfreshmartshop.com/en/sausage-ham-and-bacon',
    'https://cpfreshmartshop.com/en/snack-and-dessert',
    'https://cpfreshmartshop.com/en/ready-to-eat',
    'https://cpfreshmartshop.com/en/ready-to-cook',
    'https://cpfreshmartshop.com/en/seasoning-and-oil',
    'https://cpfreshmartshop.com/en/dried-and-canned-food',
    'https://cpfreshmartshop.com/en/beverage-and-powdered-drink',
    'https://cpfreshmartshop.com/en/dairy-product',
    'https://cpfreshmartshop.com/en/bakery',
    'https://cpfreshmartshop.com/en/fruit-and-vegetable',
    'https://cpfreshmartshop.com/en/household-product',
    'https://cpfreshmartshop.com']

    headers =  {
    'Host': 'cpfreshmartshop.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'locale=en; _gcl_au=1.1.1258816456.1631630254; _gid=GA1.2.1606466659.1631630255; visid_incap_2484750=pd+cVBJLRIOEQks4UIBwAmTAQGEAAAAAQUIPAAAAAACSLc9IsxGPk01Q1rrpYJ4L; incap_ses_1020_2484750=obRTTCW2vC5h0IGWGMUnDobAQGEAAAAAfDdtTyUMDwXp48hCPVTNzg==; incap_ses_433_2484750=dwADNNzmon8sHE4/lFMCBs46QWEAAAAAcnOUujZEbkvsoMi+++BeBQ==; nlbi_2484750=rWU2QTwkNEFuJeOzwRng+gAAAACWr1I99eUx0RPulFArcuCN; _ga=GA1.1.1283257968.1631630254; _ga_TD2MTQJFMS=GS1.1.1631664846.3.1.1631666502.0',
    }

    # This is a built-in Scrapy function that runs first where we'll override the default headers
    # Documentation: https://doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spiders.Spider.start_requests
    def start_requests(self):
        for u in self.start_urls:
            #yield scrapy.Request(u, callback=self.parse)
            #yield scrapy.Request(u, callback=self.parse)         
            yield scrapy.http.Request(u, headers=self.headers)      


    def parse(self, response):
        try:
            div_all_products=response.xpath('//div[@class="product-list row"]/div[@class="col-6 col-md-3 col-lg-20"]')
            pro_cate_url=response.url
            for div_product in div_all_products:
                pro_item=ProjectCpfreshmartshopItem()
                div_product_img=div_product.xpath('div/div/div[@class="thumb"]')
                pro_img_obj=div_product_img.xpath('a/div/img/@data-src')
                pro_img=None if pro_img_obj ==[] else pro_img_obj[0].extract().strip()
                pro_link_obj=div_product_img.xpath('a/@href').extract()
                pro_link=None if pro_link_obj==[] else pro_link_obj[0].strip()
                pro_badge_obj=div_product_img.xpath('a/h5/text()').extract()
                pro_badge=None if pro_badge_obj==[] else pro_badge_obj[0].strip()

                div_product_desc=div_product.xpath('div/div/div[@class="desc"]')
                pro_name=div_product_desc.xpath('div[@class="product-detail"]/h3/a/text()').extract()[0].strip()
                pro_price=div_product_desc.xpath('div[@class="product-price"]/div/div[@class="col"]/span/span/text()').extract()[0].strip()
                pro_sale_price_obj=div_product_desc.xpath('div[@class="product-price"]/div/div[@class="col"]/span/span/span/text()').extract()
                pro_sale_price=None if pro_sale_price_obj==[] else pro_sale_price_obj[0].strip()
                pro_regular_price_obj=div_product_desc.xpath('div[@class="product-price"]/div/div[@class="col"]/span/span/del/text()').extract()
                pro_regular_price=None if pro_regular_price_obj==[] else pro_regular_price_obj[0].strip()
                print(f'{pro_cate_url} {pro_name} {pro_img} {pro_link} {pro_badge} {pro_price} {pro_sale_price} {pro_regular_price}')
                pro_item['pro_cate_url']=pro_cate_url
                pro_item['pro_name']=pro_name
                pro_item['pro_img']=pro_img
                pro_item['pro_link']=pro_link
                pro_item['pro_badge']=pro_badge
                pro_item['pro_price']=pro_price
                pro_item['pro_sale_price']=pro_sale_price
                pro_item['pro_regular_price']=pro_regular_price
                yield pro_item
        except Exception as ex:
            traceback.print_exc()
            print()
        pass
