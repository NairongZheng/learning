// 编译命令：protoc --go_out=. --go-grpc_out=. -I . grpc_test.proto

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.2
// 	protoc        v5.26.0
// source: grpc_test.proto

package proto

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// 1. 获取最小距离
type Vector struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	X             float32                `protobuf:"fixed32,1,opt,name=x,proto3" json:"x,omitempty"`
	Y             float32                `protobuf:"fixed32,2,opt,name=y,proto3" json:"y,omitempty"`
	Z             float32                `protobuf:"fixed32,3,opt,name=z,proto3" json:"z,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *Vector) Reset() {
	*x = Vector{}
	mi := &file_grpc_test_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Vector) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Vector) ProtoMessage() {}

func (x *Vector) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Vector.ProtoReflect.Descriptor instead.
func (*Vector) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{0}
}

func (x *Vector) GetX() float32 {
	if x != nil {
		return x.X
	}
	return 0
}

func (x *Vector) GetY() float32 {
	if x != nil {
		return x.Y
	}
	return 0
}

func (x *Vector) GetZ() float32 {
	if x != nil {
		return x.Z
	}
	return 0
}

type VectorList struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PointList     []*Vector              `protobuf:"bytes,1,rep,name=point_list,json=pointList,proto3" json:"point_list,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *VectorList) Reset() {
	*x = VectorList{}
	mi := &file_grpc_test_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *VectorList) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*VectorList) ProtoMessage() {}

func (x *VectorList) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use VectorList.ProtoReflect.Descriptor instead.
func (*VectorList) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{1}
}

func (x *VectorList) GetPointList() []*Vector {
	if x != nil {
		return x.PointList
	}
	return nil
}

type GetMinDisReq struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	PointLists    []*VectorList          `protobuf:"bytes,1,rep,name=point_lists,json=pointLists,proto3" json:"point_lists,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetMinDisReq) Reset() {
	*x = GetMinDisReq{}
	mi := &file_grpc_test_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetMinDisReq) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetMinDisReq) ProtoMessage() {}

func (x *GetMinDisReq) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetMinDisReq.ProtoReflect.Descriptor instead.
func (*GetMinDisReq) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{2}
}

func (x *GetMinDisReq) GetPointLists() []*VectorList {
	if x != nil {
		return x.PointLists
	}
	return nil
}

type GetMinDisRsp struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	MinDis        []float32              `protobuf:"fixed32,1,rep,packed,name=min_dis,json=minDis,proto3" json:"min_dis,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *GetMinDisRsp) Reset() {
	*x = GetMinDisRsp{}
	mi := &file_grpc_test_proto_msgTypes[3]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *GetMinDisRsp) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetMinDisRsp) ProtoMessage() {}

func (x *GetMinDisRsp) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[3]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetMinDisRsp.ProtoReflect.Descriptor instead.
func (*GetMinDisRsp) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{3}
}

func (x *GetMinDisRsp) GetMinDis() []float32 {
	if x != nil {
		return x.MinDis
	}
	return nil
}

// 2. 统计数出现的频率，并相加
type NumList struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Num           []float32              `protobuf:"fixed32,1,rep,packed,name=num,proto3" json:"num,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *NumList) Reset() {
	*x = NumList{}
	mi := &file_grpc_test_proto_msgTypes[4]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *NumList) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*NumList) ProtoMessage() {}

func (x *NumList) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[4]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use NumList.ProtoReflect.Descriptor instead.
func (*NumList) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{4}
}

func (x *NumList) GetNum() []float32 {
	if x != nil {
		return x.Num
	}
	return nil
}

type CountAndSumListReq struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	NumList       []*NumList             `protobuf:"bytes,1,rep,name=num_list,json=numList,proto3" json:"num_list,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CountAndSumListReq) Reset() {
	*x = CountAndSumListReq{}
	mi := &file_grpc_test_proto_msgTypes[5]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CountAndSumListReq) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CountAndSumListReq) ProtoMessage() {}

