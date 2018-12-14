import scrapy

from main.items import MainItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.es/s/keywords=samsung+s8',
    ]

    def parse(self, response):
        item = MainItem()

        for r in response.xpath('//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()').extract():
            item['price'] = r

            yield {
                'price': r
            }

