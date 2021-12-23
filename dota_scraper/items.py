# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DotaScraperItem(scrapy.Item):
    base_heroe_name = scrapy.Field()
    heroe_name = scrapy.Field()
    value = scrapy.Field()
    win_rate = scrapy.Field()
    is_advantage = scrapy.Field()
    base_date = scrapy.Field()
