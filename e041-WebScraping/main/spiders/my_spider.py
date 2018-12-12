from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from main.items import MainItem


class AmazonSpider(CrawlSpider):
    name = "amazon"
    item_count = 0
    allowed_domain = ["https://www.amazon.es"]
    start_urls = ["https://www.amazon.es/s/keywords=samsung+s9"]

    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//span[@class="pagnRA"]/a')),
             callback='parse_item', follow=False)
    }

    """
            Rule(LinkExtractor(allow=(), restrict_xpaths=('//div[@class="a-row a-spacing-none sx-line-clamp-4"]/a')),
                 callback='parse_item', follow=False)
    """


    def parse_item(self, response):
        ml_item = MainItem()

        ml_item['price'] = response.xpath(
            'normalize-space(//span[@class="a-size-base a-color-price s-price a-text-bold"]/text())').extract()

        self.item_count += 1
        if self.item_count > 5:
            raise CloseSpider('item_exceeded')
        yield ml_item

