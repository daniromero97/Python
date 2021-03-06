import scrapy

from main.items import MainItem


def pages():
    search_for = 'samsung+s8'
    number_of_pages = 2
    list_of_pages = []
    for i in range(1, number_of_pages+1):
        list_of_pages.append('https://www.amazon.es/s/keywords=%s&page=%d' % (search_for, i))
    return list_of_pages


class AmazonSpider(scrapy.Spider):
    link_count = 0
    name = 'amazon'
    allowed_domains = ['amazon.es']
    start_urls = pages()

    def parse(self, response):
        for link in response.xpath('//div[@class="a-row a-spacing-small"]/div/a/@href').extract():
            yield scrapy.Request(url=link, callback=self.parse_items)

    def parse_items(self, response):
        item = MainItem()

        item['price'] = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract()
        item['title'] = str(response.xpath('//span[@id="productTitle"]/text()').extract()).replace('  ', '')
        item['stars'] = response.xpath('//a[@class="a-popover-trigger a-declarative"]/i/span[@class="a-icon-alt"]/text()').extract()
        item['customer_reviews'] = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract()
        item['recommended_price'] = response.xpath('//span[@class="a-text-strike"]/text()').extract()
        item['RAM'] = response.xpath('//tbody[1]/tr[10]/td[@class="value"]/text()').extract()
        item['ROM'] = response.xpath('//tbody[1]/tr[11]/td[@class="value"]/text()').extract()
        item['url'] = response.request.url

        yield {
            'price': item['price'],
            'title': item['title'],
            'stars': item['stars'],
            'customer_reviews': item['customer_reviews'],
            'recommended_price': item['recommended_price'],
            'RAM': item['RAM'],
            'ROM': item['ROM'],
            'url': item['url']
        }


