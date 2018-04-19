# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
client = pymongo.MongoClient('localhost')
db = client['JOB']

class TencentPipeline(object):
	def process_item(self, item, spider):
		try:
			db['Tencent'].insert(dict(item))
			print('SAVE TO MONGODB SUCCESSFULLY')
		except:
			print('FAIL TO SAVE TO MONGODB')	
		return item
