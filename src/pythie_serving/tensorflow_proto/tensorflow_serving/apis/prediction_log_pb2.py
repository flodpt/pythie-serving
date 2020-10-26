# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow_serving/apis/prediction_log.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pythie_serving.tensorflow_proto.tensorflow_serving.apis import classification_pb2 as tensorflow__serving_dot_apis_dot_classification__pb2
from pythie_serving.tensorflow_proto.tensorflow_serving.apis import inference_pb2 as tensorflow__serving_dot_apis_dot_inference__pb2
from pythie_serving.tensorflow_proto.tensorflow_serving.apis import predict_pb2 as tensorflow__serving_dot_apis_dot_predict__pb2
from pythie_serving.tensorflow_proto.tensorflow_serving.apis import regression_pb2 as tensorflow__serving_dot_apis_dot_regression__pb2
from pythie_serving.tensorflow_proto.tensorflow_serving.apis import session_service_pb2 as tensorflow__serving_dot_apis_dot_session__service__pb2
from pythie_serving.tensorflow_proto.tensorflow_serving.core import logging_pb2 as tensorflow__serving_dot_core_dot_logging__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow_serving/apis/prediction_log.proto',
  package='tensorflow.serving',
  syntax='proto3',
  serialized_options=b'\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,tensorflow_serving/apis/prediction_log.proto\x12\x12tensorflow.serving\x1a,tensorflow_serving/apis/classification.proto\x1a\'tensorflow_serving/apis/inference.proto\x1a%tensorflow_serving/apis/predict.proto\x1a(tensorflow_serving/apis/regression.proto\x1a-tensorflow_serving/apis/session_service.proto\x1a%tensorflow_serving/core/logging.proto\"\x87\x01\n\x0b\x43lassifyLog\x12:\n\x07request\x18\x01 \x01(\x0b\x32).tensorflow.serving.ClassificationRequest\x12<\n\x08response\x18\x02 \x01(\x0b\x32*.tensorflow.serving.ClassificationResponse\"~\n\nRegressLog\x12\x36\n\x07request\x18\x01 \x01(\x0b\x32%.tensorflow.serving.RegressionRequest\x12\x38\n\x08response\x18\x02 \x01(\x0b\x32&.tensorflow.serving.RegressionResponse\"x\n\nPredictLog\x12\x33\n\x07request\x18\x01 \x01(\x0b\x32\".tensorflow.serving.PredictRequest\x12\x35\n\x08response\x18\x02 \x01(\x0b\x32#.tensorflow.serving.PredictResponse\"\x8d\x01\n\x11MultiInferenceLog\x12:\n\x07request\x18\x01 \x01(\x0b\x32).tensorflow.serving.MultiInferenceRequest\x12<\n\x08response\x18\x02 \x01(\x0b\x32*.tensorflow.serving.MultiInferenceResponse\"\x81\x01\n\rSessionRunLog\x12\x36\n\x07request\x18\x01 \x01(\x0b\x32%.tensorflow.serving.SessionRunRequest\x12\x38\n\x08response\x18\x02 \x01(\x0b\x32&.tensorflow.serving.SessionRunResponse\"\xfd\x02\n\rPredictionLog\x12\x35\n\x0clog_metadata\x18\x01 \x01(\x0b\x32\x1f.tensorflow.serving.LogMetadata\x12\x37\n\x0c\x63lassify_log\x18\x02 \x01(\x0b\x32\x1f.tensorflow.serving.ClassifyLogH\x00\x12\x35\n\x0bregress_log\x18\x03 \x01(\x0b\x32\x1e.tensorflow.serving.RegressLogH\x00\x12\x35\n\x0bpredict_log\x18\x06 \x01(\x0b\x32\x1e.tensorflow.serving.PredictLogH\x00\x12\x44\n\x13multi_inference_log\x18\x04 \x01(\x0b\x32%.tensorflow.serving.MultiInferenceLogH\x00\x12<\n\x0fsession_run_log\x18\x05 \x01(\x0b\x32!.tensorflow.serving.SessionRunLogH\x00\x42\n\n\x08log_typeB\x03\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[tensorflow__serving_dot_apis_dot_classification__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_inference__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_predict__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_regression__pb2.DESCRIPTOR,tensorflow__serving_dot_apis_dot_session__service__pb2.DESCRIPTOR,tensorflow__serving_dot_core_dot_logging__pb2.DESCRIPTOR,])




