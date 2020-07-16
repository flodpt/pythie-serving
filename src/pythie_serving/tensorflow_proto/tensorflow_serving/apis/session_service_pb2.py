# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/apis/session_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow_serving.apis import model_pb2 as tensorflow__serving_dot_apis_dot_model__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.protobuf import config_pb2 as tensorflow_dot_core_dot_protobuf_dot_config__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.protobuf import named_tensor_pb2 as tensorflow_dot_core_dot_protobuf_dot_named__tensor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_serving/apis/session_service.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_options=b'\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-tensorflow_serving/apis/session_service.proto\x12\x12tensorflow.serving\x1a#tensorflow_serving/apis/model.proto\x1a%tensorflow/core/protobuf/config.proto\x1a+tensorflow/core/protobuf/named_tensor.proto\"\xba\x01\n\x11SessionRunRequest\x12\x31\n\nmodel_spec\x18\x01 \x01(\x0b\x32\x1d.tensorflow.serving.ModelSpec\x12*\n\x04\x66\x65\x65\x64\x18\x02 \x03(\x0b\x32\x1c.tensorflow.NamedTensorProto\x12\r\n\x05\x66\x65tch\x18\x03 \x03(\t\x12\x0e\n\x06target\x18\x04 \x03(\t\x12\'\n\x07options\x18\x05 \x01(\x0b\x32\x16.tensorflow.RunOptions\"\xa0\x01\n\x12SessionRunResponse\x12\x31\n\nmodel_spec\x18\x03 \x01(\x0b\x32\x1d.tensorflow.serving.ModelSpec\x12,\n\x06tensor\x18\x01 \x03(\x0b\x32\x1c.tensorflow.NamedTensorProto\x12)\n\x08metadata\x18\x02 \x01(\x0b\x32\x17.tensorflow.RunMetadata2m\n\x0eSessionService\x12[\n\nSessionRun\x12%.tensorflow.serving.SessionRunRequest\x1a&.tensorflow.serving.SessionRunResponseB\x03\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[tensorflow__serving_dot_apis_dot_model__pb2.DESCRIPTOR,tensorflow_dot_core_dot_protobuf_dot_config__pb2.DESCRIPTOR,tensorflow_dot_core_dot_protobuf_dot_named__tensor__pb2.DESCRIPTOR,])




_SESSIONRUNREQUEST = _descriptor.Descriptor(
  name='SessionRunRequest',
  full_name='tensorflow.serving.SessionRunRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_spec', full_name='tensorflow.serving.SessionRunRequest.model_spec', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='feed', full_name='tensorflow.serving.SessionRunRequest.feed', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fetch', full_name='tensorflow.serving.SessionRunRequest.fetch', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='tensorflow.serving.SessionRunRequest.target', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='options', full_name='tensorflow.serving.SessionRunRequest.options', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=191,
  serialized_end=377,
)


_SESSIONRUNRESPONSE = _descriptor.Descriptor(
  name='SessionRunResponse',
  full_name='tensorflow.serving.SessionRunResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model_spec', full_name='tensorflow.serving.SessionRunResponse.model_spec', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='tensorflow.serving.SessionRunResponse.tensor', index=1,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='tensorflow.serving.SessionRunResponse.metadata', index=2,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=380,
  serialized_end=540,
)

_SESSIONRUNREQUEST.fields_by_name['model_spec'].message_type = tensorflow__serving_dot_apis_dot_model__pb2._MODELSPEC
_SESSIONRUNREQUEST.fields_by_name['feed'].message_type = tensorflow_dot_core_dot_protobuf_dot_named__tensor__pb2._NAMEDTENSORPROTO
_SESSIONRUNREQUEST.fields_by_name['options'].message_type = tensorflow_dot_core_dot_protobuf_dot_config__pb2._RUNOPTIONS
_SESSIONRUNRESPONSE.fields_by_name['model_spec'].message_type = tensorflow__serving_dot_apis_dot_model__pb2._MODELSPEC
_SESSIONRUNRESPONSE.fields_by_name['tensor'].message_type = tensorflow_dot_core_dot_protobuf_dot_named__tensor__pb2._NAMEDTENSORPROTO
_SESSIONRUNRESPONSE.fields_by_name['metadata'].message_type = tensorflow_dot_core_dot_protobuf_dot_config__pb2._RUNMETADATA
DESCRIPTOR.message_types_by_name['SessionRunRequest'] = _SESSIONRUNREQUEST
DESCRIPTOR.message_types_by_name['SessionRunResponse'] = _SESSIONRUNRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionRunRequest = _reflection.GeneratedProtocolMessageType('SessionRunRequest', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONRUNREQUEST,
  '__module__' : 'tensorflow_serving.apis.session_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.SessionRunRequest)
  })
_sym_db.RegisterMessage(SessionRunRequest)

SessionRunResponse = _reflection.GeneratedProtocolMessageType('SessionRunResponse', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONRUNRESPONSE,
  '__module__' : 'tensorflow_serving.apis.session_service_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.SessionRunResponse)
  })
_sym_db.RegisterMessage(SessionRunResponse)


DESCRIPTOR._options = None

_SESSIONSERVICE = _descriptor.ServiceDescriptor(
  name='SessionService',
  full_name='tensorflow.serving.SessionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=542,
  serialized_end=651,
  methods=[
  _descriptor.MethodDescriptor(
    name='SessionRun',
    full_name='tensorflow.serving.SessionService.SessionRun',
    index=0,
    containing_service=None,
    input_type=_SESSIONRUNREQUEST,
    output_type=_SESSIONRUNRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SESSIONSERVICE)

DESCRIPTOR.services_by_name['SessionService'] = _SESSIONSERVICE

# @@protoc_insertion_point(module_scope)
