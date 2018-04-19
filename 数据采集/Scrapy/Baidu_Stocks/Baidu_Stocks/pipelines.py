# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaiduStocksPipeline(object):
    def process_item(self, item, spider):
        return item

class BaiduStocksPinfoipeline(object):
	"""docstring for BaiduStocksPinfoipeline"""
	def __init__(self, arg):
		super(BaiduStocksPinfoipeline, self).__init__()
		self.arg = arg
	def open_spider(self, spider):
		self.f = open('BaiduStockInfo.txt', 'w')

	def close_spider(self, spider):
		self.f.close()

	def process_item(self, item, spider):
		try:
			line = str(dict(item))
			self.f.write(line)
		except:
			pass

	