# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class JobSpider(scrapy.Spider):
	name = 'job'
	allowed_domains = ['hr.tencent.com']
	base_url = 'https://hr.tencent.com/position.php?&start=3730'
	start_urls = [base_url,]
	def parse(self, response):
		items = TencentItem()
		for item in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
			try:
				items['title'] = item.xpath('./td[1]/a/text()').extract()[0]
				items['position'] = item.xpath('./td[2]/text()').extract()[0]
				items['PositionNumber'] = item.xpath('./td[3]/text()').extract()[0]
				items['link'] = 'https://hr.tencent.com/' + item.xpath('./td[1]/a/@href').extract()[0]
				items['location'] = item.xpath('./td[4]/text()').extract()[0]
				items['PublishTime'] = item.xpath('./td[4]/text()').extract()[0]
			except:
				continue
			yield items
		if response.xpath('//*[@id="next"]/@href').extract()[0]:
			url = self.base_url + response.xpath('//*[@id="next"]/@href').extract()[0]
			yield scrapy.Request(url, callback=self.parse)
