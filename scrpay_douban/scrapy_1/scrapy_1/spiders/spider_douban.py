# -*- coding: utf-8 -*-
import scrapy


class SpiderDoubanSpider(scrapy.Spider):
    name = 'spider_douban'
    allowed_domains = ['douban.com']
    # start_urls = ['http://blog.csdn.net/']
    #
    # def parse(self, response):
    #     print('-' * 30)
    #     print(response.xpath('//div[@class="nav_com"]//li/a/text()').extract())
    #     print('-' * 30)
    def start_requests(self):
        #返回Requ对象给shudeler调度器
        page_s = int(input('start page:'))
        page_e = int(input('end page:'))
        for page in range(page_s-1,page_e):
            link_page = 'https://www.douban.com/doulist/240962/?start=%d&sort=seq&playable=0&sub_type=' %(25*page)
            print('开始传输：%d' % page)
            yield scrapy.Request(
                url = link_page,
                callback = self.parse
            )

    def parse(self,response):
        #抓取一级页面获得标题链接
        links = response.xpath('//div[@class="article"]/div[@class="doulist-item"]//div[@class="title"]/a/@href').extract()
        #将抓取数据传给pares2
        for link in links:
            # print(link)
            yield scrapy.Request(
                url = link,
                callback = self.parse2
            )

    def parse2(self,response):
        #抓取二级页面数据
        title = response.xpath('//div[@id="wrapper"]//h1/span/text()').extract_first()
        discrabe = response.xpath('//div[@class="indent"]//span[@property="v:summary"]/text()').extract_first()
        #将页面数据传给pipeline
        item = dict(
            title = title,
            discrabe = discrabe,
        )
        yield item
