# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/profiler/protobuf/tf_function.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/profiler/protobuf/tf_function.proto',
  package='tensorflow.profiler',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3tensorflow/core/profiler/protobuf/tf_function.proto\x12\x13tensorflow.profiler\"8\n\x11TfFunctionMetrics\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\x12\x14\n\x0cself_time_ps\x18\x02 \x01(\x04\"\x9b\x02\n\nTfFunction\x12=\n\x07metrics\x18\x01 \x03(\x0b\x32,.tensorflow.profiler.TfFunction.MetricsEntry\x12\x1b\n\x13total_tracing_count\x18\x02 \x01(\x03\x12\x39\n\x08\x63ompiler\x18\x03 \x01(\x0e\x32\'.tensorflow.profiler.TfFunctionCompiler\x12\x1e\n\x16\x65xpensive_call_percent\x18\x04 \x01(\x01\x1aV\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.tensorflow.profiler.TfFunctionMetrics:\x02\x38\x01\"\xad\x01\n\x0cTfFunctionDb\x12H\n\x0ctf_functions\x18\x01 \x03(\x0b\x32\x32.tensorflow.profiler.TfFunctionDb.TfFunctionsEntry\x1aS\n\x10TfFunctionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.tensorflow.profiler.TfFunction:\x02\x38\x01*t\n\x17TfFunctionExecutionMode\x12\x10\n\x0cINVALID_MODE\x10\x00\x12\x0e\n\nEAGER_MODE\x10\x01\x12\x0f\n\x0bTRACED_MODE\x10\x02\x12\x13\n\x0fNOT_TRACED_MODE\x10\x03\x12\x11\n\rCONCRETE_MODE\x10\x04*w\n\x12TfFunctionCompiler\x12\x14\n\x10INVALID_COMPILER\x10\x00\x12\x12\n\x0eOTHER_COMPILER\x10\x01\x12\x12\n\x0eMIXED_COMPILER\x10\x02\x12\x10\n\x0cXLA_COMPILER\x10\x03\x12\x11\n\rMLIR_COMPILER\x10\x04\x62\x06proto3'
)

_TFFUNCTIONEXECUTIONMODE = _descriptor.EnumDescriptor(
  name='TfFunctionExecutionMode',
  full_name='tensorflow.profiler.TfFunctionExecutionMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_MODE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EAGER_MODE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRACED_MODE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_TRACED_MODE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONCRETE_MODE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=596,
  serialized_end=712,
)
_sym_db.RegisterEnumDescriptor(_TFFUNCTIONEXECUTIONMODE)

TfFunctionExecutionMode = enum_type_wrapper.EnumTypeWrapper(_TFFUNCTIONEXECUTIONMODE)
_TFFUNCTIONCOMPILER = _descriptor.EnumDescriptor(
  name='TfFunctionCompiler',
  full_name='tensorflow.profiler.TfFunctionCompiler',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_COMPILER', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OTHER_COMPILER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIXED_COMPILER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='XLA_COMPILER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MLIR_COMPILER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=714,
  serialized_end=833,
)
_sym_db.RegisterEnumDescriptor(_TFFUNCTIONCOMPILER)

TfFunctionCompiler = enum_type_wrapper.EnumTypeWrapper(_TFFUNCTIONCOMPILER)
INVALID_MODE = 0
EAGER_MODE = 1
TRACED_MODE = 2
NOT_TRACED_MODE = 3
CONCRETE_MODE = 4
INVALID_COMPILER = 0
OTHER_COMPILER = 1
MIXED_COMPILER = 2
XLA_COMPILER = 3
MLIR_COMPILER = 4



_TFFUNCTIONMETRICS = _descriptor.Descriptor(
  name='TfFunctionMetrics',
  full_name='tensorflow.profiler.TfFunctionMetrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='count', full_name='tensorflow.profiler.TfFunctionMetrics.count', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='self_time_ps', full_name='tensorflow.profiler.TfFunctionMetrics.self_time_ps', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=76,
  serialized_end=132,
)


_TFFUNCTION_METRICSENTRY = _descriptor.Descriptor(
  name='MetricsEntry',
  full_name='tensorflow.profiler.TfFunction.MetricsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.profiler.TfFunction.MetricsEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.profiler.TfFunction.MetricsEntry.value', index=1,
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
  serialized_start=332,
  serialized_end=418,
)