_CLASSIFYLOG = _descriptor.Descriptor(
  name='ClassifyLog',
  full_name='tensorflow.serving.ClassifyLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='tensorflow.serving.ClassifyLog.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='tensorflow.serving.ClassifyLog.response', index=1,
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
  serialized_start=323,
  serialized_end=458,
)


_REGRESSLOG = _descriptor.Descriptor(
  name='RegressLog',
  full_name='tensorflow.serving.RegressLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='tensorflow.serving.RegressLog.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='tensorflow.serving.RegressLog.response', index=1,
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
  serialized_start=460,
  serialized_end=586,
)


_PREDICTLOG = _descriptor.Descriptor(
  name='PredictLog',
  full_name='tensorflow.serving.PredictLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='tensorflow.serving.PredictLog.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='tensorflow.serving.PredictLog.response', index=1,
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
  serialized_start=588,
  serialized_end=708,
)


_MULTIINFERENCELOG = _descriptor.Descriptor(
  name='MultiInferenceLog',
  full_name='tensorflow.serving.MultiInferenceLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='tensorflow.serving.MultiInferenceLog.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='tensorflow.serving.MultiInferenceLog.response', index=1,
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
  serialized_start=711,
  serialized_end=852,
)


_SESSIONRUNLOG = _descriptor.Descriptor(
  name='SessionRunLog',
  full_name='tensorflow.serving.SessionRunLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='tensorflow.serving.SessionRunLog.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response', full_name='tensorflow.serving.SessionRunLog.response', index=1,
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
  serialized_start=855,
  serialized_end=984,
)


