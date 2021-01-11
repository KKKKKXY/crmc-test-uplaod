# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from postscrape.reg import *
from itemadapter import ItemAdapter
import json

class PostscrapePipeline(object):
    # def __init__(self, *args, **kwargs):
    #     self.items = []

    # def open_spider(self, spider):
    #     pass

    # def close_spider(self, spider):
    #     pass

    # def process_item(self, item, spider):
    #     print('========================process item====================================')
    #     print(item)
    #     company_id         = item['company_id']

    #     company_type       = item['company_type']
    #     status             = item['status']
    #     objective          = item['objective']
    #     raw_directors      = item['directors']
    #     raw_company_name   = item['company_name']
    #     raw_bussiness_type = item['bussiness_type']
    #     raw_address        = item['address']#new

    #     #clean data
    #     directors      = directors_convert(raw_directors)
    #     # print(directors_text)
    #     bussiness_type      = business_type_separater(raw_bussiness_type)[1]
    #     # print(bussiness_type)
    #     bussiness_type_code = business_type_separater(raw_bussiness_type)[0]
    #     # print(bussiness_type_code)
    #     company_name        = re.split(':', raw_company_name)[1].strip()
    #     # print(company_name)
    #     street             = address_separater(raw_address)[0]
    #     subdistrict        = address_separater(raw_address)[1]
    #     district           = address_separater(raw_address)[2]
    #     province           = address_separater(raw_address)[3]
    #     address            = address_separater(raw_address)[4]
    
    #     self.items.append({
    #         'company_name': company_name,
    #         'company_id': company_id,
    #         'company_type': company_type, 
    #         'status': status,
    #         'address': address,
    #         'objective': objective,
    #         'directors': directors,
    #         'bussiness_type': bussiness_type,
    #         'bussiness_type_code': bussiness_type_code,
    #         'street': street,
    #         'subdistrict': subdistrict,
    #         'district': district,
    #         'province': province,
    #     })
    #     print('========================clean data========================')
    #     print(self.items)
        return item