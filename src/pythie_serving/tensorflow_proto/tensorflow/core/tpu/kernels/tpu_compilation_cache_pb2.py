# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/tpu/kernels/tpu_compilation_cache.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/tpu/kernels/tpu_compilation_cache.proto',
  package='tensorflow.tpu',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7tensorflow/core/tpu/kernels/tpu_compilation_cache.proto\x12\x0etensorflow.tpu*R\n\x1b\x43ompilationCacheFetchTarget\x12\x0b\n\x07INVALID\x10\x00\x12\x08\n\x04MAIN\x10\x01\x12\x0c\n\x08SHARDING\x10\x02\x12\x0e\n\nUNSHARDING\x10\x03\x62\x06proto3'
)

_COMPILATIONCACHEFETCHTARGET = _descriptor.EnumDescriptor(
  name='CompilationCacheFetchTarget',
  full_name='tensorflow.tpu.CompilationCacheFetchTarget',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAIN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SHARDING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNSHARDING', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=75,
  serialized_end=157,
)
_sym_db.RegisterEnumDescriptor(_COMPILATIONCACHEFETCHTARGET)

CompilationCacheFetchTarget = enum_type_wrapper.EnumTypeWrapper(_COMPILATIONCACHEFETCHTARGET)
INVALID = 0
MAIN = 1
SHARDING = 2
UNSHARDING = 3


DESCRIPTOR.enum_types_by_name['CompilationCacheFetchTarget'] = _COMPILATIONCACHEFETCHTARGET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
