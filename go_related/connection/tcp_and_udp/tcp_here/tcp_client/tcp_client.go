package tcp_client

import (
	"fmt"
	"net"
)

func StartClient(serverAddr string) {
    conn, err := net.Dial("tcp", serverAddr)	// 尝试与指定的地址建立TCP连接
    if err != nil {
        fmt.Println("Error connecting to server:", err)
        return
    }
    defer conn.Close()

    // 发送数据到服务端
    _, err = conn.Write([]byte("Hello, server"))
    if err != nil {
        fmt.Println("Error sending data:", err)
        return
    }

    // 接收服务端的响应
    buf := make([]byte, 1024)
    n, err := conn.Read(buf)
    if err != nil {
        fmt.Println("Error reading data:", err)
        return
    }

    fmt.Println("Received from server:", string(buf[:n]))
}
