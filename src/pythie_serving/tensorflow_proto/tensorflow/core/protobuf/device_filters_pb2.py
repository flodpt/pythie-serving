# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/device_filters.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/device_filters.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=b'\n\032org.tensorflow.distruntimeB\023DeviceFiltersProtosP\001ZHgithub.com/tensorflow/tensorflow/tensorflow/go/core/core_protos_go_proto\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-tensorflow/core/protobuf/device_filters.proto\x12\ntensorflow\"+\n\x11TaskDeviceFilters\x12\x16\n\x0e\x64\x65vice_filters\x18\x01 \x03(\t\"\xa5\x01\n\x10JobDeviceFilters\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x36\n\x05tasks\x18\x02 \x03(\x0b\x32\'.tensorflow.JobDeviceFilters.TasksEntry\x1aK\n\nTasksEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.tensorflow.TaskDeviceFilters:\x02\x38\x01\"B\n\x14\x43lusterDeviceFilters\x12*\n\x04jobs\x18\x01 \x03(\x0b\x32\x1c.tensorflow.JobDeviceFiltersB\x80\x01\n\x1aorg.tensorflow.distruntimeB\x13\x44\x65viceFiltersProtosP\x01ZHgithub.com/tensorflow/tensorflow/tensorflow/go/core/core_protos_go_proto\xf8\x01\x01\x62\x06proto3'
)




_TASKDEVICEFILTERS = _descriptor.Descriptor(
  name='TaskDeviceFilters',
  full_name='tensorflow.TaskDeviceFilters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_filters', full_name='tensorflow.TaskDeviceFilters.device_filters', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=61,
  serialized_end=104,
)


_JOBDEVICEFILTERS_TASKSENTRY = _descriptor.Descriptor(
  name='TasksEntry',
  full_name='tensorflow.JobDeviceFilters.TasksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.JobDeviceFilters.TasksEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.JobDeviceFilters.TasksEntry.value', index=1,
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
  serialized_start=197,
  serialized_end=272,
)

_JOBDEVICEFILTERS = _descriptor.Descriptor(
  name='JobDeviceFilters',
  full_name='tensorflow.JobDeviceFilters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.JobDeviceFilters.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='tensorflow.JobDeviceFilters.tasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_JOBDEVICEFILTERS_TASKSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=272,
)


_CLUSTERDEVICEFILTERS = _descriptor.Descriptor(
  name='ClusterDeviceFilters',
  full_name='tensorflow.ClusterDeviceFilters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='jobs', full_name='tensorflow.ClusterDeviceFilters.jobs', index=0,
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
  serialized_start=274,
  serialized_end=340,
)

_JOBDEVICEFILTERS_TASKSENTRY.fields_by_name['value'].message_type = _TASKDEVICEFILTERS
_JOBDEVICEFILTERS_TASKSENTRY.containing_type = _JOBDEVICEFILTERS
_JOBDEVICEFILTERS.fields_by_name['tasks'].message_type = _JOBDEVICEFILTERS_TASKSENTRY
_CLUSTERDEVICEFILTERS.fields_by_name['jobs'].message_type = _JOBDEVICEFILTERS
DESCRIPTOR.message_types_by_name['TaskDeviceFilters'] = _TASKDEVICEFILTERS
DESCRIPTOR.message_types_by_name['JobDeviceFilters'] = _JOBDEVICEFILTERS
DESCRIPTOR.message_types_by_name['ClusterDeviceFilters'] = _CLUSTERDEVICEFILTERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TaskDeviceFilters = _reflection.GeneratedProtocolMessageType('TaskDeviceFilters', (_message.Message,), {
  'DESCRIPTOR' : _TASKDEVICEFILTERS,
  '__module__' : 'tensorflow.core.protobuf.device_filters_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.TaskDeviceFilters)
  })
_sym_db.RegisterMessage(TaskDeviceFilters)

JobDeviceFilters = _reflection.GeneratedProtocolMessageType('JobDeviceFilters', (_message.Message,), {

  'TasksEntry' : _reflection.GeneratedProtocolMessageType('TasksEntry', (_message.Message,), {
    'DESCRIPTOR' : _JOBDEVICEFILTERS_TASKSENTRY,
    '__module__' : 'tensorflow.core.protobuf.device_filters_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.JobDeviceFilters.TasksEntry)
    })
  ,
  'DESCRIPTOR' : _JOBDEVICEFILTERS,
  '__module__' : 'tensorflow.core.protobuf.device_filters_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.JobDeviceFilters)
  })
_sym_db.RegisterMessage(JobDeviceFilters)
_sym_db.RegisterMessage(JobDeviceFilters.TasksEntry)

ClusterDeviceFilters = _reflection.GeneratedProtocolMessageType('ClusterDeviceFilters', (_message.Message,), {
  'DESCRIPTOR' : _CLUSTERDEVICEFILTERS,
  '__module__' : 'tensorflow.core.protobuf.device_filters_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ClusterDeviceFilters)
  })
_sym_db.RegisterMessage(ClusterDeviceFilters)


DESCRIPTOR._options = None
_JOBDEVICEFILTERS_TASKSENTRY._options = None
# @@protoc_insertion_point(module_scope)
