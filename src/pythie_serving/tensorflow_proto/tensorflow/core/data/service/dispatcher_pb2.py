# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/data/service/dispatcher.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow.core.data.service import common_pb2 as tensorflow_dot_core_dot_data_dot_service_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/data/service/dispatcher.proto',
  package='tensorflow.data',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-tensorflow/core/data/service/dispatcher.proto\x12\x0ftensorflow.data\x1a)tensorflow/core/data/service/common.proto\"/\n\x15RegisterWorkerRequest\x12\x16\n\x0eworker_address\x18\x01 \x01(\t\"T\n\x16RegisterWorkerResponse\x12\x11\n\tworker_id\x18\x01 \x01(\x03\x12\'\n\x05tasks\x18\x02 \x03(\x0b\x32\x18.tensorflow.data.TaskDef\"2\n\x0cTaskProgress\x12\x0f\n\x07task_id\x18\x01 \x01(\x03\x12\x11\n\tcompleted\x18\x02 \x01(\x08\"X\n\x13WorkerUpdateRequest\x12\x11\n\tworker_id\x18\x01 \x01(\x03\x12.\n\x07updates\x18\x02 \x03(\x0b\x32\x1d.tensorflow.data.TaskProgress\"\x16\n\x14WorkerUpdateResponse\"K\n\x1bGetOrRegisterDatasetRequest\x12,\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32\x1b.tensorflow.data.DatasetDef\"2\n\x1cGetOrRegisterDatasetResponse\x12\x12\n\ndataset_id\x18\x01 \x01(\x03\"c\n\x10\x43reateJobRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\x03\x12;\n\x0fprocessing_mode\x18\x02 \x01(\x0e\x32\".tensorflow.data.ProcessingModeDef\"#\n\x11\x43reateJobResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\x03\"\x92\x01\n\x15GetOrCreateJobRequest\x12\x12\n\ndataset_id\x18\x01 \x01(\x03\x12;\n\x0fprocessing_mode\x18\x02 \x01(\x0e\x32\".tensorflow.data.ProcessingModeDef\x12\x10\n\x08job_name\x18\x03 \x01(\t\x12\x16\n\x0ejob_name_index\x18\x04 \x01(\x03\"(\n\x16GetOrCreateJobResponse\x12\x0e\n\x06job_id\x18\x01 \x01(\x03\"!\n\x0fGetTasksRequest\x12\x0e\n\x06job_id\x18\x01 \x01(\x03\".\n\x08TaskInfo\x12\x16\n\x0eworker_address\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\"V\n\x10GetTasksResponse\x12,\n\ttask_info\x18\x01 \x03(\x0b\x32\x19.tensorflow.data.TaskInfo\x12\x14\n\x0cjob_finished\x18\x02 \x01(\x08\")\n\nWorkerInfo\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x03\"\x13\n\x11GetWorkersRequest\"B\n\x12GetWorkersResponse\x12,\n\x07workers\x18\x01 \x03(\x0b\x32\x1b.tensorflow.data.WorkerInfo*7\n\x11ProcessingModeDef\x12\x13\n\x0fPARALLEL_EPOCHS\x10\x00\x12\r\n\tONE_EPOCH\x10\x01\x32\xa7\x05\n\x11\x44ispatcherService\x12\x61\n\x0eRegisterWorker\x12&.tensorflow.data.RegisterWorkerRequest\x1a\'.tensorflow.data.RegisterWorkerResponse\x12[\n\x0cWorkerUpdate\x12$.tensorflow.data.WorkerUpdateRequest\x1a%.tensorflow.data.WorkerUpdateResponse\x12s\n\x14GetOrRegisterDataset\x12,.tensorflow.data.GetOrRegisterDatasetRequest\x1a-.tensorflow.data.GetOrRegisterDatasetResponse\x12\x61\n\x0eGetOrCreateJob\x12&.tensorflow.data.GetOrCreateJobRequest\x1a\'.tensorflow.data.GetOrCreateJobResponse\x12R\n\tCreateJob\x12!.tensorflow.data.CreateJobRequest\x1a\".tensorflow.data.CreateJobResponse\x12O\n\x08GetTasks\x12 .tensorflow.data.GetTasksRequest\x1a!.tensorflow.data.GetTasksResponse\x12U\n\nGetWorkers\x12\".tensorflow.data.GetWorkersRequest\x1a#.tensorflow.data.GetWorkersResponseb\x06proto3'
  ,
  dependencies=[tensorflow_dot_core_dot_data_dot_service_dot_common__pb2.DESCRIPTOR,])

