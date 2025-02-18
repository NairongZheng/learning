// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: grpc_test.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_grpc_5ftest_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_grpc_5ftest_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3013000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3013000 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata_lite.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_grpc_5ftest_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_grpc_5ftest_2eproto {
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::AuxiliaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTable schema[3]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::FieldMetadata field_metadata[];
  static const ::PROTOBUF_NAMESPACE_ID::internal::SerializationTable serialization_table[];
  static const ::PROTOBUF_NAMESPACE_ID::uint32 offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_grpc_5ftest_2eproto;
namespace grpc_test {
class GetMinDisReq;
class GetMinDisReqDefaultTypeInternal;
extern GetMinDisReqDefaultTypeInternal _GetMinDisReq_default_instance_;
class GetMinDisRsp;
class GetMinDisRspDefaultTypeInternal;
extern GetMinDisRspDefaultTypeInternal _GetMinDisRsp_default_instance_;
class Vector;
class VectorDefaultTypeInternal;
extern VectorDefaultTypeInternal _Vector_default_instance_;
}  // namespace grpc_test
PROTOBUF_NAMESPACE_OPEN
template<> ::grpc_test::GetMinDisReq* Arena::CreateMaybeMessage<::grpc_test::GetMinDisReq>(Arena*);
template<> ::grpc_test::GetMinDisRsp* Arena::CreateMaybeMessage<::grpc_test::GetMinDisRsp>(Arena*);
template<> ::grpc_test::Vector* Arena::CreateMaybeMessage<::grpc_test::Vector>(Arena*);
PROTOBUF_NAMESPACE_CLOSE
namespace grpc_test {

// ===================================================================

class Vector PROTOBUF_FINAL :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:grpc_test.Vector) */ {
 public:
  inline Vector() : Vector(nullptr) {}
  virtual ~Vector();

  Vector(const Vector& from);
  Vector(Vector&& from) noexcept
    : Vector() {
    *this = ::std::move(from);
  }

