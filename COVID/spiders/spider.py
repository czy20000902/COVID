import scrapy
from scrapy.http import Request
from COVID.items import CovidItem
from selenium import webdriver
import time


class mySpider(scrapy.spiders.Spider):
        name = 'COVID'
        allowed_domains = ['https://voice.baidu.com/']
        start_urls = ["https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4"]
        # 多页爬取
        download_delay = 1

        def parse(self, response):
                driver = webdriver.Edge("E:\Download\edgedriver_win32\msedgedriver.exe")
                driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4")
                time.sleep(3)
                driver.find_element_by_xpath("/html/body/div[2]/div/div/div/section/div[2]/div[3]/div[4]/div[11]/div/span").click()
                time.sleep(1)
                js = "var q=document.documentElement.scrollTop=100000"
                driver.execute_script(js)
                item = CovidItem()
                for i in range(1, 214):
                        str = '//*[@id="foreignTable"]/table/tbody/tr/td/table/tbody/tr[{}]'.format(i)
                        item['疫情地区'] = driver.find_element_by_xpath(str + '/td[1]').text
                        item['新增'] = driver.find_element_by_xpath(str + '/td[2]').text
                        item['现有'] = driver.find_element_by_xpath(str + '/td[3]').text
                        item['累计'] = driver.find_element_by_xpath(str + '/td[4]').text
                        item['治愈'] = driver.find_element_by_xpath(str + '/td[5]').text
                        item['死亡'] = driver.find_element_by_xpath(str + '/td[6]').text
                        print(dict(item))
                        yield item