_PROCESSINGMODEDEF = _descriptor.EnumDescriptor(
  name='ProcessingModeDef',
  full_name='tensorflow.data.ProcessingModeDef',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PARALLEL_EPOCHS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONE_EPOCH', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1171,
  serialized_end=1226,
)
_sym_db.RegisterEnumDescriptor(_PROCESSINGMODEDEF)

ProcessingModeDef = enum_type_wrapper.EnumTypeWrapper(_PROCESSINGMODEDEF)
PARALLEL_EPOCHS = 0
ONE_EPOCH = 1



_REGISTERWORKERREQUEST = _descriptor.Descriptor(
  name='RegisterWorkerRequest',
  full_name='tensorflow.data.RegisterWorkerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worker_address', full_name='tensorflow.data.RegisterWorkerRequest.worker_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=109,
  serialized_end=156,
)


_REGISTERWORKERRESPONSE = _descriptor.Descriptor(
  name='RegisterWorkerResponse',
  full_name='tensorflow.data.RegisterWorkerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worker_id', full_name='tensorflow.data.RegisterWorkerResponse.worker_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='tensorflow.data.RegisterWorkerResponse.tasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=158,
  serialized_end=242,
)


_TASKPROGRESS = _descriptor.Descriptor(
  name='TaskProgress',
  full_name='tensorflow.data.TaskProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='tensorflow.data.TaskProgress.task_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='completed', full_name='tensorflow.data.TaskProgress.completed', index=1,
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
  serialized_start=244,
  serialized_end=294,
)


_WORKERUPDATEREQUEST = _descriptor.Descriptor(
  name='WorkerUpdateRequest',
  full_name='tensorflow.data.WorkerUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worker_id', full_name='tensorflow.data.WorkerUpdateRequest.worker_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='updates', full_name='tensorflow.data.WorkerUpdateRequest.updates', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=296,
  serialized_end=384,
)


_WORKERUPDATERESPONSE = _descriptor.Descriptor(
  name='WorkerUpdateResponse',
  full_name='tensorflow.data.WorkerUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=386,
  serialized_end=408,
)


_GETORREGISTERDATASETREQUEST = _descriptor.Descriptor(
  name='GetOrRegisterDatasetRequest',
  full_name='tensorflow.data.GetOrRegisterDatasetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset', full_name='tensorflow.data.GetOrRegisterDatasetRequest.dataset', index=0,
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
  serialized_start=410,
  serialized_end=485,
)


_GETORREGISTERDATASETRESPONSE = _descriptor.Descriptor(
  name='GetOrRegisterDatasetResponse',
  full_name='tensorflow.data.GetOrRegisterDatasetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='tensorflow.data.GetOrRegisterDatasetResponse.dataset_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=487,
  serialized_end=537,
)


_CREATEJOBREQUEST = _descriptor.Descriptor(
  name='CreateJobRequest',
  full_name='tensorflow.data.CreateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='tensorflow.data.CreateJobRequest.dataset_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processing_mode', full_name='tensorflow.data.CreateJobRequest.processing_mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
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
  serialized_start=539,
  serialized_end=638,
)


_CREATEJOBRESPONSE = _descriptor.Descriptor(
  name='CreateJobResponse',
  full_name='tensorflow.data.CreateJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='tensorflow.data.CreateJobResponse.job_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=640,
  serialized_end=675,
)


