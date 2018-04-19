# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class RentingPipeline(object):
	def process_item(self, item, spider):
		try:
			pymongo.MongoClient('localhost')['RENTING']['ganji'].insert(dict(item))
			print('SAVE TO MONGODB SUCCESSFULLY\n')
		except:
			print('FAIL TO SVAE TO MONGODB\n')
		return item
