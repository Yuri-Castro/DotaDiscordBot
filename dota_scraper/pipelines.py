# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.automap import automap_base

from dota_scraper.database import db_session


class DotaScraperPipeline:
    db_url = 'sqlite:///../db.sqlite3'

    def open_spider(self, spider):
        engine = create_engine(self.db_url, convert_unicode=True)
        Session = sessionmaker(engine)

        Base = automap_base()
        Base.prepare(engine, reflect=True)

        self.session = Session()
        self.Base = Base

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):

        return item
