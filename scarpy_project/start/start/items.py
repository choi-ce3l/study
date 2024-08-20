# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StartItem(scrapy.Item):
    # define the fields for your item here like:
    p_tag=scrapy.Field()
    pass

class SecondItem(scrapy.Item):
    # define the fields for your item here like:
    li_tag=scrapy.Field()
    order=scrapy.Field()
    pass

class ThirdExemItem(scrapy.Item):
    p_tag=scrapy.Field() #알아서 딕셔너리 형태로 만듦
    #pass

class FourthExemItem(scrapy.Item):
    id=scrapy.Field()
    title=scrapy.Field()
    url1=scrapy.Field()
    comments=scrapy.Field()
    #pass

class MovieItem(scrapy.Item):
    rank=scrapy.Field()
    name=scrapy.Field()
    audience=scrapy.Field()
    #pass

class DaumNewsItems(scrapy.Item):
    title=scrapy.Field()
    body=scrapy.Field()
    #pass

class NaverNewsItems(scrapy.Item):
    title=scrapy.Field()
    body=scrapy.Field()
    reaction=scrapy.Field()
    #pass