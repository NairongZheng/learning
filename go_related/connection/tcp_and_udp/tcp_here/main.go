package main

import (
	"fmt"
	"tcp_here/tcp_client"
	"tcp_here/tcp_server"
	"os"
)

func main() {
    if len(os.Args) < 2 {
        fmt.Println("Usage: go run main.go [client|server]")
        return
    }

    mode := os.Args[1]
    switch mode {
    case "server":
        tcp_server.StartServer("127.0.0.1:12345")
    case "client":
        tcp_client.StartClient("127.0.0.1:12345")
    default:
        fmt.Println("Invalid mode. Use 'client' or 'server'.")
    }
}
