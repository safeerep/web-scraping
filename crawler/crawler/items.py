import scrapy


class CrawlerItem(scrapy.Item):
    title = scrapy.Field()
    heading = scrapy.Field()
    content = scrapy.Field()
    first_model_name = scrapy.Field()
    description_for_first_model = scrapy.Field()
    second_model_name = scrapy.Field()
    description_for_second_model = scrapy.Field()
    third_model_name = scrapy.Field()
    description_for_third_model = scrapy.Field()
    url = scrapy.Field()
    node = scrapy.Field()
    pass
