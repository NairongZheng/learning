#ifndef PROTO_TEST_CLIENT_H
#define PROTO_TEST_CLIENT_H

#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <grpcpp/grpcpp.h>
#include "proto/grpc_test.grpc.pb.h"

class ProtoTestClient {
public:
    explicit ProtoTestClient(std::shared_ptr<grpc::Channel> channel);

    std::vector<float> GetMinDistance(const std::vector<std::vector<std::vector<float>>>& pointLists);
    std::vector<std::map<std::string, int32_t>> CountAndSum(const std::vector<std::vector<float>>& numLists);
    std::vector<std::string> ConvertToUpper(const std::vector<std::string>& strings);

private:
    std::string SendRequest(const grpc_test::MessageData& request);
    std::unique_ptr<grpc_test::ProtoTest::Stub> stub_;
};

#endif // PROTO_TEST_CLIENT_H
