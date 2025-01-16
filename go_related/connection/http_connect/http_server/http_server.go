package http_server

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strings"
)

// 定义请求和响应格式
// 后面的部分是为结构体字段指定 JSON 格式的键名。
// 在进行 JSON 编码（序列化）或解码（反序列化）时，会使用指定的键名而不是字段的原始名称。
type SumRequest struct {
	ParaA int `json:"para_a"`
	ParaB int `json:"para_b"`
}

type SumResponse struct {
	ErrCode int    `json:"errcode"`
	Data    int    `json:"data"`
	Msg     string `json:"msg"`
}

type UpperRequest struct {
	ParaStr string `json:"para_str"`
}

type UpperResponse struct {
	ErrCode int    `json:"errcode"`
	Data    string `json:"data"`
	Msg     string `json:"msg"`
}

func sumHandler(w http.ResponseWriter, r *http.Request) {
	// 解析请求体
	var request SumRequest
	err := json.NewDecoder(r.Body).Decode(&request) // 从请求体中读取 JSON 数据，并将其解析为 SumRequest 结构体。
	if err != nil {
		// 如果解析失败，向客户端返回错误信息，状态码为 400 Bad Request。
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}
	// 计算结果
	fmt.Printf("sumHandler request: %v\n", request)
	res := request.ParaA + request.ParaB
	response := SumResponse{
		ErrCode: 200,
		Data:    res,
		Msg:     "",
	}
	// 返回JSON响应
	w.Header().Set("Content-Type", "application/json") // 设置响应头，告知客户端响应内容是 JSON 格式。
	json.NewEncoder(w).Encode(response)                // 将 response 对象编码为 JSON 格式，并写入到响应中。
}

func upperHandler(w http.ResponseWriter, r *http.Request) {
	// 解析请求体
	var request map[string]string
	err := json.NewDecoder(r.Body).Decode(&request)
	if err != nil {
		http.Error(w, "Invalid request body", http.StatusBadRequest)
		return
	}

	// 获取 para_str 字段并转换为大写
	fmt.Printf("upperHandler request: %v\n", request)
	// paraStr, ok := request["para_str"].(string)
	// if !ok {
	// 	http.Error(w, "para_str is required", http.StatusBadRequest)
	// 	return
	// }
	paraStr := request["para_str"]
	result := strings.ToUpper(paraStr)

	// 构建响应
	response := UpperResponse{
		ErrCode: 200,
		Data:    result,
		Msg:     "",
	}
	// 返回JSON响应
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(response)
}

func StartServer() {
	// 设置路由和请求处理函数
	http.HandleFunc("/sumHandler", sumHandler)
	http.HandleFunc("/upperHandler", upperHandler)

	// 启动HTTP服务器
	httpPort := 12300
	fmt.Printf("Server is running on http://localhost:%d\n", httpPort)
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", httpPort), nil))
}
