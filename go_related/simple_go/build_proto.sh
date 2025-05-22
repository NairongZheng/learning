go env -w GOPROXY=https://mirrors.aliyun.com/goproxy/,direct
apt-get install protobuf-compiler
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
export PATH=$PATH:$(go env GOPATH)/bin

protoc \
    --proto_path="proto" \
    --go_out="internal/proto" \
    --go_opt=paths=source_relative \
    proto/*.proto
