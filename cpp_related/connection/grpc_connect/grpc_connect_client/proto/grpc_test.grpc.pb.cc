// Generated by the gRPC C++ plugin.
// If you make any local change, they will be lost.
// source: grpc_test.proto

#include "grpc_test.pb.h"
#include "grpc_test.grpc.pb.h"

#include <functional>
#include <grpcpp/impl/codegen/async_stream.h>
#include <grpcpp/impl/codegen/async_unary_call.h>
#include <grpcpp/impl/codegen/channel_interface.h>
#include <grpcpp/impl/codegen/client_unary_call.h>
#include <grpcpp/impl/codegen/client_callback.h>
#include <grpcpp/impl/codegen/message_allocator.h>
#include <grpcpp/impl/codegen/method_handler.h>
#include <grpcpp/impl/codegen/rpc_service_method.h>
#include <grpcpp/impl/codegen/server_callback.h>
#include <grpcpp/impl/codegen/server_callback_handlers.h>
#include <grpcpp/impl/codegen/server_context.h>
#include <grpcpp/impl/codegen/service_type.h>
#include <grpcpp/impl/codegen/sync_stream.h>
namespace grpc_test {

static const char* GetMimDisService_method_names[] = {
  "/grpc_test.GetMimDisService/GetMinDis",
};

std::unique_ptr< GetMimDisService::Stub> GetMimDisService::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  (void)options;
  std::unique_ptr< GetMimDisService::Stub> stub(new GetMimDisService::Stub(channel, options));
  return stub;
}

GetMimDisService::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options)
  : channel_(channel), rpcmethod_GetMinDis_(GetMimDisService_method_names[0], options.suffix_for_stats(),::grpc::internal::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::Status GetMimDisService::Stub::GetMinDis(::grpc::ClientContext* context, const ::grpc_test::GetMinDisReq& request, ::grpc_test::GetMinDisRsp* response) {
  return ::grpc::internal::BlockingUnaryCall< ::grpc_test::GetMinDisReq, ::grpc_test::GetMinDisRsp, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), rpcmethod_GetMinDis_, context, request, response);
}

void GetMimDisService::Stub::async::GetMinDis(::grpc::ClientContext* context, const ::grpc_test::GetMinDisReq* request, ::grpc_test::GetMinDisRsp* response, std::function<void(::grpc::Status)> f) {
  ::grpc::internal::CallbackUnaryCall< ::grpc_test::GetMinDisReq, ::grpc_test::GetMinDisRsp, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_GetMinDis_, context, request, response, std::move(f));
}

void GetMimDisService::Stub::async::GetMinDis(::grpc::ClientContext* context, const ::grpc_test::GetMinDisReq* request, ::grpc_test::GetMinDisRsp* response, ::grpc::ClientUnaryReactor* reactor) {
  ::grpc::internal::ClientCallbackUnaryFactory::Create< ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(stub_->channel_.get(), stub_->rpcmethod_GetMinDis_, context, request, response, reactor);
}

::grpc::ClientAsyncResponseReader< ::grpc_test::GetMinDisRsp>* GetMimDisService::Stub::PrepareAsyncGetMinDisRaw(::grpc::ClientContext* context, const ::grpc_test::GetMinDisReq& request, ::grpc::CompletionQueue* cq) {
  return ::grpc::internal::ClientAsyncResponseReaderHelper::Create< ::grpc_test::GetMinDisRsp, ::grpc_test::GetMinDisReq, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(channel_.get(), cq, rpcmethod_GetMinDis_, context, request);
}

::grpc::ClientAsyncResponseReader< ::grpc_test::GetMinDisRsp>* GetMimDisService::Stub::AsyncGetMinDisRaw(::grpc::ClientContext* context, const ::grpc_test::GetMinDisReq& request, ::grpc::CompletionQueue* cq) {
  auto* result =
    this->PrepareAsyncGetMinDisRaw(context, request, cq);
  result->StartCall();
  return result;
}

GetMimDisService::Service::Service() {
  AddMethod(new ::grpc::internal::RpcServiceMethod(
      GetMimDisService_method_names[0],
      ::grpc::internal::RpcMethod::NORMAL_RPC,
      new ::grpc::internal::RpcMethodHandler< GetMimDisService::Service, ::grpc_test::GetMinDisReq, ::grpc_test::GetMinDisRsp, ::grpc::protobuf::MessageLite, ::grpc::protobuf::MessageLite>(
          [](GetMimDisService::Service* service,
             ::grpc::ServerContext* ctx,
             const ::grpc_test::GetMinDisReq* req,
             ::grpc_test::GetMinDisRsp* resp) {
               return service->GetMinDis(ctx, req, resp);
             }, this)));
}

GetMimDisService::Service::~Service() {
}

::grpc::Status GetMimDisService::Service::GetMinDis(::grpc::ServerContext* context, const ::grpc_test::GetMinDisReq* request, ::grpc_test::GetMinDisRsp* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace grpc_test
