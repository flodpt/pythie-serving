# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/graph_debug_info.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/graph_debug_info.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=b'\n\030org.tensorflow.frameworkB\024GraphDebugInfoProtosP\001ZHgithub.com/tensorflow/tensorflow/tensorflow/go/core/core_protos_go_proto\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n/tensorflow/core/protobuf/graph_debug_info.proto\x12\ntensorflow\"\xd5\x02\n\x0eGraphDebugInfo\x12\r\n\x05\x66iles\x18\x01 \x03(\t\x12\x36\n\x06traces\x18\x02 \x03(\x0b\x32&.tensorflow.GraphDebugInfo.TracesEntry\x1aX\n\x0b\x46ileLineCol\x12\x12\n\nfile_index\x18\x01 \x01(\x05\x12\x0c\n\x04line\x18\x02 \x01(\x05\x12\x0b\n\x03\x63ol\x18\x03 \x01(\x05\x12\x0c\n\x04\x66unc\x18\x04 \x01(\t\x12\x0c\n\x04\x63ode\x18\x05 \x01(\t\x1aL\n\nStackTrace\x12>\n\x0e\x66ile_line_cols\x18\x01 \x03(\x0b\x32&.tensorflow.GraphDebugInfo.FileLineCol\x1aT\n\x0bTracesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x34\n\x05value\x18\x02 \x01(\x0b\x32%.tensorflow.GraphDebugInfo.StackTrace:\x02\x38\x01\x42\x7f\n\x18org.tensorflow.frameworkB\x14GraphDebugInfoProtosP\x01ZHgithub.com/tensorflow/tensorflow/tensorflow/go/core/core_protos_go_proto\xf8\x01\x01\x62\x06proto3'
)




_GRAPHDEBUGINFO_FILELINECOL = _descriptor.Descriptor(
  name='FileLineCol',
  full_name='tensorflow.GraphDebugInfo.FileLineCol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_index', full_name='tensorflow.GraphDebugInfo.FileLineCol.file_index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='tensorflow.GraphDebugInfo.FileLineCol.line', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='col', full_name='tensorflow.GraphDebugInfo.FileLineCol.col', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='func', full_name='tensorflow.GraphDebugInfo.FileLineCol.func', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='tensorflow.GraphDebugInfo.FileLineCol.code', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=153,
  serialized_end=241,
)

_GRAPHDEBUGINFO_STACKTRACE = _descriptor.Descriptor(
  name='StackTrace',
  full_name='tensorflow.GraphDebugInfo.StackTrace',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_line_cols', full_name='tensorflow.GraphDebugInfo.StackTrace.file_line_cols', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=243,
  serialized_end=319,
)

_GRAPHDEBUGINFO_TRACESENTRY = _descriptor.Descriptor(
  name='TracesEntry',
  full_name='tensorflow.GraphDebugInfo.TracesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.GraphDebugInfo.TracesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.GraphDebugInfo.TracesEntry.value', index=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=405,
)

_GRAPHDEBUGINFO = _descriptor.Descriptor(
  name='GraphDebugInfo',
  full_name='tensorflow.GraphDebugInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='files', full_name='tensorflow.GraphDebugInfo.files', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='traces', full_name='tensorflow.GraphDebugInfo.traces', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GRAPHDEBUGINFO_FILELINECOL, _GRAPHDEBUGINFO_STACKTRACE, _GRAPHDEBUGINFO_TRACESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=405,
)

_GRAPHDEBUGINFO_FILELINECOL.containing_type = _GRAPHDEBUGINFO
_GRAPHDEBUGINFO_STACKTRACE.fields_by_name['file_line_cols'].message_type = _GRAPHDEBUGINFO_FILELINECOL
_GRAPHDEBUGINFO_STACKTRACE.containing_type = _GRAPHDEBUGINFO
_GRAPHDEBUGINFO_TRACESENTRY.fields_by_name['value'].message_type = _GRAPHDEBUGINFO_STACKTRACE
_GRAPHDEBUGINFO_TRACESENTRY.containing_type = _GRAPHDEBUGINFO
_GRAPHDEBUGINFO.fields_by_name['traces'].message_type = _GRAPHDEBUGINFO_TRACESENTRY
DESCRIPTOR.message_types_by_name['GraphDebugInfo'] = _GRAPHDEBUGINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GraphDebugInfo = _reflection.GeneratedProtocolMessageType('GraphDebugInfo', (_message.Message,), {

  'FileLineCol' : _reflection.GeneratedProtocolMessageType('FileLineCol', (_message.Message,), {
    'DESCRIPTOR' : _GRAPHDEBUGINFO_FILELINECOL,
    '__module__' : 'tensorflow.core.protobuf.graph_debug_info_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.GraphDebugInfo.FileLineCol)
    })
  ,

  'StackTrace' : _reflection.GeneratedProtocolMessageType('StackTrace', (_message.Message,), {
    'DESCRIPTOR' : _GRAPHDEBUGINFO_STACKTRACE,
    '__module__' : 'tensorflow.core.protobuf.graph_debug_info_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.GraphDebugInfo.StackTrace)
    })
  ,

  'TracesEntry' : _reflection.GeneratedProtocolMessageType('TracesEntry', (_message.Message,), {
    'DESCRIPTOR' : _GRAPHDEBUGINFO_TRACESENTRY,
    '__module__' : 'tensorflow.core.protobuf.graph_debug_info_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.GraphDebugInfo.TracesEntry)
    })
  ,
  'DESCRIPTOR' : _GRAPHDEBUGINFO,
  '__module__' : 'tensorflow.core.protobuf.graph_debug_info_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.GraphDebugInfo)
  })
_sym_db.RegisterMessage(GraphDebugInfo)
_sym_db.RegisterMessage(GraphDebugInfo.FileLineCol)
_sym_db.RegisterMessage(GraphDebugInfo.StackTrace)
_sym_db.RegisterMessage(GraphDebugInfo.TracesEntry)


DESCRIPTOR._options = None
_GRAPHDEBUGINFO_TRACESENTRY._options = None
# @@protoc_insertion_point(module_scope)
