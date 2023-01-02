# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class CovidPipeline:
        def open_spider(self, spider):
                try:
                        self.file = open('1219.csv', "w", newline='', encoding="utf-8")
                        self.f_csv = csv.writer(self.file)  # 把列表对象数据写入到CSV文件中
                        first_line = [('疫情地区', '新增', '现有', '累计', '治愈', '死亡')]
                        self.f_csv.writerows(first_line)
                except Exception as err:
                        print(err)

        def process_item(self, item, spider):
                line = [item['疫情地区'], item['新增'], item['现有'], item['累计'],
                                item['治愈'], item['死亡']]  # 构造csv文件的一行
                self.f_csv.writerow(line)
                return item

        def close_spider(self, spider):
                self.file.close()