func (x *CountAndSumListReq) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[5]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CountAndSumListReq.ProtoReflect.Descriptor instead.
func (*CountAndSumListReq) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{5}
}

func (x *CountAndSumListReq) GetNumList() []*NumList {
	if x != nil {
		return x.NumList
	}
	return nil
}

type CountAndSumResInstruct struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	CountDict     map[string]int32       `protobuf:"bytes,1,rep,name=count_dict,json=countDict,proto3" json:"count_dict,omitempty" protobuf_key:"bytes,1,opt,name=key" protobuf_val:"varint,2,opt,name=value"`
	SumRes        float32                `protobuf:"fixed32,2,opt,name=sum_res,json=sumRes,proto3" json:"sum_res,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *CountAndSumResInstruct) Reset() {
	*x = CountAndSumResInstruct{}
	mi := &file_grpc_test_proto_msgTypes[6]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CountAndSumResInstruct) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CountAndSumResInstruct) ProtoMessage() {}

func (x *CountAndSumResInstruct) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[6]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CountAndSumResInstruct.ProtoReflect.Descriptor instead.
func (*CountAndSumResInstruct) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{6}
}

func (x *CountAndSumResInstruct) GetCountDict() map[string]int32 {
	if x != nil {
		return x.CountDict
	}
	return nil
}

func (x *CountAndSumResInstruct) GetSumRes() float32 {
	if x != nil {
		return x.SumRes
	}
	return 0
}

type CountAndSumListRsp struct {
	state          protoimpl.MessageState    `protogen:"open.v1"`
	CountAndSumRes []*CountAndSumResInstruct `protobuf:"bytes,1,rep,name=count_and_sum_res,json=countAndSumRes,proto3" json:"count_and_sum_res,omitempty"`
	unknownFields  protoimpl.UnknownFields
	sizeCache      protoimpl.SizeCache
}

func (x *CountAndSumListRsp) Reset() {
	*x = CountAndSumListRsp{}
	mi := &file_grpc_test_proto_msgTypes[7]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *CountAndSumListRsp) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*CountAndSumListRsp) ProtoMessage() {}

func (x *CountAndSumListRsp) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[7]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use CountAndSumListRsp.ProtoReflect.Descriptor instead.
func (*CountAndSumListRsp) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{7}
}

func (x *CountAndSumListRsp) GetCountAndSumRes() []*CountAndSumResInstruct {
	if x != nil {
		return x.CountAndSumRes
	}
	return nil
}

// 3. 字符转大写
type Letter struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	S             string                 `protobuf:"bytes,1,opt,name=s,proto3" json:"s,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *Letter) Reset() {
	*x = Letter{}
	mi := &file_grpc_test_proto_msgTypes[8]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Letter) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Letter) ProtoMessage() {}

func (x *Letter) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[8]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Letter.ProtoReflect.Descriptor instead.
func (*Letter) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{8}
}

func (x *Letter) GetS() string {
	if x != nil {
		return x.S
	}
	return ""
}

type UpperLettersReq struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	LetterList    []*Letter              `protobuf:"bytes,1,rep,name=letter_list,json=letterList,proto3" json:"letter_list,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *UpperLettersReq) Reset() {
	*x = UpperLettersReq{}
	mi := &file_grpc_test_proto_msgTypes[9]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpperLettersReq) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpperLettersReq) ProtoMessage() {}

func (x *UpperLettersReq) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[9]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpperLettersReq.ProtoReflect.Descriptor instead.
func (*UpperLettersReq) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{9}
}

func (x *UpperLettersReq) GetLetterList() []*Letter {
	if x != nil {
		return x.LetterList
	}
	return nil
}

type UpperLettersRsp struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	LetterResList []*Letter              `protobuf:"bytes,1,rep,name=letter_res_list,json=letterResList,proto3" json:"letter_res_list,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *UpperLettersRsp) Reset() {
	*x = UpperLettersRsp{}
	mi := &file_grpc_test_proto_msgTypes[10]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *UpperLettersRsp) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UpperLettersRsp) ProtoMessage() {}

