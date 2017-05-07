# -*- coding: UTF-8 -*-

from encodings.utf_8 import encode
from scrapy import Selector
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from biyao.items import BiyaoItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class Douban(CrawlSpider):
    name = "biyao"
    start_urls = ['http://www.biyao.com/classify/category.html?categoryId=1']
    rules = (
        Rule(SgmlLinkExtractor(allow=("category.html", )), callback='parse',follow = True),
        Rule(SgmlLinkExtractor(allow=('category', )), callback='parse'),
        )

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


    #  
    #   <td>amazon</td>
    #  
    # def parse(self,response):
    #     response = Selector(response)
    #     container  = response.xpath("//div[@class='s-item-container']")
    #     items = []
    #     for e in container :
    #         name = e.xpath("//h2/text()").extract()
    #         item = BiyaoItem()
    #         item["name"] = name
    #         print name
    #         items.append(item)
    #     return items
        