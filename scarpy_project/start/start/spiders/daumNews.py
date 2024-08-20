from typing import Iterable
import scrapy
from ..items import DaumNewsItems


class DaumnewsSpider(scrapy.Spider):
    name = "daumNews"
    allowed_domains = ["daum.net"]
    # start_urls = ["https://news.daum.net/breakingnews/society"]

    def start_requests(self):
        url='https://news.daum.net/breakingnews/society'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        a_tags=response.css('list_news2.list_allnews li div.cont_thumb a::attr(href)').getall()

        for link in a_tags:
            yield scrapy.Request(link,callback=self.newsbody)
    
    def newsbody(self,response):
        
        title=response.css('#mArticle div.head_view h3.tit_view::text').get().strip()
        body=response.css('article_view section::text').getall()
        body=' '.join(line.strip() for line in body)#리스트를 하나의 str로

        item=DaumNewsItems()
        item['title']=title
        item['body']=body
        yield item
