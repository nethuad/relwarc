# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class P2peyeItem(scrapy.Item):
    pname = scrapy.Field()
    href = scrapy.Field()
    tags = scrapy.Field()
    descriptions = scrapy.Field()
    
class QuoteItem(scrapy.Item):
    author = scrapy.Field()
    tags = scrapy.Field()
    text = scrapy.Field()
    
class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    birthdate = scrapy.Field()
    bio = scrapy.Field()

    
    
