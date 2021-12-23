from scrapy.http import request
from dota_scraper.items import DotaScraperItem
from dota_scraper.data import HEROE_NAMES, DotaUrls
from dota_scraper.spiders.__types__ import CountersQueryParams

import scrapy
import numpy as np
from urllib.parse import urlparse
from urllib.parse import parse_qs
from requests.models import PreparedRequest

from typing import List, Tuple


class DotaSpider(scrapy.Spider):
    name = 'dota'
    allowed_domains = ['www.dotabuff.com']

    def start_requests(self):
        for dota_url in DotaUrls.get_counter_urls():
            yield scrapy.Request(dota_url, self.parse)

    def parse(self, response):
        countered_table, counter_table = response.css('.col-6')

        countered_data: List[str] = countered_table.css(
            'tbody > tr > td::text').getall()
        counter_data: List[str] = counter_table.css(
            'tbody > tr > td::text').getall()

        countered_data: np.ndarray = np.array(countered_data)
        counter_data: np.ndarray = np.array(counter_data)
        countered_data = countered_data.reshape(
            countered_data.shape[0] // 3, 3)
        counter_data = counter_data.reshape(
            counter_data.shape[0] // 3, 3)

        base_heroe = response.url.split('/')[-2]

        for ced_data in countered_data:

            yield DotaScraperItem(**{
                'base_heroe_name': base_heroe,
                'heroe_name': ced_data[0],
                'value': ced_data[1],
                'win_rate': ced_data[2],
                'is_advantage': False
            })

        for cer_data in counter_data:

            yield DotaScraperItem(**{
                'base_heroe_name': base_heroe,
                'heroe_name': cer_data[0],
                'value': cer_data[1],
                'win_rate': cer_data[2],
                'is_advantage': True
            })

        next_page = self.__make_next_request(response.url)
        yield scrapy.Request(next_page, dont_filter=True, cb_kwargs={

        })

    def __make_next_request(self, url):

        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)

        if not query_params:
            ...
        else:

            for counter_param in CountersQueryParams.values:
                pass

        return

# params = {'lang':'en','tag':'python'}
# req = PreparedRequest()
# req.prepare_url(url, params)
# print(req.url)
