# coding: utf8

from .models import Book


def get_books(where, limit, offset):
    """
    获取书籍的信息
    :param where:
    :param limit:
    :param offset:
    :return:
    """
    fields = ['id', 'name', 'author', 'category', 'score', 'img_url', 'download_url', 'introduction', 'author_info',
              'directory', 'create_edit']
    # TODO where的数据验证 cerberus
    records = Book.objects.values(*fields).all()[offset:limit + offset]
    data = [i for i in records]
    return data
