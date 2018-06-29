import scrapy

class XueshandaiSpider(scrapy.Spider):
    name = "xueshandai"
    
    def start_requests(self):
        urls = [
            "https://www.xueshandai.com/invest/list",
        ]
        for i, url in enumerate(urls):
            yield scrapy.Request(url, meta={'cookiejar': i},callback=self.parse)

    def parse(self, response):
        result = response.css('#main_wrap div.bid_list.clearfix.bg_white')
        for r in result:
            print("===================")
            name = r.css('div.bid_main>h2::text').re('[^\s]+')
            print(name)
            href = r.css('div.bid_main>h2>a::attr(href)').extract_first()
            print(href)
            desc = r.css('div.bid_main>h2>a::text').extract_first()
            print(desc)
            for li in r.css('div.bid_main ul li'):
                l = li.css('*::text').re('[^\s]+')
                print(l)
        next_page = response.css('#main_wrap div.page a:contains("下页")::attr(href)').extract_first()
        if next_page is not None:
#             yield response.follow(next_page, self.parse)
            next_page = response.urljoin(next_page)
#             print(next_page)
            yield scrapy.Request(next_page, meta={"cookiejar": response.meta["cookiejar"]}, callback=self.parse)
            
            
            
# ip 58.247.0.166
# user_agent:Scrapy/1.5.0 (+https://scrapy.org)
