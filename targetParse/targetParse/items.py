# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import json
import pprint


class TargetItems(scrapy.Item):
	def __repr__(self):
		return f"""
{{
	'url': {self['url']},
	'title':{self['title']},
	'price':{self['price']},
	'currency':{self['currency']},
	'description':{self['description']},
	'tcin':{self['tcin']},
	'upc':{self['upc']},
	'specs':
{pprint.pformat(self['specs'], indent=12)}
}} """

    # define the fields for your item here like:
	url = scrapy.Field()
	title = scrapy.Field()
	price = scrapy.Field()
	currency = scrapy.Field()
	description = scrapy.Field()
	specs = scrapy.Field()
	upc = scrapy.Field()
	tcin = scrapy.Field()

