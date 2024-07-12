import grpc
import grpc_test_pb2
import grpc_test_pb2_grpc
import multiprocessing
import traceback
from typing import List, Tuple


class Client:
    def __init__(self, server_address=["127.0.0.1:50051"]):
        self.timeout = 500
        self.server_address = server_address
        self.server_num = len(self.server_address)
        self.req_batch_queue = multiprocessing.Queue()
        self.res_list = multiprocessing.Manager().list()
        self.thread_num = 2
        self.handler = {
            "GetMinDisReq": grpc_test_pb2.GetMinDisRsp,
            "CountAndSumListReq": grpc_test_pb2.CountAndSumListRsp,
            "UpperLettersReq": grpc_test_pb2.UpperLettersRsp,
        }
        for i in range(self.thread_num):
            p = multiprocessing.Process(target=self.proc, args=(i,))
            p.start()

    def proc(self, i):
        stubs = [grpc_test_pb2_grpc.ProtoTestStub(grpc.insecure_channel(add)) for add in self.server_address]
        stub = stubs[i % self.server_num]
        while True:
            req_id, req_data, req_type = self.req_batch_queue.get()
            if req_data is None:
                continue
            req_msg = self.create_request(req_data, req_type)
            # 所有类型的请求的数据都编码放到data字段中，很好地统一了服务接口
            msg = grpc_test_pb2.MessageData(
                id=req_id,
                name=req_type,
                data=req_msg.SerializeToString()
            )
            try:
                res_msg = stub.doRequest(msg, timeout=self.timeout)
                data = self.handler[req_type]()
                data.ParseFromString(res_msg.data)
                self.res_list.append({"id": req_id, "name": req_type, "data": data})
            except grpc.RpcError as rpc_error:
                print("exception grpc.RpcError")
                self.res_list.append({"id": -10000, "name": rpc_error.details(), "data": ""})
                traceback.print_exc()
            except Exception as e:
                print("exception unknown")
                self.res_list.append({"id": -20000, "name": str(e), "data": ""})
                traceback.print_exc()

    def create_request(self, req_data, req_type):
        if req_type == "GetMinDisReq":
            return grpc_test_pb2.GetMinDisReq(
                point_lists=[
                    grpc_test_pb2.VectorList(
                        point_list=[
                            grpc_test_pb2.Vector(x=point[0], y=point[1], z=point[2])
                            for point in point_list
                        ]
                    )
                    for point_list in req_data
                ]
            )
        elif req_type == "CountAndSumListReq":
            return grpc_test_pb2.CountAndSumListReq(
                num_list=[
                    grpc_test_pb2.NumList(num=num_list)
                    for num_list in req_data
                ]
            )
        elif req_type == "UpperLettersReq":
            return grpc_test_pb2.UpperLettersReq(
                letter_list=[
                    grpc_test_pb2.Letter(s=letter)
                    for letter in req_data
                ]
            )
        else:
            raise ValueError(f"Unknown request type: {req_type}")

    def divide_list(self, lst, k) -> Tuple[List, List]:
        n = len(lst) // k
        remainder = len(lst) % k
        result = []
        index = 0
        indexs = []
        for i in range(k):
            if i < remainder:
                result.append(lst[index: index + n + 1])
                indexs.append((index, index + n + 1))
                index += n + 1
            else:
                result.append(lst[index: index + n])
                indexs.append((index, index + n))
                index += n
        return result, indexs

    def proc_get_min_dis(self, point_lists):
        return self.process_requests(point_lists, "GetMinDisReq")

    def proc_count_and_sum_list(self, numbers):
        return self.process_requests(numbers, "CountAndSumListReq")

    def proc_upper_letters(self, string):
        return self.process_requests(string, "UpperLettersReq")

    def process_requests(self, data, req_type):
        request_batch = data if isinstance(data, list) else [data]
        req_batch_idx, _ = self.divide_list(request_batch, self.thread_num)     # 分batch
        for req_id, req_data in enumerate(req_batch_idx):
            self.req_batch_queue.put((req_id, req_data, req_type))              # 将请求数据放到队列中
        reply_batch = []
        while len(reply_batch) < len(req_batch_idx):    # 拿返回，拿到所有返回才继续执行
            res = self.get_res()
            if res is not None:
                reply_batch.append(res)
        # 对返回进行后处理
        sorted_res = sorted(reply_batch, key=lambda x: x["id"])
        if req_type == "GetMinDisReq":
            result = [item for sublist in [x["data"].min_dis for x in sorted_res] for item in sublist]
        elif req_type == "CountAndSumListReq":
            result = [(item.count_dict, item.sum_res) for sublist in [x["data"].count_and_sum_res for x in sorted_res] for item in sublist]
        elif req_type == "UpperLettersReq":
            result = [letter.s for res in [x["data"] for x in sorted_res] for letter in res.letter_res_list]
        return result

    def get_res(self):
        if len(self.res_list) == 0:
            return None
        return self.res_list.pop(0)

class Test:
    def __init__(self, client: Client):
        self.client = client

    def get_min_dis(self):
        point_lists = [
            [[1, 2, 3], [4, 6, 9], [3.6, 9.2, 2.3]],
            [[3, 0.1, 2], [9, 6, 5.6], [9.3, 32, 12], [1.2, 3, 0.6]],
            [[9, 2, 1]],
        ]
        min_dis_list = self.client.proc_get_min_dis(point_lists)
        print(f"min_dis_result: {min_dis_list}")

    def count_and_sum_list(self):
        numbers = [
            [1.1, 2.2, 3.3, 1.1, 2.2, 4.4],
            [1, 2, 3, 1, 2, 4],
            [0, 1, 2, 3, 3, 2, 0]
        ]
        count_sum_res = self.client.proc_count_and_sum_list(numbers)
        print(f"count_and_sum_result: {count_sum_res}")

    def upper_letters(self):
        string_list = [
            "hello grpc",
            "fxxk grpc",
            "legendary grpc"
        ]
        upper_case_res = self.client.proc_upper_letters(string_list)
        print(f"upper_letters_result: {upper_case_res}")

def main():
    client = Client()
    test_func = Test(client)
    test_func.get_min_dis()
    test_func.count_and_sum_list()
    test_func.upper_letters()

if __name__ == "__main__":
    main()
