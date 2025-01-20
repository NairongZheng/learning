#include "grpc_connect2_server.h"
#include <cmath>
#include <numeric>
#include <algorithm>
#include <iostream>

// GrpcConnect2ServerImpl 构造函数
ProtoTestServer::GrpcConnect2ServerImpl::GrpcConnect2ServerImpl(ProtoTestServer* parent) : parent_(parent) {}

// 计算最小距离
float ProtoTestServer::GetMinDistance(const grpc_test::VectorList& point_list) {
    float min_dis = std::numeric_limits<float>::infinity();
    int point_size = point_list.point_list_size();
    for (int i = 0; i < point_size; ++i) {
        for (int j = i + 1; j < point_size; ++j) {
            float dis = std::sqrt(
                std::pow(point_list.point_list(i).x() - point_list.point_list(j).x(), 2) +
                std::pow(point_list.point_list(i).y() - point_list.point_list(j).y(), 2) +
                std::pow(point_list.point_list(i).z() - point_list.point_list(j).z(), 2)
            );
            min_dis = std::min(min_dis, dis);
        }
    }
    return (min_dis == std::numeric_limits<float>::infinity()) ? -1.0f : min_dis;
}

// 处理 GetMinDisReq
grpc::Status ProtoTestServer::HandleGetMinDisReq(const grpc_test::GetMinDisReq& get_min_dis_req, grpc_test::GetMinDisRsp* response) {
    for (const auto& point_lists : get_min_dis_req.point_lists()) {
        std::cout << " request type: get_min_dis_req, point_lists_len is: " << point_lists.point_list_size() << std::endl;
        float min_dis = GetMinDistance(point_lists);
        response->add_min_dis(min_dis);
    }
    return grpc::Status::OK;
}

// 处理 CountAndSumListReq
grpc::Status ProtoTestServer::HandleCountAndSumListReq(const grpc_test::CountAndSumListReq& count_and_sum_req, grpc_test::CountAndSumListRsp* response) {
    std::cout << " request type: count_and_sum_req, num_list_len is: " << count_and_sum_req.num_list_size() << std::endl;
    for (const auto& num_list : count_and_sum_req.num_list()) {
        grpc_test::CountAndSumResInstruct result;
        std::unordered_map<std::string, int32_t> count_dict;
        float sum_res = 0.0f;
        for (float num : num_list.num()) {
            count_dict[std::to_string(round(num * 100) / 100.0f)]++;
            sum_res += num;
        }
        result.mutable_count_dict()->insert(count_dict.begin(), count_dict.end());
        result.set_sum_res(sum_res);
        response->add_count_and_sum_res()->CopyFrom(result);
    }
    return grpc::Status::OK;
}

// 处理 UpperLettersReq
grpc::Status ProtoTestServer::HandleUpperLettersReq(const grpc_test::UpperLettersReq& upper_letters_req, grpc_test::UpperLettersRsp* response) {
    std::cout << " request type: upper_letters_req, letter_list_len is: " << upper_letters_req.letter_list_size() << std::endl;
    for (const auto& letter : upper_letters_req.letter_list()) {
        grpc_test::Letter upper_letter;
        std::string upper_str = letter.s();
        std::transform(upper_str.begin(), upper_str.end(), upper_str.begin(), ::toupper);
        upper_letter.set_s(upper_str);
        response->add_letter_res_list()->CopyFrom(upper_letter);
    }
    return grpc::Status::OK;
}

// 通用请求处理函数
grpc::Status ProtoTestServer::HandleRequest(const std::string& request_name, const std::string& data, grpc_test::MessageData* response) {
    if (request_name == "GetMinDisReq") {
        grpc_test::GetMinDisReq get_min_dis_req;
        get_min_dis_req.ParseFromString(data);
        grpc_test::GetMinDisRsp min_dis_rsp;
        HandleGetMinDisReq(get_min_dis_req, &min_dis_rsp);
        response->set_name(request_name);
        response->set_data(min_dis_rsp.SerializeAsString());
    } else if (request_name == "CountAndSumListReq") {
        grpc_test::CountAndSumListReq count_and_sum_req;
        count_and_sum_req.ParseFromString(data);
        grpc_test::CountAndSumListRsp count_and_sum_rsp;
        HandleCountAndSumListReq(count_and_sum_req, &count_and_sum_rsp);
        response->set_name(request_name);
        response->set_data(count_and_sum_rsp.SerializeAsString());
    } else if (request_name == "UpperLettersReq") {
        grpc_test::UpperLettersReq upper_letters_req;
        upper_letters_req.ParseFromString(data);
        grpc_test::UpperLettersRsp upper_letters_rsp;
        HandleUpperLettersReq(upper_letters_req, &upper_letters_rsp);
        response->set_name(request_name);
        response->set_data(upper_letters_rsp.SerializeAsString());
    }
    return grpc::Status::OK;
}

// 实现 ProtoTest 服务
grpc::Status ProtoTestServer::GrpcConnect2ServerImpl::doRequest(grpc::ServerContext* context,
                                                                const grpc_test::MessageData* request,
                                                                grpc_test::MessageData* response) {
    return parent_->HandleRequest(request->name(), request->data(), response);
}

// 运行服务器
void ProtoTestServer::RunServer() {
    std::string server_address("0.0.0.0:50051");
    GrpcConnect2ServerImpl service(this);

    grpc::ServerBuilder builder;
    builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
    builder.RegisterService(&service);

    std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
    std::cout << "Server listening on " << server_address << std::endl;

    server->Wait();
}
int main() {
    ProtoTestServer server;
    server.RunServer();
    return 0;
}