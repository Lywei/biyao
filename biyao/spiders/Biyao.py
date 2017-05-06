# -*- coding: UTF-8 -*-

from encodings.utf_8 import encode

from scrapy import Selector
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.contrib.linkextractors import LinkExtractor
from biyao.items import BiyaoItem

class Douban(CrawlSpider):
    name = "biyao"
    start_urls = ['http://www.biyao.com/classify/category.html?categoryId=122']

    def parse(self, response):
        response = Selector(response)
        ul = response.xpath("//*[@class='category-list']/li")
        items = []
        for li in ul:
            item = BiyaoItem()
            name = li.xpath("dl/dt/text()").extract()
            price = li.xpath("dl/dd/text()").extract()
            link = li.xpath("a/@href").extract()
            image = li.xpath("a/img/@src").extract()
            item["name"] = name
            item["price"] = price
            item["link"] = link
            item["image"] = image
            items.append(item)
        return items