package http_client

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func testSum(serverHost string) {
	serverHandler := serverHost + "/sumHandler"
	request := map[string]interface{}{
		"para_a": 10,
		"para_b": 36,
	}

	fmt.Printf("debug damonzheng, request: %v\n", request)

	// 将请求序列化为 JSON
	requestBody, err := json.Marshal(request)
	if err != nil {
		fmt.Printf("Failed to marshal request: %v\n", err)
		return
	}

	// 发送 POST 请求
	resp, err := http.Post(serverHandler, "application/json", bytes.NewBuffer(requestBody))
	if err != nil {
		fmt.Printf("Failed to connect to server: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// 解析响应
	if resp.StatusCode == http.StatusOK {
		body, _ := ioutil.ReadAll(resp.Body)
		var result map[string]interface{}
		if err := json.Unmarshal(body, &result); err != nil {
			fmt.Printf("Failed to parse response: %v\n", err)
			return
		}

		if result["errcode"] == float64(200) {
			fmt.Printf("sum result from server: %v\n", result["data"])
		} else if result["errcode"] == float64(400) {
			fmt.Printf("Server error: %v\n", result["data"])
		}
	} else {
		fmt.Println("Failed to connect to server")
	}
}

func testUpper(serverHost string) {
	serverHandler := serverHost + "/upperHandler"
	request := map[string]string{
		"para_str": "lower string to upper string",
	}

	fmt.Printf("debug damonzheng, request: %v\n", request)

	// 将请求序列化为 JSON
	requestBody, err := json.Marshal(request)
	if err != nil {
		fmt.Printf("Failed to marshal request: %v\n", err)
		return
	}

	// 发送 POST 请求
	resp, err := http.Post(serverHandler, "application/json", bytes.NewBuffer(requestBody))
	if err != nil {
		fmt.Printf("Failed to connect to server: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// 解析响应
	if resp.StatusCode == http.StatusOK {
		body, _ := ioutil.ReadAll(resp.Body)
		var result map[string]interface{}
		if err := json.Unmarshal(body, &result); err != nil {
			fmt.Printf("Failed to parse response: %v\n", err)
			return
		}

		if result["errcode"] == float64(200) {
			fmt.Printf("Uppercase string from server: %v\n", result["data"])
		} else if result["errcode"] == float64(400) {
			fmt.Printf("Server error: %v\n", result["data"])
		}
	} else {
		fmt.Println("Failed to connect to server")
	}
}

func StartClient() {
	serverHost := "http://localhost:12300"
	testSum(serverHost)
	testUpper(serverHost)
}
