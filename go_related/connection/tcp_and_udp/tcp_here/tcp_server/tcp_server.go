package tcp_server

import (
	"fmt"
	"net"
)

func StartServer(serverAddr string) {
    listener, err := net.Listen("tcp", serverAddr)	// 创建一个TCP监听器
    if err != nil {
        fmt.Println("Error starting server:", err)	// 如果出错，打印错误并退出
        return
    }
    defer listener.Close()

    fmt.Println("Server listening on", serverAddr)

    for {
        conn, err := listener.Accept()		// 接受连接请求
        if err != nil {
            fmt.Println("Error accepting connection:", err)	// 连接失败（如中断），则打印错误并等待下一个连接
            continue
        }
        go handleConnection(conn)	// 并发处理，启动一个新的goruntine，可以同事处理多个客户端请求
    }
}

func handleConnection(conn net.Conn) {
    defer conn.Close() // 确保函数退出时关闭与客户端的连接

    // 获取并打印客户端的IP和端口
    clientAddr := conn.RemoteAddr().(*net.TCPAddr)
    fmt.Printf("Connected to client: %s:%d\n", clientAddr.IP.String(), clientAddr.Port)

    // 接收客户端数据
    buf := make([]byte, 1024)
    n, err := conn.Read(buf)
    if err != nil {
        fmt.Println("Error reading data:", err)
        return
    }

    fmt.Println("Received from client:", string(buf[:n]))

    // 发送响应给客户端
    _, err = conn.Write([]byte("Successful connection"))
    if err != nil {
        fmt.Println("Error sending data:", err)
    }
}
