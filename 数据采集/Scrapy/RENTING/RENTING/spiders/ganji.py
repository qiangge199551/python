# -*- coding: utf-8 -*-
import scrapy
from RENTING.items import RentingItem

class GanjiSpider(scrapy.Spider):
	name = 'ganji'
	allowed_domains = ['hz.ganji.com']
	start_urls = ['http://hz.ganji.com/fang1/o1/']
	def parse(self, response):
		items = RentingItem()
		for item in response.xpath('//*[@id]/dl[@class]'):
			try:
				items['name'] = item.xpath('./dd[1]/a/text()').extract()[0]
				items['info'] = item.xpath('./dd[2]/span/text()').extract()[0]
				items['address'] = ' '.join(item.xpath('./dd[3]/span/a/text()').extract())
				items['price'] = ''.join(item.xpath('./dd[5]/div[1]/span/text()').extract())
				items['publishTime'] = item.xpath('./dd[5]/div[2]/text()').extract()[0]				
			except:
				continue
			yield items
		if response.xpath('//ul/li/a[@class="next"]/@href').extract()[0]:
			url = str(self.start_urls[0].split('/fang1')[0]) + str(response.xpath('//ul/li/a[@class="next"]/@href').extract()[0])
			print(url)
			yield scrapy.Request(url, callback=self.parse)
