package grpc_server

import (
	"context"
	"log"
	"math"
	"net"

	pb "grpc_connect/proto" // 替换为实际 proto 文件的导入路径

	"google.golang.org/grpc"
)

// 定义服务结构体
type server struct {
	pb.UnimplementedGetMimDisServiceServer
}

// 实现 GetMinDis 方法
func (s *server) GetMinDis(ctx context.Context, req *pb.GetMinDisReq) (*pb.GetMinDisRsp, error) {
	pointList := req.PointList
	var minDis float32 = math.MaxFloat32

	for i := 0; i < len(pointList); i++ {
		for j := 0; j < len(pointList); j++ {
			if i != j {
				dis := float32(math.Sqrt(
					math.Pow(float64(pointList[i].X-pointList[j].X), 2) +
						math.Pow(float64(pointList[i].Y-pointList[j].Y), 2) +
						math.Pow(float64(pointList[i].Z-pointList[j].Z), 2),
				))
				if dis < minDis {
					minDis = dis
				}
			}
		}
	}
	return &pb.GetMinDisRsp{MinDis: minDis}, nil
}

func StartServer() {
	listener, err := net.Listen("tcp", ":50051")	// 创建一个 TCP 监听器，监听端口 50051。
	if err != nil {
		log.Fatalf("Failed to listen on port 50051: %v", err)
	}

	grpcServer := grpc.NewServer()	// 创建一个 gRPC 服务器实例。
	pb.RegisterGetMimDisServiceServer(grpcServer, &server{})	// 注册 GetMinDis 服务，将 server{} 作为服务实例。

	log.Println("Server is listening on port 50051...")
	if err := grpcServer.Serve(listener); err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
