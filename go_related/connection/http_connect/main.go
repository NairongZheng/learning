package main

import (
	"fmt"
	"http_connect/http_client"
	"http_connect/http_server"
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
		http_server.StartServer()
	case "client":
		http_client.StartClient()
	default:
		fmt.Println("Invalid mode. Use 'client' or 'server'.")
	}
}
