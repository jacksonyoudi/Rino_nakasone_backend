# coding=utf-8

import scrapy
from bs4 import BeautifulSoup
from RinoNakasone.items import MeiZiTuItem


class MeiZiTuSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['www.mzitu.com']
    # custom_settings = {
    #     "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    #     "REFERER": 'http://i.meizitu.net'
    # }
    start_urls = ['https://www.mzitu.com/']

    def parse(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'html.parser')

        li_list = soup.find(id="pins").find_all(name="li")
        next_url_ele = soup.find("a", class_="next page-numbers")
        for li in li_list:
            img_ele = li.find("a")
            if img_ele:
                full_url = img_ele.get("href")
                yield scrapy.Request(full_url, callback=self.parse_detail, meta={"url": full_url})

        if next_url_ele:
            next_url = next_url_ele.get("href")
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'html.parser')
        span = soup.find(class_="pagenavi").findAll('span')
        title = soup.find('h2', class_="main-title").text

        if len(span) >= 2:
            total = int(span[-2].text)
            for i in range(1, total + 1):
                url = response.meta.get("url") + "/{}".format(i)
                path = "/Users/youdi/Project/python/Rino_nakasone_backend/RinoNakasone/img/{}".format(title)
                item = MeiZiTuItem(title=title, name=str(i) + ".jpg", path=path, referer=url)
                yield scrapy.Request(url, callback=self.parse_img, meta={"item": item})

    def parse_img(self, response):
        item = response.meta.get("item")
        html_doc = response.body
        soup = BeautifulSoup(html_doc, 'html.parser')
        img_url = soup.find('img', alt=item.get("title")).get("src")
        if img_url:
            item["img_url"] = img_url
            return item
