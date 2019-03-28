import scrapy
from jiandan.items import JiandanItem


class JiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = []
    start_urls = ['http://699pic.com/people.html']

    def parse(self, response):
        item = JiandanItem()
        item["image_urls"] = response.xpath('//div[@class="swipeboxEx"]/div[@class="list"]/a/img/@data-original').extract()
        url = "http://699pic.com"
        yield item
        new_url ='%s%s'%(url,response.xpath('//*[@id="wrapper"]/div[3]/a[@class="downPage"]//@href').extract_first())
        print(new_url)
        if new_url:
            print(new_url)
            yield scrapy.Request(new_url, callback=self.parse)

    # def parseContext(self, response):






