import scrapy
import json
import pprint
import logging
from ..items import TargetItems


# Spider for Target.com
class TargetSpider(scrapy.Spider):
	name = "TargetSpider"
	allowed_domains = ["target.com"]

	def __init__(self, *args, **kwargs):
		super(TargetSpider, self).__init__(*args, **kwargs)
		self.start_urls = [kwargs.get('start_url')]

	def parse(self, response):
		# parse result to:
		item = TargetItems()
		
		specs_raw = response.css('.h-padding-h-default div')
		# for loop to create dict of specs
		specs = {}
		for spec in specs_raw:
			vals = spec.css('div::text').getall()
			keys = spec.css('b::text').getall()
			if keys:
				if keys[0] == 'UPC' or keys[0] == 'TCIN':
					item[keys[0].lower()] = vals[1] if len(vals) > 1 else vals[0] 
					item[keys[0].lower()] = vals[1] if len(vals) > 1 else vals[0]
					continue
				specs[keys[0].replace(':','')] = vals[1] if len(vals) > 1 else vals[0]
		
		item["url"] = response.url
		item["title"] = response.css('.h-margin-b-tiny span::text').get()
		item["description"] = response.css('#specAndDescript .h-margin-v-default::text').get()
		item["specs"] = specs 

		price_url = 'https://redsky.target.com/web/pdp_location/v1/tcin/'+ item['tcin'] +'?pricing_store_id=3991&key=eb2551e4accc14f38cc42d32fbc2b2ea'
		yield scrapy.Request(price_url, callback=self.combine_parse, meta={'item': item})

	def combine_parse(self, response):
		item = response.meta['item']
		price_data = json.loads(response.body)
		price_raw = price_data['price']['formatted_current_price']
		item['price'] = price_raw[1:]
		# can create a dict of curencies and check if it is in it and grab corresponding value
		if price_raw[0] == '$':
			item['currency'] = 'USD'
		else:
			item['currency'] = 'other currency'

		logging.log(logging.CRITICAL, item)
		return item
