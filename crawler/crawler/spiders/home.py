from typing import Any
from scrapy import Spider
from scrapy.http import Response
from crawler.items import CrawlerItem

class ProductSpider(Spider):
    name = 'home'
    start_urls = [
        'https://www.renault.co.in/'
    ]
    
    def parse(self, response: Response) -> Any:
        title = response.xpath("//h1/text()").get()
        
        item = CrawlerItem()
        item["title"] = title
        yield item    