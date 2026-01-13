"""
    爬取网页里所有的标题和链接
"""
import requests
from bs4 import BeautifulSoup
import threading
import time

urls = [f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)]


# 生产者，爬html的内容
def craw(url):
    r = requests.get(url)
    return r.text


# 消费者，解析生产者爬出来的内容
def parse(html):
    soup = BeautifulSoup(html, "html.parser")   # 第一个参数是要被解析的文档字符串或是文件句柄，第二个参数用来标识怎样解析文档
    links = soup.find_all('a', class_='post-item-title')    # 'a'是这个网页里面标题的标签
    return [(link['href'], link.get_text()) for link in links]


if __name__ == '__main__':
    for result in parse(craw(urls[0])):
        print(result)
