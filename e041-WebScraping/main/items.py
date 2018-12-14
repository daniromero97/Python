# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    prices = scrapy.Field()
    titles = scrapy.Field()
    stars = scrapy.Field()
    customer_reviews = scrapy.Field()