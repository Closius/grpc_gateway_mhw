# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculator_pb2 as calculator__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class CalculatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NewTestSet = channel.unary_unary(
                '/calculator.Calculator/NewTestSet',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=calculator__pb2.NewTestSet_response.FromString,
                )
        self.ChangeSettings = channel.unary_unary(
                '/calculator.Calculator/ChangeSettings',
                request_serializer=calculator__pb2.ChangeSettings_request.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DoMath = channel.unary_unary(
                '/calculator.Calculator/DoMath',
                request_serializer=calculator__pb2.DoMath_request.SerializeToString,
                response_deserializer=calculator__pb2.DoMath_response.FromString,
                )
        self.ListToDict = channel.unary_unary(
                '/calculator.Calculator/ListToDict',
                request_serializer=calculator__pb2.ListToDict_request.SerializeToString,
                response_deserializer=calculator__pb2.ListToDict_response.FromString,
                )
        self.DictToList = channel.unary_unary(
                '/calculator.Calculator/DictToList',
                request_serializer=calculator__pb2.DictToList_request.SerializeToString,
                response_deserializer=calculator__pb2.DictToList_response.FromString,
                )
        self.StartLongProcessStreaming = channel.unary_stream(
                '/calculator.Calculator/StartLongProcessStreaming',
                request_serializer=calculator__pb2.StartLongProcessStreaming_request.SerializeToString,
                response_deserializer=calculator__pb2.StartLongProcessStreaming_response.FromString,
                )
        self.StopLongProcessStreaming = channel.unary_unary(
                '/calculator.Calculator/StopLongProcessStreaming',
                request_serializer=calculator__pb2.StopLongProcessStreaming_request.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class CalculatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NewTestSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeSettings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DoMath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListToDict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DictToList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartLongProcessStreaming(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StopLongProcessStreaming(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NewTestSet': grpc.unary_unary_rpc_method_handler(
                    servicer.NewTestSet,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=calculator__pb2.NewTestSet_response.SerializeToString,
            ),
            'ChangeSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeSettings,
                    request_deserializer=calculator__pb2.ChangeSettings_request.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DoMath': grpc.unary_unary_rpc_method_handler(
                    servicer.DoMath,
                    request_deserializer=calculator__pb2.DoMath_request.FromString,
                    response_serializer=calculator__pb2.DoMath_response.SerializeToString,
            ),
            'ListToDict': grpc.unary_unary_rpc_method_handler(
                    servicer.ListToDict,
                    request_deserializer=calculator__pb2.ListToDict_request.FromString,
                    response_serializer=calculator__pb2.ListToDict_response.SerializeToString,
            ),
            'DictToList': grpc.unary_unary_rpc_method_handler(
                    servicer.DictToList,
                    request_deserializer=calculator__pb2.DictToList_request.FromString,
                    response_serializer=calculator__pb2.DictToList_response.SerializeToString,
            ),
            'StartLongProcessStreaming': grpc.unary_stream_rpc_method_handler(
                    servicer.StartLongProcessStreaming,
                    request_deserializer=calculator__pb2.StartLongProcessStreaming_request.FromString,
                    response_serializer=calculator__pb2.StartLongProcessStreaming_response.SerializeToString,
            ),
            'StopLongProcessStreaming': grpc.unary_unary_rpc_method_handler(
                    servicer.StopLongProcessStreaming,
                    request_deserializer=calculator__pb2.StopLongProcessStreaming_request.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calculator.Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calculator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NewTestSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/NewTestSet',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            calculator__pb2.NewTestSet_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/ChangeSettings',
            calculator__pb2.ChangeSettings_request.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DoMath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/DoMath',
            calculator__pb2.DoMath_request.SerializeToString,
            calculator__pb2.DoMath_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListToDict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/ListToDict',
            calculator__pb2.ListToDict_request.SerializeToString,
            calculator__pb2.ListToDict_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DictToList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/DictToList',
            calculator__pb2.DictToList_request.SerializeToString,
            calculator__pb2.DictToList_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StartLongProcessStreaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/calculator.Calculator/StartLongProcessStreaming',
            calculator__pb2.StartLongProcessStreaming_request.SerializeToString,
            calculator__pb2.StartLongProcessStreaming_response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StopLongProcessStreaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/StopLongProcessStreaming',
            calculator__pb2.StopLongProcessStreaming_request.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
