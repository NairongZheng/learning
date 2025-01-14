#include <iostream>
#include <memory>
#include <string>
#include <grpcpp/grpcpp.h>
#include "proto/grpc_test.grpc.pb.h"

using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;
using grpc_test::GetMimDisService;
using grpc_test::GetMinDisReq;
using grpc_test::GetMinDisRsp;
using grpc_test::Vector;

class GetMinDisClient {
public:
    // 构造函数中初始化 stub_，用于与服务端通信。
    GetMinDisClient(std::shared_ptr<Channel> channel) : stub_(GetMimDisService::NewStub(channel)) {}

    float GetMinDis(const std::vector<Vector>& point_list) {
        GetMinDisReq request;
        for (const auto& point : point_list) {
            auto* vector = request.add_point_list();
            vector->set_x(point.x());
            vector->set_y(point.y());
            vector->set_z(point.z());
        }

        GetMinDisRsp reply;
        ClientContext context;

        Status status = stub_->GetMinDis(&context, request, &reply);

        if (status.ok()) {
            return reply.min_dis();
        } else {
            std::cerr << "gRPC call failed: " << status.error_message() << std::endl;
            return -1.0f;
        }
    }

private:
    std::unique_ptr<GetMimDisService::Stub> stub_;
};

int main() {
    GetMinDisClient client(grpc::CreateChannel("127.0.0.1:50051", grpc::InsecureChannelCredentials()));

    std::vector<Vector> points = {
        [] { Vector v; v.set_x(1); v.set_y(2); v.set_z(3); return v; }(),
        [] { Vector v; v.set_x(4); v.set_y(6); v.set_z(9); return v; }(),
        [] { Vector v; v.set_x(3.6); v.set_y(9.2); v.set_z(2.3); return v; }()
    };

    float min_dis = client.GetMinDis(points);   // 这里的points可以不用std::vector<Vector>，直接用std::vector<vector>，然后再在函数里面赋值就行
    std::cout << "Minimum distance: " << min_dis << std::endl;

    return 0;
}
