"""
    python在Flask服务中使用线程池在web服务中实现加速（IO密集）
"""
import flask
import json
import time


app = flask.Flask(__name__)


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
    result_file = read_file()
    result_db = read_db()
    result_api = read_api()

    return json.dumps({"result_file": result_file, 
                       "reuslt_dp": result_db,
                       "result_api": result_api})


def main():
    app.run()       # 运行之后要在网页打开那个网址


if __name__ == '__main__':
    main()