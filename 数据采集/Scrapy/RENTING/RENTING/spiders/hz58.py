# -*- coding: utf-8 -*-
import scrapy
from RENTING.items import RentingItem

class Hz58Spider(scrapy.Spider):
	name = 'hz58'
	allowed_domains = ['hz.58.com']
	start_urls = ['http://hz.58.com/xiaoshan/zufang/pn1']

	def parse(self, response):
		items = RentingItem()
		# print(response.text)
		for item in response.xpath('//div[@class="listBox"]/ul/li'):
			try:
				items['name'] = ''.join(item.xpath('./div[@class="des"]/h2/a/text()').extract()).replace(' ', '').replace('\n', '')
				items['room'] = item.xpath('./div[@class="des"]/p[@class="room"]/text()').extract()[0].replace(' ', '').replace('\xa0', '')
				items['address'] = item.xpath('./div[@class="des"]/p[@class="add"]/a/text()').extract()[0].replace(' ', '')
				items['price'] = (item.xpath('./div/div[@class="money"]/b/text()').extract()[0] + '元/月').replace(' ', '')
				items['publishTime'] = item.xpath('./div[3]/div[@class="sendTime"]/text()').extract()[0].replace(' ', '').replace('\n', '')
				items['image'] = item.xpath('./div[1]/a/@href').extract()[0]
				# print(items, '\n----------------------------------------------------------------\n\n')
				yield items
			except:
				continue
		if response.xpath('//a[@class="next"]/span/text()').extract()[0]:
			url = response.xpath('//a[@class="next"]/@href').extract()[0]
			print('\n\n\n', '当前爬取页面：{}页'.format(url.split('pn')[-1].split('/')[0]), '\n\n\n')
			yield scrapy.Request(url, callback=self.parse)	
