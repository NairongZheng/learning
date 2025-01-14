package udp_server

import (
	"fmt"
	"net"
)

func StartUDPServer(serverAddr string) {
	// 创建UDP socket
	serverSocket, err := net.ListenPacket("udp", serverAddr)
	if err != nil {
		fmt.Println("Error starting server:", err)
		return
	}
	defer serverSocket.Close()

	fmt.Println("UDP server listening on", serverAddr)

	for {
		buf := make([]byte, 1024)
		// 接收数据
		n, clientAddr, err := serverSocket.ReadFrom(buf)
		if err != nil {
			fmt.Println("Error reading data:", err)
			continue
		}

		fmt.Printf("Received message from client %s: %s\n", clientAddr, string(buf[:n]))

		// 发送响应
		responseMessage := "Hello, UDP client!"
		_, err = serverSocket.WriteTo([]byte(responseMessage), clientAddr)
		if err != nil {
			fmt.Println("Error sending response:", err)
		}
	}
}
