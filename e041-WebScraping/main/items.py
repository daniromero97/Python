# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MainItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    price = scrapy.Field()
    title = scrapy.Field()
    stars = scrapy.Field()
    customer_reviews = scrapy.Field()
    recommended_price = scrapy.Field()
    RAM = scrapy.Field()
    ROM = scrapy.Field()
    url = scrapy.Field()
