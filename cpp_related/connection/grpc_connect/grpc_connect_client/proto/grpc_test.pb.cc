// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: grpc_test.proto

#include "grpc_test.pb.h"

#include <algorithm>

#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/wire_format_lite.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>

PROTOBUF_PRAGMA_INIT_SEG
namespace grpc_test {
constexpr Vector::Vector(
  ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized)
  : x_(0)
  , y_(0)
  , z_(0){}
struct VectorDefaultTypeInternal {
  constexpr VectorDefaultTypeInternal()
    : _instance(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized{}) {}
  ~VectorDefaultTypeInternal() {}
  union {
    Vector _instance;
  };
};
PROTOBUF_ATTRIBUTE_NO_DESTROY PROTOBUF_CONSTINIT VectorDefaultTypeInternal _Vector_default_instance_;
constexpr GetMinDisReq::GetMinDisReq(
  ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized)
  : point_list_(){}
struct GetMinDisReqDefaultTypeInternal {
  constexpr GetMinDisReqDefaultTypeInternal()
    : _instance(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized{}) {}
  ~GetMinDisReqDefaultTypeInternal() {}
  union {
    GetMinDisReq _instance;
  };
};
PROTOBUF_ATTRIBUTE_NO_DESTROY PROTOBUF_CONSTINIT GetMinDisReqDefaultTypeInternal _GetMinDisReq_default_instance_;
constexpr GetMinDisRsp::GetMinDisRsp(
  ::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized)
  : min_dis_(0){}
struct GetMinDisRspDefaultTypeInternal {
  constexpr GetMinDisRspDefaultTypeInternal()
    : _instance(::PROTOBUF_NAMESPACE_ID::internal::ConstantInitialized{}) {}
  ~GetMinDisRspDefaultTypeInternal() {}
  union {
    GetMinDisRsp _instance;
  };
};
PROTOBUF_ATTRIBUTE_NO_DESTROY PROTOBUF_CONSTINIT GetMinDisRspDefaultTypeInternal _GetMinDisRsp_default_instance_;
}  // namespace grpc_test
static ::PROTOBUF_NAMESPACE_ID::Metadata file_level_metadata_grpc_5ftest_2eproto[3];
static constexpr ::PROTOBUF_NAMESPACE_ID::EnumDescriptor const** file_level_enum_descriptors_grpc_5ftest_2eproto = nullptr;
static constexpr ::PROTOBUF_NAMESPACE_ID::ServiceDescriptor const** file_level_service_descriptors_grpc_5ftest_2eproto = nullptr;

const uint32_t TableStruct_grpc_5ftest_2eproto::offsets[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::grpc_test::Vector, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  ~0u,  // no _inlined_string_donated_
  PROTOBUF_FIELD_OFFSET(::grpc_test::Vector, x_),
  PROTOBUF_FIELD_OFFSET(::grpc_test::Vector, y_),
  PROTOBUF_FIELD_OFFSET(::grpc_test::Vector, z_),
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::grpc_test::GetMinDisReq, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  ~0u,  // no _inlined_string_donated_
  PROTOBUF_FIELD_OFFSET(::grpc_test::GetMinDisReq, point_list_),
  ~0u,  // no _has_bits_
  PROTOBUF_FIELD_OFFSET(::grpc_test::GetMinDisRsp, _internal_metadata_),
  ~0u,  // no _extensions_
  ~0u,  // no _oneof_case_
  ~0u,  // no _weak_field_map_
  ~0u,  // no _inlined_string_donated_
  PROTOBUF_FIELD_OFFSET(::grpc_test::GetMinDisRsp, min_dis_),
};
static const ::PROTOBUF_NAMESPACE_ID::internal::MigrationSchema schemas[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) = {
  { 0, -1, -1, sizeof(::grpc_test::Vector)},
  { 9, -1, -1, sizeof(::grpc_test::GetMinDisReq)},
  { 16, -1, -1, sizeof(::grpc_test::GetMinDisRsp)},
};

