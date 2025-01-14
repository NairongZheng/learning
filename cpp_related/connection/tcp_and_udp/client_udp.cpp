#include <iostream>
#include <winsock2.h> // Windows 套接字头文件
#include <ws2tcpip.h> // inet_ntop 等函数
#pragma comment(lib, "ws2_32.lib") // 链接 WinSock 库

void send_message_to_server(const std::string& server_ip, int server_port, const std::string& message) {
    // 初始化 WinSock
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed!" << std::endl;
        return;
    }

    SOCKET client_sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (client_sock == INVALID_SOCKET) {
        std::cerr << "Socket creation failed!" << std::endl;
        WSACleanup();
        return;
    }

    sockaddr_in server_addr{};
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(server_port);
    server_addr.sin_addr.s_addr = inet_addr(server_ip.c_str());

    int send_result = sendto(client_sock, message.c_str(), message.size(), 0,
                             (sockaddr*)&server_addr, sizeof(server_addr));
    if (send_result == SOCKET_ERROR) {
        std::cerr << "sendto failed!" << std::endl;
        closesocket(client_sock);
        WSACleanup();
        return;
    }

    char buffer[1024];
    sockaddr_in recv_addr{};
    int recv_addr_len = sizeof(recv_addr);

    int bytes_received = recvfrom(client_sock, buffer, sizeof(buffer) - 1, 0,
                                  (sockaddr*)&recv_addr, &recv_addr_len);
    if (bytes_received > 0) {
        buffer[bytes_received] = '\0';

        // 获取服务器返回信息
        char server_ip[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &recv_addr.sin_addr, server_ip, INET_ADDRSTRLEN);
        int server_port = ntohs(recv_addr.sin_port);

        std::cout << "Received response from server (" << server_ip << ", " << server_port << "): "
                  << buffer << std::endl;
    }

    closesocket(client_sock);
    WSACleanup();

    // 添加等待逻辑
    std::cout << "Press Enter to exit...";
    std::cin.get(); // 等待用户按下回车键
}

int main() {
    send_message_to_server("127.0.0.1", 12345, "Hello, UDP server!");
    return 0;
}
