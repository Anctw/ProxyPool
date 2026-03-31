from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy
import re
from pyquery import PyQuery as pq

""" 免费的国内代理大部分失效 可爬取海外代理 重写代码爬取成功 """

# BASE_URL = 'https://www.kuaidaili.com/free/{type}/{page}/'
# MAX_PAGE = 3
#
#
# class KuaidailiCrawler(BaseCrawler):
#     """
#     kuaidaili crawler, https://www.kuaidaili.com/
#     """
#     urls = [BASE_URL.format(type=type,page=page)  for type in ('intr','inha', 'dps', 'fps') for page in range(1, MAX_PAGE + 1)]
#
#     def parse(self, html):
#         """
#         parse html file to get proxies
#         :return:
#         """
#         doc = pq(html)
#         for item in doc('table tr').items():
#             td_ip = item.find('td[data-title="IP"]').text()
#             td_port = item.find('td[data-title="PORT"]').text()
#             if td_ip and td_port:
#                 yield Proxy(host=td_ip, port=td_port)


BASE_URL = 'https://www.kuaidaili.com/free/{type}/{page}/'
MAX_PAGE = 10


class KuaidailiCrawler(BaseCrawler):
    """
    kuaidaili crawler, https://www.kuaidaili.com/
    """
    urls = [BASE_URL.format(type=type, page=page) for type in ('intr', 'inha', 'dps', 'fps') for page in range(1, MAX_PAGE + 1)]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        doc = pq(html)
        for item in doc('tbody tr').items():
            td_ip = item.find('td')[0].text
            td_port = item.find('td')[1].text
            if td_ip and td_port:
                yield Proxy(host=td_ip, port=td_port)

if __name__ == '__main__':
    crawler = KuaidailiCrawler()
    for proxy in crawler.crawl():
        print(proxy)
