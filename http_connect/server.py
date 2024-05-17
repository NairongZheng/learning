import tornado.ioloop
import tornado.web
import tornado.httpserver


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            data = self.request.body.decode("utf-8")
            upper_case_data = data.upper()
            self.write({"success": True, "data": upper_case_data})
        except Exception as e:
            self.write({"success": False, "error": str(e)})


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()
