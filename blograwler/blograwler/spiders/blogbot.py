import scrapy

class NewsbotSpider(scrapy.Spider):
	name = 'blogbot'
	start_urls = ['https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5']

	def parse(self, response):
		titles = response.xpath('//*[@id="content"]/section/div[2]/div/div/div/div/a/text()').extract()
		# authors = response.css('.writing::text').extract()
		# previews = response.css('.lede::text').extract()

		for item in zip(titles):
			scraped_info = {
				'title' : item[0].strip()
				# 'author' : item[1].strip(),
				# 'preview' : item[2].strip(),
			}
			yield scraped_info