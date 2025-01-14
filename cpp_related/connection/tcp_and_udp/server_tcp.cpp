#include <iostream>
#include <winsock2.h> // Windows 套接字头文件
#pragma comment(lib, "ws2_32.lib") // 链接 WinSock 库

void start_server(const std::string& server_ip, int server_port) {
    // 初始化 WinSock
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed!" << std::endl;
        return;
    }

    SOCKET server_sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
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

    if (listen(server_sock, 1) == SOCKET_ERROR) {
        std::cerr << "Listen failed!" << std::endl;
        closesocket(server_sock);
        WSACleanup();
        return;
    }

    std::cout << "Server listening on " << server_ip << ":" << server_port << std::endl;

    while (true) {
        sockaddr_in client_addr{};
        int client_addr_len = sizeof(client_addr);
        SOCKET client_sock = accept(server_sock, (sockaddr*)&client_addr, &client_addr_len);
        if (client_sock == INVALID_SOCKET) {
            std::cerr << "Accept failed!" << std::endl;
            continue;
        }

        // 获取客户端 IP 和端口信息
        const char* client_ip = inet_ntoa(client_addr.sin_addr);
        int client_port = ntohs(client_addr.sin_port);

        std::cout << "Connected by (" << client_ip << ", " << client_port << ")" << std::endl;

        char buffer[1024] = {0};
        int bytes_received = recv(client_sock, buffer, sizeof(buffer) - 1, 0);
        if (bytes_received > 0) {
            buffer[bytes_received] = '\0';
            std::cout << "Received from client: " << buffer << std::endl;

            const char* response = "Successful connection";
            send(client_sock, response, strlen(response), 0);
        }

        closesocket(client_sock);
    }

    closesocket(server_sock);
    WSACleanup();
}

int main() {
    start_server("127.0.0.1", 12345);
    return 0;
}
