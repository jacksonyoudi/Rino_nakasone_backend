# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from RinoNakasone.settings import DOMAIN, CDN
from urllib.parse import urljoin
from RinoNakasone.items import IreadweekItem


class IreadweekSpider(scrapy.Spider):
    name = 'ireadweek'
    allowed_domains = ['www.ireadweek.com']
    start_urls = ['http://www.ireadweek.com/']

    def parse(self, response):
        # response._declared_encoding = 'utf-8'
        # response._encoding = 'utf-8'
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'html.parser')

        # names = soup.find_all('div', class_="hanghang-list-name")
        # hrefs = [i.parent.parent.attrs.get('href') for i in names]

        for i in soup.find_all('div', class_="hanghang-list-name"):
            if i.parent.parent.attrs.get('href'):
                url = i.parent.parent.attrs.get('href')
                full_url = urljoin(DOMAIN, url)
                yield scrapy.Request(full_url, callback=self.parse_news)

        next_url = urljoin(DOMAIN, soup.find_all('a')[-2].attrs.get('href'))
        yield scrapy.Request(next_url, callback=self.parse)

    def parse_news(self, response):
        item = IreadweekItem()
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'html.parser')

        img_url = urljoin(CDN, soup.find('img').attrs.get('src').replace('//', '/'))


        download_url = soup.find('a', class_='downloads').attrs.get('href')
        title = soup.find_all('div', class_='hanghang-za-title')
        name = title[0].text

        content = soup.find_all('div', class_='hanghang-za-content')
        author_info = content[0].text
        directory = '\n'.join([i.text.replace("\u3000", '') for i in content[1].find_all('p')])

        info = soup.find('div', class_='hanghang-shu-content-font').find_all('p')

        author = info[0].text.split('作者：')[1]
        category = info[1].text.split('分类：')[1]
        score = info[2].text.split('豆瓣评分：')[1]
        introduction = info[4].text

        item['name'] = name
        item['img_url'] = img_url
        item['download_url'] = download_url
        item['author'] = author
        item['author_info'] = author_info
        item['category'] = category
        item['score'] = score
        item['introduction'] = introduction
        item['directory'] = directory

        return item
