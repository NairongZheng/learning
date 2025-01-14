# connection

- tcp_and_udp: 很基础的tcp/udp传输
- grpc_connect: grpc通信(proto)



## go使用grpc
1. 安装 `protoc-gen-go` 和 `protoc-gen-go-grpc`：
   1. `go install google.golang.org/protobuf/cmd/protoc-gen-go@latest`
   2. `go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest`
2. 编译：在proto文件夹下运行以下命令：
   1. `protoc --go_out=. --go-grpc_out=. -I proto proto/grpc_test.proto`
   2. 由于proto文件中有一行 `option go_package = "*********/pb;pb";`，就会在pb文件夹下输出生成的文件