package udp_client

import (
	"fmt"
	"net"
)

func SendMessageToServer(serverAddr string, message string) {
	// 创建UDP socket
	clientSocket, err := net.Dial("udp", serverAddr)
	if err != nil {
		fmt.Println("Error connecting to server:", err)
		return
	}
	defer clientSocket.Close()

	// 发送消息到服务器
	_, err = clientSocket.Write([]byte(message))
	if err != nil {
		fmt.Println("Error sending message:", err)
		return
	}

	// 接收服务器响应
	buf := make([]byte, 1024)
	n, err := clientSocket.Read(buf)
	if err != nil {
		fmt.Println("Error reading response:", err)
		return
	}

	fmt.Printf("Received response from server: %s\n", string(buf[:n]))
}
