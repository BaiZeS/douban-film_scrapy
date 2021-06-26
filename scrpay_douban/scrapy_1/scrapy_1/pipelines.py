# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Scrapy1Pipeline(object):
    def process_item(self, item, spider):
        #将spider传入的字典数据存入本地
        title = item['title']
        discrabe = item['discrabe']
        print(title+'\tcompletion')
        # save_data = ','.join(data)  #将列表拼接成字符串并用'，'隔开
        with open('.\\douban\\%s.txt' % title,'w',encoding='utf-8') as f:
            f.write(discrabe)
            f.close()
        return item
