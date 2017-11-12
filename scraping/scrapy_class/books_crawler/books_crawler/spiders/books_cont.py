# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

class BooksSpider(Spider):
    name = 'books_cont '
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']


    def parse(self, response):
        books = response.xpath('//h3/a/@href').extract()

        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)

        next_page_url = response.xpath('//a[text()="next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request()

        def parse_book(self, response):
            pass
        #yield {'URL': response.url}
