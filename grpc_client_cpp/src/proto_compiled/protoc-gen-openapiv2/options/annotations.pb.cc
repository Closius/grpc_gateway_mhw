// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: protoc-gen-openapiv2/options/annotations.proto

#include "protoc-gen-openapiv2/options/annotations.pb.h"

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
namespace grpc {
namespace gateway {
namespace protoc_gen_openapiv2 {
namespace options {
}  // namespace options
}  // namespace protoc_gen_openapiv2
}  // namespace gateway
}  // namespace grpc
static constexpr ::PROTOBUF_NAMESPACE_ID::EnumDescriptor const** file_level_enum_descriptors_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto = nullptr;
static constexpr ::PROTOBUF_NAMESPACE_ID::ServiceDescriptor const** file_level_service_descriptors_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto = nullptr;
const uint32_t TableStruct_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto::offsets[1] = {};
static constexpr ::PROTOBUF_NAMESPACE_ID::internal::MigrationSchema* schemas = nullptr;
static constexpr ::PROTOBUF_NAMESPACE_ID::Message* const* file_default_instances = nullptr;

const char descriptor_table_protodef_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto[] PROTOBUF_SECTION_VARIABLE(protodesc_cold) =
  "\n.protoc-gen-openapiv2/options/annotatio"
  "ns.proto\022)grpc.gateway.protoc_gen_openap"
  "iv2.options\032 google/protobuf/descriptor."
  "proto\032,protoc-gen-openapiv2/options/open"
  "apiv2.proto:l\n\021openapiv2_swagger\022\034.googl"
  "e.protobuf.FileOptions\030\222\010 \001(\01322.grpc.gat"
  "eway.protoc_gen_openapiv2.options.Swagge"
  "r:r\n\023openapiv2_operation\022\036.google.protob"
  "uf.MethodOptions\030\222\010 \001(\01324.grpc.gateway.p"
  "rotoc_gen_openapiv2.options.Operation:m\n"
  "\020openapiv2_schema\022\037.google.protobuf.Mess"
  "ageOptions\030\222\010 \001(\01321.grpc.gateway.protoc_"
  "gen_openapiv2.options.Schema:g\n\ropenapiv"
  "2_tag\022\037.google.protobuf.ServiceOptions\030\222"
  "\010 \001(\0132..grpc.gateway.protoc_gen_openapiv"
  "2.options.Tag:n\n\017openapiv2_field\022\035.googl"
  "e.protobuf.FieldOptions\030\222\010 \001(\01325.grpc.ga"
  "teway.protoc_gen_openapiv2.options.JSONS"
  "chemaBHZFgithub.com/grpc-ecosystem/grpc-"
  "gateway/v2/protoc-gen-openapiv2/optionsb"
  "\006proto3"
  ;
static const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable*const descriptor_table_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto_deps[2] = {
  &::descriptor_table_google_2fprotobuf_2fdescriptor_2eproto,
  &::descriptor_table_protoc_2dgen_2dopenapiv2_2foptions_2fopenapiv2_2eproto,
};
static ::PROTOBUF_NAMESPACE_ID::internal::once_flag descriptor_table_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto_once;
const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto = {
  false, false, 807, descriptor_table_protodef_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto, "protoc-gen-openapiv2/options/annotations.proto", 
  &descriptor_table_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto_once, descriptor_table_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto_deps, 2, 0,
  schemas, file_default_instances, TableStruct_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto::offsets,
  nullptr, file_level_enum_descriptors_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto, file_level_service_descriptors_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto,
};
PROTOBUF_ATTRIBUTE_WEAK const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable* descriptor_table_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto_getter() {
  return &descriptor_table_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto;
}

// Force running AddDescriptors() at dynamic initialization time.
PROTOBUF_ATTRIBUTE_INIT_PRIORITY static ::PROTOBUF_NAMESPACE_ID::internal::AddDescriptorsRunner dynamic_init_dummy_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto(&descriptor_table_protoc_2dgen_2dopenapiv2_2foptions_2fannotations_2eproto);
namespace grpc {
namespace gateway {
namespace protoc_gen_openapiv2 {
namespace options {
PROTOBUF_ATTRIBUTE_INIT_PRIORITY ::PROTOBUF_NAMESPACE_ID::internal::ExtensionIdentifier< ::PROTOBUF_NAMESPACE_ID::FileOptions,
    ::PROTOBUF_NAMESPACE_ID::internal::MessageTypeTraits< ::grpc::gateway::protoc_gen_openapiv2::options::Swagger >, 11, false >
  openapiv2_swagger(kOpenapiv2SwaggerFieldNumber, ::grpc::gateway::protoc_gen_openapiv2::options::Swagger::default_instance());
PROTOBUF_ATTRIBUTE_INIT_PRIORITY ::PROTOBUF_NAMESPACE_ID::internal::ExtensionIdentifier< ::PROTOBUF_NAMESPACE_ID::MethodOptions,
    ::PROTOBUF_NAMESPACE_ID::internal::MessageTypeTraits< ::grpc::gateway::protoc_gen_openapiv2::options::Operation >, 11, false >
  openapiv2_operation(kOpenapiv2OperationFieldNumber, ::grpc::gateway::protoc_gen_openapiv2::options::Operation::default_instance());
PROTOBUF_ATTRIBUTE_INIT_PRIORITY ::PROTOBUF_NAMESPACE_ID::internal::ExtensionIdentifier< ::PROTOBUF_NAMESPACE_ID::MessageOptions,
    ::PROTOBUF_NAMESPACE_ID::internal::MessageTypeTraits< ::grpc::gateway::protoc_gen_openapiv2::options::Schema >, 11, false >
  openapiv2_schema(kOpenapiv2SchemaFieldNumber, ::grpc::gateway::protoc_gen_openapiv2::options::Schema::default_instance());
PROTOBUF_ATTRIBUTE_INIT_PRIORITY ::PROTOBUF_NAMESPACE_ID::internal::ExtensionIdentifier< ::PROTOBUF_NAMESPACE_ID::ServiceOptions,
    ::PROTOBUF_NAMESPACE_ID::internal::MessageTypeTraits< ::grpc::gateway::protoc_gen_openapiv2::options::Tag >, 11, false >
  openapiv2_tag(kOpenapiv2TagFieldNumber, ::grpc::gateway::protoc_gen_openapiv2::options::Tag::default_instance());
PROTOBUF_ATTRIBUTE_INIT_PRIORITY ::PROTOBUF_NAMESPACE_ID::internal::ExtensionIdentifier< ::PROTOBUF_NAMESPACE_ID::FieldOptions,
    ::PROTOBUF_NAMESPACE_ID::internal::MessageTypeTraits< ::grpc::gateway::protoc_gen_openapiv2::options::JSONSchema >, 11, false >
  openapiv2_field(kOpenapiv2FieldFieldNumber, ::grpc::gateway::protoc_gen_openapiv2::options::JSONSchema::default_instance());

// @@protoc_insertion_point(namespace_scope)
}  // namespace options
}  // namespace protoc_gen_openapiv2
}  // namespace gateway
}  // namespace grpc
PROTOBUF_NAMESPACE_OPEN
PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)
#include <google/protobuf/port_undef.inc>
