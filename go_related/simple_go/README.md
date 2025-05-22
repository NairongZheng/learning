
以该 simple_go 为例

**go项目结构**

```bash
simple_go/
├── cmd/                    # 各个可执行程序的 main 包
│   └── simple_go/          # 主程序入口
│       └── main.go
├── docs/                   # 文档
├── etc/                    # 配置文件等
│   └── configs
│       └── config.yaml
├── internal/               # 私有逻辑包，只能被本模块导入
│   └── core/               # 核心业务逻辑
│       └── core.go
├── pkg/                    # 可被外部导入的库包
│   └── utils/              # 工具函数
│       └── utils.go
├── scripts/                # 各种脚本（如构建、部署脚本）
├── api/                    # 存放 API 定义、proto 文件等（可选）
├── test/                   # 额外测试代码
├── go.mod                  # 模块定义文件
├── go.sum                  # 依赖哈希校验文件
├── Makefile                # 项目构建与自动化命令
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
	go test -v ./...

.PHONY: run-test
run-test: build run test

.PHONY: proto
proto:
	sh build_proto.sh

.PHONY: clean
clean:
	$(CLEAN_CMD)
```

**运行**

```bash
sh start.sh
# make proto   # 编译proto
# make build   # 构建
# make run     # 运行
# make test    # 测试
```

**makefile部分解释**

在makefile中，每个规则的基本格式是：

```bash
.PHONY: target
target: dependencies
	<shell 命令>
	# @ <shell 命令>

# 具体解释：
# .PHONY: target
    # .PHONY 是一个特殊的伪目标，它的作用是告诉 make，target 不是一个实际的文件，而是一个伪目标。
    # make 默认会检查文件是否存在，如果目标是一个文件，且文件没有变化，make 会跳过这个目标。但通过 .PHONY 告诉 make，即使文件存在，依然执行目标规则。
    # 所以，.PHONY: target 使得 make 每次运行时，都会执行 target 相关的命令，无论 target 是否存在。
# target: dependencies
    # target 是一个目标名，它可以是你希望 make 构建的任何东西。例如，build、clean、install 等等。
    # dependencies 是 target 的依赖，它可以是一个或多个目标，表示 target 在执行前，必须先执行这些依赖。
# <shell 命令>
    # 这行命令是 make 在构建目标时执行的操作。命令通常是一个或多个 shell 命令。它们是执行具体工作的部分。
    # 每行命令都必须以 TAB 键缩进（而不是空格），否则 make 会报错。
# @
    # 可选是否加@，如果加@就不会在命令行中显示'<shell 命令>'本身

# 如：
.PHONY: build
build: clean
	@ go build -o $(BIN_FILE) ./$(CMD_DIR)
```