import scrapy

from main.items import MainItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    search_for1, search_for2 = 'samsung+s8', 'samsung+s9'
    start_urls = [
        'https://www.amazon.es/s/keywords='+search_for1,
        'https://www.amazon.es/s/keywords='+search_for2
    ]

    def parse(self, response):
        item = MainItem()
        price_list, title_list, star_list, customer_reviews_list = [], [], [], []

        for r in response.xpath('//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()').extract():
            price_list.append(r)

        for r in response.xpath(
                '//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]/text()').extract():
            title_list.append(r)

        for r in response.xpath(
                '//span/span/a/i/span[@class="a-icon-alt"]/text()').extract():
            star_list.append(r)

        for r in response.xpath(
                '//div[@class="a-row a-spacing-mini"]/a[@class="a-size-small a-link-normal a-text-normal"]/text()').extract():
            customer_reviews_list.append(r)

        for i in range(len(price_list)):
            item['prices'] = price_list[i]
            item['titles'] = title_list[i]
            item['stars'] = star_list[i]
            item['customer_reviews'] = customer_reviews_list[i]

            yield {
                'prices': item['prices'],
                'titles': item['titles'],
                'stars': item['stars'],
                'customer_reviews': item['customer_reviews']
            }