_PREDICTIONLOG = _descriptor.Descriptor(
  name='PredictionLog',
  full_name='tensorflow.serving.PredictionLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_metadata', full_name='tensorflow.serving.PredictionLog.log_metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classify_log', full_name='tensorflow.serving.PredictionLog.classify_log', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regress_log', full_name='tensorflow.serving.PredictionLog.regress_log', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='predict_log', full_name='tensorflow.serving.PredictionLog.predict_log', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multi_inference_log', full_name='tensorflow.serving.PredictionLog.multi_inference_log', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='session_run_log', full_name='tensorflow.serving.PredictionLog.session_run_log', index=5,
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
    _descriptor.OneofDescriptor(
      name='log_type', full_name='tensorflow.serving.PredictionLog.log_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=987,
  serialized_end=1368,
)

_CLASSIFYLOG.fields_by_name['request'].message_type = tensorflow__serving_dot_apis_dot_classification__pb2._CLASSIFICATIONREQUEST
_CLASSIFYLOG.fields_by_name['response'].message_type = tensorflow__serving_dot_apis_dot_classification__pb2._CLASSIFICATIONRESPONSE
_REGRESSLOG.fields_by_name['request'].message_type = tensorflow__serving_dot_apis_dot_regression__pb2._REGRESSIONREQUEST
_REGRESSLOG.fields_by_name['response'].message_type = tensorflow__serving_dot_apis_dot_regression__pb2._REGRESSIONRESPONSE
_PREDICTLOG.fields_by_name['request'].message_type = tensorflow__serving_dot_apis_dot_predict__pb2._PREDICTREQUEST
_PREDICTLOG.fields_by_name['response'].message_type = tensorflow__serving_dot_apis_dot_predict__pb2._PREDICTRESPONSE
_MULTIINFERENCELOG.fields_by_name['request'].message_type = tensorflow__serving_dot_apis_dot_inference__pb2._MULTIINFERENCEREQUEST
_MULTIINFERENCELOG.fields_by_name['response'].message_type = tensorflow__serving_dot_apis_dot_inference__pb2._MULTIINFERENCERESPONSE
_SESSIONRUNLOG.fields_by_name['request'].message_type = tensorflow__serving_dot_apis_dot_session__service__pb2._SESSIONRUNREQUEST
_SESSIONRUNLOG.fields_by_name['response'].message_type = tensorflow__serving_dot_apis_dot_session__service__pb2._SESSIONRUNRESPONSE
_PREDICTIONLOG.fields_by_name['log_metadata'].message_type = tensorflow__serving_dot_core_dot_logging__pb2._LOGMETADATA
_PREDICTIONLOG.fields_by_name['classify_log'].message_type = _CLASSIFYLOG
_PREDICTIONLOG.fields_by_name['regress_log'].message_type = _REGRESSLOG
_PREDICTIONLOG.fields_by_name['predict_log'].message_type = _PREDICTLOG
_PREDICTIONLOG.fields_by_name['multi_inference_log'].message_type = _MULTIINFERENCELOG
_PREDICTIONLOG.fields_by_name['session_run_log'].message_type = _SESSIONRUNLOG
_PREDICTIONLOG.oneofs_by_name['log_type'].fields.append(
  _PREDICTIONLOG.fields_by_name['classify_log'])
_PREDICTIONLOG.fields_by_name['classify_log'].containing_oneof = _PREDICTIONLOG.oneofs_by_name['log_type']
_PREDICTIONLOG.oneofs_by_name['log_type'].fields.append(
  _PREDICTIONLOG.fields_by_name['regress_log'])
_PREDICTIONLOG.fields_by_name['regress_log'].containing_oneof = _PREDICTIONLOG.oneofs_by_name['log_type']
_PREDICTIONLOG.oneofs_by_name['log_type'].fields.append(
  _PREDICTIONLOG.fields_by_name['predict_log'])
_PREDICTIONLOG.fields_by_name['predict_log'].containing_oneof = _PREDICTIONLOG.oneofs_by_name['log_type']
_PREDICTIONLOG.oneofs_by_name['log_type'].fields.append(
  _PREDICTIONLOG.fields_by_name['multi_inference_log'])
_PREDICTIONLOG.fields_by_name['multi_inference_log'].containing_oneof = _PREDICTIONLOG.oneofs_by_name['log_type']
_PREDICTIONLOG.oneofs_by_name['log_type'].fields.append(
  _PREDICTIONLOG.fields_by_name['session_run_log'])
_PREDICTIONLOG.fields_by_name['session_run_log'].containing_oneof = _PREDICTIONLOG.oneofs_by_name['log_type']
DESCRIPTOR.message_types_by_name['ClassifyLog'] = _CLASSIFYLOG
DESCRIPTOR.message_types_by_name['RegressLog'] = _REGRESSLOG
DESCRIPTOR.message_types_by_name['PredictLog'] = _PREDICTLOG
DESCRIPTOR.message_types_by_name['MultiInferenceLog'] = _MULTIINFERENCELOG
DESCRIPTOR.message_types_by_name['SessionRunLog'] = _SESSIONRUNLOG
DESCRIPTOR.message_types_by_name['PredictionLog'] = _PREDICTIONLOG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClassifyLog = _reflection.GeneratedProtocolMessageType('ClassifyLog', (_message.Message,), {
  'DESCRIPTOR' : _CLASSIFYLOG,
  '__module__' : 'tensorflow_serving.apis.prediction_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.ClassifyLog)
  })
_sym_db.RegisterMessage(ClassifyLog)

RegressLog = _reflection.GeneratedProtocolMessageType('RegressLog', (_message.Message,), {
  'DESCRIPTOR' : _REGRESSLOG,
  '__module__' : 'tensorflow_serving.apis.prediction_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.RegressLog)
  })
_sym_db.RegisterMessage(RegressLog)

PredictLog = _reflection.GeneratedProtocolMessageType('PredictLog', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTLOG,
  '__module__' : 'tensorflow_serving.apis.prediction_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.PredictLog)
  })
_sym_db.RegisterMessage(PredictLog)

MultiInferenceLog = _reflection.GeneratedProtocolMessageType('MultiInferenceLog', (_message.Message,), {
  'DESCRIPTOR' : _MULTIINFERENCELOG,
  '__module__' : 'tensorflow_serving.apis.prediction_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.MultiInferenceLog)
  })
_sym_db.RegisterMessage(MultiInferenceLog)

SessionRunLog = _reflection.GeneratedProtocolMessageType('SessionRunLog', (_message.Message,), {
  'DESCRIPTOR' : _SESSIONRUNLOG,
  '__module__' : 'tensorflow_serving.apis.prediction_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.SessionRunLog)
  })
_sym_db.RegisterMessage(SessionRunLog)

PredictionLog = _reflection.GeneratedProtocolMessageType('PredictionLog', (_message.Message,), {
  'DESCRIPTOR' : _PREDICTIONLOG,
  '__module__' : 'tensorflow_serving.apis.prediction_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.serving.PredictionLog)
  })
_sym_db.RegisterMessage(PredictionLog)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
