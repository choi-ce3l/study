import scrapy
from start.items import StartItem,SecondItem,ThirdExemItem,FourthExemItem,MovieItem
import json

class PracticeSpider(scrapy.Spider):
    name = "practice"
    allowed_domains = ["crawlingstudy-dd3c9.web.app"]
    start_urls = ["https://crawlingstudy-dd3c9.web.app/02/"]

    def start_request(self):
        url='https://crawlingstudy-dd3c9.web.app/02/'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        
        a_tags=response.css('a::attr(href)').getall() #해당 속성 모두 가져오기

        for link in a_tags:
            link=response.url+link
            yield scrapy.Request(link,callback=self.secondParse)

    def secondParse(self,response):
        p_tag=response.css('p::text').get()
        item=StartItem()
        item['p_tag']=p_tag.strip()

        yield item
        #pass

class SecondPractice(scrapy.Spider):
    name = "SecondPractice"
    allowed_domains = ["crawlingstudy-dd3c9.web.app"]
    start_urls = ["https://crawlingstudy-dd3c9.web.app/02/"]

    def start_request(self):
        url='https://crawlingstudy-dd3c9.web.app/02/'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        
        li_tags=response.css('ul li::text').getall()
        print(li_tags)

        item2=SecondItem()
        for i in range(len(li_tags)):
            item2['order']=i
            item2['li_tag']=li_tags[i]
            yield item2

        #pass

class ThirdExem(scrapy.Spider):
    name = "ThirdExem"
    allowed_domains = ["crawlingstudy-dd3c9.web.app"]
    #start_urls = ["https://crawlingstudy-dd3c9.web.app/01/"]

    def start_requests(self):
        url='https://crawlingstudy-dd3c9.web.app/01/'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        a_tags=response.css('a::attr(href)').getall()

        for link in a_tags:
            link=response.url+link
            yield scrapy.Request(link,callback=self.Secondparse)
    
    def Secondparse(self, response):
        p_tag=response.css('p::text').get().strip()
        print(p_tag)

        item=ThirdExemItem()
        item['p_tag']=p_tag

        yield item

class FourthExem(scrapy.Spider):
    name = "FourthExem"
    #allowed_domains = ["crawlingstudy-dd3c9.web.app"]
    #start_urls = ["https://crawlingstudy-dd3c9.web.app/01/"]

    def start_requests(self):
        url='https://jsonplaceholder.typicode.com/photos'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        data=json.loads(response.text) #비동기 방식은 이와 같이 해야 함.

        for post in data[:5]:
            id=post['id']
            title=post['title']
            url1=post['url']
        
            item=FourthExemItem()
            item['id']=id
            item['title']=title
            item['url1']=url1
            item['comments']=[]

            
            comments_url=f'https://jsonplaceholder.typicode.com/comments?postId={id}'
            yield scrapy.Request(comments_url,meta={'item':item},callback=self.test)

    def test(self,response):
        comments_data=json.loads(response.text)

        for data in comments_data:
            item=response.meta['item']
            item['comments'].append(data['body'].strip())
        yield item


class MovieSpider(scrapy.Spider):
    name = "MovieSpider"
    #allowed_domains = ["search.naver.com/"]
    #start_urls = ["https://crawlingstudy-dd3c9.web.app/02/"]

    def start_request(self):
        url='https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=0&acr=2&ie=utf8&query=%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        li_tags=response.css('div._panel_popular._tab_content div.list_image_box ul._panel li')
        item=MovieItem()

        for li in li_tags:
            rank=li.css('a div.thumb span.this_text::text').get().strip()
            name=li.css('a div.title_box strong::text').get().strip()
            audience=li.css('a div.title_box span::text').get()

            item['rank']=rank
            item['name']=name
            item['audience']=audience

            yield item

class NewsSpider(scrapy.Spider):
    name = "NewsSpider"
    #allowed_domains = ["crawlingstudy-dd3c9.web.app"]
    #start_urls = ["https://crawlingstudy-dd3c9.web.app/01/"]

    def start_requests(self):
        url='https://news.daum.net/breakingnews/society'
        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        li_tags=response.css('ul.list_news2.list_allnews li')

        for li in li_tags:
            link=li.css('strong.tit_thumb a::attr(href)').get()
        yield scrapy.Request(link,callback=self.Secondparse)

    def Secondparse(self, response):
        title=response.css('h3.tit_view::text').get().strip()
        body=response.css('article section p::text').getall()

        item2=SecondItem()







        #scrapy crawl FourthExem

