# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/tpu/kernels/tpu_executable_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.compiler.xla.service import hlo_pb2 as tensorflow_dot_compiler_dot_xla_dot_service_dot_hlo__pb2
from pythie_serving.tensorflow_proto.tensorflow.compiler.xla import xla_data_pb2 as tensorflow_dot_compiler_dot_xla_dot_xla__data__pb2
from pythie_serving.tensorflow_proto.tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/tpu/kernels/tpu_executable_info.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5tensorflow/core/tpu/kernels/tpu_executable_info.proto\x12\ntensorflow\x1a)tensorflow/compiler/xla/service/hlo.proto\x1a&tensorflow/compiler/xla/xla_data.proto\x1a,tensorflow/core/framework/tensor_shape.proto\"\x82\x04\n\x16TPUExecutableInfoProto\x12%\n\x0cinput_shapes\x18\x02 \x03(\x0b\x32\x0f.xla.ShapeProto\x12%\n\x0coutput_shape\x18\x03 \x01(\x0b\x32\x0f.xla.ShapeProto\x12M\n\x16\x64ynamic_output_indices\x18\x0b \x03(\x0b\x32-.tensorflow.TPUExecutableInfoProto.ShapeIndex\x12L\n\x10variable_indices\x18\n \x03(\x0b\x32\x32.tensorflow.TPUExecutableInfoProto.UpdateIndexPair\x12:\n\x14output_tensor_shapes\x18\x08 \x03(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12(\n\x0esession_module\x18\x05 \x01(\x0b\x32\x10.xla.HloSnapshot\x12\x35\n\x11\x64\x65vice_assignment\x18\x06 \x01(\x0b\x32\x1a.xla.DeviceAssignmentProto\x1a\x31\n\x0fUpdateIndexPair\x12\r\n\x05index\x18\x01 \x01(\x05\x12\x0f\n\x07updated\x18\x02 \x01(\x08\x1a\x1b\n\nShapeIndex\x12\r\n\x05index\x18\x01 \x03(\x05J\x04\x08\x01\x10\x02J\x04\x08\x07\x10\x08J\x04\x08\x04\x10\x05\"\xd7\x02\n\x14TPUHostTransferProto\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x03\x12\x45\n\tdirection\x18\x02 \x01(\x0e\x32\x32.tensorflow.TPUHostTransferProto.TransferDirection\x12\x0b\n\x03key\x18\x03 \x01(\t\x12\x1a\n\x12nested_while_level\x18\x04 \x01(\x03\x12\x1e\n\x05shape\x18\x05 \x01(\x0b\x32\x0f.xla.ShapeProto\x12\x15\n\rbuffer_offset\x18\x06 \x01(\x03\x12)\n\roriginal_type\x18\x07 \x01(\x0e\x32\x12.xla.PrimitiveType\x12\x15\n\ris_lower_bits\x18\x08 \x01(\x08\"E\n\x11TransferDirection\x12\x08\n\x04NONE\x10\x00\x12\x12\n\x0e\x44\x45VICE_TO_HOST\x10\x01\x12\x12\n\x0eHOST_TO_DEVICE\x10\x02\"T\n\x18TPUHostTransferInfoProto\x12\x38\n\x0ehost_transfers\x18\x01 \x03(\x0b\x32 .tensorflow.TPUHostTransferProtob\x06proto3'
  ,
  dependencies=[tensorflow_dot_compiler_dot_xla_dot_service_dot_hlo__pb2.DESCRIPTOR,tensorflow_dot_compiler_dot_xla_dot_xla__data__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,])



_TPUHOSTTRANSFERPROTO_TRANSFERDIRECTION = _descriptor.EnumDescriptor(
  name='TransferDirection',
  full_name='tensorflow.TPUHostTransferProto.TransferDirection',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEVICE_TO_HOST', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOST_TO_DEVICE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=990,
  serialized_end=1059,
)
_sym_db.RegisterEnumDescriptor(_TPUHOSTTRANSFERPROTO_TRANSFERDIRECTION)


