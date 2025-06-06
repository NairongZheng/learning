// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.36.6
// 	protoc        v5.26.0
// source: simple_go.proto

package proto

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
	unsafe "unsafe"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Point struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	X             int32                  `protobuf:"varint,1,opt,name=x,proto3" json:"x,omitempty"`
	Y             int32                  `protobuf:"varint,2,opt,name=y,proto3" json:"y,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *Point) Reset() {
	*x = Point{}
	mi := &file_simple_go_proto_msgTypes[0]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *Point) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*Point) ProtoMessage() {}

func (x *Point) ProtoReflect() protoreflect.Message {
	mi := &file_simple_go_proto_msgTypes[0]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use Point.ProtoReflect.Descriptor instead.
func (*Point) Descriptor() ([]byte, []int) {
	return file_simple_go_proto_rawDescGZIP(), []int{0}
}

func (x *Point) GetX() int32 {
	if x != nil {
		return x.X
	}
	return 0
}

func (x *Point) GetY() int32 {
	if x != nil {
		return x.Y
	}
	return 0
}

type SimpleGoRequest struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Id            int32                  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	Content       string                 `protobuf:"bytes,2,opt,name=content,proto3" json:"content,omitempty"`
	Points        []*Point               `protobuf:"bytes,3,rep,name=points,proto3" json:"points,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SimpleGoRequest) Reset() {
	*x = SimpleGoRequest{}
	mi := &file_simple_go_proto_msgTypes[1]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SimpleGoRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SimpleGoRequest) ProtoMessage() {}

func (x *SimpleGoRequest) ProtoReflect() protoreflect.Message {
	mi := &file_simple_go_proto_msgTypes[1]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SimpleGoRequest.ProtoReflect.Descriptor instead.
func (*SimpleGoRequest) Descriptor() ([]byte, []int) {
	return file_simple_go_proto_rawDescGZIP(), []int{1}
}

func (x *SimpleGoRequest) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *SimpleGoRequest) GetContent() string {
	if x != nil {
		return x.Content
	}
	return ""
}

func (x *SimpleGoRequest) GetPoints() []*Point {
	if x != nil {
		return x.Points
	}
	return nil
}

type SimpleGoResponse struct {
	state         protoimpl.MessageState `protogen:"open.v1"`
	Id            int32                  `protobuf:"varint,1,opt,name=id,proto3" json:"id,omitempty"`
	Content       string                 `protobuf:"bytes,2,opt,name=content,proto3" json:"content,omitempty"`
	Addresult     []int32                `protobuf:"varint,3,rep,packed,name=addresult,proto3" json:"addresult,omitempty"`
	unknownFields protoimpl.UnknownFields
	sizeCache     protoimpl.SizeCache
}

func (x *SimpleGoResponse) Reset() {
	*x = SimpleGoResponse{}
	mi := &file_simple_go_proto_msgTypes[2]
	ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
	ms.StoreMessageInfo(mi)
}

func (x *SimpleGoResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SimpleGoResponse) ProtoMessage() {}

func (x *SimpleGoResponse) ProtoReflect() protoreflect.Message {
	mi := &file_simple_go_proto_msgTypes[2]
	if x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SimpleGoResponse.ProtoReflect.Descriptor instead.
func (*SimpleGoResponse) Descriptor() ([]byte, []int) {
	return file_simple_go_proto_rawDescGZIP(), []int{2}
}

func (x *SimpleGoResponse) GetId() int32 {
	if x != nil {
		return x.Id
	}
	return 0
}

func (x *SimpleGoResponse) GetContent() string {
	if x != nil {
		return x.Content
	}
	return ""
}

func (x *SimpleGoResponse) GetAddresult() []int32 {
	if x != nil {
		return x.Addresult
	}
	return nil
}

var File_simple_go_proto protoreflect.FileDescriptor

const file_simple_go_proto_rawDesc = "" +
	"\n" +
	"\x0fsimple_go.proto\x12\rsimpleGoProto\"#\n" +
	"\x05Point\x12\f\n" +
	"\x01x\x18\x01 \x01(\x05R\x01x\x12\f\n" +
	"\x01y\x18\x02 \x01(\x05R\x01y\"i\n" +
	"\x0fSimpleGoRequest\x12\x0e\n" +
	"\x02id\x18\x01 \x01(\x05R\x02id\x12\x18\n" +
	"\acontent\x18\x02 \x01(\tR\acontent\x12,\n" +
	"\x06points\x18\x03 \x03(\v2\x14.simpleGoProto.PointR\x06points\"Z\n" +
	"\x10SimpleGoResponse\x12\x0e\n" +
	"\x02id\x18\x01 \x01(\x05R\x02id\x12\x18\n" +
	"\acontent\x18\x02 \x01(\tR\acontent\x12\x1c\n" +
	"\taddresult\x18\x03 \x03(\x05R\taddresultB)Z'github.com/nairongzheng/simple_go/protob\x06proto3"

var (
	file_simple_go_proto_rawDescOnce sync.Once
	file_simple_go_proto_rawDescData []byte
)

func file_simple_go_proto_rawDescGZIP() []byte {
	file_simple_go_proto_rawDescOnce.Do(func() {
		file_simple_go_proto_rawDescData = protoimpl.X.CompressGZIP(unsafe.Slice(unsafe.StringData(file_simple_go_proto_rawDesc), len(file_simple_go_proto_rawDesc)))
	})
	return file_simple_go_proto_rawDescData
}

var file_simple_go_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_simple_go_proto_goTypes = []any{
	(*Point)(nil),            // 0: simpleGoProto.Point
	(*SimpleGoRequest)(nil),  // 1: simpleGoProto.SimpleGoRequest
	(*SimpleGoResponse)(nil), // 2: simpleGoProto.SimpleGoResponse
}
var file_simple_go_proto_depIdxs = []int32{
	0, // 0: simpleGoProto.SimpleGoRequest.points:type_name -> simpleGoProto.Point
	1, // [1:1] is the sub-list for method output_type
	1, // [1:1] is the sub-list for method input_type
	1, // [1:1] is the sub-list for extension type_name
	1, // [1:1] is the sub-list for extension extendee
	0, // [0:1] is the sub-list for field type_name
}

func init() { file_simple_go_proto_init() }
func file_simple_go_proto_init() {
	if File_simple_go_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: unsafe.Slice(unsafe.StringData(file_simple_go_proto_rawDesc), len(file_simple_go_proto_rawDesc)),
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_simple_go_proto_goTypes,
		DependencyIndexes: file_simple_go_proto_depIdxs,
		MessageInfos:      file_simple_go_proto_msgTypes,
	}.Build()
	File_simple_go_proto = out.File
	file_simple_go_proto_goTypes = nil
	file_simple_go_proto_depIdxs = nil
}
