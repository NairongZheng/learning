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
