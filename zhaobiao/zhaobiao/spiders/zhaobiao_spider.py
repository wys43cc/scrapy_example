#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest
from zhaobiao.items import ZhaobiaoItem
import scrapy



class ZhaobiaoSipder(CrawlSpider) :
    name = "zhaobiao"
    allowed_domains = ["b2b.10086.cn"]
    start_urls = [
        "https://b2b.10086.cn/b2b/main/listVendorNotice.html?noticeType=2"
    ]

    hearders = {"Accept":"*/*",
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"zh-CN,zh;q=0.8",
                "Connection":"keep-alive",
                "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie":"saplb_*=(J2EE204289920)204289950; JSESSIONID=x2g0Q4CT16i4pQChlgq_UrfsR1lFWgGeNy0M_SAP9NH8ROfeozM_SR2-dTJRXKus",
                "Host":"b2b.10086.cn",
                "Origin":"https://b2b.10086.cn",
                "Referer":"https://b2b.10086.cn/b2b/main/listVendorNotice.html?noticeType=2",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
                "X-Requested-With":"XMLHttpRequest"}

    def start_requests(self):
        return [FormRequest(url="https://b2b.10086.cn/b2b/main/listVendorNoticeResult.html?noticeBean.noticeType=2",headers =self.hearders,
                    formdata={'page.currentPage': '1', 'page.perPageSize': '20','noticeBean.noticeType':'2','noticeBean.sourceCH':'','noticeBean.source':'',
                    'noticeBean.title':'','noticeBean.startDate':'','noticeBean.endDate':''})]

    def parse(self, response):
        for sel in response.xpath('//table//tr'):
            item = ZhaobiaoItem()
            item['company'] = sel.xpath('td[1]/text()').extract()
            item['title'] = sel.xpath('td[3]/a/text()').extract()
            yield item
       