static ::PROTOBUF_NAMESPACE_ID::Message const * const file_default_instances[] = {
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::grpc_test::_Vector_default_instance_),
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::grpc_test::_GetMinDisReq_default_instance_),
  reinterpret_cast<const ::PROTOBUF_NAMESPACE_ID::Message*>(&::grpc_test::_GetMinDisRsp_default_instance_),
};

const char descriptor_table_protodef_grpc_5ftest_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n\017grpc_test.proto\022\tgrpc_test\")\n\006Vector\022\t"
  "\n\001x\030\001 \001(\002\022\t\n\001y\030\002 \001(\002\022\t\n\001z\030\003 \001(\002\"5\n\014GetMi"
  "nDisReq\022%\n\npoint_list\030\001 \003(\0132\021.grpc_test."
  "Vector\"\037\n\014GetMinDisRsp\022\017\n\007min_dis\030\001 \001(\0022"
  "S\n\020GetMimDisService\022\?\n\tGetMinDis\022\027.grpc_"
  "test.GetMinDisReq\032\027.grpc_test.GetMinDisR"
  "sp\"\000b\006proto3"
  ;
static ::PROTOBUF_NAMESPACE_ID::internal::once_flag descriptor_table_grpc_5ftest_2eproto_once;
const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_grpc_5ftest_2eproto = {
  false, false, 252, descriptor_table_protodef_grpc_5ftest_2eproto, "grpc_test.proto", 
  &descriptor_table_grpc_5ftest_2eproto_once, nullptr, 0, 3,
  schemas, file_default_instances, TableStruct_grpc_5ftest_2eproto::offsets,
  file_level_metadata_grpc_5ftest_2eproto, file_level_enum_descriptors_grpc_5ftest_2eproto, file_level_service_descriptors_grpc_5ftest_2eproto,
};
PROTOBUF_ATTRIBUTE_WEAK const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable* descriptor_table_grpc_5ftest_2eproto_getter() {
  return &descriptor_table_grpc_5ftest_2eproto;
}

// Force running AddDescriptors() at dynamic initialization time.
PROTOBUF_ATTRIBUTE_INIT_PRIORITY static ::PROTOBUF_NAMESPACE_ID::internal::AddDescriptorsRunner dynamic_init_dummy_grpc_5ftest_2eproto(&descriptor_table_grpc_5ftest_2eproto);
namespace grpc_test {

// ===================================================================

class Vector::_Internal {
 public:
};

Vector::Vector(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                         bool is_message_owned)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena, is_message_owned) {
  SharedCtor();
  if (!is_message_owned) {
    RegisterArenaDtor(arena);
  }
  // @@protoc_insertion_point(arena_constructor:grpc_test.Vector)
}
Vector::Vector(const Vector& from)
  : ::PROTOBUF_NAMESPACE_ID::Message() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  ::memcpy(&x_, &from.x_,
    static_cast<size_t>(reinterpret_cast<char*>(&z_) -
    reinterpret_cast<char*>(&x_)) + sizeof(z_));
  // @@protoc_insertion_point(copy_constructor:grpc_test.Vector)
}

inline void Vector::SharedCtor() {
::memset(reinterpret_cast<char*>(this) + static_cast<size_t>(
    reinterpret_cast<char*>(&x_) - reinterpret_cast<char*>(this)),
    0, static_cast<size_t>(reinterpret_cast<char*>(&z_) -
    reinterpret_cast<char*>(&x_)) + sizeof(z_));
}

Vector::~Vector() {
  // @@protoc_insertion_point(destructor:grpc_test.Vector)
  if (GetArenaForAllocation() != nullptr) return;
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

inline void Vector::SharedDtor() {
  GOOGLE_DCHECK(GetArenaForAllocation() == nullptr);
}

void Vector::ArenaDtor(void* object) {
  Vector* _this = reinterpret_cast< Vector* >(object);
  (void)_this;
}
void Vector::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void Vector::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}

