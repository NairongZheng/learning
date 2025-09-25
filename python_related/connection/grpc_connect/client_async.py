import asyncio
import grpc
import grpc_test_pb2
import grpc_test_pb2_grpc
import random
import uuid


class AsyncGetMinDisClient:
    def __init__(self, ip="127.0.0.1", port=50051, retry=5):
        self.addr = f"{ip}:{port}"
        self.retry = retry

    async def query(self, point_list):
        async with grpc.aio.insecure_channel(self.addr) as channel:
            stub = grpc_test_pb2_grpc.GetMimDisServiceStub(channel)
            # 构建请求
            points = [grpc_test_pb2.Vector(x=p[0], y=p[1], z=p[2]) for p in point_list]
            req = grpc_test_pb2.GetMinDisReq(point_list=points)

            for _ in range(self.retry):
                try:
                    response = await stub.GetMinDis(req)
                    if response.min_dis is not None:
                        return response
                except Exception as e:
                    pass
            return None


class AsyncGrpcTest:
    def __init__(self):
        self.client = AsyncGetMinDisClient()
        self.pending_tasks = {}  # request_id -> asyncio.Task

    def random_str(self, num=6):
        uln = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        rs = random.sample(uln, num)
        a = uuid.uuid1()
        return ''.join(rs + str(a).split("-"))

    async def upload(self, point_list):
        request_id = self.random_str()
        task = asyncio.create_task(self._query_task(request_id, point_list))
        self.pending_tasks[request_id] = task
        return request_id

    async def _query_task(self, request_id, point_list):
        res = await self.client.query(point_list)
        return {"request_id": request_id, "point_list": point_list, "min_dis": res.min_dis if res else "err"}

    async def parse_request(self, point_lists):
        for pl in point_lists:
            await self.upload(pl)

    async def get_responses(self):
        """等待所有 pending_tasks 完成并收集结果"""
        done, _ = await asyncio.wait(self.pending_tasks.values())
        results = [t.result() for t in done]
        self.pending_tasks.clear()
        return results


async def main():
    grpc_test = AsyncGrpcTest()

    point_lists = [
        [[1, 2, 3], [4, 6, 9], [3.6, 9.2, 2.3]],
        [[3, 0.1, 2], [9, 6, 5.6], [9.3, 32, 12], [1.2, 3, 0.6]],
        [[9, 2, 1]]
    ]

    await grpc_test.parse_request(point_lists)

    # 获取结果
    results = await grpc_test.get_responses()
    print(f"Results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
