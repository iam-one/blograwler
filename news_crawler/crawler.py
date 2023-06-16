import os

os.system("conda activate mlenv")
os.system("cd news_crawler/spiders")
with open("naver_news.json", 'r+') as f: f.truncate(0)
os.system("scrapy crawl newsbot")
os.system("cat naver_news.json")