void Vector::Clear() {
// @@protoc_insertion_point(message_clear_start:grpc_test.Vector)
  uint32_t cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  ::memset(&x_, 0, static_cast<size_t>(
      reinterpret_cast<char*>(&z_) -
      reinterpret_cast<char*>(&x_)) + sizeof(z_));
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* Vector::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    uint32_t tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    switch (tag >> 3) {
      // float x = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<uint8_t>(tag) == 13)) {
          x_ = ::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<float>(ptr);
          ptr += sizeof(float);
        } else
          goto handle_unusual;
        continue;
      // float y = 2;
      case 2:
        if (PROTOBUF_PREDICT_TRUE(static_cast<uint8_t>(tag) == 21)) {
          y_ = ::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<float>(ptr);
          ptr += sizeof(float);
        } else
          goto handle_unusual;
        continue;
      // float z = 3;
      case 3:
        if (PROTOBUF_PREDICT_TRUE(static_cast<uint8_t>(tag) == 29)) {
          z_ = ::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<float>(ptr);
          ptr += sizeof(float);
        } else
          goto handle_unusual;
        continue;
      default:
        goto handle_unusual;
    }  // switch
  handle_unusual:
    if ((tag == 0) || ((tag & 7) == 4)) {
      CHK_(ptr);
      ctx->SetLastTag(tag);
      goto message_done;
    }
    ptr = UnknownFieldParse(
        tag,
        _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
        ptr, ctx);
    CHK_(ptr != nullptr);
  }  // while
message_done:
  return ptr;
failure:
  ptr = nullptr;
  goto message_done;
#undef CHK_
}

uint8_t* Vector::_InternalSerialize(
    uint8_t* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:grpc_test.Vector)
  uint32_t cached_has_bits = 0;
  (void) cached_has_bits;

  // float x = 1;
  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_x = this->_internal_x();
  uint32_t raw_x;
  memcpy(&raw_x, &tmp_x, sizeof(tmp_x));
  if (raw_x != 0) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteFloatToArray(1, this->_internal_x(), target);
  }

  // float y = 2;
  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_y = this->_internal_y();
  uint32_t raw_y;
  memcpy(&raw_y, &tmp_y, sizeof(tmp_y));
  if (raw_y != 0) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteFloatToArray(2, this->_internal_y(), target);
  }

  // float z = 3;
  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_z = this->_internal_z();
  uint32_t raw_z;
  memcpy(&raw_z, &tmp_z, sizeof(tmp_z));
  if (raw_z != 0) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteFloatToArray(3, this->_internal_z(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:grpc_test.Vector)
  return target;
}

size_t Vector::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:grpc_test.Vector)
  size_t total_size = 0;

  uint32_t cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // float x = 1;
  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_x = this->_internal_x();
  uint32_t raw_x;
  memcpy(&raw_x, &tmp_x, sizeof(tmp_x));
  if (raw_x != 0) {
    total_size += 1 + 4;
  }

  // float y = 2;
  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_y = this->_internal_y();
  uint32_t raw_y;
  memcpy(&raw_y, &tmp_y, sizeof(tmp_y));
  if (raw_y != 0) {
    total_size += 1 + 4;
  }

  // float z = 3;
  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_z = this->_internal_z();
  uint32_t raw_z;
  memcpy(&raw_z, &tmp_z, sizeof(tmp_z));
  if (raw_z != 0) {
    total_size += 1 + 4;
  }

  return MaybeComputeUnknownFieldsSize(total_size, &_cached_size_);
}

const ::PROTOBUF_NAMESPACE_ID::Message::ClassData Vector::_class_data_ = {
    ::PROTOBUF_NAMESPACE_ID::Message::CopyWithSizeCheck,
    Vector::MergeImpl
};
const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*Vector::GetClassData() const { return &_class_data_; }