_GETORCREATEJOBREQUEST = _descriptor.Descriptor(
  name='GetOrCreateJobRequest',
  full_name='tensorflow.data.GetOrCreateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='tensorflow.data.GetOrCreateJobRequest.dataset_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='processing_mode', full_name='tensorflow.data.GetOrCreateJobRequest.processing_mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_name', full_name='tensorflow.data.GetOrCreateJobRequest.job_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_name_index', full_name='tensorflow.data.GetOrCreateJobRequest.job_name_index', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=678,
  serialized_end=824,
)


_GETORCREATEJOBRESPONSE = _descriptor.Descriptor(
  name='GetOrCreateJobResponse',
  full_name='tensorflow.data.GetOrCreateJobResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='tensorflow.data.GetOrCreateJobResponse.job_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=826,
  serialized_end=866,
)


_GETTASKSREQUEST = _descriptor.Descriptor(
  name='GetTasksRequest',
  full_name='tensorflow.data.GetTasksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='tensorflow.data.GetTasksRequest.job_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=868,
  serialized_end=901,
)


_TASKINFO = _descriptor.Descriptor(
  name='TaskInfo',
  full_name='tensorflow.data.TaskInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='worker_address', full_name='tensorflow.data.TaskInfo.worker_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.data.TaskInfo.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=903,
  serialized_end=949,
)


_GETTASKSRESPONSE = _descriptor.Descriptor(
  name='GetTasksResponse',
  full_name='tensorflow.data.GetTasksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_info', full_name='tensorflow.data.GetTasksResponse.task_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='job_finished', full_name='tensorflow.data.GetTasksResponse.job_finished', index=1,
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
  serialized_start=951,
  serialized_end=1037,
)


_WORKERINFO = _descriptor.Descriptor(
  name='WorkerInfo',
  full_name='tensorflow.data.WorkerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='tensorflow.data.WorkerInfo.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='tensorflow.data.WorkerInfo.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=1039,
  serialized_end=1080,
)


_GETWORKERSREQUEST = _descriptor.Descriptor(
  name='GetWorkersRequest',
  full_name='tensorflow.data.GetWorkersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1082,
  serialized_end=1101,
)


_GETWORKERSRESPONSE = _descriptor.Descriptor(
  name='GetWorkersResponse',
  full_name='tensorflow.data.GetWorkersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='workers', full_name='tensorflow.data.GetWorkersResponse.workers', index=0,
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
  serialized_start=1103,
  serialized_end=1169,
)

