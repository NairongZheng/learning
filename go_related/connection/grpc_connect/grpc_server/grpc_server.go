package grpc_server

import (
	"context"
	"log"
	"math"
	"net"

	pb "grpc_connect/proto"

	"google.golang.org/grpc"
)

// 定义服务结构体
type server struct {
	// 创建server结构体，继承了pb.UnimplementedGetMimDisServiceServer结构体的所有方法
	pb.UnimplementedGetMimDisServiceServer
}

// 实现 server 的 GetMinDis 方法
func (s *server) GetMinDis(ctx context.Context, req *pb.GetMinDisReq) (*pb.GetMinDisRsp, error) {
	pointList := req.PointList

	// 打印收到的点的个数
	log.Printf("Received %d points.\n", len(pointList))

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
	if minDis == math.MaxFloat32 {
		minDis = -1
	}
	log.Printf("result %f.\n", minDis)
	return &pb.GetMinDisRsp{MinDis: minDis}, nil
}

func StartServer() {
	listener, err := net.Listen("tcp", ":50051")	// 创建一个TCP监听器，监听端口50051。
	if err != nil {
		log.Fatalf("Failed to listen on port 50051: %v", err)
	}

	grpcServer := grpc.NewServer()	// 初始化grpc服务
	pb.RegisterGetMimDisServiceServer(grpcServer, &server{})	// 将自定义的业务逻辑注册到grpc服务器中

	log.Println("Server is listening on port 50051...")
	err = grpcServer.Serve(listener)	// 将grpc服务绑定在上面创建的tcp端口
	if err != nil {
		log.Fatalf("Failed to serve: %v", err)
	}
}