void Vector::MergeImpl(::PROTOBUF_NAMESPACE_ID::Message* to,
                      const ::PROTOBUF_NAMESPACE_ID::Message& from) {
  static_cast<Vector *>(to)->MergeFrom(
      static_cast<const Vector &>(from));
}


void Vector::MergeFrom(const Vector& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:grpc_test.Vector)
  GOOGLE_DCHECK_NE(&from, this);
  uint32_t cached_has_bits = 0;
  (void) cached_has_bits;

  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_x = from._internal_x();
  uint32_t raw_x;
  memcpy(&raw_x, &tmp_x, sizeof(tmp_x));
  if (raw_x != 0) {
    _internal_set_x(from._internal_x());
  }
  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_y = from._internal_y();
  uint32_t raw_y;
  memcpy(&raw_y, &tmp_y, sizeof(tmp_y));
  if (raw_y != 0) {
    _internal_set_y(from._internal_y());
  }
  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_z = from._internal_z();
  uint32_t raw_z;
  memcpy(&raw_z, &tmp_z, sizeof(tmp_z));
  if (raw_z != 0) {
    _internal_set_z(from._internal_z());
  }
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
}

void Vector::CopyFrom(const Vector& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:grpc_test.Vector)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool Vector::IsInitialized() const {
  return true;
}

void Vector::InternalSwap(Vector* other) {
  using std::swap;
  _internal_metadata_.InternalSwap(&other->_internal_metadata_);
  ::PROTOBUF_NAMESPACE_ID::internal::memswap<
      PROTOBUF_FIELD_OFFSET(Vector, z_)
      + sizeof(Vector::z_)
      - PROTOBUF_FIELD_OFFSET(Vector, x_)>(
          reinterpret_cast<char*>(&x_),
          reinterpret_cast<char*>(&other->x_));
}

::PROTOBUF_NAMESPACE_ID::Metadata Vector::GetMetadata() const {
  return ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(
      &descriptor_table_grpc_5ftest_2eproto_getter, &descriptor_table_grpc_5ftest_2eproto_once,
      file_level_metadata_grpc_5ftest_2eproto[0]);
}

// ===================================================================

class GetMinDisReq::_Internal {
 public:
};

GetMinDisReq::GetMinDisReq(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                         bool is_message_owned)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena, is_message_owned),
  point_list_(arena) {
  SharedCtor();
  if (!is_message_owned) {
    RegisterArenaDtor(arena);
  }
  // @@protoc_insertion_point(arena_constructor:grpc_test.GetMinDisReq)
}
GetMinDisReq::GetMinDisReq(const GetMinDisReq& from)
  : ::PROTOBUF_NAMESPACE_ID::Message(),
      point_list_(from.point_list_) {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  // @@protoc_insertion_point(copy_constructor:grpc_test.GetMinDisReq)
}

inline void GetMinDisReq::SharedCtor() {
}

GetMinDisReq::~GetMinDisReq() {
  // @@protoc_insertion_point(destructor:grpc_test.GetMinDisReq)
  if (GetArenaForAllocation() != nullptr) return;
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

inline void GetMinDisReq::SharedDtor() {
  GOOGLE_DCHECK(GetArenaForAllocation() == nullptr);
}

void GetMinDisReq::ArenaDtor(void* object) {
  GetMinDisReq* _this = reinterpret_cast< GetMinDisReq* >(object);
  (void)_this;
}
void GetMinDisReq::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void GetMinDisReq::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}

