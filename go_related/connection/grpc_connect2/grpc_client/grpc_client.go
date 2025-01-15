// 只有一个服务器一个进程请求
package grpc_client

import (
	"context"
	"fmt"
	"log"

	grpc_test_pb "grpc_connect2/proto"

	"google.golang.org/grpc"
	"google.golang.org/protobuf/proto"
)

// 创建一个Test结构体（可理解为python的类）
type Test struct {
	client Client
}

// 创建一个Client结构体（可理解为python的类）
type Client struct {
	serverAddress  string
	handler      map[string]func([]byte) interface{}
}

// Client结构体的方法（可以理解为python类中的self函数）
func (c *Client) divideList(lst interface{}, batchSize int) [][]interface{} {
	var result [][]interface{}
	var currentBatch []interface{}
	switch v := lst.(type) {
	case [][][]float32:
		for _, item := range v {
			currentBatch = append(currentBatch, item)
			if len(currentBatch) == batchSize {
				result = append(result, currentBatch)
				currentBatch = nil
			}
		}
	case [][]float32:
		for _, item := range v {
			currentBatch = append(currentBatch, item)
			if len(currentBatch) == batchSize {
				result = append(result, currentBatch)
				currentBatch = nil
			}
		}
	case []string:
		for _, item := range v {
			currentBatch = append(currentBatch, item)
			if len(currentBatch) == batchSize {
				result = append(result, currentBatch)
				currentBatch = nil
			}
		}
	}
	if len(currentBatch) > 0 {
		result = append(result, currentBatch)
	}
	return result
}

// Client结构体的方法（可以理解为python类中的self函数）
func (c *Client) createRequest(reqData interface{}, reqType string) ([]byte, error) {
	batchItems, ok := reqData.([]interface{})
	if !ok {
		return nil, fmt.Errorf("invalid type for reqData, expected []interface{}")
	}
	switch reqType {
	case "GetMinDisReq":
		reqMsg := &grpc_test_pb.GetMinDisReq{}
		for _, item := range batchItems {
			pointList, ok := item.([][]float32)
			if !ok {
                return nil, fmt.Errorf("invalid item type in reqData, expected [][]float32")
            }
			pointListMsg := &grpc_test_pb.VectorList{}
            for _, point := range pointList {
                pointMsg := &grpc_test_pb.Vector{
                    X: point[0],
                    Y: point[1],
                    Z: point[2],
                }
                pointListMsg.PointList = append(pointListMsg.PointList, pointMsg)
            }
            reqMsg.PointLists = append(reqMsg.PointLists, pointListMsg)
		}
		// fmt.Println("GetMinDisReq reqMsg: ", reqMsg)
		return proto.Marshal(reqMsg)
	case "CountAndSumListReq":
		reqMsg := &grpc_test_pb.CountAndSumListReq{}
		for _, item := range batchItems {
			numList, ok := item.([]float32)
			if !ok {
                return nil, fmt.Errorf("invalid item type in batch, expected []float32")
            }
			numListMsg := &grpc_test_pb.NumList{}
            numListMsg.Num = append(numListMsg.Num, numList...)
            reqMsg.NumList = append(reqMsg.NumList, numListMsg)
		}
		// fmt.Println("CountAndSumListReq reqMsg: ", reqMsg)
		return proto.Marshal(reqMsg)
	case "UpperLettersReq":
		reqMsg := &grpc_test_pb.UpperLettersReq{}
		for _, item := range batchItems {
			letter, ok := item.(string)
			if !ok {
                return nil, fmt.Errorf("invalid item type in batch, expected string")
            }
			reqMsg.LetterList = append(reqMsg.LetterList, &grpc_test_pb.Letter{S: letter})
		}
		// fmt.Println("UpperLettersReq reqMsg: ", reqMsg)
		return proto.Marshal(reqMsg)
	default:
		return nil, fmt.Errorf("unknown request type: %s", reqType)
	}
}

// Client结构体的方法（可以理解为python类中的self函数）
func (c *Client) decodeGetMinDisRsp(data []byte) interface{} {
	var rsp grpc_test_pb.GetMinDisRsp
	if err := proto.Unmarshal(data, &rsp); err != nil {
		log.Printf("Error unmarshaling GetMinDisRsp: %v", err)
		return nil
	}
	return rsp.MinDis
}

// Client结构体的方法（可以理解为python类中的self函数）
func (c *Client) decodeCountAndSumListRsp(data []byte) interface{} {
	var rsp grpc_test_pb.CountAndSumListRsp
	if err := proto.Unmarshal(data, &rsp); err != nil {
		log.Printf("Error unmarshaling CountAndSumListRsp: %v", err)
		return nil
	}
	return rsp.CountAndSumRes
}

// Client结构体的方法（可以理解为python类中的self函数）
func (c *Client) decodeUpperLettersRsp(data []byte) interface{} {
	var rsp grpc_test_pb.UpperLettersRsp
	if err := proto.Unmarshal(data, &rsp); err != nil {
		log.Printf("Error unmarshaling UpperLettersRsp: %v", err)
		return nil
	}
	return rsp.LetterResList
}

