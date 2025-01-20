#include <iostream>
#include <memory>
#include <string>
#include <grpcpp/grpcpp.h>
#include "proto/grpc_test.grpc.pb.h"

using grpc::Server;
using grpc::ServerBuilder;
using grpc::ServerContext;
using grpc::Status;
using grpc_test::GetMimDisService;
using grpc_test::GetMinDisReq;
using grpc_test::GetMinDisRsp;
using grpc_test::Vector;

// 声明一个服务实现类 GetMimDisServiceImpl，继承自 GetMimDisService::Service
class GetMimDisServiceImpl final : public GetMimDisService::Service {
public:
    Status GetMinDis(ServerContext* context, const GetMinDisReq* request, GetMinDisRsp* reply) override {
        // 打印客户端地址
        std::cout << "Client connected from: " << context->peer() << std::endl;

        const auto& point_list = request->point_list(); // 获取请求内容
        float min_dis = std::numeric_limits<float>::infinity();

        // 打印请求中的 point_list 的长度
        std::cout << "Received request with point_list, len is: " << point_list.size() << std::endl;

        for (int i = 0; i < point_list.size(); ++i) {
            for (int j = 0; j < point_list.size(); ++j) {
                if (i != j) {
                    float dx = point_list[i].x() - point_list[j].x();
                    float dy = point_list[i].y() - point_list[j].y();
                    float dz = point_list[i].z() - point_list[j].z();
                    float dis = std::sqrt(dx * dx + dy * dy + dz * dz);
                    if (dis < min_dis) {
                        min_dis = dis;
                    }
                }
            }
        }

        reply->set_min_dis(min_dis);
        return Status::OK;
    }
};

void RunServer() {
    std::string server_address("127.0.0.1:50051");
    GetMimDisServiceImpl service;

    ServerBuilder builder;  // 使用 ServerBuilder 构建gRPC服务。
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());    // 设置服务地址和不安全的服务器凭证。
    builder.RegisterService(&service);  // 注册服务实现。

    std::unique_ptr<Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;
    server->Wait();     // server->Wait() 阻塞主线程，等待客户端请求。
}

int main() {
    RunServer();
    return 0;
}
