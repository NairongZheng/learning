#ifndef GRPC_CONNECT2_SERVER_H
#define GRPC_CONNECT2_SERVER_H

#include <grpcpp/grpcpp.h>
#include "proto/grpc_test.grpc.pb.h"
#include <string>
#include <unordered_map>

// ProtoTestServer 类
class ProtoTestServer {
public:
    // 计算最小距离
    static float GetMinDistance(const grpc_test::VectorList& point_list);

    // 处理 GetMinDisReq 的函数
    grpc::Status HandleGetMinDisReq(const grpc_test::GetMinDisReq& get_min_dis_req, grpc_test::GetMinDisRsp* response);

    // 处理 CountAndSumListReq 的函数
    grpc::Status HandleCountAndSumListReq(const grpc_test::CountAndSumListReq& count_and_sum_req, grpc_test::CountAndSumListRsp* response);

    // 处理 UpperLettersReq 的函数
    grpc::Status HandleUpperLettersReq(const grpc_test::UpperLettersReq& upper_letters_req, grpc_test::UpperLettersRsp* response);

    // 通用请求处理函数
    grpc::Status HandleRequest(const std::string& request_name, const std::string& data, grpc_test::MessageData* response);

    // 运行服务器
    void RunServer();

private:
    class GrpcConnect2ServerImpl : public grpc_test::ProtoTest::Service {
    public:
        explicit GrpcConnect2ServerImpl(ProtoTestServer* parent);

        grpc::Status doRequest(grpc::ServerContext* context,
                               const grpc_test::MessageData* request,
                               grpc_test::MessageData* response) override;

    private:
        ProtoTestServer* parent_;
    };
};

#endif // GRPC_CONNECT2_SERVER_H
