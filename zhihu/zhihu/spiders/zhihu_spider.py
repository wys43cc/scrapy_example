#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
一个简单的Python爬虫, 用于抓取coursera网站的下载链接和pdf

Anthor: Andrew Liu
Version: 0.0.2
Date: 2014-12-15
Language: Python2.7.8
Editor: Sublime Text2
Operate: 具体操作请看README.md介绍
"""
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from zhihu.items import ZhihuItem
import scrapy



class ZhihuSipder(CrawlSpider) :
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
        "https://www.zhihu.com/collection/38624707"
    ]
 
    headers_dict = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip,deflate",
    "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
    "Connection": "keep-alive",
    "Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
    "Cookie":'''q_c1=2283bb595e304c7c9557024cade3a8cd|1486961452000|1486961452000; d_c0="AEDC1HWHTQuPTvkgiOkJLl82Z8-w4-nQACs=|1486961453"; _zap=f56b4282-b44f-4dcf-8c2b-e8c715f48f9d; _xsrf=cf403907dcb1cc5659101e088646a973; aliyungf_tc=AQAAACNIeXz2CgQA80DgelDkMdng4Guj; l_n_c=1; login="YThlZjlkMTdmNjExNDY3ZDhlNzJmZGY3Y2NlMTViZmM=|1487130279|b8275dea10cf1e542132ac692465c2f22e937439"; l_cap_id="NGJkNWMyYTQwZDBhNDljY2I5YWQzNTdmZWM0YWExOTg=|1487130434|2f63b658e07480a99165f3fe4facb3549ac06d47"; cap_id="YjY2OThiZWVlOThjNDI0ZGFhNzczODE5ZDYyZTgxZmM=|1487130434|5d73f1898868d486826b0282f8020a6d84a494f1"; __utma=51854390.1792666199.1487134612.1487134612.1487136758.2; __utmb=51854390.0.10.1487136758; __utmc=51854390; __utmz=51854390.1487134612.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.100-1|2=registration_date=20131227=1^3=entry_date=20131227=1; z_c0=Mi4wQUFEQXJnTWpBQUFBUU1MVWRZZE5DeGNBQUFCaEFsVk5TRnpMV0FCYnUxSzJRRzQwSS04Nkl2cmJMUzdXZm9rTGtR|1487136601|d7fb981f957ec2f6ecc1f951780ad373b8de5537"
    ''',
    "Referer": "http://www.zhihu.com/"
    }

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.zhihu.com/collection/38624707",
            headers=self.headers_dict,
            meta={
                "cookiejar": 1
            },
        )

    def parse(self, response):
        problem = Selector(response)
        item = ZhihuItem()
        item['url'] = response.url
        item['name'] = problem.xpath('//span[@class="name"]/text()').extract()
        print item['name']
        item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        item['answer']= problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        return item
