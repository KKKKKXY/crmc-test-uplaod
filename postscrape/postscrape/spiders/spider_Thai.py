import os, time, re, pickle, signal
import pytesseract
from PIL import Image
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import scrapy
import json
from postscrape.items import PostscrapeItem

class DBDSpider(scrapy.Spider):
    name = "dbd"
    # start_urls = ['https://datawarehouse.dbd.go.th/company/profile/5/0105554123553']
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    allowed_domains = ["datawarehouse.dbd.go.th"]

    def start_requests(self):
        urls = [
            "https://datawarehouse.dbd.go.th/company/profile/5/0105554123553"
        ]
        for url in urls:
            yield scrapy.Request(url=url, cookies={"JSESSIONID":self.getCookie}, callback=self.parse)

    def getCookie(self):
        cookie_path = '/Users/mya/Desktop/Development/scrapyTest/postscrape/postscrape/spiders/temp/cookie.json'
        if os.path.isfile(cookie_path):
            try:
                with open(cookie_path, 'rb') as f: 
                    cookies = pickle.load(f)
            except EOFError:
                cookies = None

        for i in cookies:
            if i['name']=='JSESSIONID':
                cookies= i['value']
                break
        print(cooikes)
        return cookies

    def writeJsonFile(self, data):
        filePath = '/Users/mya/Desktop/Development/scrapyTest/postscrape/postscrape/spiders/temp/thaiVersion.json'
        a_file = open(filePath, "w", encoding='utf-8')
        line = json.dumps(dict(data), ensure_ascii=False) + "\n"
        a_file.write(line)
        # json.dumps(data, a_file, ensure_ascii=False)
        # with open(filePath, 'w') as fb:
        #     json.dump(data, ensure_ascii=False)

    # def jsonload(self):
    #     filePath = '/Users/mya/Desktop/Development/scrapyTest/postscrape/postscrape/spiders/temp/data.json'
    #     data = json.load(open(filePath))
    #     # print(data)
    #     print("----Starting Dump----")
    #     dumpdata = json.dumps(data) #json.dumps take a dictionary as input and returns a string as output.
    #     print(dumpdata)
    #     print("----Starting Loads----")
    #     dict_json=json.loads(dumpdata) # json.loads take a string as input and returns a dictionary as output.
    #     print(dict_json)

    #     # Store Data into target file
    #     with open(filePath, "w") as outfile:  
    #         json.load(dict_json)
    #     for i in dict_json:
    #         with open(filePath, 'w') as f:
    #             json.dump(dict_json, f)
    #         print(dict_json)
    #     return dict_json

    def readLoadsFile(self):
        loadsfilePath = '/Users/mya/Desktop/Development/scrapyTest/postscrape/companyInfo_Thai.json'
        print('------------Target Company Information------------')
        loadsdata = json.load(open(loadsfilePath))
        dumpdata = json.dumps(loadsdata)
        print(dumpdata)

    def parse(self, response):
        print('------------START SCRAPING------------')
        time.sleep(5)
        # Request(url="https://datawarehouse.dbd.go.th/company/profile/5/0105554123553", cookies=self.getTokenAndStore())
        objective = response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[5]/div/p/text()').get()
        if objective == '-':
            objective = response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[3]/div/p/text()').get()

        director_list = []
        directors = response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/ol/li/text()').getall()
        for i in directors:
            director_list.append(i.strip())

        raw_bussiness_type = response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[4]/div/p/text()').get()
        try:
            raw_bussiness_type = raw_bussiness_type.strip()
        except:
            raw_bussiness_type = 'ERRRRRRRRRRRRRRRRRRRORRRRRRRRRRRRRRRRRRRRRR:' + response.url.split('/')[-1]

        if raw_bussiness_type == '-':
            raw_bussiness_type = response.xpath('/html/body/div/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[3]/div[2]/div/p/text()').get().strip()

        item = {}
        item['companies'] = []
        item['companies'].append({
            'company_name': response.xpath('/html/body/div/div[4]/div[2]/div[1]/div[1]/h2/text()').get(),
            'company_id': '0105554123553',
            'company_type': response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table/tr[1]/th[2]/text()').get(),
            'status': response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table/tr[3]/td[2]/text()').get(),
            'address': response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/table/tr[2]/td/text()').get(),
            'objective': objective,
            'directors': director_list,
            'bussiness_type': raw_bussiness_type 
        })

        # item['company_name']   = response.xpath('/html/body/div/div[4]/div[2]/div[1]/div[1]/h2/text()').get()
        # item['company_id']     = '0105554123553'
        # item['company_type']   = response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table/tr[1]/th[2]/text()').get()
        # item['status']         = response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table/tr[3]/td[2]/text()').get()
        # item['address']        = response.xpath('/html/body/div[1]/div[4]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/table/tr[2]/td/text()').get()
        # item['objective']      = objective
        # item['directors']      = director_list
        # item['bussiness_type'] = raw_bussiness_type

        self.writeJsonFile(item)
        print('######### Target Company Information #########')
        return item




# import scrapy
# from scrapy.http import FormRequest

# class PostsSpider(scrapy.Spider):
#     name = "posts"

#     start_urls = [
#         'https://datawarehouse.dbd.go.th/'
#     ]

#     def parse(self, response):
#         token = response.css().extract_first()
#         return FormRequest.from_response(response, formdata={
#             'JSESSIONID': 'ZTU5ZjNiMTUtMTA4Ny00Y2Q5LTk4Y2MtZTUxZTllZTk2Mjgw'
#         }, callback= self.start_scraping)

#     def start_scraping(self, response):






# ----------------

# class PostsSpider(scrapy.Spider):
#    name = "posts"

# def parse(self, response):
#     # do something
#     yield scrapy.Request(
#         url= "https://datawarehouse.dbd.go.th/company/profile/5/0105554123553",
#         cookies= {
#             'JSESSIONID':'ZTU5ZjNiMTUtMTA4Ny00Y2Q5LTk4Y2MtZTUxZTllZTk2Mjgw',
#         },
#         callback= self.parse

#     for post in response.css('div.container-fluid'):
#             yield {
#                 'title': post.css('.navbar-info hidden-sm hidden-xs h2 a::text')[0].get(),
#             }
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)
#     )

# ----------------

# import scrapy

# class PostsSpider(scrapy.Spider):
#     name = "posts"

#     start_urls = [
#         'https://datawarehouse.dbd.go.th/'
#     ]

#     # def parse(self, response):
#     #     return [FormRequest.from_response(response,
#     #                 formdata={'captchaCode': 'fyfpm'},
#     #                 callback=self.after_login)]

#     # def after_login(self, response):
#     # # check login succeed before going on
#     # if "authentication failed" in response.body:
#     #     self.log("Login failed", level=log.ERROR)
#     #     return
#     # # We've successfully authenticated, let's have some fun!
#     # else:
#     #     return Request(url="https://datawarehouse.dbd.go.th/company/profile/5/0105554123553",
#     #            callback=self.parse_tastypage)

#     # def parse(self, response):
#     #     filename = 'posts.html'
#     #     with open(filename, 'wb') as f:
#     #         f.write(response.body)
#         # for post in response.css('div.post-item'):
#         #     yield {
#         #         'title': post.css('.post-header h2 a::text')[0].get(),
#         #         'date': post.css('.post-header a::text')[1].get(),
#         #         'author': post.css('.post-header a::text')[2].get()
#         #     }
#         # next_page = response.css('a.next-posts-link::attr(href)').get()
#         # if next_page is not None:
#         #     next_page = response.urljoin(next_page)
#         #     yield scrapy.Request(next_page, callback=self.parse)