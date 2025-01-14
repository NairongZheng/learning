#include <iostream>
#include <winsock2.h> // Windows 套接字头文件
#include <ws2tcpip.h> // inet_ntop 等函数
#pragma comment(lib, "ws2_32.lib") // 链接 WinSock 库

void start_udp_server(const std::string& server_ip, int server_port) {
    // 初始化 WinSock
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed!" << std::endl;
        return;
    }

    SOCKET server_sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (server_sock == INVALID_SOCKET) {
        std::cerr << "Socket creation failed!" << std::endl;
        WSACleanup();
        return;
    }

    sockaddr_in server_addr{};
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(server_port);
    server_addr.sin_addr.s_addr = inet_addr(server_ip.c_str());

    if (bind(server_sock, (sockaddr*)&server_addr, sizeof(server_addr)) == SOCKET_ERROR) {
        std::cerr << "Bind failed!" << std::endl;
        closesocket(server_sock);
        WSACleanup();
        return;
    }

    std::cout << "UDP server listening on " << server_ip << ":" << server_port << std::endl;

    char buffer[1024];
    sockaddr_in client_addr{};
    int client_addr_len = sizeof(client_addr);

    while (true) {
        memset(buffer, 0, sizeof(buffer));
        int bytes_received = recvfrom(server_sock, buffer, sizeof(buffer) - 1, 0,
                                      (sockaddr*)&client_addr, &client_addr_len);

        if (bytes_received == SOCKET_ERROR) {
            std::cerr << "recvfrom failed!" << std::endl;
            continue;
        }

        // 获取客户端 IP 和端口
        char client_ip[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, &client_addr.sin_addr, client_ip, INET_ADDRSTRLEN);
        int client_port = ntohs(client_addr.sin_port);

        std::cout << "Received message from client (" << client_ip << ", " << client_port << "): "
                  << buffer << std::endl;

        const char* response_str = "Hello, UDP client!";
        sendto(server_sock, response_str, strlen(response_str), 0, (sockaddr*)&client_addr, client_addr_len);

    }

    closesocket(server_sock);
    WSACleanup();
}

int main() {
    start_udp_server("127.0.0.1", 12345);
    return 0;
}