// Client结构体的方法（可以理解为python类中的self函数）
func (c *Client) decodeResponse(rspByteData []byte, reqType string) (interface{}, error) {
	handlerFunc, exists := c.handler[reqType]
	if !exists {
		return nil, fmt.Errorf("no handler found for request type: %s", reqType)
	}
	decodedResult := handlerFunc(rspByteData)
	return decodedResult, nil
}

// Client结构体的方法（可以理解为python类中的self函数）
func (c *Client) processRequests(data interface{}, reqType string) ([]interface{}, error){
	batches := c.divideList(data, 2)
	// fmt.Println("batches: ", batches)
	var result []interface{}

	conn, err := grpc.Dial(c.serverAddress, grpc.WithInsecure())
	if err != nil {
		log.Printf("failed to connect: %v", err)
		return nil, err
	}
	defer conn.Close()
	ctx := context.Background()
	client := grpc_test_pb.NewProtoTestClient(conn)
	for idx, batch := range batches {
		// fmt.Println("batch: ", batch)
		// fmt.Printf("Type of batch: %T\n", batch)
		reqDataBytes, err := c.createRequest(batch, reqType)
		if err != nil {
			return nil, err
		}
		msg := &grpc_test_pb.MessageData{}
		msg.Id = int32(idx)
		msg.Name = reqType
		msg.Data = reqDataBytes

		rspByteData, err := client.DoRequest(ctx, msg)
		if err != nil {
			return nil, err
		}
		rspPost, _ := c.decodeResponse(rspByteData.GetData(), reqType)	// 只解析了一层，懒得解析了
		result = append(result, rspPost)
	}
	return result, nil
}

// Test结构体的方法（可以理解为python类中的self函数）
func (t *Test) testGetMinDisReq() {
	// 测试GetMinDisReq
	pointLists := [][][]float32{
		{{1, 2, 3}, {4, 6, 9}, {3.6, 9.2, 2.3}},
		{{3, 0.1, 2}, {9, 6, 5.6}, {9.2, 32, 12}},
		{{1.2, 3, 0.6}},
	}
	results1, err1 := t.client.processRequests(pointLists, "GetMinDisReq")
	if err1 != nil {
		log.Printf("GetMinDisReq error: %v", err1)
	} else {
		fmt.Println("GetMinDisReq Results:", results1)
	}
}

// Test结构体的方法（可以理解为python类中的self函数）
func (t *Test) testCountAndSumListReq() {
	// 测试CountAndSumListReq
	numbers := [][]float32{
		{1.1, 2.2, 3.3, 1.1, 2.2, 4.4},
		{1, 2, 3, 1, 2, 4},
		{0, 1, 2, 3, 3, 2, 0},
	}
	results2, err2 := t.client.processRequests(numbers, "CountAndSumListReq")
	if err2 != nil {
		log.Printf("CountAndSumListReq error: %v", err2)
	} else {
		fmt.Println("CountAndSumListReq Results:", results2)
	}
}

// Test结构体的方法（可以理解为python类中的self函数）
func (t *Test) testUpperLettersReq() {
	// 测试UpperLettersReq
	stringList := []string{
		"hello grpc",
		"fxxk grpc",
		"legendary grpc",
	}
	results3, err3 := t.client.processRequests(stringList, "UpperLettersReq")
	if err3 != nil {
		log.Printf("UpperLettersReq error: %v", err3)
	} else {
		fmt.Println("UpperLettersReq Results:", results3)
	}
}

// 普通方法
func testUpperLettersReq(client *Client) {
	// 测试UpperLettersReq
	stringList := []string{
		"hello grpc",
		"fxxk grpc",
		"legendary grpc",
	}
	results3, err3 := client.processRequests(stringList, "UpperLettersReq")
	if err3 != nil {
		log.Printf("UpperLettersReq error: %v", err3)
	} else {
		fmt.Println("UpperLettersReq Results:", results3)
	}
}

// 这个函数用来创建一个Test实例
func NewTest(client Client) *Test {
	t := &Test{
		client: client,
	}
	return t
}

// 这个函数用来创建一个Client实例
func NewClient(servers string) *Client {
	c := &Client{
		serverAddress: servers,
	}
	c.handler = map[string]func([]byte) interface{}{
        "GetMinDisReq":       c.decodeGetMinDisRsp,
        "CountAndSumListReq": c.decodeCountAndSumListRsp,
        "UpperLettersReq":    c.decodeUpperLettersRsp,
    }
	// 输出调试信息
	log.Println("Client is initialized.")
	return c
}

func StartClient() {
	client := NewClient("127.0.0.1:50051")
	test := NewTest(*client)
	test.testGetMinDisReq()
	test.testCountAndSumListReq()
	test.testUpperLettersReq()
	
	testUpperLettersReq(client)	// 也可以不用这么麻烦，直接用普通函数，就不需要Test类了
}