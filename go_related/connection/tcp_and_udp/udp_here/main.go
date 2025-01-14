package main

import (
	"fmt"
	"udp_here/udp_client"
	"udp_here/udp_server"
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
		udp_server.StartUDPServer("127.0.0.1:12345")
	case "client":
		udp_client.SendMessageToServer("127.0.0.1:12345", "Hello, UDP server!")
	default:
		fmt.Println("Invalid mode. Use 'client' or 'server'.")
	}
}
