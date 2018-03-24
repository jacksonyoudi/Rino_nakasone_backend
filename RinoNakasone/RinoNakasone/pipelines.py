# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from ireadweek.models import Book
import datetime


class RinonakasonePipeline(object):
    def process_item(self, item, spider):
        book = Book()
        book.name = item.get('name')
        book.author = item.get('author')
        book.category = item.get('category')
        book.score = item.get('score')
        book.image_url = item.get('image_url')
        book.download_url = item.get('download_url')
        book.introduction = item.get('introduction')
        book.author_info = item.get('author_info')
        book.directory = item.get('directory')
        book.create_edit = datetime.datetime.now()
        book.save()
        return item
