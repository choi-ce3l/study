import scrapy
from start.items import NaverNewsItems
import json

class NavernewsSpider(scrapy.Spider):
    name = "NaverNews"
    allowed_domains = ["news.naver.com","news.like.naver.com"]

    def start_requests(self):
        url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=032&date=20240818'
        yield scrapy.Request(url, callback=self.getUrls)

    def getUrls(self, response):
        li_tags = response.css('div.list_body.newsflash_body ul li')
        header = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
        for li in li_tags:
            try: 
                link=li.css('dt')[1].css('a::attr(href)').get()
            except:
                link=li.css('dt')[0].css('a::attr(href)').get()

            yield scrapy.Request(link,callback=self.parse,headers=header)
    
    def parse(self,response):
        title = response.css('#title_area span::text').get().strip()
        body = response.css('#dic_area::text').getall()
        body = ' '.join(line.strip() for line in body)
        
        item = NaverNewsItems()
        item['title'] = title
        item['body'] = body
        item['reaction'] = {}

        code = response.url.split("/")[-2]
        id=response.url.split('/')[-1]
        react_url=f'https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&q=JOURNALIST%5B77887(period)%5D%7CNEWS%5Bne_{code}_{id}%5D&isDuplication=false&cssIds=MULTI_MOBILE%2CNEWS_MOBILE&_=1724118759763'
        yield scrapy.Request(react_url,meta={'item':item}, callback=self.reactParse)

    def reactParse(self,response):
        item=response.meta['item']
        response=json.loads(response.text)['contents'][1]['reactions']
        
        try:
            for react in response:
                self.logger.info(f"{response=}")
                reaction=react['reactionType']
                count=react['count']                
                item['reaction'][reaction]=count
            yield item
        except:
            print('리액션 없음')
            yield item

#scrapy crawl NaverNews
#scrapy crawl NaverNews -o NaverNewsPractice.json