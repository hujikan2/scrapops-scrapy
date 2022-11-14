# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExchangeRateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    mata_uang = scrapy.Field()
    nilai = scrapy.Field()
    kurs_jual = scrapy.Field()
    kurs_beli = scrapy.Field()
    pass