_TPUEXECUTABLEINFOPROTO_UPDATEINDEXPAIR = _descriptor.Descriptor(
  name='UpdateIndexPair',
  full_name='tensorflow.TPUExecutableInfoProto.UpdateIndexPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='tensorflow.TPUExecutableInfoProto.UpdateIndexPair.index', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updated', full_name='tensorflow.TPUExecutableInfoProto.UpdateIndexPair.updated', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=617,
  serialized_end=666,
)

_TPUEXECUTABLEINFOPROTO_SHAPEINDEX = _descriptor.Descriptor(
  name='ShapeIndex',
  full_name='tensorflow.TPUExecutableInfoProto.ShapeIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='tensorflow.TPUExecutableInfoProto.ShapeIndex.index', index=0,
      number=1, type=5, cpp_type=1, label=3,
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
  serialized_start=668,
  serialized_end=695,
)

_TPUEXECUTABLEINFOPROTO = _descriptor.Descriptor(
  name='TPUExecutableInfoProto',
  full_name='tensorflow.TPUExecutableInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_shapes', full_name='tensorflow.TPUExecutableInfoProto.input_shapes', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_shape', full_name='tensorflow.TPUExecutableInfoProto.output_shape', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dynamic_output_indices', full_name='tensorflow.TPUExecutableInfoProto.dynamic_output_indices', index=2,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='variable_indices', full_name='tensorflow.TPUExecutableInfoProto.variable_indices', index=3,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_tensor_shapes', full_name='tensorflow.TPUExecutableInfoProto.output_tensor_shapes', index=4,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_module', full_name='tensorflow.TPUExecutableInfoProto.session_module', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_assignment', full_name='tensorflow.TPUExecutableInfoProto.device_assignment', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TPUEXECUTABLEINFOPROTO_UPDATEINDEXPAIR, _TPUEXECUTABLEINFOPROTO_SHAPEINDEX, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=713,
)


_TPUHOSTTRANSFERPROTO = _descriptor.Descriptor(
  name='TPUHostTransferProto',
  full_name='tensorflow.TPUHostTransferProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='tensorflow.TPUHostTransferProto.channel', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='direction', full_name='tensorflow.TPUHostTransferProto.direction', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.TPUHostTransferProto.key', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nested_while_level', full_name='tensorflow.TPUHostTransferProto.nested_while_level', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow.TPUHostTransferProto.shape', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buffer_offset', full_name='tensorflow.TPUHostTransferProto.buffer_offset', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='original_type', full_name='tensorflow.TPUHostTransferProto.original_type', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_lower_bits', full_name='tensorflow.TPUHostTransferProto.is_lower_bits', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TPUHOSTTRANSFERPROTO_TRANSFERDIRECTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=1059,
)


_TPUHOSTTRANSFERINFOPROTO = _descriptor.Descriptor(
  name='TPUHostTransferInfoProto',
  full_name='tensorflow.TPUHostTransferInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='host_transfers', full_name='tensorflow.TPUHostTransferInfoProto.host_transfers', index=0,
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
  serialized_start=1061,
  serialized_end=1145,
)

