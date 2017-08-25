# -*- coding: utf-8 -*-
import scrapy
from proxy_pool_crawler.items import ProxyPoolCrawlerItem

class XcdlspiderSpider(scrapy.Spider):
    name = 'xcdlspider'
    allowed_domains = ['xicidaili.com']
    start_urls = []
    
    for i in range(1, 5):
        start_urls.append('http://www.xicidaili.com/nn/' + str(i))

    def parse(self, response):
        item = ProxyPoolCrawlerItem()
        rows = response.xpath('//table[@id="ip_list"]//tr')
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        
        for cell in rows:
            ip = cell.xpath('//td/text()').extract()[0]
            port = cell.xpath('//td/text()').extract()[1]
            item['address'] = ip + ':' + port
            yield item
            
