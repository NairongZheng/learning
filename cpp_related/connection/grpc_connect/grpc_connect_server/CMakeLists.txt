cmake_minimum_required(VERSION 3.16)

# 项目名称和版本
project(grpc_connect_server VERSION 1.0 LANGUAGES CXX)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 定义构建类型
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Debug)
endif()

# 设置路径变量
set(GRPC_SOURCE_DIR D:/code/grpc)
set(THIRD_PARTY_DIR D:/code/grpc/third_party)
set(GRPC_BUILD_DIR D:/code/grpc/cmake_out)

# 包含目录
include_directories(
    ${THIRD_PARTY_DIR}/re2
    ${THIRD_PARTY_DIR}/address_sorting/include
    ${THIRD_PARTY_DIR}/abseil-cpp
    ${THIRD_PARTY_DIR}/protobuf/src
    ${GRPC_SOURCE_DIR}/include
)

# 动态设置库目录
if(CMAKE_BUILD_TYPE STREQUAL "Debug")
    set(BUILD_TYPE_DIR Debug)
else()
    set(BUILD_TYPE_DIR Release)
endif()

# 库目录
link_directories(
    ${GRPC_BUILD_DIR}/third_party/re2/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/types/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/synchronization/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/status/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/random/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/flags/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/debugging/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/container/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/hash/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/numeric/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/time/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/base/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/abseil-cpp/absl/strings/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/boringssl-with-bazel/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/protobuf/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/zlib/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/third_party/cares/cares/lib/${BUILD_TYPE_DIR}
    ${GRPC_BUILD_DIR}/${BUILD_TYPE_DIR}
)

# 源文件
set(SOURCE_FILES
    grpc_connect_server.cpp
    proto/grpc_test.grpc.pb.cc
    proto/grpc_test.pb.cc
)

# 添加可执行文件
add_executable(grpc_connect_server ${SOURCE_FILES})
# add_executable(grpc_connect_server
#     grpc_connect_server.cpp # 替换为您的项目的源文件
#     proto/grpc_test.grpc.pb.cc
#     proto/grpc_test.pb.cc
# )

# 链接库
target_link_libraries(grpc_connect_server
    libprotobufd
    gpr
    grpc
    grpc++
    grpc++_reflection
    address_sorting
    ws2_32
    cares
    zlibstaticd
    upb
    ssl
    crypto
    absl_bad_any_cast_impl
    absl_bad_optional_access
    absl_bad_variant_access
    absl_base
    absl_city
    absl_civil_time
    absl_cord
    absl_debugging_internal
    absl_demangle_internal
    absl_examine_stack
    absl_exponential_biased
    absl_failure_signal_handler
    absl_flags
    absl_flags_config
    absl_flags_internal
    absl_flags_marshalling
    absl_flags_parse
    absl_flags_program_name
    absl_flags_usage
    absl_flags_usage_internal
    absl_graphcycles_internal
    absl_hash
    absl_hashtablez_sampler
    absl_int128
    absl_leak_check
    absl_leak_check_disable
    absl_log_severity
    absl_malloc_internal
    absl_periodic_sampler
    absl_random_distributions
    absl_random_internal_distribution_test_util
    absl_random_internal_pool_urbg
    absl_random_internal_randen
    absl_random_internal_randen_hwaes
    absl_random_internal_randen_hwaes_impl
    absl_random_internal_randen_slow
    absl_random_internal_seed_material
    absl_random_seed_gen_exception
    absl_random_seed_sequences
    absl_raw_hash_set
    absl_raw_logging_internal
    absl_scoped_set_env
    absl_spinlock_wait
    absl_stacktrace
    absl_status
    absl_strings
    absl_strings_internal
    absl_str_format_internal
    absl_symbolize
    absl_synchronization
    absl_throw_delegate
    absl_time
    absl_time_zone
    absl_statusor
    re2
)
