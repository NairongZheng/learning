import grpc
from concurrent import futures
import grpc_test_pb2
import grpc_test_pb2_grpc
import math


class GetMimDisServiceServicer(grpc_test_pb2_grpc.GetMimDisServiceServicer):
    def GetMinDis(self, request, context):
        point_list = request.point_list
        print(f"debug damonzheng, point_list:{point_list}")
        for i in range(len(point_list)):
            min_dis = float('inf')
            for j in range(len(point_list)):
                if i != j:
                    dis = math.sqrt(
                        (point_list[i].x - point_list[j].x) ** 2 +
                        (point_list[i].y - point_list[j].y) ** 2 +
                        (point_list[i].z - point_list[j].z) ** 2
                    )
                    if dis < min_dis:
                        min_dis = dis
        return grpc_test_pb2.GetMinDisRsp(min_dis=min_dis)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_test_pb2_grpc.add_GetMimDisServiceServicer_to_server(GetMimDisServiceServicer(), server)
    # server.add_insecure_port('[::]:50051')
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()