func (x *UpperLettersRsp) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[10]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UpperLettersRsp.ProtoReflect.Descriptor instead.
func (*UpperLettersRsp) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{10}
}

func (x *UpperLettersRsp) GetLetterResList() []*Letter {
	if x != nil {
		return x.LetterResList
	}
	return nil
}

// //////////////////////////////////////////
// 定义服务数据类型
type MessageData struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Id            int32                  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`    // request package id.
	Name          string                 `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"` // message name.
	Data          []byte                 `protobuf:"bytes,3,opt,name=data,proto3" json:"data,omitempty"` // data payload
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *MessageData) Reset() {
	*x = MessageData{}
	mi := &file_grpc_test_proto_msgTypes[11]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *MessageData) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MessageData) ProtoMessage() {}

func (x *MessageData) ProtoReflect() protoreflect.Message {
	mi := &file_grpc_test_proto_msgTypes[11]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MessageData.ProtoReflect.Descriptor instead.
func (*MessageData) Descriptor() ([]byte, []int) {
	return file_grpc_test_proto_rawDescGZIP(), []int{11}
}

func (x *MessageData) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *MessageData) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *MessageData) GetData() []byte {
	if x != nil {
		return x.Data
	}
	return nil
}

var File_grpc_test_proto protoreflect.FileDescriptor

