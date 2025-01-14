package grpc_server

import (
	"context"
	"fmt"
	"log"
	"math"
	"net"
	"strings"

	pb "grpc_connect2/proto"

	"google.golang.org/grpc"
	"google.golang.org/protobuf/proto" // 导入 proto 包
)

// ProtoTestServer 实现 ProtoTest gRPC 服务
type ProtoTestServer struct {
	pb.UnimplementedProtoTestServer
}

// GetMinDis 处理 GetMinDisReq 请求
func (s *ProtoTestServer) GetMinDis(req *pb.GetMinDisReq) (*pb.GetMinDisRsp, error) {
	log.Printf("Received GetMinDisReq: %v", req) // 打印请求内容
	log.Printf("-------------------------------------------------")
	var minDisList []float32
	for _, pointLists := range req.PointLists {
		minDis := float32(math.MaxFloat32)
		points := pointLists.PointList
		for i := 0; i < len(points); i++ {
			for j := i + 1; j < len(points); j++ {
				dis := float32(math.Sqrt(
					math.Pow(float64(points[i].X-points[j].X), 2) +
						math.Pow(float64(points[i].Y-points[j].Y), 2) +
						math.Pow(float64(points[i].Z-points[j].Z), 2),
				))
				if dis < minDis {
					minDis = dis
				}
			}
		}
		if minDis == float32(math.MaxFloat32) {
			minDisList = append(minDisList, -1)
		} else {
			minDisList = append(minDisList, minDis)
		}
	}
	return &pb.GetMinDisRsp{MinDis: minDisList}, nil
}

// CountAndSumList 处理 CountAndSumListReq 请求
func (s *ProtoTestServer) CountAndSumList(req *pb.CountAndSumListReq) (*pb.CountAndSumListRsp, error) {
	log.Printf("Received CountAndSumListReq: %v", req) // 打印请求内容
	log.Printf("-------------------------------------------------")
	var resList []*pb.CountAndSumResInstruct
	for _, numList := range req.NumList {
		countMap := make(map[string]int32)
		var sum float32
		for _, num := range numList.Num {
			key := fmt.Sprintf("%.2f", num)
			countMap[key]++
			sum += num
		}
		resList = append(resList, &pb.CountAndSumResInstruct{
			CountDict: countMap,
			SumRes:    sum,
		})
	}
	return &pb.CountAndSumListRsp{CountAndSumRes: resList}, nil
}

// UpperLetters 处理 UpperLettersReq 请求
func (s *ProtoTestServer) UpperLetters(req *pb.UpperLettersReq) (*pb.UpperLettersRsp, error) {
	log.Printf("Received UpperLettersReq: %v", req) // 打印请求内容
	log.Printf("-------------------------------------------------")
	var resList []*pb.Letter
	for _, letter := range req.LetterList {
		resList = append(resList, &pb.Letter{S: strings.ToUpper(letter.S)})
	}
	return &pb.UpperLettersRsp{LetterResList: resList}, nil
}

// DoRequest 处理通用请求
func (s *ProtoTestServer) DoRequest(ctx context.Context, req *pb.MessageData) (*pb.MessageData, error) {
	switch req.Name {
	case "GetMinDisReq":
		data := &pb.GetMinDisReq{}
		if err := proto.Unmarshal(req.Data, data); err != nil { // 使用 proto.Unmarshal
			return nil, err
		}
		res, err := s.GetMinDis(data)
		if err != nil {
			return nil, err
		}
		dataBytes, err := proto.Marshal(res) // 使用 proto.Marshal
		if err != nil {
			return nil, err
		}
		return &pb.MessageData{Id: req.Id, Name: req.Name, Data: dataBytes}, nil
	case "CountAndSumListReq":
		data := &pb.CountAndSumListReq{}
		if err := proto.Unmarshal(req.Data, data); err != nil { // 使用 proto.Unmarshal
			return nil, err
		}
		res, err := s.CountAndSumList(data)
		if err != nil {
			return nil, err
		}
		dataBytes, err := proto.Marshal(res) // 使用 proto.Marshal
		if err != nil {
			return nil, err
		}
		return &pb.MessageData{Id: req.Id, Name: req.Name, Data: dataBytes}, nil
	case "UpperLettersReq":
		data := &pb.UpperLettersReq{}
		if err := proto.Unmarshal(req.Data, data); err != nil { // 使用 proto.Unmarshal
			return nil, err
		}
		res, err := s.UpperLetters(data)
		if err != nil {
			return nil, err
		}
		dataBytes, err := proto.Marshal(res) // 使用 proto.Marshal
		if err != nil {
			return nil, err
		}
		return &pb.MessageData{Id: req.Id, Name: req.Name, Data: dataBytes}, nil
	default:
		return nil, fmt.Errorf("unknown request type: %s", req.Name)
	}
}

// 启动 gRPC 服务
func StartServer() {
	listener, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("Failed to listen on port 50051: %v", err)
	}

	grpcServer := grpc.NewServer()
	pb.RegisterProtoTestServer(grpcServer, &ProtoTestServer{})

	log.Println("Server is running on 127.0.0.1:50051...")
	if err := grpcServer.Serve(listener); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
