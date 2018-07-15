# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from urllib.parse import urljoin

DOMAIN = 'http://www.biquge.com.tw'


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['www.biquge.com.tw']
    start_urls = ['http://www.biquge.com.tw/0_276/']

    def parse(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'html.parser')

        a = soup.find('div', id="list")
        for i in a.findAll('a'):
            url = i.attrs.get('href')
            full_url = urljoin(DOMAIN, url)
            yield scrapy.Request(full_url, callback=self.parse_news)

    def parse_news(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'html.parser')
        title = soup.find('title').text
        cont = soup.find('div', id='content').text.replace('\xa0\xa0\xa0\xa0', '')

        with open("/Users/youdi/Project/python/Rino_nakasone_backend/RinoNakasone/book/{}.txt".format(title), 'w') as f:
            f.write(cont)
        print(title)
        print(cont)
