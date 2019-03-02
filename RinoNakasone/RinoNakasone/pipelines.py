# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from ireadweek.models import Book
import datetime

import shutil
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

import requests


def save_img(img_url, name, path, referer):
    req = requests.get(img_url, headers={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                                         'Referer': referer})
    if not os.path.exists(path):
        os.mkdir(path)

    with open(path + "/" + name, 'wb') as f:
        f.write(req.content)


class RinonakasonePipeline(object):
    def process_item(self, item, spider):
        book = Book()
        book.name = item.get('name')
        book.author = item.get('author')
        book.category = item.get('category')
        book.score = item.get('score')
        book.img_url = item.get('img_url')
        book.download_url = item.get('download_url')
        book.introduction = item.get('introduction')
        book.author_info = item.get('author_info')
        book.directory = item.get('directory')
        book.create_edit = datetime.datetime.now()
        book.save()
        return item


class MZTImagesPipelinse(object):
    # IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
    #
    # def get_media_requests(self, item, info):
    #     image_url = item["img_url"]
    #     yield scrapy.Request(image_url, headers={'Referer': item['referer']})
    #
    # def item_completed(self, result, item, info):
    #     image_path = [x["path"] for ok, x in result if ok]
    #     img_path = item.get("path")
    #     name = item.get("name")
    #     if not os.path.exists(img_path):
    #         os.mkdir(img_path)
    #     # 将文件从默认下路路径移动到指定路径下
    #     shutil.move(self.IMAGES_STORE + "/" + image_path[0],
    #                 img_path + "/" + name)
    #     return item

    def process_item(self, item, spider):
        save_img(item.get("img_url"), item.get("name"), item.get("path"), item.get("referer"))
        return item