void GetMinDisReq::Clear() {
// @@protoc_insertion_point(message_clear_start:grpc_test.GetMinDisReq)
  uint32_t cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  point_list_.Clear();
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* GetMinDisReq::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    uint32_t tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    switch (tag >> 3) {
      // repeated .grpc_test.Vector point_list = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<uint8_t>(tag) == 10)) {
          ptr -= 1;
          do {
            ptr += 1;
            ptr = ctx->ParseMessage(_internal_add_point_list(), ptr);
            CHK_(ptr);
            if (!ctx->DataAvailable(ptr)) break;
          } while (::PROTOBUF_NAMESPACE_ID::internal::ExpectTag<10>(ptr));
        } else
          goto handle_unusual;
        continue;
      default:
        goto handle_unusual;
    }  // switch
  handle_unusual:
    if ((tag == 0) || ((tag & 7) == 4)) {
      CHK_(ptr);
      ctx->SetLastTag(tag);
      goto message_done;
    }
    ptr = UnknownFieldParse(
        tag,
        _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
        ptr, ctx);
    CHK_(ptr != nullptr);
  }  // while
message_done:
  return ptr;
failure:
  ptr = nullptr;
  goto message_done;
#undef CHK_
}

uint8_t* GetMinDisReq::_InternalSerialize(
    uint8_t* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:grpc_test.GetMinDisReq)
  uint32_t cached_has_bits = 0;
  (void) cached_has_bits;

  // repeated .grpc_test.Vector point_list = 1;
  for (unsigned int i = 0,
      n = static_cast<unsigned int>(this->_internal_point_list_size()); i < n; i++) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::
      InternalWriteMessage(1, this->_internal_point_list(i), target, stream);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:grpc_test.GetMinDisReq)
  return target;
}

size_t GetMinDisReq::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:grpc_test.GetMinDisReq)
  size_t total_size = 0;

  uint32_t cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // repeated .grpc_test.Vector point_list = 1;
  total_size += 1UL * this->_internal_point_list_size();
  for (const auto& msg : this->point_list_) {
    total_size +=
      ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::MessageSize(msg);
  }

  return MaybeComputeUnknownFieldsSize(total_size, &_cached_size_);
}

const ::PROTOBUF_NAMESPACE_ID::Message::ClassData GetMinDisReq::_class_data_ = {
    ::PROTOBUF_NAMESPACE_ID::Message::CopyWithSizeCheck,
    GetMinDisReq::MergeImpl
};
const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*GetMinDisReq::GetClassData() const { return &_class_data_; }

void GetMinDisReq::MergeImpl(::PROTOBUF_NAMESPACE_ID::Message* to,
                      const ::PROTOBUF_NAMESPACE_ID::Message& from) {
  static_cast<GetMinDisReq *>(to)->MergeFrom(
      static_cast<const GetMinDisReq &>(from));
}


void GetMinDisReq::MergeFrom(const GetMinDisReq& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:grpc_test.GetMinDisReq)
  GOOGLE_DCHECK_NE(&from, this);
  uint32_t cached_has_bits = 0;
  (void) cached_has_bits;

  point_list_.MergeFrom(from.point_list_);
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
}

void GetMinDisReq::CopyFrom(const GetMinDisReq& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:grpc_test.GetMinDisReq)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool GetMinDisReq::IsInitialized() const {
  return true;
}

void GetMinDisReq::InternalSwap(GetMinDisReq* other) {
  using std::swap;
  _internal_metadata_.InternalSwap(&other->_internal_metadata_);
  point_list_.InternalSwap(&other->point_list_);
}

::PROTOBUF_NAMESPACE_ID::Metadata GetMinDisReq::GetMetadata() const {
  return ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(
      &descriptor_table_grpc_5ftest_2eproto_getter, &descriptor_table_grpc_5ftest_2eproto_once,
      file_level_metadata_grpc_5ftest_2eproto[1]);
}

// ===================================================================

class GetMinDisRsp::_Internal {
 public:
};

GetMinDisRsp::GetMinDisRsp(::PROTOBUF_NAMESPACE_ID::Arena* arena,
                         bool is_message_owned)
  : ::PROTOBUF_NAMESPACE_ID::Message(arena, is_message_owned) {
  SharedCtor();
  if (!is_message_owned) {
    RegisterArenaDtor(arena);
  }
  // @@protoc_insertion_point(arena_constructor:grpc_test.GetMinDisRsp)
}
GetMinDisRsp::GetMinDisRsp(const GetMinDisRsp& from)
  : ::PROTOBUF_NAMESPACE_ID::Message() {
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
  min_dis_ = from.min_dis_;
  // @@protoc_insertion_point(copy_constructor:grpc_test.GetMinDisRsp)
}