_TPUEXECUTABLEINFOPROTO_UPDATEINDEXPAIR.containing_type = _TPUEXECUTABLEINFOPROTO
_TPUEXECUTABLEINFOPROTO_SHAPEINDEX.containing_type = _TPUEXECUTABLEINFOPROTO
_TPUEXECUTABLEINFOPROTO.fields_by_name['input_shapes'].message_type = tensorflow_dot_compiler_dot_xla_dot_xla__data__pb2._SHAPEPROTO
_TPUEXECUTABLEINFOPROTO.fields_by_name['output_shape'].message_type = tensorflow_dot_compiler_dot_xla_dot_xla__data__pb2._SHAPEPROTO
_TPUEXECUTABLEINFOPROTO.fields_by_name['dynamic_output_indices'].message_type = _TPUEXECUTABLEINFOPROTO_SHAPEINDEX
_TPUEXECUTABLEINFOPROTO.fields_by_name['variable_indices'].message_type = _TPUEXECUTABLEINFOPROTO_UPDATEINDEXPAIR
_TPUEXECUTABLEINFOPROTO.fields_by_name['output_tensor_shapes'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_TPUEXECUTABLEINFOPROTO.fields_by_name['session_module'].message_type = tensorflow_dot_compiler_dot_xla_dot_service_dot_hlo__pb2._HLOSNAPSHOT
_TPUEXECUTABLEINFOPROTO.fields_by_name['device_assignment'].message_type = tensorflow_dot_compiler_dot_xla_dot_xla__data__pb2._DEVICEASSIGNMENTPROTO
_TPUHOSTTRANSFERPROTO.fields_by_name['direction'].enum_type = _TPUHOSTTRANSFERPROTO_TRANSFERDIRECTION
_TPUHOSTTRANSFERPROTO.fields_by_name['shape'].message_type = tensorflow_dot_compiler_dot_xla_dot_xla__data__pb2._SHAPEPROTO
_TPUHOSTTRANSFERPROTO.fields_by_name['original_type'].enum_type = tensorflow_dot_compiler_dot_xla_dot_xla__data__pb2._PRIMITIVETYPE
_TPUHOSTTRANSFERPROTO_TRANSFERDIRECTION.containing_type = _TPUHOSTTRANSFERPROTO
_TPUHOSTTRANSFERINFOPROTO.fields_by_name['host_transfers'].message_type = _TPUHOSTTRANSFERPROTO
DESCRIPTOR.message_types_by_name['TPUExecutableInfoProto'] = _TPUEXECUTABLEINFOPROTO
DESCRIPTOR.message_types_by_name['TPUHostTransferProto'] = _TPUHOSTTRANSFERPROTO
DESCRIPTOR.message_types_by_name['TPUHostTransferInfoProto'] = _TPUHOSTTRANSFERINFOPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TPUExecutableInfoProto = _reflection.GeneratedProtocolMessageType('TPUExecutableInfoProto', (_message.Message,), {

  'UpdateIndexPair' : _reflection.GeneratedProtocolMessageType('UpdateIndexPair', (_message.Message,), {
    'DESCRIPTOR' : _TPUEXECUTABLEINFOPROTO_UPDATEINDEXPAIR,
    '__module__' : 'tensorflow.core.tpu.kernels.tpu_executable_info_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.TPUExecutableInfoProto.UpdateIndexPair)
    })
  ,

  'ShapeIndex' : _reflection.GeneratedProtocolMessageType('ShapeIndex', (_message.Message,), {
    'DESCRIPTOR' : _TPUEXECUTABLEINFOPROTO_SHAPEINDEX,
    '__module__' : 'tensorflow.core.tpu.kernels.tpu_executable_info_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.TPUExecutableInfoProto.ShapeIndex)
    })
  ,
  'DESCRIPTOR' : _TPUEXECUTABLEINFOPROTO,
  '__module__' : 'tensorflow.core.tpu.kernels.tpu_executable_info_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.TPUExecutableInfoProto)
  })
_sym_db.RegisterMessage(TPUExecutableInfoProto)
_sym_db.RegisterMessage(TPUExecutableInfoProto.UpdateIndexPair)
_sym_db.RegisterMessage(TPUExecutableInfoProto.ShapeIndex)

TPUHostTransferProto = _reflection.GeneratedProtocolMessageType('TPUHostTransferProto', (_message.Message,), {
  'DESCRIPTOR' : _TPUHOSTTRANSFERPROTO,
  '__module__' : 'tensorflow.core.tpu.kernels.tpu_executable_info_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.TPUHostTransferProto)
  })
_sym_db.RegisterMessage(TPUHostTransferProto)

TPUHostTransferInfoProto = _reflection.GeneratedProtocolMessageType('TPUHostTransferInfoProto', (_message.Message,), {
  'DESCRIPTOR' : _TPUHOSTTRANSFERINFOPROTO,
  '__module__' : 'tensorflow.core.tpu.kernels.tpu_executable_info_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.TPUHostTransferInfoProto)
  })
_sym_db.RegisterMessage(TPUHostTransferInfoProto)


# @@protoc_insertion_point(module_scope)
