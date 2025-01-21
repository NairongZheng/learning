#include <iostream>
#include <string>
#include "include/httplib/httplib.h"
#include "include/nlohmann/json.hpp"

using json = nlohmann::json;

// 测试 sum 请求
void test_sum(std::string server_addr) {
    json request = {
        {"para_a", 10},
        {"para_b", 36}
    };
    std::cout << "debug damonzheng, request: " << request.dump() << std::endl;

    httplib::Client client(server_addr);
    auto response = client.Post("/sumHandler", request.dump(), "application/json");

    if (response && response->status == 200) {
        json result = json::parse(response->body);
        if (result["errcode"] == 200) {
            std::cout << "sum result from server: " << result["data"] << std::endl;
        }
        else if (result["errcode"] == 400) {
            std::cout << "Server error: " << result["data"] << std::endl;
        }
    }
    else {
        std::cout << "Failed to connect to server" << std::endl;
    }
}

// 测试 upper 请求
void test_upper(std::string server_addr) {
    json request = {
        {"para_str", "lower string to upper string"}
    };
    std::cout << "debug damonzheng, request: " << request.dump() << std::endl;

    httplib::Client client(server_addr);
    auto response = client.Post("/upperHandler", request.dump(), "application/json");

    if (response && response->status == 200) {
        json result = json::parse(response->body);
        if (result["errcode"] == 200) {
            std::cout << "Uppercase string from server: " << result["data"] << std::endl;
        }
        else if (result["errcode"] == 400) {
            std::cout << "Server error: " << result["data"] << std::endl;
        }
    }
    else {
        std::cout << "Failed to connect to server" << std::endl;
    }
}

int main() {
    std::string server_addr = "http://localhost:12300";
    test_sum(server_addr);
    test_upper(server_addr);
    return 0;
}
