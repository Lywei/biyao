# -*- coding: UTF-8 -*-

from encodings.utf_8 import encode
from scrapy import Selector
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from biyao.items import BiyaoItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class Douban(CrawlSpider):
    name = "biyao"
    start_urls = [
        'http://www.biyao.com/classify/category.html?categoryId=%s' % p for p in xrange(1,300)
        ]
    rules = (
        Rule(SgmlLinkExtractor(allow=("category.html", )), callback='parse',follow = True),
        Rule(SgmlLinkExtractor(allow=('category', )), callback='parse'),
        )

    def parse(self, response):
        response = Selector(response)
        ul = response.xpath("//*[@class='category-list']/li")
        items = []
        category  = response.xpath("//div[@class='category-title']/dl/dt/text()").extract()[0]
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
            item["category"] = category
            items.append(item)
        return items