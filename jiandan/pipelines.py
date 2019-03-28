# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib.request
from jiandan import settings

class JiandanPipeline(object):
    def process_item(self, item, spider):
        dir_path = '%s/%s'%(settings.IMAGE_STOR, spider.name)
        print(dir_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['image_urls']:
            list_name = image_url.split("/")
            file_name = list_name[len(list_name)-1]
            file_path = '%s/%s'%(dir_path,file_name)
            if os.path.exists(file_path):
                continue
            with open(file_path,"wb") as file_write:
                if image_url.startswith('//'):
                    image_url = image_url.replace('//','http://')
                print(image_url)
                conn = urllib.request.urlopen(image_url)
                file_write.write(conn.read())
            file_write.close()
        return item