_REGISTERWORKERRESPONSE.fields_by_name['tasks'].message_type = tensorflow_dot_core_dot_data_dot_service_dot_common__pb2._TASKDEF
_WORKERUPDATEREQUEST.fields_by_name['updates'].message_type = _TASKPROGRESS
_GETORREGISTERDATASETREQUEST.fields_by_name['dataset'].message_type = tensorflow_dot_core_dot_data_dot_service_dot_common__pb2._DATASETDEF
_CREATEJOBREQUEST.fields_by_name['processing_mode'].enum_type = _PROCESSINGMODEDEF
_GETORCREATEJOBREQUEST.fields_by_name['processing_mode'].enum_type = _PROCESSINGMODEDEF
_GETTASKSRESPONSE.fields_by_name['task_info'].message_type = _TASKINFO
_GETWORKERSRESPONSE.fields_by_name['workers'].message_type = _WORKERINFO
DESCRIPTOR.message_types_by_name['RegisterWorkerRequest'] = _REGISTERWORKERREQUEST
DESCRIPTOR.message_types_by_name['RegisterWorkerResponse'] = _REGISTERWORKERRESPONSE
DESCRIPTOR.message_types_by_name['TaskProgress'] = _TASKPROGRESS
DESCRIPTOR.message_types_by_name['WorkerUpdateRequest'] = _WORKERUPDATEREQUEST
DESCRIPTOR.message_types_by_name['WorkerUpdateResponse'] = _WORKERUPDATERESPONSE
DESCRIPTOR.message_types_by_name['GetOrRegisterDatasetRequest'] = _GETORREGISTERDATASETREQUEST
DESCRIPTOR.message_types_by_name['GetOrRegisterDatasetResponse'] = _GETORREGISTERDATASETRESPONSE
DESCRIPTOR.message_types_by_name['CreateJobRequest'] = _CREATEJOBREQUEST
DESCRIPTOR.message_types_by_name['CreateJobResponse'] = _CREATEJOBRESPONSE
DESCRIPTOR.message_types_by_name['GetOrCreateJobRequest'] = _GETORCREATEJOBREQUEST
DESCRIPTOR.message_types_by_name['GetOrCreateJobResponse'] = _GETORCREATEJOBRESPONSE
DESCRIPTOR.message_types_by_name['GetTasksRequest'] = _GETTASKSREQUEST
DESCRIPTOR.message_types_by_name['TaskInfo'] = _TASKINFO
DESCRIPTOR.message_types_by_name['GetTasksResponse'] = _GETTASKSRESPONSE
DESCRIPTOR.message_types_by_name['WorkerInfo'] = _WORKERINFO
DESCRIPTOR.message_types_by_name['GetWorkersRequest'] = _GETWORKERSREQUEST
DESCRIPTOR.message_types_by_name['GetWorkersResponse'] = _GETWORKERSRESPONSE
DESCRIPTOR.enum_types_by_name['ProcessingModeDef'] = _PROCESSINGMODEDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterWorkerRequest = _reflection.GeneratedProtocolMessageType('RegisterWorkerRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERWORKERREQUEST,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.RegisterWorkerRequest)
  })
_sym_db.RegisterMessage(RegisterWorkerRequest)

RegisterWorkerResponse = _reflection.GeneratedProtocolMessageType('RegisterWorkerResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERWORKERRESPONSE,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.RegisterWorkerResponse)
  })
_sym_db.RegisterMessage(RegisterWorkerResponse)

TaskProgress = _reflection.GeneratedProtocolMessageType('TaskProgress', (_message.Message,), {
  'DESCRIPTOR' : _TASKPROGRESS,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.TaskProgress)
  })
_sym_db.RegisterMessage(TaskProgress)

WorkerUpdateRequest = _reflection.GeneratedProtocolMessageType('WorkerUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _WORKERUPDATEREQUEST,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.WorkerUpdateRequest)
  })
_sym_db.RegisterMessage(WorkerUpdateRequest)

WorkerUpdateResponse = _reflection.GeneratedProtocolMessageType('WorkerUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _WORKERUPDATERESPONSE,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.WorkerUpdateResponse)
  })
_sym_db.RegisterMessage(WorkerUpdateResponse)

GetOrRegisterDatasetRequest = _reflection.GeneratedProtocolMessageType('GetOrRegisterDatasetRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORREGISTERDATASETREQUEST,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.GetOrRegisterDatasetRequest)
  })
_sym_db.RegisterMessage(GetOrRegisterDatasetRequest)

GetOrRegisterDatasetResponse = _reflection.GeneratedProtocolMessageType('GetOrRegisterDatasetResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORREGISTERDATASETRESPONSE,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.GetOrRegisterDatasetResponse)
  })
_sym_db.RegisterMessage(GetOrRegisterDatasetResponse)

CreateJobRequest = _reflection.GeneratedProtocolMessageType('CreateJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEJOBREQUEST,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.CreateJobRequest)
  })
_sym_db.RegisterMessage(CreateJobRequest)

CreateJobResponse = _reflection.GeneratedProtocolMessageType('CreateJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEJOBRESPONSE,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.CreateJobResponse)
  })
_sym_db.RegisterMessage(CreateJobResponse)

