# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CovidItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    疫情地区 = scrapy.Field()
    新增 = scrapy.Field()
    现有 = scrapy.Field()
    累计 = scrapy.Field()
    治愈 = scrapy.Field()
    死亡 = scrapy.Field()
