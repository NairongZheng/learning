package main

import (
	"fmt"
	"grpc_connect/grpc_client"
	"grpc_connect/grpc_server"
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
		grpc_server.StartServer()
	case "client":
		grpc_client.StartClient()
	default:
		fmt.Println("Invalid mode. Use 'client' or 'server'.")
	}
}