GetOrCreateJobRequest = _reflection.GeneratedProtocolMessageType('GetOrCreateJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORCREATEJOBREQUEST,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.GetOrCreateJobRequest)
  })
_sym_db.RegisterMessage(GetOrCreateJobRequest)

GetOrCreateJobResponse = _reflection.GeneratedProtocolMessageType('GetOrCreateJobResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETORCREATEJOBRESPONSE,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.GetOrCreateJobResponse)
  })
_sym_db.RegisterMessage(GetOrCreateJobResponse)

GetTasksRequest = _reflection.GeneratedProtocolMessageType('GetTasksRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKSREQUEST,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.GetTasksRequest)
  })
_sym_db.RegisterMessage(GetTasksRequest)

TaskInfo = _reflection.GeneratedProtocolMessageType('TaskInfo', (_message.Message,), {
  'DESCRIPTOR' : _TASKINFO,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.TaskInfo)
  })
_sym_db.RegisterMessage(TaskInfo)

GetTasksResponse = _reflection.GeneratedProtocolMessageType('GetTasksResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTASKSRESPONSE,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.GetTasksResponse)
  })
_sym_db.RegisterMessage(GetTasksResponse)

WorkerInfo = _reflection.GeneratedProtocolMessageType('WorkerInfo', (_message.Message,), {
  'DESCRIPTOR' : _WORKERINFO,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.WorkerInfo)
  })
_sym_db.RegisterMessage(WorkerInfo)

GetWorkersRequest = _reflection.GeneratedProtocolMessageType('GetWorkersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETWORKERSREQUEST,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.GetWorkersRequest)
  })
_sym_db.RegisterMessage(GetWorkersRequest)

GetWorkersResponse = _reflection.GeneratedProtocolMessageType('GetWorkersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETWORKERSRESPONSE,
  '__module__' : 'tensorflow.core.data.service.dispatcher_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.GetWorkersResponse)
  })
_sym_db.RegisterMessage(GetWorkersResponse)



_DISPATCHERSERVICE = _descriptor.ServiceDescriptor(
  name='DispatcherService',
  full_name='tensorflow.data.DispatcherService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1229,
  serialized_end=1908,
  methods=[
  _descriptor.MethodDescriptor(
    name='RegisterWorker',
    full_name='tensorflow.data.DispatcherService.RegisterWorker',
    index=0,
    containing_service=None,
    input_type=_REGISTERWORKERREQUEST,
    output_type=_REGISTERWORKERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WorkerUpdate',
    full_name='tensorflow.data.DispatcherService.WorkerUpdate',
    index=1,
    containing_service=None,
    input_type=_WORKERUPDATEREQUEST,
    output_type=_WORKERUPDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetOrRegisterDataset',
    full_name='tensorflow.data.DispatcherService.GetOrRegisterDataset',
    index=2,
    containing_service=None,
    input_type=_GETORREGISTERDATASETREQUEST,
    output_type=_GETORREGISTERDATASETRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetOrCreateJob',
    full_name='tensorflow.data.DispatcherService.GetOrCreateJob',
    index=3,
    containing_service=None,
    input_type=_GETORCREATEJOBREQUEST,
    output_type=_GETORCREATEJOBRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateJob',
    full_name='tensorflow.data.DispatcherService.CreateJob',
    index=4,
    containing_service=None,
    input_type=_CREATEJOBREQUEST,
    output_type=_CREATEJOBRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTasks',
    full_name='tensorflow.data.DispatcherService.GetTasks',
    index=5,
    containing_service=None,
    input_type=_GETTASKSREQUEST,
    output_type=_GETTASKSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetWorkers',
    full_name='tensorflow.data.DispatcherService.GetWorkers',
    index=6,
    containing_service=None,
    input_type=_GETWORKERSREQUEST,
    output_type=_GETWORKERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISPATCHERSERVICE)

DESCRIPTOR.services_by_name['DispatcherService'] = _DISPATCHERSERVICE

# @@protoc_insertion_point(module_scope)
