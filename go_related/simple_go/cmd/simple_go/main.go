package main

import (
	"fmt"

	"github.com/nairongzheng/simple_go/internal/core"
)

func main() {
	fmt.Println("Starting app...")
	core.Run()
	fmt.Println("Press Enter to exit...")
	fmt.Scanln() // 等待用户输入
}
