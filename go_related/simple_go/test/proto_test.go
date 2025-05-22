package test

import (
	"encoding/json"
	"strings"
	"testing"

	simpleGoProto "github.com/nairongzheng/simple_go/internal/proto"
	"github.com/nairongzheng/simple_go/pkg/logger"
	"github.com/nairongzheng/simple_go/pkg/utils"
	"google.golang.org/protobuf/proto"
)

type Point struct {
	X int32 `json:"x"`
	Y int32 `json:"y"`
}

type ReqStruct struct {
	Id      int32   `json:"id"`
	Content string  `json:"content"`
	Point   []Point `json:"points"`
}

func GenReq() ([]byte, error) {
	var req simpleGoProto.SimpleGoRequest
	req.Id = 1
	req.Content = "hello"
	req.Points = []*simpleGoProto.Point{}
	req.Points = append(req.Points, &simpleGoProto.Point{X: 5, Y: 7})
	req.Points = append(req.Points, &simpleGoProto.Point{X: 1, Y: 2})
	// 也可以这么写
	// req := &simpleGoProto.SimpleGoRequest{
	// 	Id:      1,
	// 	Content: "hello",
	// 	Points: []*simpleGoProto.Point{
	// 		{X: 5, Y: 7},
	// 		{X: 1, Y: 2},
	// 	},
	// }

	data, err := proto.Marshal(&req)
	if err != nil {
		return nil, err
	}
	return data, nil
}

func ProcessReq(reqByte []byte) (*simpleGoProto.SimpleGoResponse, error) {
	var (
		req simpleGoProto.SimpleGoRequest
		res simpleGoProto.SimpleGoResponse
	)
	if err := proto.Unmarshal(reqByte, &req); err != nil {
		return nil, err
	}
	var sumList []int32
	for _, p := range req.Points {
		sumList = append(sumList, p.X+p.Y)
	}

	res.Id = req.GetId()
	res.Content = "response to: " + req.GetContent()
	res.Addresult = sumList

	return &res, nil
}

func TestProtoSerialization(t *testing.T) {
	// 生成请求
	reqByte, err := GenReq()
	if err != nil {
		t.Fatalf("GenReq failed: %v", err)
	}

	// 处理请求
	resp, err := ProcessReq(reqByte)
	if err != nil {
		t.Fatalf("ProcessReq failed: %v", err)
	}

	// 验证响应内容
	expected := simpleGoProto.SimpleGoResponse{
		Id:        1,
		Content:   "response to: hello",
		Addresult: []int32{12, 3},
	}

	logger.Info("resp: %v", resp)

	if !proto.Equal(resp, &expected) {
		t.Errorf("unexpected response.\nGot: %+v\nWant: %+v", resp, &expected)
	}
}

func TestProtoSerializationFromJSON(t *testing.T) {
	// 生成请求（通过读取json文件）
	jsonPath := "../etc/testfiles/proto_test.json"
	jsonByte, err := utils.ReadJSONFile(jsonPath)
	if err != nil {
		t.Fatalf("read jsonfile failed: %v", err)
	}

	var jsonData ReqStruct
	if err = json.Unmarshal([]byte(jsonByte), &jsonData); err != nil {
		t.Fatalf("Unmarshal jsondata failed: %v", err)
	}

	// 将 jsonData 转换为 protobuf 请求
	protoReq := &simpleGoProto.SimpleGoRequest{
		Id:      jsonData.Id,
		Content: jsonData.Content,
	}

	for _, p := range jsonData.Point {
		protoReq.Points = append(protoReq.Points, &simpleGoProto.Point{
			X: p.X,
			Y: p.Y,
		})
	}
	// 序列化为字节流
	reqByte, err := proto.Marshal(protoReq)
	if err != nil {
		t.Fatalf("proto.Marshal failed: %v", err)
	}

	// 调用业务逻辑
	resp, err := ProcessReq(reqByte)
	if err != nil {
		t.Fatalf("ProcessReq failed: %v", err)
	}

	// 打印响应
	logger.Info("Response: %+v\n", resp)

	// 简单验证（可以根据你测试用例中 json 的实际数据进行断言）
	if resp.Id != protoReq.Id {
		t.Errorf("unexpected response ID: got %v, want %v", resp.Id, protoReq.Id)
	}
	if !strings.Contains(resp.Content, protoReq.Content) {
		t.Errorf("unexpected content: got %v, want to contain %v", resp.Content, protoReq.Content)
	}
}
