from typing import Any
from scrapy import Spider
from scrapy.http import Response
from crawler.items import CrawlerItem

class ProductSpider(Spider):
    name = 'limited_edition'
    start_urls = [
        'https://www.renault.co.in/renault_limited_edition.html'
    ]
    
    def parse(self, response: Response) -> Any:
        title = response.xpath("//h1/text()").get()

        edition_element = response.xpath('//h2[contains(text(), "Night and Day")]')
        edition_name = edition_element.xpath('string()').get().strip() if edition_element else ''
        # here we will extract the texts by the headings;
        first_model_div = response.xpath('//div[p[contains(text(), "RENAULT KIGER - BOLD SUV STANCE")]]')
        second_model_div = response.xpath('//div[p[contains(text(), "RENAULT TRIBER - STYLISH 5 TO 7 SEATER")]]')
        third_model_div = response.xpath('//div[p[contains(text(), "RENAULT KWID - SUV INSPIRED DESIGN")]]')
        
        # an helper function to retrieve texts from similar div element;
        def _get_model_name_and_description (model_div):
                if model_div:
                    model_name = model_div.xpath('.//p[contains(@class, "Component1v0__title")]/text()').get().strip()
                    description = model_div.xpath('.//div[contains(@class, "Component1v0__bodyCopy")]//p/text()').get().strip()
                else:
                    model_name = ''
                    description = ''
                return { model_name, description }
    
        first_model_name, first_model_description = _get_model_name_and_description(first_model_div)
        second_model_name, second_model_description = _get_model_name_and_description(second_model_div)
        third_model_name, third_model_description = _get_model_name_and_description(third_model_div)
        item = CrawlerItem()
        item["title"] = title
        item["heading"] = edition_name
        item["first_model_name"] = first_model_name
        item["description_for_first_model"] = first_model_description
        item["second_model_name"] = second_model_name
        item["description_for_second_model"] = second_model_description
        item["third_model_name"] = third_model_name
        item["description_for_third_model"] = third_model_description
        
        item["url"] = response.url
        item["node"] = "parent" if response.url in self.start_urls else "child"
        yield item
    