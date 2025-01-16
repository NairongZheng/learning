import tornado.ioloop
import tornado.web
import tornado.httpserver
from instance_handler import SumHandler, UpperHandler


def make_app():
    return tornado.web.Application(
        [
            (r"/sumHandler", SumHandler),
            (r"/upperHandler", UpperHandler, dict(test_para="Successful parameter passing")),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    http_port = 12300
    server.listen(http_port)
    print(f"debug damonzheng, listen on {http_port}")
    tornado.ioloop.IOLoop.current().start()
