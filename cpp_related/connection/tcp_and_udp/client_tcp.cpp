#include <iostream>
#include <winsock2.h> // Windows 套接字头文件
#pragma comment(lib, "ws2_32.lib") // 链接 WinSock 库

void start_client(const std::string& server_ip, int server_port) {
    // 初始化 WinSock
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        std::cerr << "WSAStartup failed!" << std::endl;
        return;
    }

    SOCKET sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (sock == INVALID_SOCKET) {
        std::cerr << "Socket creation failed!" << std::endl;
        WSACleanup();
        return;
    }

    sockaddr_in server_addr{};
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(server_port);
    server_addr.sin_addr.s_addr = inet_addr(server_ip.c_str());

    if (connect(sock, (sockaddr*)&server_addr, sizeof(server_addr)) == SOCKET_ERROR) {
        std::cerr << "Connection failed!" << std::endl;
        closesocket(sock);
        WSACleanup();
        return;
    }

    const char* message = "Hello, server";
    send(sock, message, strlen(message), 0);

    char buffer[1024] = {0};
    int bytes_received = recv(sock, buffer, sizeof(buffer) - 1, 0);
    if (bytes_received > 0) {
        buffer[bytes_received] = '\0';
        std::cout << "Received from server: " << buffer << std::endl;
    }

    closesocket(sock);
    WSACleanup();

    // 添加等待逻辑
    std::cout << "Press Enter to exit...";
    std::cin.get(); // 等待用户按下回车键
}

int main() {
    start_client("127.0.0.1", 12345);
    return 0;
}
