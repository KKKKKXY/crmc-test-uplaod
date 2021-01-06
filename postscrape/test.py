# import json

# for line in open('items.jl'):
#     data = json.loads(line)

# def jsonload():

# item['companies'].append({'company_name':"\u0e0a\u0e37\u0e48\u0e2d\u0e19\u0e34\u0e15\u0e34\u0e1a\u0e38\u0e04\u0e04\u0e25 : \u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17 \u0e42\u0e2d\u0e40\u0e1e\u0e19\u0e04\u0e25\u0e32\u0e27\u0e14\u0e4c \u0e08\u0e33\u0e01\u0e31\u0e14",'company_id':"0105554123553",'company_type':"\u0e1a\u0e23\u0e34\u0e29\u0e31\u0e17\u0e08\u0e33\u0e01\u0e31\u0e14",'status': "\u0e22\u0e31\u0e07\u0e14\u0e33\u0e40\u0e19\u0e34\u0e19\u0e01\u0e34\u0e08\u0e01\u0e32\u0e23\u0e2d\u0e22\u0e39\u0e48",'address':"857 \u0e0b\u0e2d\u0e22\u0e40\u0e1e\u0e0a\u0e23\u0e40\u0e01\u0e29\u0e2194  \u0e41\u0e02\u0e27\u0e07\u0e1a\u0e32\u0e07\u0e41\u0e04\u0e40\u0e2b\u0e19\u0e37\u0e2d \u0e40\u0e02\u0e15\u0e1a\u0e32\u0e07\u0e41\u0e04 \u0e01\u0e23\u0e38\u0e07\u0e40\u0e17\u0e1e\u0e21\u0e2b\u0e32\u0e19\u0e04\u0e23",'objective':"\u0e01\u0e32\u0e23\u0e43\u0e2b\u0e49\u0e04\u0e33\u0e1b\u0e23\u0e36\u0e01\u0e29\u0e32\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e2b\u0e32\u0e40\u0e01\u0e35\u0e48\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e0b\u0e2d\u0e1f\u0e15\u0e4c\u0e41\u0e27\u0e23\u0e4c",'directors':["\u0e19\u0e32\u0e22\u0e40\u0e09\u0e25\u0e34\u0e21\u0e1e\u0e25 \u0e28\u0e23\u0e35\u0e2a\u0e38\u0e27\u0e23\u0e23\u0e13/"],'bussiness_type':"62022 \u0e01\u0e34\u0e08\u0e01\u0e23\u0e23\u0e21\u0e01\u0e32\u0e23\u0e43\u0e2b\u0e49\u0e04\u0e33\u0e1b\u0e23\u0e36\u0e01\u0e29\u0e32\u0e17\u0e32\u0e07\u0e14\u0e49\u0e32\u0e19\u0e0b\u0e2d\u0e1f\u0e15\u0e4c\u0e41\u0e27\u0e23\u0e4c"})



# # Define here the models for your spider middleware
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# import time
# import os.path
# import requests
# import pickle
# import os
# from scrapy import signals

# from scrapy.http import HtmlResponse
# from requests.exceptions import Timeout
# from scrapy.downloadermiddlewares.retry import RetryMiddleware

# # useful for handling different item types with a single interface
# from itemadapter import is_item, ItemAdapter


# class PostscrapeSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.

#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s

#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.

#         # Should return None or raise an exception.
#         return None

#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.

#         # Must return an iterable of Request, or item objects.
#         for i in result:
#             yield i

#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.

#         # Should return either None or an iterable of Request or item objects.
#         pass

#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.

#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r

#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)


# class PostscrapeDownloaderMiddleware(RetryMiddleware):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.

#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s

#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.

#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called

#         #load cookie from local
#         cookie_path = '/Users/mya/Desktop/Development/scrapyTest/postscrape/postscrape/spiders/temp/cookie.json'
#         if os.path.isfile(cookie_path):
#             try:
#                 with open(cookie_path, 'rb') as f: 
#                     cookies = pickle.load(f)
#             except EOFError:
#                 cookies = None

#         for i in cookies:
#             if i['name']=='JSESSIONID':
#                 cookies= i['value']
#                 break

#         try:
#             response = requests.get(request.url, cookies = {'JSESSIONID':cookies}, timeout=10)
#             html = str(response.content,'utf-8')
#             page =  html
#             scrapy_response = HtmlResponse(url=request.url, body=page, request=request, encoding='utf-8')
#             scrapy_response.status_code = response.status_code

#         except Timeout:
#             print('Get page time out!')
#             request.status = False
#             scrapy_response = HtmlResponse(url=request.url, body='', request=request, encoding='utf-8')
#             scrapy_response.status_code = 'timeout'
#             return scrapy_response

#         return scrapy_response

#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.

#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         code = response.status_code

#         if code == 404:
#             #if the company cannot be found
#             print(f'Downloader: cannot find the page in datawarehouse {response.url}')
#             request.status = False

#         # elif code == 200:
#         #     #find the search bar
#         #     search_bar = response.xpath('/html/body/div/div[4]/div[1]')
#         #     if search_bar:
#         #         # if search bar exist but the name is not exist. the company is not exist
#         #         check = response.xpath('/html/body/div/div[4]/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/h2/text()')
#         #         if not check:
#         #             request.status = False
#         #         else:
#         #             request.status = True
#         #     else:
#         #         print(f'time out {request.url}')
#         #         request.status = False
#         #         return self._retry(request, response, spider) or response

#         elif code == 'timeout':
#             print(f'time out {request.url}')
#             request.status = False
#             return self._retry(request, response, spider) or response

#         elif code == 401:
#             #if cookie died
#             #raise CloseSpider('@@@@@@@@@@@@@@@the cooike expired in scraping@@@@@@@@@@@@@@@@')
#             print('Downloader: cookie expired!')
#             spider.close_it = 'cookie expired!'
#         elif  code == 500 or code == 503:
#             #if the server down:500, 503
#             #or some error system does not know: 000

#             #self.fake_browser.driver.save_screenshot('failed.png')
#             #raise CloseSpider('@@@@@@@@@@@@@@@@@@@@the server is down! Please try to run it later@@@@@@@@@@@@@@@@@')
#             print(f'Downloader: server is down! code{code}')
#             spider.close_it = f'server is down! code{code}'
#         else:
#             print(f'Downloader: unexpect error! code {code}')
#             spider.close_it = f'unexpect error! code{code}'

#         return response

#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.

#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass

#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
