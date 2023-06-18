import os
import scrapy

os.system("conda activate mlenv") # activate mlenv
os.system("cd news_crawler/spiders") # move to spider
with open("naver_news.json", 'r+') as f: f.truncate(0) # initialize json file
os.system("scrapy crawl newsbot") # crawl with scrapy
os.system("cat naver_news.json") # output crawled data

