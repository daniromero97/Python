import scrapy

from main.items import MainItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.es/s/keywords=samsung+s8',
    ]

    def parse(self, response):
        item = MainItem()
        price_list, title_list, star_list = [], [], []

        for r in response.xpath('//span[@class="a-size-base a-color-price s-price a-text-bold"]/text()').extract():
            price_list.append(r)

        for r in response.xpath(
                '//h2[@class="a-size-medium s-inline  s-access-title  a-text-normal"]/text()').extract():
            title_list.append(r)

        for r in response.xpath(
                '////span/span/a/i/span[@class="a-icon-alt"]/text()').extract():
            star_list.append(r)

        for i in range(len(price_list)):
            item['prices'] = price_list[i]
            item['titles'] = title_list[i]
            item['stars'] = star_list[i]

            yield {
                'price': item['prices'],
                'title': item['titles'],
                'star': item['stars']
            }

