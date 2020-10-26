# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pythie_serving.tensorflow_proto.tensorflow_serving.apis import session_service_pb2 as tensorflow__serving_dot_apis_dot_session__service__pb2


class SessionServiceStub(object):
    """SessionService defines a service with which a client can interact to execute
    Tensorflow model inference. The SessionService::SessionRun method is similar
    to MasterService::RunStep of Tensorflow, except that all sessions are ready
    to run, and you request a specific model/session with ModelSpec.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SessionRun = channel.unary_unary(
                '/tensorflow.serving.SessionService/SessionRun',
                request_serializer=tensorflow__serving_dot_apis_dot_session__service__pb2.SessionRunRequest.SerializeToString,
                response_deserializer=tensorflow__serving_dot_apis_dot_session__service__pb2.SessionRunResponse.FromString,
                )


class SessionServiceServicer(object):
    """SessionService defines a service with which a client can interact to execute
    Tensorflow model inference. The SessionService::SessionRun method is similar
    to MasterService::RunStep of Tensorflow, except that all sessions are ready
    to run, and you request a specific model/session with ModelSpec.
    """

    def SessionRun(self, request, context):
        """Runs inference of a given model.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SessionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SessionRun': grpc.unary_unary_rpc_method_handler(
                    servicer.SessionRun,
                    request_deserializer=tensorflow__serving_dot_apis_dot_session__service__pb2.SessionRunRequest.FromString,
                    response_serializer=tensorflow__serving_dot_apis_dot_session__service__pb2.SessionRunResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tensorflow.serving.SessionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SessionService(object):
    """SessionService defines a service with which a client can interact to execute
    Tensorflow model inference. The SessionService::SessionRun method is similar
    to MasterService::RunStep of Tensorflow, except that all sessions are ready
    to run, and you request a specific model/session with ModelSpec.
    """

    @staticmethod
    def SessionRun(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tensorflow.serving.SessionService/SessionRun',
            tensorflow__serving_dot_apis_dot_session__service__pb2.SessionRunRequest.SerializeToString,
            tensorflow__serving_dot_apis_dot_session__service__pb2.SessionRunResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
