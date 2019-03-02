# coding: utf8
from scrapy import cmdline

"""main"""


def main():
    cmdline.execute('scrapy crawl meizitu'.split())


if __name__ == '__main__':
    main()
