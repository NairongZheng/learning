"""
    爬取网页里所有的标题和链接
"""
import requests
from bs4 import BeautifulSoup
import threading
import time
import random
import queue

urls = [f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)]


# 生产者，爬html的内容
def craw(url):
    r = requests.get(url)
    return r.text


# 消费者，解析生产者爬出来的内容
def parse(html):
    soup = BeautifulSoup(html, "html.parser")       # 第一个参数是要被解析的文档字符串或是文件句柄，第二个参数用来标识怎样解析文档
    links = soup.find_all('a', class_='post-item-title')    # 'a'是这个网页里面标题的标签
    return [(link['href'], link.get_text()) for link in links]


def do_craw(url_queue, html_queue):
    while True:
        url = url_queue.get()
        html = craw(url)
        html_queue.put(html)
        print(threading.current_thread().name, f"craw {url}", "url_queue.size=", url_queue.qsize())
        time.sleep(random.randint(1, 2))


def do_parse(html_queue, fout):
    while True:
        html = html_queue.get()
        results = parse(html)
        for result in results:
            fout.write(str(result) + "\n")
        print(threading.current_thread().name, f"results.size", len(results), "html_queue.size=", html_queue.qsize())
        time.sleep(random.randint(1, 2))


def main():
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for url in urls:            # 把要爬取的所有url放进queue
        url_queue.put(url)
    
    for idx in range(3):        # 开启三个生产者线程。生产者爬取url的内容，并放进html的queue
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue), name=f"craw {idx}")
        t.start()

    fout = open('p5_producer_consumer_spider_02.txt', 'w')
    for idx in range(2):        # 开启两个消费者线程，消费者解析html的内容，存到文件中
        t = threading.Thread(target=do_parse, args=(html_queue, fout), name=f"parse {idx}")
        t.start()


if __name__ == '__main__':
    main()