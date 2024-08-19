"""
    python在Flask服务中使用多进程池在web服务中实现加速（CPU密集）
"""

import math
import json
import flask
from concurrent.futures import ProcessPoolExecutor

app = flask.Flask(__name__)


def is_prime(n):
    """
        判断是不是素数
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    squrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, squrt_n + 1, 2):
        if n % i == 0:
            return False


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(',')]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))

def main():
    app.run()          # 运行之后要在网页打开那个网址，并且在后面加上"/is_prime/<numbers>"，numbers换成几个数字，比如1,2,3,4


if __name__ == '__main__':
    process_pool = ProcessPoolExecutor()        # 这个要放在所有函数声明之后才能用，跟p8对比
    main()
