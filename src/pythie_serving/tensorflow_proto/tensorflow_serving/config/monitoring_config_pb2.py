# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/config/monitoring_config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_serving/config/monitoring_config.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_options=b'\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1tensorflow_serving/config/monitoring_config.proto\x12\x12tensorflow.serving\"0\n\x10PrometheusConfig\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x12\x0c\n\x04path\x18\x02 \x01(\t\"S\n\x10MonitoringConfig\x12?\n\x11prometheus_config\x18\x01 \x01(\x0b\x32$.tensorflow.serving.PrometheusConfigB\x03\xf8\x01\x01\x62\x06proto3'
)




_PROMETHEUSCONFIG = _descriptor.Descriptor(
  name='PrometheusConfig',
  full_name='tensorflow.serving.PrometheusConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='tensorflow.serving.PrometheusConfig.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='tensorflow.serving.PrometheusConfig.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=73,
  serialized_end=121,
)


_MONITORINGCONFIG = _descriptor.Descriptor(
  name='MonitoringConfig',
  full_name='tensorflow.serving.MonitoringConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prometheus_config', full_name='tensorflow.serving.MonitoringConfig.prometheus_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=123,
  serialized_end=206,
)

_MONITORINGCONFIG.fields_by_name['prometheus_config'].message_type = _PROMETHEUSCONFIG
DESCRIPTOR.message_types_by_name['PrometheusConfig'] = _PROMETHEUSCONFIG
DESCRIPTOR.message_types_by_name['MonitoringConfig'] = _MONITORINGCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PrometheusConfig = _reflection.GeneratedProtocolMessageType('PrometheusConfig', (_message.Message,), {
  'DESCRIPTOR' : _PROMETHEUSCONFIG,
  '__module__' : 'tensorflow_serving.config.monitoring_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.PrometheusConfig)
  })
_sym_db.RegisterMessage(PrometheusConfig)

MonitoringConfig = _reflection.GeneratedProtocolMessageType('MonitoringConfig', (_message.Message,), {
  'DESCRIPTOR' : _MONITORINGCONFIG,
  '__module__' : 'tensorflow_serving.config.monitoring_config_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.MonitoringConfig)
  })
_sym_db.RegisterMessage(MonitoringConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
