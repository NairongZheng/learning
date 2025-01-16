import json
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.web import HTTPError


class SumHandler(tornado.web.RequestHandler):
    def post(self):
        """ 处理请求并返回结果 """
        try:
            request = self.request.body.decode("utf-8")
            request = json.loads(request)
            print(f"debug damonzheng, SumHandler_request:{request}")
            para_a = request["para_a"]
            para_b = request["para_b"]
            res = para_a + para_b
            response = {
                "errcode": 200,
                "data": res,
                "msg": "",
            }
            self.write(json.dumps(response))
        except Exception as e:
            response = {
                "errcode": 400,
                "data": str(e),
                "mas": ""
            }
            self.write(json.dumps(response))


class UpperHandler(tornado.web.RequestHandler):
    def initialize(self, test_para):
        """ 初始化变量 """
        self.test_para = test_para
    
    def post(self):
        """ 处理请求并返回结果 """
        try:
            request = self.request.body.decode("utf-8")
            request = json.loads(request)
            request = request["para_str"]
            print(f"debug damonzheng, UpperHandler_request:{request}")
            upper_case_data = request.upper()
            response = {
                "errcode": 200,
                "data": upper_case_data,
                "msg": self.test_para,
            }
            self.write(json.dumps(response))
        except Exception as e:
            response = {
                "errcode": 400,
                "data": str(e),
                "mas": ""
            }
            self.write(json.dumps(response))