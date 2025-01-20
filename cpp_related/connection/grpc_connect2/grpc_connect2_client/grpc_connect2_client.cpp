#include "grpc_connect2_client.h"

ProtoTestClient::ProtoTestClient(std::shared_ptr<grpc::Channel> channel)
    : stub_(grpc_test::ProtoTest::NewStub(channel)) {
}

std::string ProtoTestClient::SendRequest(const grpc_test::MessageData& request) {
    grpc_test::MessageData response;
    grpc::ClientContext context;

    grpc::Status status = stub_->doRequest(&context, request, &response);

    if (!status.ok()) {
        std::cerr << "gRPC request failed: " << status.error_message() << std::endl;
        return "";
    }
    return response.data();
}

std::vector<float> ProtoTestClient::GetMinDistance(const std::vector<std::vector<std::vector<float>>>& pointLists) {
    grpc_test::GetMinDisReq request;
    for (const auto& pointList : pointLists) {
        auto* vectorList = request.add_point_lists();
        for (const auto& point : pointList) {
            auto* vector = vectorList->add_point_list();
            vector->set_x(point[0]);
            vector->set_y(point[1]);
            vector->set_z(point[2]);
        }
    }

    grpc_test::MessageData message;
    message.set_id(1);
    message.set_name("GetMinDisReq");
    message.set_data(request.SerializeAsString());

    std::string response_data = SendRequest(message);
    grpc_test::GetMinDisRsp response;
    response.ParseFromString(response_data);

    return std::vector<float>(response.min_dis().begin(), response.min_dis().end());
}

std::vector<std::map<std::string, int32_t>> ProtoTestClient::CountAndSum(const std::vector<std::vector<float>>& numLists) {
    grpc_test::CountAndSumListReq request;
    for (const auto& nums : numLists) {
        auto* numList = request.add_num_list();
        for (const auto& num : nums) {
            numList->add_num(num);
        }
    }

    grpc_test::MessageData message;
    message.set_id(2);
    message.set_name("CountAndSumListReq");
    message.set_data(request.SerializeAsString());

    std::string response_data = SendRequest(message);
    grpc_test::CountAndSumListRsp response;
    response.ParseFromString(response_data);

    std::vector<std::map<std::string, int32_t>> results;
    for (const auto& res : response.count_and_sum_res()) {
        std::map<std::string, int32_t> count_dict(res.count_dict().begin(), res.count_dict().end());
        results.push_back(count_dict);
    }

    return results;
}

std::vector<std::string> ProtoTestClient::ConvertToUpper(const std::vector<std::string>& strings) {
    grpc_test::UpperLettersReq request;
    for (const auto& str : strings) {
        auto* letter = request.add_letter_list();
        letter->set_s(str);
    }

    grpc_test::MessageData message;
    message.set_id(3);
    message.set_name("UpperLettersReq");
    message.set_data(request.SerializeAsString());

    std::string response_data = SendRequest(message);
    grpc_test::UpperLettersRsp response;
    response.ParseFromString(response_data);

    std::vector<std::string> results;
    for (const auto& res : response.letter_res_list()) {
        results.push_back(res.s());
    }
    return results;
}
int main(int argc, char** argv) {
    ProtoTestClient client(grpc::CreateChannel("localhost:50051", grpc::InsecureChannelCredentials()));

    // Test GetMinDistance
    std::vector<std::vector<std::vector<float>>> pointLists = {
        {{1, 2, 3}, {4, 6, 9}, {3.6, 9.2, 2.3}},
        {{3, 0.1, 2}, {9, 6, 5.6}, {9.2, 32, 12}},
        {{1.2, 3, 0.6}}
    };
    auto minDistances = client.GetMinDistance(pointLists);
    std::cout << "Min Distances: ";
    for (const auto& dist : minDistances) {
        std::cout << dist << " ";
    }
    std::cout << std::endl;

    // Test CountAndSum
    std::vector<std::vector<float>> numLists = {
        {1.1, 2.2, 3.3, 1.1, 2.2, 4.4},
        {1, 2, 3, 1, 2, 4},
        {0, 1, 2, 3, 3, 2, 0}
    };
    auto countAndSum = client.CountAndSum(numLists);
    for (const auto& result : countAndSum) {
        std::cout << "CountAndSum: ";
        for (const auto& pair : result) {
            std::cout << pair.first << ": " << pair.second << " ";
        }
        std::cout << std::endl;
    }

    // Test ConvertToUpper
    std::vector<std::string> strings = { "hello grpc", "fxxk grpc", "legendary grpc" };
    auto upperStrings = client.ConvertToUpper(strings);
    std::cout << "Upper Strings: ";
    for (const auto& str : upperStrings) {
        std::cout << str << " ";
    }
    std::cout << std::endl;

    std::cout << "Press Enter to exit...";
    std::cin.get(); // 等待用户按回车键
    return 0;
}