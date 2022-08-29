from ast import Yield
from gc import callbacks
from itertools import product
import scrapy


class PlantsSpider(scrapy.Spider):
    name = 'plants'
    allowed_domains = ['fake-plants.co.uk']
    start_urls = ['http://fake-plants.co.uk/']

    def parse(self, response):
        for link in response.css('li.product-category a::attr(href)'):
            yield response.follow(link.get(), callbacks=self.parse_categories)
        
    def parse_categories(self, response):
        products =  response.css('div.astra-shop-summary-wrap')
        for product in products:
            yield {
                'name': product.css('span').get(),
                # 'name': product.css('h2::text').get().strip(),
            }
               


# 1 response
# 2 response.css('li.product-category a::attr(href)')
# 3 response.css('li.product-category a::attr(href)').get()
#4 response.css('li.product-category a::attr(href)').getall()