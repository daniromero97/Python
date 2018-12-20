import scrapy
from main.items import MainItem


class AmazonSpider(scrapy.Spider):
    link_count = 0
    name = 'amazon'
    allowed_domains = ['amazon.es']
    search_for = 'samsung+s8'
    start_urls = [
        'https://www.amazon.es/s/keywords='+search_for
    ]

    def parse(self, response):
        for link in response.xpath('//div[@class="a-row a-spacing-small"]/div/a/@href').extract():
            yield scrapy.Request(url=link, callback=self.parse_items)

    def parse_items(self, response):
        item = MainItem()

        item['price'] = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract()
        item['title'] = response.xpath('//span[@id="productTitle"]/text()').extract()
        item['stars'] = response.xpath('//a[@class="a-popover-trigger a-declarative"]/i/span[@class="a-icon-alt"]/text()').extract()
        item['customer_reviews'] = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract()

        yield {
            'price': item['price'],
            'title': item['title'],
            'stars': item['stars'],
            'customer_reviews': item['customer_reviews']
        }


