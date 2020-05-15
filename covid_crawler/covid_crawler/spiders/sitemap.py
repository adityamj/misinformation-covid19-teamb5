
import base64
import hashlib
import scrapy
import os.path


class sitemap_spider(scrapy.spiders.SitemapSpider):
    name = "sitemap"
    sitemap_urls = ['https://www.poynter.org/sitemap-ifcn_misinformation.xml']


    def parse(self, response):
        return {
            'title' : ' '.join(response.xpath('//div/main/article/div/header/h1/text()').getall()),
            'flag' : response.xpath('//div/main/article/div/header/h1/span/text()').get(),
            'url' : response.xpath('//div/main/article/div/div/div/a/@href').get(),
            'source': response.xpath('//div/main/article/div/div/div/p[1]/text()').get().split(':')[1].strip(),
            'country':response.xpath('//div/main/article/div/header/p[2]/strong/text()').get().split('|')[1].strip(),
            'date':response.xpath('//div/main/article/div/header/p[2]/strong/text()').get().split('|')[0].strip()
            }
