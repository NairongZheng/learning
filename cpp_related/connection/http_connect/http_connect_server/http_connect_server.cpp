#include <iostream>
#include <string>
#include "include/httplib/httplib.h"
#include "include/nlohmann/json.hpp"

using json = nlohmann::json;

// 处理 /sumHandler 请求的函数
void sumHandler(const httplib::Request& req, httplib::Response& res) {
    std::cout << "Client addr is: " << req.remote_addr << std::endl;
    try {
        auto request_body = json::parse(req.body);
        std::cout << " server receive a sumHandler request: " << request_body << std::endl;
        int para_a = request_body["para_a"];
        int para_b = request_body["para_b"];
        int result = para_a + para_b;

        json response = {
            {"errcode", 200},
            {"data", result},
            {"msg", ""}
        };
        res.set_content(response.dump(), "application/json");
        std::cout << " sumHandler res is: " << response.dump() << std::endl;
    }
    catch (const std::exception& e) {
        json response = {
            {"errcode", 400},
            {"data", e.what()},
            {"msg", ""}
        };
        res.set_content(response.dump(), "application/json");
        std::cout << " sumHandler res is: " << response.dump() << std::endl;
    }
}

// 处理 /upperHandler 请求的函数
void upperHandler(const httplib::Request& req, httplib::Response& res, const std::string& test_para) {
    std::cout << "Client addr is: " << req.remote_addr << std::endl;
    try {
        auto request_body = json::parse(req.body);
        std::cout << " server receive a upperHandler request: " << request_body << std::endl;
        std::string para_str = request_body["para_str"];
        std::string upper_str;
        for (char c : para_str) {
            upper_str += std::toupper(c);
        }

        json response = {
            {"errcode", 200},
            {"data", upper_str},
            {"msg", test_para}
        };
        res.set_content(response.dump(), "application/json");
        std::cout << " upperHandler res is: " << response.dump() << std::endl;
    }
    catch (const std::exception& e) {
        json response = {
            {"errcode", 400},
            {"data", e.what()},
            {"msg", ""}
        };
        res.set_content(response.dump(), "application/json");
        std::cout << " upperHandler res is: " << response.dump() << std::endl;
    }
}

int main() {
    httplib::Server server; // 创建 HTTP 服务器

    // 注册 /sumHandler 路由
    server.Post("/sumHandler", [](const httplib::Request& req, httplib::Response& res) {
        sumHandler(req, res);
    });

    // 注册 /upperHandler 路由
    server.Post("/upperHandler", [](const httplib::Request& req, httplib::Response& res) {
        const std::string test_para = "Successful parameter passing";
        upperHandler(req, res, test_para);
    });

    int port = 12300;
    std::cout << "Server listening on 0.0.0.0:" << port << std::endl;
    server.listen("0.0.0.0", port); // 启动服务器
    return 0;
}
