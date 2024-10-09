from typing import Any
from scrapy import Spider
from scrapy.http import Response

class ProductSpider(Spider):
    name = 'home'
    start_urls = [
        'https://www.renault.co.in/'
    ]
    
    def parse(self, response: Response) -> Any:
        title = response.xpath("//h1/text()").get()
        
        # item = Item()
        # item["title"] = title
        
        # item["url"] = response.url
        # item["node"] = "parent" if response.url in self.start_urls else "child"
        # yield item
        yield {'title': title}
    