var file_grpc_test_proto_rawDesc = []byte{
	0x0a, 0x0f, 0x67, 0x72, 0x70, 0x63, 0x5f, 0x74, 0x65, 0x73, 0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x12, 0x09, 0x67, 0x72, 0x70, 0x63, 0x5f, 0x74, 0x65, 0x73, 0x74, 0x22, 0x32, 0x0a, 0x06,
	0x56, 0x65, 0x63, 0x74, 0x6f, 0x72, 0x12, 0x0c, 0x0a, 0x01, 0x78, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x02, 0x52, 0x01, 0x78, 0x12, 0x0c, 0x0a, 0x01, 0x79, 0x18, 0x02, 0x20, 0x01, 0x28, 0x02, 0x52,
	0x01, 0x79, 0x12, 0x0c, 0x0a, 0x01, 0x7a, 0x18, 0x03, 0x20, 0x01, 0x28, 0x02, 0x52, 0x01, 0x7a,
	0x22, 0x3e, 0x0a, 0x0a, 0x56, 0x65, 0x63, 0x74, 0x6f, 0x72, 0x4c, 0x69, 0x73, 0x74, 0x12, 0x30,
	0x0a, 0x0a, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x5f, 0x6c, 0x69, 0x73, 0x74, 0x18, 0x01, 0x20, 0x03,
	0x28, 0x0b, 0x32, 0x11, 0x2e, 0x67, 0x72, 0x70, 0x63, 0x5f, 0x74, 0x65, 0x73, 0x74, 0x2e, 0x56,
	0x65, 0x63, 0x74, 0x6f, 0x72, 0x52, 0x09, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x4c, 0x69, 0x73, 0x74,
	0x22, 0x46, 0x0a, 0x0c, 0x47, 0x65, 0x74, 0x4d, 0x69, 0x6e, 0x44, 0x69, 0x73, 0x52, 0x65, 0x71,
	0x12, 0x36, 0x0a, 0x0b, 0x70, 0x6f, 0x69, 0x6e, 0x74, 0x5f, 0x6c, 0x69, 0x73, 0x74, 0x73, 0x18,
	0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x15, 0x2e, 0x67, 0x72, 0x70, 0x63, 0x5f, 0x74, 0x65, 0x73,
	0x74, 0x2e, 0x56, 0x65, 0x63, 0x74, 0x6f, 0x72, 0x4c, 0x69, 0x73, 0x74, 0x52, 0x0a, 0x70, 0x6f,
	0x69, 0x6e, 0x74, 0x4c, 0x69, 0x73, 0x74, 0x73, 0x22, 0x27, 0x0a, 0x0c, 0x47, 0x65, 0x74, 0x4d,
	0x69, 0x6e, 0x44, 0x69, 0x73, 0x52, 0x73, 0x70, 0x12, 0x17, 0x0a, 0x07, 0x6d, 0x69, 0x6e, 0x5f,
	0x64, 0x69, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x02, 0x52, 0x06, 0x6d, 0x69, 0x6e, 0x44, 0x69,
	0x73, 0x22, 0x1b, 0x0a, 0x07, 0x4e, 0x75, 0x6d, 0x4c, 0x69, 0x73, 0x74, 0x12, 0x10, 0x0a, 0x03,
	0x6e, 0x75, 0x6d, 0x18, 0x01, 0x20, 0x03, 0x28, 0x02, 0x52, 0x03, 0x6e, 0x75, 0x6d, 0x22, 0x43,
	0x0a, 0x12, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x41, 0x6e, 0x64, 0x53, 0x75, 0x6d, 0x4c, 0x69, 0x73,
	0x74, 0x52, 0x65, 0x71, 0x12, 0x2d, 0x0a, 0x08, 0x6e, 0x75, 0x6d, 0x5f, 0x6c, 0x69, 0x73, 0x74,
	0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x12, 0x2e, 0x67, 0x72, 0x70, 0x63, 0x5f, 0x74, 0x65,
	0x73, 0x74, 0x2e, 0x4e, 0x75, 0x6d, 0x4c, 0x69, 0x73, 0x74, 0x52, 0x07, 0x6e, 0x75, 0x6d, 0x4c,
	0x69, 0x73, 0x74, 0x22, 0xc0, 0x01, 0x0a, 0x16, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x41, 0x6e, 0x64,
	0x53, 0x75, 0x6d, 0x52, 0x65, 0x73, 0x49, 0x6e, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x12, 0x4f,
	0x0a, 0x0a, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x64, 0x69, 0x63, 0x74, 0x18, 0x01, 0x20, 0x03,
	0x28, 0x0b, 0x32, 0x30, 0x2e, 0x67, 0x72, 0x70, 0x63, 0x5f, 0x74, 0x65, 0x73, 0x74, 0x2e, 0x43,
	0x6f, 0x75, 0x6e, 0x74, 0x41, 0x6e, 0x64, 0x53, 0x75, 0x6d, 0x52, 0x65, 0x73, 0x49, 0x6e, 0x73,
	0x74, 0x72, 0x75, 0x63, 0x74, 0x2e, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x44, 0x69, 0x63, 0x74, 0x45,
	0x6e, 0x74, 0x72, 0x79, 0x52, 0x09, 0x63, 0x6f, 0x75, 0x6e, 0x74, 0x44, 0x69, 0x63, 0x74, 0x12,
	0x17, 0x0a, 0x07, 0x73, 0x75, 0x6d, 0x5f, 0x72, 0x65, 0x73, 0x18, 0x02, 0x20, 0x01, 0x28, 0x02,
	0x52, 0x06, 0x73, 0x75, 0x6d, 0x52, 0x65, 0x73, 0x1a, 0x3c, 0x0a, 0x0e, 0x43, 0x6f, 0x75, 0x6e,
	0x74, 0x44, 0x69, 0x63, 0x74, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65,
	0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x14, 0x0a, 0x05,
	0x76, 0x61, 0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x05, 0x76, 0x61, 0x6c,
	0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x22, 0x62, 0x0a, 0x12, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x41,
	0x6e, 0x64, 0x53, 0x75, 0x6d, 0x4c, 0x69, 0x73, 0x74, 0x52, 0x73, 0x70, 0x12, 0x4c, 0x0a, 0x11,
	0x63, 0x6f, 0x75, 0x6e, 0x74, 0x5f, 0x61, 0x6e, 0x64, 0x5f, 0x73, 0x75, 0x6d, 0x5f, 0x72, 0x65,
	0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x21, 0x2e, 0x67, 0x72, 0x70, 0x63, 0x5f, 0x74,
	0x65, 0x73, 0x74, 0x2e, 0x43, 0x6f, 0x75, 0x6e, 0x74, 0x41, 0x6e, 0x64, 0x53, 0x75, 0x6d, 0x52,
	0x65, 0x73, 0x49, 0x6e, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x52, 0x0e, 0x63, 0x6f, 0x75, 0x6e,
	0x74, 0x41, 0x6e, 0x64, 0x53, 0x75, 0x6d, 0x52, 0x65, 0x73, 0x22, 0x16, 0x0a, 0x06, 0x4c, 0x65,
	0x74, 0x74, 0x65, 0x72, 0x12, 0x0c, 0x0a, 0x01, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x01, 0x73, 0x22, 0x45, 0x0a, 0x0f, 0x55, 0x70, 0x70, 0x65, 0x72, 0x4c, 0x65, 0x74, 0x74, 0x65,
	0x72, 0x73, 0x52, 0x65, 0x71, 0x12, 0x32, 0x0a, 0x0b, 0x6c, 0x65, 0x74, 0x74, 0x65, 0x72, 0x5f,
	0x6c, 0x69, 0x73, 0x74, 0x18, 0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x11, 0x2e, 0x67, 0x72, 0x70,
	0x63, 0x5f, 0x74, 0x65, 0x73, 0x74, 0x2e, 0x4c, 0x65, 0x74, 0x74, 0x65, 0x72, 0x52, 0x0a, 0x6c,
	0x65, 0x74, 0x74, 0x65, 0x72, 0x4c, 0x69, 0x73, 0x74, 0x22, 0x4c, 0x0a, 0x0f, 0x55, 0x70, 0x70,
	0x65, 0x72, 0x4c, 0x65, 0x74, 0x74, 0x65, 0x72, 0x73, 0x52, 0x73, 0x70, 0x12, 0x39, 0x0a, 0x0f,
	0x6c, 0x65, 0x74, 0x74, 0x65, 0x72, 0x5f, 0x72, 0x65, 0x73, 0x5f, 0x6c, 0x69, 0x73, 0x74, 0x18,
	0x01, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x11, 0x2e, 0x67, 0x72, 0x70, 0x63, 0x5f, 0x74, 0x65, 0x73,
	0x74, 0x2e, 0x4c, 0x65, 0x74, 0x74, 0x65, 0x72, 0x52, 0x0d, 0x6c, 0x65, 0x74, 0x74, 0x65, 0x72,
	0x52, 0x65, 0x73, 0x4c, 0x69, 0x73, 0x74, 0x22, 0x45, 0x0a, 0x0b, 0x4d, 0x65, 0x73, 0x73, 0x61,
	0x67, 0x65, 0x44, 0x61, 0x74, 0x61, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x05, 0x52, 0x02, 0x69, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x64, 0x61,
	0x74, 0x61, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0c, 0x52, 0x04, 0x64, 0x61, 0x74, 0x61, 0x32, 0x4a,
	0x0a, 0x09, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x54, 0x65, 0x73, 0x74, 0x12, 0x3d, 0x0a, 0x09, 0x64,
	0x6f, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x16, 0x2e, 0x67, 0x72, 0x70, 0x63, 0x5f,
	0x74, 0x65, 0x73, 0x74, 0x2e, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x44, 0x61, 0x74, 0x61,
	0x1a, 0x16, 0x2e, 0x67, 0x72, 0x70, 0x63, 0x5f, 0x74, 0x65, 0x73, 0x74, 0x2e, 0x4d, 0x65, 0x73,
	0x73, 0x61, 0x67, 0x65, 0x44, 0x61, 0x74, 0x61, 0x22, 0x00, 0x42, 0x0a, 0x5a, 0x08, 0x2e, 0x2f,
	0x3b, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_grpc_test_proto_rawDescOnce sync.Once
	file_grpc_test_proto_rawDescData = file_grpc_test_proto_rawDesc
)

