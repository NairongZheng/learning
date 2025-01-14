// 好像会有并发问题

package grpc_client

import (
	"context"
	"fmt"
	"log"
	"sync"

	pb "grpc_connect2/proto"

	"google.golang.org/grpc"
	"google.golang.org/protobuf/proto"
)

type Client struct {
	servers      []string
	timeout      int
	handler      map[string]func([]byte) interface{}
	responses    []map[string]interface{}
	mu           sync.Mutex
	reqBatchChan chan request
	wg           sync.WaitGroup // 增加 WaitGroup，用于同步请求
}

type request struct {
	id      int
	reqType string
	reqData []byte
}

func NewClient(servers []string) *Client {
	c := &Client{
		servers: servers,
		timeout: 500,
		handler: map[string]func([]byte) interface{}{
			"GetMinDisReq":       decodeGetMinDisRsp,
			"CountAndSumListReq": decodeCountAndSumListRsp,
			"UpperLettersReq":    decodeUpperLettersRsp,
		},
		reqBatchChan: make(chan request, 10),
	}

	// 启动与服务器数量相同的工作者
	for i := 0; i < len(c.servers); i++ {
		go c.worker(i)
	}

	// 输出调试信息
	log.Println("Client is initialized and workers are started.")

	return c
}

func (c *Client) worker(index int) {
	if len(c.servers) == 0 {
		log.Fatalf("No servers available")
	}

	server := c.servers[index%len(c.servers)] // 为每个worker分配服务器
	conn, err := grpc.Dial(server, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to connect to server: %v", err)
	}
	defer conn.Close()

	log.Printf("Worker %d connected to server %s", index, server)

	client := pb.NewProtoTestClient(conn)
	for req := range c.reqBatchChan {
		// log.Printf("Worker %d processing request: %+v", index, req)

		ctx := context.Background()
		msg := &pb.MessageData{
			Id:   int32(req.id),
			Name: req.reqType,
			Data: req.reqData,
		}

		resp, err := client.DoRequest(ctx, msg)
		if err != nil {
			log.Printf("gRPC error: %v", err)
			continue
		}

		c.mu.Lock()
		c.responses = append(c.responses, map[string]interface{}{
			"id":   req.id,
			"name": req.reqType,
			"data": c.handler[req.reqType](resp.Data),
		})
		c.mu.Unlock()

		// log.Printf("Worker %d processed request successfully", index) // 输出请求处理成功信息
		log.Printf("Worker %d get return: %+v", index, c.handler[req.reqType](resp.Data)) // 输出请求处理成功信息
	}

	// 完成所有请求后通知 WaitGroup
	c.wg.Done()
}

// 确保每次请求都被发送
func (c *Client) SendRequest(reqType string, reqData []byte) {
	// 如果 reqBatchChan 没有缓冲区，可能会造成阻塞问题
	// 可以调整缓冲区大小，或者在发送请求前确认队列没有被满
	select {
	case c.reqBatchChan <- request{id: len(c.responses), reqType: reqType, reqData: reqData}:
		log.Printf("Request for %s sent", reqType)
		// 在发送请求时增加一个 WaitGroup
		c.wg.Add(1)
	default:
		log.Printf("Request for %s dropped due to channel being full", reqType)
	}
}

func (c *Client) GetResponses() []map[string]interface{} {
	c.mu.Lock()
	defer c.mu.Unlock()
	return c.responses
}

// Handlers for decoding responses
func decodeGetMinDisRsp(data []byte) interface{} {
	var rsp pb.GetMinDisRsp
	if err := proto.Unmarshal(data, &rsp); err != nil {
		log.Printf("Error unmarshaling GetMinDisRsp: %v", err)
		return nil
	}
	return rsp.MinDis
}

func decodeCountAndSumListRsp(data []byte) interface{} {
	var rsp pb.CountAndSumListRsp
	if err := proto.Unmarshal(data, &rsp); err != nil {
		log.Printf("Error unmarshaling CountAndSumListRsp: %v", err)
		return nil
	}
	return rsp.CountAndSumRes
}

func decodeUpperLettersRsp(data []byte) interface{} {
	var rsp pb.UpperLettersRsp
	if err := proto.Unmarshal(data, &rsp); err != nil {
		log.Printf("Error unmarshaling UpperLettersRsp: %v", err)
		return nil
	}
	return rsp.LetterResList
}

func StartClient() {
	var wg sync.WaitGroup

	c := NewClient([]string{"127.0.0.1:50051"})
	wg.Add(3)

	// 发起请求1：GetMinDisReq
	go func() {
		pointLists := []*pb.VectorList{
			{
				PointList: []*pb.Vector{
					{X: 1, Y: 2, Z: 3},
					{X: 4, Y: 6, Z: 9},
					{X: 3.6, Y: 9.2, Z: 2.3},
				},
			},
			{
				PointList: []*pb.Vector{
					{X: 3, Y: 0.1, Z: 2},
					{X: 9, Y: 6, Z: 5.6},
					{X: 9.2, Y: 32, Z: 12},
					{X: 1.2, Y: 3, Z: 0.6},
				},
			},
			{
				PointList: []*pb.Vector{
					{X: 9, Y: 2, Z: 1},
				},
			},
		}
		req := &pb.GetMinDisReq{PointLists: pointLists}
		data, _ := proto.Marshal(req)
		c.SendRequest("GetMinDisReq", data)
		wg.Done()
	}()

	// 发起请求2：CountAndSumListReq
	go func() {
		numLists := []*pb.NumList{
			{Num: []float32{1.1, 2.2, 3.3, 1.1, 2.2, 4,4}},
			{Num: []float32{1, 2, 3, 1, 2, 4}},
			{Num: []float32{0, 1, 2, 3, 3, 2, 0}},
		}
		req2 := &pb.CountAndSumListReq{NumList: numLists}
		data2, _ := proto.Marshal(req2)
		c.SendRequest("CountAndSumListReq", data2)
		wg.Done()
	}()

	// 发起请求3：UpperLettersReq
	go func() {
		letters := []*pb.Letter{
			{S: "hello grpc"},
			{S: "fxxk grpc"},
			{S: "legendary grpc"},
		}
		req3 := &pb.UpperLettersReq{LetterList: letters}
		data3, _ := proto.Marshal(req3)
		c.SendRequest("UpperLettersReq", data3)
		wg.Done()
	}()

	// 等待所有请求完成
	wg.Wait()

	// 获取响应并打印
	responses := c.GetResponses()
	for _, resp := range responses {
		fmt.Printf("Response: %+v\n", resp)
	}
}