inline void GetMinDisRsp::SharedCtor() {
min_dis_ = 0;
}

GetMinDisRsp::~GetMinDisRsp() {
  // @@protoc_insertion_point(destructor:grpc_test.GetMinDisRsp)
  if (GetArenaForAllocation() != nullptr) return;
  SharedDtor();
  _internal_metadata_.Delete<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

inline void GetMinDisRsp::SharedDtor() {
  GOOGLE_DCHECK(GetArenaForAllocation() == nullptr);
}

void GetMinDisRsp::ArenaDtor(void* object) {
  GetMinDisRsp* _this = reinterpret_cast< GetMinDisRsp* >(object);
  (void)_this;
}
void GetMinDisRsp::RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena*) {
}
void GetMinDisRsp::SetCachedSize(int size) const {
  _cached_size_.Set(size);
}

void GetMinDisRsp::Clear() {
// @@protoc_insertion_point(message_clear_start:grpc_test.GetMinDisRsp)
  uint32_t cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  min_dis_ = 0;
  _internal_metadata_.Clear<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>();
}

const char* GetMinDisRsp::_InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) {
#define CHK_(x) if (PROTOBUF_PREDICT_FALSE(!(x))) goto failure
  while (!ctx->Done(&ptr)) {
    uint32_t tag;
    ptr = ::PROTOBUF_NAMESPACE_ID::internal::ReadTag(ptr, &tag);
    switch (tag >> 3) {
      // float min_dis = 1;
      case 1:
        if (PROTOBUF_PREDICT_TRUE(static_cast<uint8_t>(tag) == 13)) {
          min_dis_ = ::PROTOBUF_NAMESPACE_ID::internal::UnalignedLoad<float>(ptr);
          ptr += sizeof(float);
        } else
          goto handle_unusual;
        continue;
      default:
        goto handle_unusual;
    }  // switch
  handle_unusual:
    if ((tag == 0) || ((tag & 7) == 4)) {
      CHK_(ptr);
      ctx->SetLastTag(tag);
      goto message_done;
    }
    ptr = UnknownFieldParse(
        tag,
        _internal_metadata_.mutable_unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(),
        ptr, ctx);
    CHK_(ptr != nullptr);
  }  // while
message_done:
  return ptr;
failure:
  ptr = nullptr;
  goto message_done;
#undef CHK_
}

