# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy import  Item, Field

class BiyaoItem(Item):
    name = Field()
    price = Field()
    link = Field()
    image = Field()
    category = Field()
    pass
