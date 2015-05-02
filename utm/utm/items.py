# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Course(scrapy.Item):
    section = scrapy.Field()
    instructor = scrapy.Field()
    current_enrolmlment = scrapy.Field()
    max_enrolment = scrapy.Field()
    wait_list = scrapy.Field()
    weekday = scrapy.Field()
    start_time = scrapy.Field()
    end_time = scrapy.Field()
    room = scrapy.Field()
    notes = scrapy.Field()
