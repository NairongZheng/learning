
import requests
import threading
import time

urls = [f"https://www.cnblogs.com/#p{page}" for page in range(1, 50 + 1)]


# 爬
def craw(url):
    r = requests.get(url)
    print(url, len(r.text))


# 单线程
def single_thread():
    print("single_thread begin")
    for url in urls:
        craw(url)
    print("single_thread end")


# 多线程
def multi_thread():
    print("multi_thread begin")
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=craw, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("multi_thread end")


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread cost: ", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread cost: ", end - start, "seconds")