uint8_t* GetMinDisRsp::_InternalSerialize(
    uint8_t* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const {
  // @@protoc_insertion_point(serialize_to_array_start:grpc_test.GetMinDisRsp)
  uint32_t cached_has_bits = 0;
  (void) cached_has_bits;

  // float min_dis = 1;
  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_min_dis = this->_internal_min_dis();
  uint32_t raw_min_dis;
  memcpy(&raw_min_dis, &tmp_min_dis, sizeof(tmp_min_dis));
  if (raw_min_dis != 0) {
    target = stream->EnsureSpace(target);
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormatLite::WriteFloatToArray(1, this->_internal_min_dis(), target);
  }

  if (PROTOBUF_PREDICT_FALSE(_internal_metadata_.have_unknown_fields())) {
    target = ::PROTOBUF_NAMESPACE_ID::internal::WireFormat::InternalSerializeUnknownFieldsToArray(
        _internal_metadata_.unknown_fields<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(::PROTOBUF_NAMESPACE_ID::UnknownFieldSet::default_instance), target, stream);
  }
  // @@protoc_insertion_point(serialize_to_array_end:grpc_test.GetMinDisRsp)
  return target;
}

size_t GetMinDisRsp::ByteSizeLong() const {
// @@protoc_insertion_point(message_byte_size_start:grpc_test.GetMinDisRsp)
  size_t total_size = 0;

  uint32_t cached_has_bits = 0;
  // Prevent compiler warnings about cached_has_bits being unused
  (void) cached_has_bits;

  // float min_dis = 1;
  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_min_dis = this->_internal_min_dis();
  uint32_t raw_min_dis;
  memcpy(&raw_min_dis, &tmp_min_dis, sizeof(tmp_min_dis));
  if (raw_min_dis != 0) {
    total_size += 1 + 4;
  }

  return MaybeComputeUnknownFieldsSize(total_size, &_cached_size_);
}

const ::PROTOBUF_NAMESPACE_ID::Message::ClassData GetMinDisRsp::_class_data_ = {
    ::PROTOBUF_NAMESPACE_ID::Message::CopyWithSizeCheck,
    GetMinDisRsp::MergeImpl
};
const ::PROTOBUF_NAMESPACE_ID::Message::ClassData*GetMinDisRsp::GetClassData() const { return &_class_data_; }

void GetMinDisRsp::MergeImpl(::PROTOBUF_NAMESPACE_ID::Message* to,
                      const ::PROTOBUF_NAMESPACE_ID::Message& from) {
  static_cast<GetMinDisRsp *>(to)->MergeFrom(
      static_cast<const GetMinDisRsp &>(from));
}


void GetMinDisRsp::MergeFrom(const GetMinDisRsp& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:grpc_test.GetMinDisRsp)
  GOOGLE_DCHECK_NE(&from, this);
  uint32_t cached_has_bits = 0;
  (void) cached_has_bits;

  static_assert(sizeof(uint32_t) == sizeof(float), "Code assumes uint32_t and float are the same size.");
  float tmp_min_dis = from._internal_min_dis();
  uint32_t raw_min_dis;
  memcpy(&raw_min_dis, &tmp_min_dis, sizeof(tmp_min_dis));
  if (raw_min_dis != 0) {
    _internal_set_min_dis(from._internal_min_dis());
  }
  _internal_metadata_.MergeFrom<::PROTOBUF_NAMESPACE_ID::UnknownFieldSet>(from._internal_metadata_);
}

void GetMinDisRsp::CopyFrom(const GetMinDisRsp& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:grpc_test.GetMinDisRsp)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool GetMinDisRsp::IsInitialized() const {
  return true;
}

void GetMinDisRsp::InternalSwap(GetMinDisRsp* other) {
  using std::swap;
  _internal_metadata_.InternalSwap(&other->_internal_metadata_);
  swap(min_dis_, other->min_dis_);
}

::PROTOBUF_NAMESPACE_ID::Metadata GetMinDisRsp::GetMetadata() const {
  return ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(
      &descriptor_table_grpc_5ftest_2eproto_getter, &descriptor_table_grpc_5ftest_2eproto_once,
      file_level_metadata_grpc_5ftest_2eproto[2]);
}

// @@protoc_insertion_point(namespace_scope)
}  // namespace grpc_test
PROTOBUF_NAMESPACE_OPEN
template<> PROTOBUF_NOINLINE ::grpc_test::Vector* Arena::CreateMaybeMessage< ::grpc_test::Vector >(Arena* arena) {
  return Arena::CreateMessageInternal< ::grpc_test::Vector >(arena);
}
template<> PROTOBUF_NOINLINE ::grpc_test::GetMinDisReq* Arena::CreateMaybeMessage< ::grpc_test::GetMinDisReq >(Arena* arena) {
  return Arena::CreateMessageInternal< ::grpc_test::GetMinDisReq >(arena);
}
template<> PROTOBUF_NOINLINE ::grpc_test::GetMinDisRsp* Arena::CreateMaybeMessage< ::grpc_test::GetMinDisRsp >(Arena* arena) {
  return Arena::CreateMessageInternal< ::grpc_test::GetMinDisRsp >(arena);
}
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>