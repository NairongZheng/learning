#include <iostream>
#include <memory>
#include <string>
#include <vector>
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
    explicit GetMinDisClient(std::shared_ptr<Channel> channel) 
        : stub_(GetMimDisService::NewStub(channel)) {}

    float GetMinDis(const std::vector<std::vector<float>>& points) {
        GetMinDisReq request;

        for (const auto& point : points) {
            auto* vector = request.add_point_list();
            vector->set_x(point[0]);
            vector->set_y(point[1]);
            vector->set_z(point[2]);
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
    auto channel = grpc::CreateChannel("127.0.0.1:50051", grpc::InsecureChannelCredentials());
    GetMinDisClient client(channel);

    std::vector<std::vector<std::vector<float>>> point_lists = {
        {{1.0f, 2.0f, 3.0f}, {4.0f, 6.0f, 9.0f}, {3.6f, 9.2f, 2.3f}},
        {{3.0f, 0.1f, 2.0f}, {9.0f, 6.0f, 5.6f}, {1.2f, 3.0f, 0.6f}},
        {{9.0f, 2.0f, 1.0f}}
    };

    for (auto &points : point_lists) {
        float min_dis = client.GetMinDis(points);
        std::cout << "Minimum distance: " << min_dis << std::endl;
    }

    return 0;
}
