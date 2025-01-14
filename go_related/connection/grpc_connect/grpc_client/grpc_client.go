package grpc_client

import (
	"context"
	"log"
	"time"

	pb "grpc_connect/proto" // 替换为实际 proto 文件的导入路径

	"google.golang.org/grpc"
)

func StartClient() {
	conn, err := grpc.Dial("127.0.0.1:50051", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Failed to connect to server: %v", err)
	}
	defer conn.Close()

	client := pb.NewGetMimDisServiceClient(conn)

	pointLists := [][]*pb.Vector{
		{{X: 1, Y: 2, Z: 3}, {X: 4, Y: 6, Z: 9}, {X: 3.6, Y: 9.2, Z: 2.3}},
		{{X: 3, Y: 0.1, Z: 2}, {X: 9, Y: 6, Z: 5.6}, {X: 9.3, Y: 32, Z: 12}, {X: 1.2, Y: 3, Z: 0.6}},
		{{X: 9, Y: 2, Z: 1}},
	}

	for _, pointList := range pointLists {
		req := &pb.GetMinDisReq{PointList: pointList}
		ctx, cancel := context.WithTimeout(context.Background(), time.Second)
		defer cancel()

		resp, err := client.GetMinDis(ctx, req)
		if err != nil {
			log.Printf("Error calling GetMinDis: %v", err)
			continue
		}

		log.Printf("Min distance: %f", resp.MinDis)
	}
}
