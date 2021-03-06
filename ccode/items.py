# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CcodeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    code = scrapy.Field()
    successful_submission = scrapy.Field()
    accuracy = scrapy.Field()
    answer = scrapy.Field()

class Answer(scrapy.Item):
	pass