  inline Vector& operator=(const Vector& from) {
    CopyFrom(from);
    return *this;
  }
  inline Vector& operator=(Vector&& from) noexcept {
    if (GetArena() == from.GetArena()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const Vector& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const Vector* internal_default_instance() {
    return reinterpret_cast<const Vector*>(
               &_Vector_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(Vector& a, Vector& b) {
    a.Swap(&b);
  }
  inline void Swap(Vector* other) {
    if (other == this) return;
    if (GetArena() == other->GetArena()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(Vector* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetArena() == other->GetArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline Vector* New() const final {
    return CreateMaybeMessage<Vector>(nullptr);
  }

  Vector* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<Vector>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const Vector& from);
  void MergeFrom(const Vector& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  ::PROTOBUF_NAMESPACE_ID::uint8* _InternalSerialize(
      ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(Vector* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "grpc_test.Vector";
  }
  protected:
  explicit Vector(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_grpc_5ftest_2eproto);
    return ::descriptor_table_grpc_5ftest_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kXFieldNumber = 1,
    kYFieldNumber = 2,
    kZFieldNumber = 3,
  };
  // float x = 1;
  void clear_x();
  float x() const;
  void set_x(float value);
  private:
  float _internal_x() const;
  void _internal_set_x(float value);
  public:

  // float y = 2;
  void clear_y();
  float y() const;
  void set_y(float value);
  private:
  float _internal_y() const;
  void _internal_set_y(float value);
  public:

  // float z = 3;
  void clear_z();
  float z() const;
  void set_z(float value);
  private:
  float _internal_z() const;
  void _internal_set_z(float value);
  public:

  // @@protoc_insertion_point(class_scope:grpc_test.Vector)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  float x_;
  float y_;
  float z_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_grpc_5ftest_2eproto;
};
// -------------------------------------------------------------------

class GetMinDisReq PROTOBUF_FINAL :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:grpc_test.GetMinDisReq) */ {
 public:
  inline GetMinDisReq() : GetMinDisReq(nullptr) {}
  virtual ~GetMinDisReq();

  GetMinDisReq(const GetMinDisReq& from);
  GetMinDisReq(GetMinDisReq&& from) noexcept
    : GetMinDisReq() {
    *this = ::std::move(from);
  }

  inline GetMinDisReq& operator=(const GetMinDisReq& from) {
    CopyFrom(from);
    return *this;
  }
  inline GetMinDisReq& operator=(GetMinDisReq&& from) noexcept {
    if (GetArena() == from.GetArena()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const GetMinDisReq& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const GetMinDisReq* internal_default_instance() {
    return reinterpret_cast<const GetMinDisReq*>(
               &_GetMinDisReq_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    1;

  friend void swap(GetMinDisReq& a, GetMinDisReq& b) {
    a.Swap(&b);
  }
  inline void Swap(GetMinDisReq* other) {
    if (other == this) return;
    if (GetArena() == other->GetArena()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(GetMinDisReq* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetArena() == other->GetArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline GetMinDisReq* New() const final {
    return CreateMaybeMessage<GetMinDisReq>(nullptr);
  }

  GetMinDisReq* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<GetMinDisReq>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const GetMinDisReq& from);
  void MergeFrom(const GetMinDisReq& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  ::PROTOBUF_NAMESPACE_ID::uint8* _InternalSerialize(
      ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(GetMinDisReq* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "grpc_test.GetMinDisReq";
  }
  protected:
  explicit GetMinDisReq(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_grpc_5ftest_2eproto);
    return ::descriptor_table_grpc_5ftest_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kPointListFieldNumber = 1,
  };
  // repeated .grpc_test.Vector point_list = 1;
  int point_list_size() const;
  private:
  int _internal_point_list_size() const;
  public:
  void clear_point_list();
  ::grpc_test::Vector* mutable_point_list(int index);
  ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::grpc_test::Vector >*
      mutable_point_list();
  private:
  const ::grpc_test::Vector& _internal_point_list(int index) const;
  ::grpc_test::Vector* _internal_add_point_list();
  public:
  const ::grpc_test::Vector& point_list(int index) const;
  ::grpc_test::Vector* add_point_list();
  const ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::grpc_test::Vector >&
      point_list() const;

  // @@protoc_insertion_point(class_scope:grpc_test.GetMinDisReq)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::grpc_test::Vector > point_list_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_grpc_5ftest_2eproto;
};
// -------------------------------------------------------------------

class GetMinDisRsp PROTOBUF_FINAL :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:grpc_test.GetMinDisRsp) */ {
 public:
  inline GetMinDisRsp() : GetMinDisRsp(nullptr) {}
  virtual ~GetMinDisRsp();

  GetMinDisRsp(const GetMinDisRsp& from);
  GetMinDisRsp(GetMinDisRsp&& from) noexcept
    : GetMinDisRsp() {
    *this = ::std::move(from);
  }

  inline GetMinDisRsp& operator=(const GetMinDisRsp& from) {
    CopyFrom(from);
    return *this;
  }
  inline GetMinDisRsp& operator=(GetMinDisRsp&& from) noexcept {
    if (GetArena() == from.GetArena()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const GetMinDisRsp& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const GetMinDisRsp* internal_default_instance() {
    return reinterpret_cast<const GetMinDisRsp*>(
               &_GetMinDisRsp_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    2;

  friend void swap(GetMinDisRsp& a, GetMinDisRsp& b) {
    a.Swap(&b);
  }
  inline void Swap(GetMinDisRsp* other) {
    if (other == this) return;
    if (GetArena() == other->GetArena()) {
      InternalSwap(other);
    } else {
      ::PROTOBUF_NAMESPACE_ID::internal::GenericSwap(this, other);
    }
  }
  void UnsafeArenaSwap(GetMinDisRsp* other) {
    if (other == this) return;
    GOOGLE_DCHECK(GetArena() == other->GetArena());
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline GetMinDisRsp* New() const final {
    return CreateMaybeMessage<GetMinDisRsp>(nullptr);
  }

  GetMinDisRsp* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<GetMinDisRsp>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const GetMinDisRsp& from);
  void MergeFrom(const GetMinDisRsp& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  ::PROTOBUF_NAMESPACE_ID::uint8* _InternalSerialize(
      ::PROTOBUF_NAMESPACE_ID::uint8* target, ::PROTOBUF_NAMESPACE_ID::io::EpsCopyOutputStream* stream) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(GetMinDisRsp* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "grpc_test.GetMinDisRsp";
  }
  protected:
  explicit GetMinDisRsp(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  private:
  static void ArenaDtor(void* object);
  inline void RegisterArenaDtor(::PROTOBUF_NAMESPACE_ID::Arena* arena);
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_grpc_5ftest_2eproto);
    return ::descriptor_table_grpc_5ftest_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  enum : int {
    kMinDisFieldNumber = 1,
  };
  // float min_dis = 1;
  void clear_min_dis();
  float min_dis() const;
  void set_min_dis(float value);
  private:
  float _internal_min_dis() const;
  void _internal_set_min_dis(float value);
  public:

  // @@protoc_insertion_point(class_scope:grpc_test.GetMinDisRsp)
 private:
  class _Internal;

  template <typename T> friend class ::PROTOBUF_NAMESPACE_ID::Arena::InternalHelper;
  typedef void InternalArenaConstructable_;
  typedef void DestructorSkippable_;
  float min_dis_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_grpc_5ftest_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// Vector

// float x = 1;
inline void Vector::clear_x() {
  x_ = 0;
}
inline float Vector::_internal_x() const {
  return x_;
}
inline float Vector::x() const {
  // @@protoc_insertion_point(field_get:grpc_test.Vector.x)
  return _internal_x();
}
inline void Vector::_internal_set_x(float value) {
  
  x_ = value;
}
inline void Vector::set_x(float value) {
  _internal_set_x(value);
  // @@protoc_insertion_point(field_set:grpc_test.Vector.x)
}

// float y = 2;
inline void Vector::clear_y() {
  y_ = 0;
}
inline float Vector::_internal_y() const {
  return y_;
}
inline float Vector::y() const {
  // @@protoc_insertion_point(field_get:grpc_test.Vector.y)
  return _internal_y();
}
inline void Vector::_internal_set_y(float value) {
  
  y_ = value;
}
inline void Vector::set_y(float value) {
  _internal_set_y(value);
  // @@protoc_insertion_point(field_set:grpc_test.Vector.y)
}

// float z = 3;
inline void Vector::clear_z() {
  z_ = 0;
}
inline float Vector::_internal_z() const {
  return z_;
}
inline float Vector::z() const {
  // @@protoc_insertion_point(field_get:grpc_test.Vector.z)
  return _internal_z();
}
inline void Vector::_internal_set_z(float value) {
  
  z_ = value;
}
inline void Vector::set_z(float value) {
  _internal_set_z(value);
  // @@protoc_insertion_point(field_set:grpc_test.Vector.z)
}

// -------------------------------------------------------------------

// GetMinDisReq

// repeated .grpc_test.Vector point_list = 1;
inline int GetMinDisReq::_internal_point_list_size() const {
  return point_list_.size();
}
inline int GetMinDisReq::point_list_size() const {
  return _internal_point_list_size();
}
inline void GetMinDisReq::clear_point_list() {
  point_list_.Clear();
}
inline ::grpc_test::Vector* GetMinDisReq::mutable_point_list(int index) {
  // @@protoc_insertion_point(field_mutable:grpc_test.GetMinDisReq.point_list)
  return point_list_.Mutable(index);
}
inline ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::grpc_test::Vector >*
GetMinDisReq::mutable_point_list() {
  // @@protoc_insertion_point(field_mutable_list:grpc_test.GetMinDisReq.point_list)
  return &point_list_;
}
inline const ::grpc_test::Vector& GetMinDisReq::_internal_point_list(int index) const {
  return point_list_.Get(index);
}
inline const ::grpc_test::Vector& GetMinDisReq::point_list(int index) const {
  // @@protoc_insertion_point(field_get:grpc_test.GetMinDisReq.point_list)
  return _internal_point_list(index);
}
inline ::grpc_test::Vector* GetMinDisReq::_internal_add_point_list() {
  return point_list_.Add();
}
inline ::grpc_test::Vector* GetMinDisReq::add_point_list() {
  // @@protoc_insertion_point(field_add:grpc_test.GetMinDisReq.point_list)
  return _internal_add_point_list();
}
inline const ::PROTOBUF_NAMESPACE_ID::RepeatedPtrField< ::grpc_test::Vector >&
GetMinDisReq::point_list() const {
  // @@protoc_insertion_point(field_list:grpc_test.GetMinDisReq.point_list)
  return point_list_;
}

// -------------------------------------------------------------------

// GetMinDisRsp

// float min_dis = 1;
inline void GetMinDisRsp::clear_min_dis() {
  min_dis_ = 0;
}
inline float GetMinDisRsp::_internal_min_dis() const {
  return min_dis_;
}
inline float GetMinDisRsp::min_dis() const {
  // @@protoc_insertion_point(field_get:grpc_test.GetMinDisRsp.min_dis)
  return _internal_min_dis();
}
inline void GetMinDisRsp::_internal_set_min_dis(float value) {
  
  min_dis_ = value;
}
inline void GetMinDisRsp::set_min_dis(float value) {
  _internal_set_min_dis(value);
  // @@protoc_insertion_point(field_set:grpc_test.GetMinDisRsp.min_dis)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__
// -------------------------------------------------------------------

// -------------------------------------------------------------------


// @@protoc_insertion_point(namespace_scope)

}  // namespace grpc_test

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_grpc_5ftest_2eproto