func file_grpc_test_proto_rawDescGZIP() []byte {
	file_grpc_test_proto_rawDescOnce.Do(func() {
		file_grpc_test_proto_rawDescData = protoimpl.X.CompressGZIP(file_grpc_test_proto_rawDescData)
	})
	return file_grpc_test_proto_rawDescData
}

var file_grpc_test_proto_msgTypes = make([]protoimpl.MessageInfo, 13)
var file_grpc_test_proto_goTypes = []any{
	(*Vector)(nil),                 // 0: grpc_test.Vector
	(*VectorList)(nil),             // 1: grpc_test.VectorList
	(*GetMinDisReq)(nil),           // 2: grpc_test.GetMinDisReq
	(*GetMinDisRsp)(nil),           // 3: grpc_test.GetMinDisRsp
	(*NumList)(nil),                // 4: grpc_test.NumList
	(*CountAndSumListReq)(nil),     // 5: grpc_test.CountAndSumListReq
	(*CountAndSumResInstruct)(nil), // 6: grpc_test.CountAndSumResInstruct
	(*CountAndSumListRsp)(nil),     // 7: grpc_test.CountAndSumListRsp
	(*Letter)(nil),                 // 8: grpc_test.Letter
	(*UpperLettersReq)(nil),        // 9: grpc_test.UpperLettersReq
	(*UpperLettersRsp)(nil),        // 10: grpc_test.UpperLettersRsp
	(*MessageData)(nil),            // 11: grpc_test.MessageData
	nil,                            // 12: grpc_test.CountAndSumResInstruct.CountDictEntry
}
var file_grpc_test_proto_depIdxs = []int32{
	0,  // 0: grpc_test.VectorList.point_list:type_name -> grpc_test.Vector
	1,  // 1: grpc_test.GetMinDisReq.point_lists:type_name -> grpc_test.VectorList
	4,  // 2: grpc_test.CountAndSumListReq.num_list:type_name -> grpc_test.NumList
	12, // 3: grpc_test.CountAndSumResInstruct.count_dict:type_name -> grpc_test.CountAndSumResInstruct.CountDictEntry
	6,  // 4: grpc_test.CountAndSumListRsp.count_and_sum_res:type_name -> grpc_test.CountAndSumResInstruct
	8,  // 5: grpc_test.UpperLettersReq.letter_list:type_name -> grpc_test.Letter
	8,  // 6: grpc_test.UpperLettersRsp.letter_res_list:type_name -> grpc_test.Letter
	11, // 7: grpc_test.ProtoTest.doRequest:input_type -> grpc_test.MessageData
	11, // 8: grpc_test.ProtoTest.doRequest:output_type -> grpc_test.MessageData
	8,  // [8:9] is the sub-list for method output_type
	7,  // [7:8] is the sub-list for method input_type
	7,  // [7:7] is the sub-list for extension type_name
	7,  // [7:7] is the sub-list for extension extendee
	0,  // [0:7] is the sub-list for field type_name
}

func init() { file_grpc_test_proto_init() }
func file_grpc_test_proto_init() {
	if File_grpc_test_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_grpc_test_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   13,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_grpc_test_proto_goTypes,
		DependencyIndexes: file_grpc_test_proto_depIdxs,
		MessageInfos:      file_grpc_test_proto_msgTypes,
	}.Build()
	File_grpc_test_proto = out.File
	file_grpc_test_proto_rawDesc = nil
	file_grpc_test_proto_goTypes = nil
	file_grpc_test_proto_depIdxs = nil
}
