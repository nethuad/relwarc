import scrapy

class IpchinaSpider(scrapy.Spider):
    name = "ipchina"
    
    def start_requests(self):
        urls = [
            'http://ip.chinaz.com/getip.aspx',
        ]
        for i, url in enumerate(urls):
            yield scrapy.Request(url, meta={'cookiejar': i},callback=self.parse)

    def parse(self, response):
        print(response.text)

        

        
