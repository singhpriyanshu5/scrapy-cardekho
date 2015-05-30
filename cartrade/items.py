# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CartradeItem(scrapy.Item):
    model=scrapy.Field()
    price=scrapy.Field()
    kms=scrapy.Field()
    transm=scrapy.Field()
    fuel=scrapy.Field()
    yom=scrapy.Field()
    city=scrapy.Field()
    owner=scrapy.Field()
    url=scrapy.Field()
    carid=scrapy.Field()
    
    
   
