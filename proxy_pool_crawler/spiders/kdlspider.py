# -*- coding: utf-8 -*-
import scrapy
from proxy_pool_crawler.items import ProxyPoolCrawlerItem


class KdlspiderSpider(scrapy.Spider):
    name = 'kdlspider'
    allowed_domains = ['kuaidaili.com']
    start_urls = []
    
    #设置需要爬的页数
    for i in range(1, 5):
        start_urls.append('http://www.kuaidaili.com/free/inha/' + str(i) + '/')

    def parse(self, response):
        item = ProxyPoolCrawlerItem()
        rows = response.xpath('//div[@id="list"]/table/tbody/tr')
        
        for cell in rows:
            ip = cell.xpath('td/text()').extract()[0]
            port = cell.xpath('td/text()').extract()[1]
            item['address'] = ip + ':' + port
            yield item
