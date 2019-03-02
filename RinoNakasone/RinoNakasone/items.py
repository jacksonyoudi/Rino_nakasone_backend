# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RinonakasoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class IreadweekItem(scrapy.Item):
    name = scrapy.Field()
    author = scrapy.Field()
    category = scrapy.Field()
    score = scrapy.Field()
    img_url = scrapy.Field()
    download_url = scrapy.Field()
    introduction = scrapy.Field()
    author_info = scrapy.Field()
    directory = scrapy.Field()
    create_edit = scrapy.Field()


class MeiZiTuItem(scrapy.Item):
    title = scrapy.Field()
    name = scrapy.Field()
    path = scrapy.Field()
    img_url = scrapy.Field()
    referer = scrapy.Field()
