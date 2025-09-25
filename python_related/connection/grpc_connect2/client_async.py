import asyncio
import grpc
import grpc_test_pb2
import grpc_test_pb2_grpc
from typing import List, Tuple


class AsyncClient:
    def __init__(self, server_address=["127.0.0.1:50051"], timeout=5.0, thread_num=2):
        self.timeout = timeout
        self.server_address = server_address
        self.server_num = len(self.server_address)
        self.thread_num = thread_num
        self.handler = {
            "GetMinDisReq": grpc_test_pb2.GetMinDisRsp,
            "CountAndSumListReq": grpc_test_pb2.CountAndSumListRsp,
            "UpperLettersReq": grpc_test_pb2.UpperLettersRsp,
        }
        self.stubs = []
        self.res_list = []

    async def init_stubs(self):
        """初始化异步 gRPC stub"""
        for add in self.server_address:
            channel = grpc.aio.insecure_channel(add)
            stub = grpc_test_pb2_grpc.ProtoTestStub(channel)
            self.stubs.append(stub)

    async def send_request(self, req_id, req_data, req_type):
        stub = self.stubs[req_id % self.server_num]
        req_msg = self.create_request(req_data, req_type)
        msg = grpc_test_pb2.MessageData(
            id=req_id,
            name=req_type,
            data=req_msg.SerializeToString()
        )
        try:
            res_msg = await stub.doRequest(msg, timeout=self.timeout)
            data = self.handler[req_type]()
            data.ParseFromString(res_msg.data)
            return {"id": req_id, "name": req_type, "data": data}
        except grpc.RpcError as rpc_error:
            print(f"gRPC error: {rpc_error.details()}")
            return {"id": -10000, "name": rpc_error.details(), "data": ""}
        except Exception as e:
            print(f"Unknown exception: {e}")
            return {"id": -20000, "name": str(e), "data": ""}

    def create_request(self, req_data, req_type):
        if req_type == "GetMinDisReq":
            req_msg = grpc_test_pb2.GetMinDisReq()
            for point_list in req_data:  # req_data 是二维列表 [[x,y,z], ...]
                point_list_msg = req_msg.point_lists.add()
                for point in point_list:
                    point_msg = point_list_msg.point_list.add()
                    point_msg.x = point[0]
                    point_msg.y = point[1]
                    point_msg.z = point[2]
        elif req_type == "CountAndSumListReq":
            req_msg = grpc_test_pb2.CountAndSumListReq(
                num_list=[grpc_test_pb2.NumList(num=num_list) for num_list in req_data]
            )
        elif req_type == "UpperLettersReq":
            req_msg = grpc_test_pb2.UpperLettersReq(
                letter_list=[grpc_test_pb2.Letter(s=letter) for letter in req_data]
            )
        else:
            raise ValueError(f"Unknown request type: {req_type}")
        return req_msg

    def divide_list(self, lst, k) -> Tuple[List, List]:
        """将列表均分成 k 份"""
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

    async def process_requests(self, data, req_type):
        request_batch = data if isinstance(data, list) else [data]

        # 分 batch
        req_batch_idx, _ = self.divide_list(request_batch, self.thread_num)

        tasks = [self.send_request(i, req_data, req_type) for i, req_data in enumerate(req_batch_idx)]
        reply_batch = await asyncio.gather(*tasks)

        sorted_res = sorted(reply_batch, key=lambda x: x["id"])
        if req_type == "GetMinDisReq":
            return [item for sublist in [x["data"].min_dis for x in sorted_res] for item in sublist]
        elif req_type == "CountAndSumListReq":
            return [(item.count_dict, item.sum_res) for sublist in [x["data"].count_and_sum_res for x in sorted_res] for item in sublist]
        elif req_type == "UpperLettersReq":
            return [letter.s for res in [x["data"] for x in sorted_res] for letter in res.letter_res_list]

    async def proc_get_min_dis(self, point_lists):
        return await self.process_requests(point_lists, "GetMinDisReq")

    async def proc_count_and_sum_list(self, numbers):
        return await self.process_requests(numbers, "CountAndSumListReq")

    async def proc_upper_letters(self, string_list):
        return await self.process_requests(string_list, "UpperLettersReq")


class AsyncTest:
    def __init__(self, client: AsyncClient):
        self.client = client

    async def get_min_dis(self):
        point_lists = [
            [[1, 2, 3], [4, 6, 9], [3.6, 9.2, 2.3]],
            [[3, 0.1, 2], [9, 6, 5.6], [9.3, 32, 12], [1.2, 3, 0.6]],
            [[9, 2, 1]],
        ]
        min_dis_list = await self.client.proc_get_min_dis(point_lists)
        print(f"min_dis_result: {min_dis_list}")

    async def count_and_sum_list(self):
        numbers = [
            [1.1, 2.2, 3.3, 1.1, 2.2, 4.4],
            [1, 2, 3, 1, 2, 4],
            [0, 1, 2, 3, 3, 2, 0]
        ]
        count_sum_res = await self.client.proc_count_and_sum_list(numbers)
        print(f"count_and_sum_result: {count_sum_res}")

    async def upper_letters(self):
        string_list = [
            "hello grpc",
            "fxxk grpc",
            "legendary grpc"
        ]
        upper_case_res = await self.client.proc_upper_letters(string_list)
        print(f"upper_letters_result: {upper_case_res}")


async def main():
    client = AsyncClient()
    await client.init_stubs()
    test_func = AsyncTest(client)
    await test_func.get_min_dis()
    await test_func.count_and_sum_list()
    await test_func.upper_letters()


if __name__ == "__main__":
    asyncio.run(main())
