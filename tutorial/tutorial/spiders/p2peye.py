import scrapy

class P2peyeSpider(scrapy.Spider):
    name = "p2peye"

    def start_requests(self):
        urls = [
            "https://www.p2peye.com/platform/all/",
        ]
        for i, url in enumerate(urls):
            yield scrapy.Request(url, meta={'cookiejar': i},callback=self.parse)

    def parse(self, response):
        result = response.css('ul.ui-result.clearfix li.ui-result-item div.ui-result-box')
        for r in result:
            top = r.css('div.ui-result-top')
            href = top.css('a.ui-result-pname::attr(href)').extract_first()
            pname = top.css('a.ui-result-pname::text').extract_first()
            tags = top.css('div.ui-result-promptbox::text').re('[^\n ]+')
            
#             print("=========")
#             print(pname)
#             print(href)
#             print(tags)

            bottom = r.css('div.ui-result-bottom')
            
            descriptions=[]
            for bot in bottom.css('p.ui-result-text'):
                desc = "".join(a.strip('\n ') for a in bot.css('*::text').re('[^\n ]+'))
                descriptions.append(desc)
#                 print(1,"".join(a.strip('\n ') for a in bot.css('*::text').extract()))
#             print(descriptions)
            
            jsondata ={
                'pname':pname,
                'href':href,
                'tags':tags,
                'descriptions':descriptions,                
            }
    #         print(jsondata)
            yield jsondata
        
        
        next_page = response.css('div.c-page a:contains("下一页")::attr(href)').extract_first()
        print(next_page)
        if next_page is not None:
#             # yield response.follow(next_page, self.parse)
            abs_next_page = response.urljoin(next_page)
            print(abs_next_page)
#             yield scrapy.Request(next_page, callback=self.parse)
            yield scrapy.Request(abs_next_page, meta={"cookiejar": response.meta["cookiejar"]}, callback=self.parse)
            
# ui-platwt-ptsl
# ui-platwt-txkn
           

