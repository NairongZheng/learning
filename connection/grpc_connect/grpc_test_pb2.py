# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fgrpc_test.proto\x12\tgrpc_test\")\n\x06Vector\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"5\n\x0cGetMinDisReq\x12%\n\npoint_list\x18\x01 \x03(\x0b\x32\x11.grpc_test.Vector\"\x1f\n\x0cGetMinDisRsp\x12\x0f\n\x07min_dis\x18\x01 \x01(\x02\x32S\n\x10GetMimDisService\x12?\n\tGetMinDis\x12\x17.grpc_test.GetMinDisReq\x1a\x17.grpc_test.GetMinDisRsp\"\x00\x62\x06proto3')



_VECTOR = DESCRIPTOR.message_types_by_name['Vector']
_GETMINDISREQ = DESCRIPTOR.message_types_by_name['GetMinDisReq']
_GETMINDISRSP = DESCRIPTOR.message_types_by_name['GetMinDisRsp']
Vector = _reflection.GeneratedProtocolMessageType('Vector', (_message.Message,), {
  'DESCRIPTOR' : _VECTOR,
  '__module__' : 'grpc_test_pb2'
  # @@protoc_insertion_point(class_scope:grpc_test.Vector)
  })
_sym_db.RegisterMessage(Vector)

GetMinDisReq = _reflection.GeneratedProtocolMessageType('GetMinDisReq', (_message.Message,), {
  'DESCRIPTOR' : _GETMINDISREQ,
  '__module__' : 'grpc_test_pb2'
  # @@protoc_insertion_point(class_scope:grpc_test.GetMinDisReq)
  })
_sym_db.RegisterMessage(GetMinDisReq)

GetMinDisRsp = _reflection.GeneratedProtocolMessageType('GetMinDisRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETMINDISRSP,
  '__module__' : 'grpc_test_pb2'
  # @@protoc_insertion_point(class_scope:grpc_test.GetMinDisRsp)
  })
_sym_db.RegisterMessage(GetMinDisRsp)

_GETMIMDISSERVICE = DESCRIPTOR.services_by_name['GetMimDisService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VECTOR._serialized_start=30
  _VECTOR._serialized_end=71
  _GETMINDISREQ._serialized_start=73
  _GETMINDISREQ._serialized_end=126
  _GETMINDISRSP._serialized_start=128
  _GETMINDISRSP._serialized_end=159
  _GETMIMDISSERVICE._serialized_start=161
  _GETMIMDISSERVICE._serialized_end=244
# @@protoc_insertion_point(module_scope)
