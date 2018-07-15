# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from six.moves import urllib
DOMAIN = 'http://flagpedia.asia'


class FlagSpider(scrapy.Spider):
    name = 'flag'
    allowed_domains = ['flagpedia.asia', 'flags.fmcdn.net']
    start_urls = ['http://flagpedia.asia/index']

    def parse(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'html.parser')

        a = soup.findAll('td', class_="td-flag")
        for i in a:
            url = i.a.attrs.get("href")
            full_url = urljoin(DOMAIN, url)
            yield scrapy.Request(full_url, callback=self.parse_news)

    def parse_news(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'html.parser')
        p = soup.find("p", id="flag-detail")
        img_url = p.img.attrs.get("srcset").split(" 2x")[0]
        url = "http:" + img_url
        img_name = img_url.split("/")[-1]

        urllib.request.urlretrieve(url, "/Users/youdi/Project/python/Rino_nakasone_backend/RinoNakasone/flag/{}".format(img_name))
        print(url)