"""
    python在Flask服务中使用线程池在web服务中实现加速（IO密集）
"""
import flask
import json
import time
from concurrent.futures import ThreadPoolExecutor


app = flask.Flask(__name__)
pool = ThreadPoolExecutor()     # 定义在哪里都可以，多进程共享当前进程的所有环境


def read_file():
    time.sleep(0.1)
    return "file result"


def read_db():
    time.sleep(0.2)
    return "db result"


def read_api():
    time.sleep(0.3)
    return "api result"


@app.route("/")
def index():
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)

    return json.dumps({"result_file": result_file.result(), 
                       "reuslt_dp": result_db.result(),
                       "result_api": result_api.result()})


def main():
    app.run()


if __name__ == '__main__':
    main()