_TFFUNCTION = _descriptor.Descriptor(
  name='TfFunction',
  full_name='tensorflow.profiler.TfFunction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='tensorflow.profiler.TfFunction.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_tracing_count', full_name='tensorflow.profiler.TfFunction.total_tracing_count', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compiler', full_name='tensorflow.profiler.TfFunction.compiler', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expensive_call_percent', full_name='tensorflow.profiler.TfFunction.expensive_call_percent', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TFFUNCTION_METRICSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=418,
)


_TFFUNCTIONDB_TFFUNCTIONSENTRY = _descriptor.Descriptor(
  name='TfFunctionsEntry',
  full_name='tensorflow.profiler.TfFunctionDb.TfFunctionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.profiler.TfFunctionDb.TfFunctionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.profiler.TfFunctionDb.TfFunctionsEntry.value', index=1,
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
  serialized_start=511,
  serialized_end=594,
)

_TFFUNCTIONDB = _descriptor.Descriptor(
  name='TfFunctionDb',
  full_name='tensorflow.profiler.TfFunctionDb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tf_functions', full_name='tensorflow.profiler.TfFunctionDb.tf_functions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TFFUNCTIONDB_TFFUNCTIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=421,
  serialized_end=594,
)

_TFFUNCTION_METRICSENTRY.fields_by_name['value'].message_type = _TFFUNCTIONMETRICS
_TFFUNCTION_METRICSENTRY.containing_type = _TFFUNCTION
_TFFUNCTION.fields_by_name['metrics'].message_type = _TFFUNCTION_METRICSENTRY
_TFFUNCTION.fields_by_name['compiler'].enum_type = _TFFUNCTIONCOMPILER
_TFFUNCTIONDB_TFFUNCTIONSENTRY.fields_by_name['value'].message_type = _TFFUNCTION
_TFFUNCTIONDB_TFFUNCTIONSENTRY.containing_type = _TFFUNCTIONDB
_TFFUNCTIONDB.fields_by_name['tf_functions'].message_type = _TFFUNCTIONDB_TFFUNCTIONSENTRY
DESCRIPTOR.message_types_by_name['TfFunctionMetrics'] = _TFFUNCTIONMETRICS
DESCRIPTOR.message_types_by_name['TfFunction'] = _TFFUNCTION
DESCRIPTOR.message_types_by_name['TfFunctionDb'] = _TFFUNCTIONDB
DESCRIPTOR.enum_types_by_name['TfFunctionExecutionMode'] = _TFFUNCTIONEXECUTIONMODE
DESCRIPTOR.enum_types_by_name['TfFunctionCompiler'] = _TFFUNCTIONCOMPILER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TfFunctionMetrics = _reflection.GeneratedProtocolMessageType('TfFunctionMetrics', (_message.Message,), {
  'DESCRIPTOR' : _TFFUNCTIONMETRICS,
  '__module__' : 'tensorflow.core.profiler.protobuf.tf_function_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.TfFunctionMetrics)
  })
_sym_db.RegisterMessage(TfFunctionMetrics)

TfFunction = _reflection.GeneratedProtocolMessageType('TfFunction', (_message.Message,), {

  'MetricsEntry' : _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TFFUNCTION_METRICSENTRY,
    '__module__' : 'tensorflow.core.profiler.protobuf.tf_function_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.profiler.TfFunction.MetricsEntry)
    })
  ,
  'DESCRIPTOR' : _TFFUNCTION,
  '__module__' : 'tensorflow.core.profiler.protobuf.tf_function_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.TfFunction)
  })
_sym_db.RegisterMessage(TfFunction)
_sym_db.RegisterMessage(TfFunction.MetricsEntry)

TfFunctionDb = _reflection.GeneratedProtocolMessageType('TfFunctionDb', (_message.Message,), {

  'TfFunctionsEntry' : _reflection.GeneratedProtocolMessageType('TfFunctionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TFFUNCTIONDB_TFFUNCTIONSENTRY,
    '__module__' : 'tensorflow.core.profiler.protobuf.tf_function_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.profiler.TfFunctionDb.TfFunctionsEntry)
    })
  ,
  'DESCRIPTOR' : _TFFUNCTIONDB,
  '__module__' : 'tensorflow.core.profiler.protobuf.tf_function_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.profiler.TfFunctionDb)
  })
_sym_db.RegisterMessage(TfFunctionDb)
_sym_db.RegisterMessage(TfFunctionDb.TfFunctionsEntry)


_TFFUNCTION_METRICSENTRY._options = None
_TFFUNCTIONDB_TFFUNCTIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
