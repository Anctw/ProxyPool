from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
from bs4 import BeautifulSoup
import re

"""网站可以访问 重写代码爬取成功"""

# MAX_NUM = 9999
# BASE_URL = 'http://api.89ip.cn/tqdl.html?api=1&num={MAX_NUM}&port=&address=&isp='.format(MAX_NUM=MAX_NUM)
#
#
# class Ip89Crawler(BaseCrawler):
#     """
#     89ip crawler, http://api.89ip.cn
#     """
#     urls = [BASE_URL]
#
#     def parse(self, html):
#         """
#         parse html file to get proxies
#         :return:
#         """
#         ip_address = re.compile('([\d:\.]*)<br>')
#         hosts_ports = ip_address.findall(html)
#         for addr in hosts_ports:
#             addr_split = addr.split(':')
#             if(len(addr_split) == 2):
#                 host = addr_split[0]
#                 port = addr_split[1]
#                 yield Proxy(host=host, port=port)


MAX_PAGE = 113
BASE_URL = 'https://www.89ip.cn/index_{page}.html'

class Ip89Crawler(BaseCrawler):
    """
    89ip crawler, http://api.89ip.cn
    """
    urls = [BASE_URL.format(page=page) for page in range(1, MAX_PAGE + 1)]
    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        soup = BeautifulSoup(html, 'lxml')
        tr_list = soup.find_all('tr')
        for tr in tr_list:
            tds = tr.find_all('td')
            data_list = []
            if len(tds) >= 2:
                for td in tds:
                    data_list.append(td.string.strip())
                host = data_list[0]
                port = data_list[1]
                yield Proxy(host=host, port=port)

if __name__ == '__main__':
    crawler = Ip89Crawler()
    for proxy in crawler.crawl():
        print(proxy)
