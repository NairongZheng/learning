"""
一般要将主线程阻塞
不过这边是仿造主函数while True的方式写的
不用等到返回就可以继续往下执行
"""
import grpc
import grpc_test_pb2
import grpc_test_pb2_grpc

import multiprocessing
import random
import uuid
import time, math


class GetMinDisClient:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 50051
        self.retry = 5
        self.req_queue = multiprocessing.Queue()
        self.res_dict = multiprocessing.Manager().dict()
        self.proc_num = 10
        for i in range(self.proc_num):
            p = multiprocessing.Process(target=self.proc, args=())
            p.start()

    def proc(self):
        while True:
            req = self.req_queue.get()
            if req is not None:
                request_id = req["request_id"]
                point_list = req["point_list"]
                # print(f"debug damonzheng, point_list:{point_list}")
                try:
                    response = self.query(point_list)
                    # print(f"debug damonzheng, response:{response}")
                    if response is None:
                        print(f"debug damonzheng, response is None")
                        res = {"errcode": 404, "request_id": request_id, "point_list": point_list, "min_dis":"err"}
                    else:
                        res = {"errcode": 0, "request_id": request_id, "point_list": point_list, "min_dis":response.min_dis}
                except Exception as e:
                    print(f"debug damonzheng, some error:{e}")
                    res = {"errcode": 404, "request_id": request_id, "point_list": point_list, "min_dis":"err"}
                self.res_dict[request_id] = res
    
    def query(self, point_list):
        # try:
        addr = f"{self.ip}:{self.port}"
        # print(f"debug damonzheng, addr:{addr}")
        # print(f"debug damonzheng, point_list:{point_list}")
        with grpc.insecure_channel(addr) as channel:
            stub = grpc_test_pb2_grpc.GetMimDisServiceStub(channel)
            point_list = [grpc_test_pb2.Vector(x=point[0], y=point[1], z=point[2]) for point in point_list]
            req = grpc_test_pb2.GetMinDisReq(point_list=point_list)
            for i in range(self.retry):
                # try:
                response = stub.GetMinDis(req)
                # print(f"debug damonzheng, response:{response}")
                return response
                # except:
                #     pass
                if response.min_dis == None:
                    return None
        # except Exception as e:
        #     return None
        return None

    def proc_req(self, request_id, point_list):
        """ 入口, 往req请求队列中添加请求 """
        request_dict = {
            "request_id": request_id,
            "point_list": point_list,
        }
        self.req_queue.put(request_dict)
        print(f"debug damonzheng, request_dict:{request_dict}")

    def get_res(self, request_id):
        """ 出口, 根据发送请求的id拿结果 """
        if request_id not in self.res_dict.keys():
            return []
        res = self.res_dict[request_id]
        del self.res_dict[request_id]
        return [res]


class GrpcTest:
    def __init__(self):
        self.request_id_points_dict = {} # 记录有哪些还在处理
        self.get_min_dis_client = GetMinDisClient()
    
    def random_str(self, num=6):
        uln = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        rs = random.sample(uln, num)  # 生成一个 指定位数的随机字符串
        a = uuid.uuid1()  # 根据 时间戳生成 uuid , 保证全球唯一
        b = ''.join(rs + str(a).split("-"))  # 生成将随机字符串 与 uuid拼接
        return b  # 返回随机字符串
    
    def upload(self, request_id, point_list):
        self.get_min_dis_client.proc_req(request_id, point_list)
    
    def re_upload(self, re_id):
        new_id = self.random_str()
        re_point_list = self.request_id_points_dict.pop(re_id)
        self.request_id_points_dict[new_id] = re_point_list
        self.get_min_dis_client.proc_req(new_id, re_point_list)
    
    def parse_request(self, point_lists):
        for point_list in point_lists:
            request_id = self.random_str()
            self.upload(request_id, point_list)
            self.request_id_points_dict[request_id] = point_list
    
    def get_response(self):
        results = []
        fail_id_list = []
        success_id_list = []
        for request_id in self.request_id_points_dict:
            reply = self.get_min_dis_client.get_res(request_id)
            if len(reply) != 0 and reply[0]["errcode"] in [404]:
                fail_id_list.append(request_id)
            elif len(reply) != 0:
                results.append(reply[0])
                success_id_list.append(request_id)
        
        for success_id in success_id_list:
            self.request_id_points_dict.pop(success_id)
        for fail_id in fail_id_list:
            self.re_upload(fail_id)
        return results


def main():
    grpc_test = GrpcTest()
    point_lists = [
        [[1, 2, 3], [4, 6, 9], [3.6, 9.2, 2.3]],
        [[3, 0.1, 2], [9, 6, 5.6], [9.3, 32, 12], [1.2, 3, 0.6]],
        [[9, 2, 1]]
    ]
    result = []
    grpc_test.parse_request(point_lists)
    while len(result) < len(point_lists):
        res = grpc_test.get_response()
        print(f"debug damonzheng, res:{res}")
        result.extend(res)
    print(f"debug damonzheng, result:{result}")


if __name__ == "__main__":
    main()