import scrapy

class UniversityItem(scrapy.Item):
    name = scrapy.Field()
    website = scrapy.Field()
    email = scrapy.Field()
    country = scrapy.Field()
