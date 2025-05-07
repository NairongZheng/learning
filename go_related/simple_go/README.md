
以该 simple_go 为例

**go项目结构**

```bash
simple_go/
├── cmd/                # 各个可执行程序的 main 包
│   └── simple_go/          # 主程序入口
│       └── main.go
├── internal/           # 私有逻辑包，只能被本模块导入
│   └── core/           # 核心业务逻辑
│       └── core.go
├── pkg/                # 可被外部导入的库包
│   └── utils/          # 工具函数
│       └── utils.go
├── api/                # 存放 API 定义、proto 文件等（可选）
├── configs/            # 配置文件
│   └── config.yaml
├── scripts/            # 各种脚本（如构建、部署脚本）
├── test/               # 额外测试代码
├── go.mod              # 模块定义文件
├── go.sum              # 依赖哈希校验文件
├── Makefile            # 项目构建与自动化命令
└── README.md
```

**初始化项目**

```bash
# 创建项目
mkdir simple_go
cd simple_go
# 初始化项目
go mod init github.com/<yourname>/simple_go
# 创建文件夹和文件
mkdir -p cmd/simple_go internal/core pkg/utils configs scripts test
touch cmd/simple_go/main.go internal/core/core.go pkg/utils/utils.go configs/config.yaml
```

**开发**

```go
// cmd/simple_go/main.go
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
```

```go
// internal/core/core.go
package core

import "fmt"

func Run() {
	fmt.Println("Core logic running!")
}
```

```go
// pkg/utils/utils.go
package utils

func Add(a, b int) int {
	return a + b
}
```

```go
// test/utils_test.go
package test

import (
	"fmt"
	"testing"

	"github.com/nairongzheng/simple_go/pkg/utils"
)

func TestAdd(t *testing.T) {
	result := utils.Add(1, 2)
	fmt.Println("Result of Add(1, 2):", result) // 打印结果
	t.Logf("Result of Add(1, 2) = %d", result)  // go test -v 中打印结果
	if result != 3 {
		t.Errorf("Expected 3, got %d", result)
	}
}
```

**整理依赖**

```bash
go mod tidy
```

**编写makefile**

```bash
APP_NAME = simple_go
CMD_DIR = cmd/$(APP_NAME)
BIN_DIR = bin

# 判断平台
ifeq ($(OS),Windows_NT)
	BIN_FILE = $(BIN_DIR)/$(APP_NAME).exe
	RUN_BIN = .\\$(BIN_FILE)
	CLEAN_CMD = del /Q /S $(subst /,\\,$(BIN_DIR))\* 2>NUL || exit 0 & rmdir /S /Q $(subst /,\\,$(BIN_DIR)) 2>NUL || exit 0
else
	BIN_FILE = $(BIN_DIR)/$(APP_NAME)
	RUN_BIN = ./$(BIN_FILE)
	CLEAN_CMD = rm -rf $(BIN_DIR)/
endif

.PHONY: build
build:
	go build -o $(BIN_FILE) ./$(CMD_DIR)

.PHONY: run
run:
	go run ./$(CMD_DIR)

.PHONY: run-bin
run-bin:
	$(RUN_BIN)

.PHONY: test
test:
	go test ./...

.PHONY: fmt
fmt:
	go fmt ./...

.PHONY: lint
lint:
	golangci-lint run

.PHONY: install-linter
install-linter:
	go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest

.PHONY: clean
clean:
	$(CLEAN_CMD)
```

**运行**

```bash
make build   # 构建
make run     # 运行
make test    # 测试
```