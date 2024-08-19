import grpc
from concurrent import futures
import grpc_test_pb2
import grpc_test_pb2_grpc
import math
from collections import Counter


class ProtoTestServicer(grpc_test_pb2_grpc.ProtoTestServicer):
    def __init__(self):
        self.handler = {
            "GetMinDisReq": grpc_test_pb2.GetMinDisReq,
            "CountAndSumListReq": grpc_test_pb2.CountAndSumListReq,
            "UpperLettersReq": grpc_test_pb2.UpperLettersReq,
        }
        self.func_map = {
            "GetMinDisReq": self.GetMinDis,
            "CountAndSumListReq": self.CountAndSumList,
            "UpperLettersReq": self.UpperLetters,
        }

    def GetMinDis(self, data):
        min_dis_list = []
        for point_lists in data.point_lists:
            min_dis = float("inf")
            for i in range(len(point_lists.point_list)):
                for j in range(i + 1, len(point_lists.point_list)):
                    dis = math.sqrt(
                        (point_lists.point_list[i].x - point_lists.point_list[j].x) ** 2 +
                        (point_lists.point_list[i].y - point_lists.point_list[j].y) ** 2 +
                        (point_lists.point_list[i].z - point_lists.point_list[j].z) ** 2
                    )
                    min_dis = min(min_dis, dis)
            min_dis_list.append(min_dis if min_dis != float("inf") else -1)
        rsp_msg = grpc_test_pb2.GetMinDisRsp(min_dis=min_dis_list)
        return rsp_msg.SerializeToString()

    def CountAndSumList(self, data):
        res_list = []
        for num_list in data.num_list:
            count = Counter(num_list.num)
            count_dict = {str(round(k, 2)): v for k, v in count.items()}
            sum_res = round(sum(num_list.num), 2)
            res_list.append(grpc_test_pb2.CountAndSumResInstruct(count_dict=count_dict, sum_res=sum_res))
        rsp_msg = grpc_test_pb2.CountAndSumListRsp(count_and_sum_res=res_list)
        return rsp_msg.SerializeToString()

    def UpperLetters(self, data):
        res_list = [grpc_test_pb2.Letter(s=letter.s.upper()) for letter in data.letter_list]
        rsp_msg = grpc_test_pb2.UpperLettersRsp(letter_res_list=res_list)
        return rsp_msg.SerializeToString()

    def doRequest(self, request, context):
        name = request.name
        data = self.handler[name]()             # 发送的时候进行了编码，所以这边要解码
        data.ParseFromString(request.data)
        func = self.func_map[name]              # 根据请求的类型选择处理函数
        res = func(data)
        response = grpc_test_pb2.MessageData(
            id=request.id,
            name=name,
            data=res
        )
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_test_pb2_grpc.add_ProtoTestServicer_to_server(ProtoTestServicer(), server)
    server.add_insecure_port("127.0.0.1:50051")
    print("Server is running on 127.0.0.1:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
