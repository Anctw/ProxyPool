import time
from retrying import RetryError
from loguru import logger
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
import json

"""可以获取，获取的代理为 45.67.221.18:80:80  优化了一下"""

BASE_URL = 'https://www.docip.net/data/free.json?t={date}'



class DocipCrawler(BaseCrawler):
    """
    Docip crawler, https://www.docip.net/data/free.json
    """
    urls = [BASE_URL.format(date=time.strftime("%Y%m%d", time.localtime()))]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        try:
            result = json.loads(html)
            proxy_list = result['data']
            for proxy_item in proxy_list:
                origin_host = proxy_item['ip']
                host = proxy_item['ip'].split(':')[0]
                port = origin_host.split(':')[-1]
                yield Proxy(host=host, port=port)
        except json.JSONDecodeError:
            print("json.JSONDecodeError")
            return


if __name__ == '__main__':
    crawler = DocipCrawler()
    for proxy in crawler.crawl():
        print(proxy)
