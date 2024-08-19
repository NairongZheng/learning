"""
    线程池
"""

import requests
import concurrent.futures
from bs4 import BeautifulSoup

urls = [f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)]


# craw
def craw(url):
    r = requests.get(url)
    return r.text


# parse
def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('a', class_='post-item-title')
    return [(link['href'], link.get_text()) for link in links]


def main():
    # craw
    with concurrent.futures.ThreadPoolExecutor() as pool:       # 第一种用pool.map，不能随时提交任务，要把任务按照列表准备好(如urls)，并且顺序返回
        htmls = pool.map(craw, urls)
        htmls = list(zip(urls, htmls))
        for url, html in htmls:
            print(url, len(htmls))
    print('craw over')


    # parse
    with concurrent.futures.ThreadPoolExecutor() as pool:       # 第二种用pool.submit，返回future，可以用future.result()获取结果，获取也有两种方法
        futures = {}
        for url, html in htmls:
            future = pool.submit(parse, html)
            futures[future] = url

        # # 第一种获取方法，字典按key，所以顺序
        # for future, url in futures.items():
        #     print(url, future.result())

        # 第二种获取方法，不是顺序
        for future in concurrent.futures.as_completed(futures):     # as_completed哪个任务先完成，就先返回哪个
            url = futures[future]
            print(url, future.result())

    print('parse over')


if __name__ == '__main__':
    main()