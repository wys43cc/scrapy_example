#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy.contrib.spiders import Spider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest
from yidong.items import YidongItem



class YidongSipder(Spider) :
    name = "zhaobiao"
    allowed_domains = ["b2b.10086.cn"]
    start_urls = [
        "https://b2b.10086.cn/b2b/main/listVendorNotice.html?noticeType=2"
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow = ('/b2b.10086.cn/', )), callback = 'parse_page', follow = True),
    )


    def parse(self, response):
        message = Selector(response)
        item = YidongItem()
        item['company'] = message.xpath('//table//tr/td/text()').extract_first()
        print item['company']
        item['title'] = message.xpath('//table//tr/td/text()').extract_first()
       
        return item