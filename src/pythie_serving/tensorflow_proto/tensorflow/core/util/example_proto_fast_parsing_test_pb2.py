# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/util/example_proto_fast_parsing_test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.example import feature_pb2 as tensorflow_dot_core_dot_example_dot_feature__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/util/example_proto_fast_parsing_test.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=b'\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:tensorflow/core/util/example_proto_fast_parsing_test.proto\x12\ntensorflow\x1a%tensorflow/core/example/feature.proto\"\xc8\x01\n\x11\x45xampleWithExtras\x12&\n\x08\x66\x65\x61tures\x18\x01 \x01(\x0b\x32\x14.tensorflow.Features\x12\x0f\n\x06\x65xtra1\x18\xb9\n \x01(\t\x12\x0f\n\x06\x65xtra2\x18\xba\n \x01(\x03\x12\x0f\n\x06\x65xtra3\x18\xbb\n \x01(\x07\x12\x0f\n\x06\x65xtra4\x18\xbc\n \x01(\x06\x12\x0f\n\x06\x65xtra5\x18\xbd\n \x01(\x01\x12\x0f\n\x06\x65xtra6\x18\xbe\n \x03(\x02\x12%\n\x06\x65xtra7\x18\xbf\n \x01(\x0b\x32\x14.tensorflow.FeaturesB\x03\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[tensorflow_dot_core_dot_example_dot_feature__pb2.DESCRIPTOR,])




_EXAMPLEWITHEXTRAS = _descriptor.Descriptor(
  name='ExampleWithExtras',
  full_name='tensorflow.ExampleWithExtras',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='tensorflow.ExampleWithExtras.features', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra1', full_name='tensorflow.ExampleWithExtras.extra1', index=1,
      number=1337, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra2', full_name='tensorflow.ExampleWithExtras.extra2', index=2,
      number=1338, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra3', full_name='tensorflow.ExampleWithExtras.extra3', index=3,
      number=1339, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra4', full_name='tensorflow.ExampleWithExtras.extra4', index=4,
      number=1340, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra5', full_name='tensorflow.ExampleWithExtras.extra5', index=5,
      number=1341, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra6', full_name='tensorflow.ExampleWithExtras.extra6', index=6,
      number=1342, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra7', full_name='tensorflow.ExampleWithExtras.extra7', index=7,
      number=1343, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=314,
)

_EXAMPLEWITHEXTRAS.fields_by_name['features'].message_type = tensorflow_dot_core_dot_example_dot_feature__pb2._FEATURES
_EXAMPLEWITHEXTRAS.fields_by_name['extra7'].message_type = tensorflow_dot_core_dot_example_dot_feature__pb2._FEATURES
DESCRIPTOR.message_types_by_name['ExampleWithExtras'] = _EXAMPLEWITHEXTRAS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExampleWithExtras = _reflection.GeneratedProtocolMessageType('ExampleWithExtras', (_message.Message,), {
  'DESCRIPTOR' : _EXAMPLEWITHEXTRAS,
  '__module__' : 'tensorflow.core.util.example_proto_fast_parsing_test_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ExampleWithExtras)
  })
_sym_db.RegisterMessage(ExampleWithExtras)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
