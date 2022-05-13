import inspect
import traceback
from concurrent import futures

import grpc
from google.protobuf.empty_pb2 import Empty
from google.protobuf import json_format

import proto_compiled.calculator_pb2 as calculator_pb2
import proto_compiled.calculator_pb2_grpc as calculator_pb2_grpc
import misc
import settings


class MyInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        next_handler = continuation(handler_call_details)
        if next_handler.unary_unary:
            def _handler(request, context):
                r = next_handler.unary_unary(request, context)  # rpc method from .proto
                # json_format.MessageToDict(request, preserving_proto_field_name=True,
                #                           including_default_value_fields=True)
                # request_serializer=calculator_pb2.DictToList_request.SerializeToString,
                # response_deserializer=calculator_pb2.DictToList_response.FromString,
                # misc.log(f"r: {str(r)}")
                # misc.log(f"r.ListFields(): {r.ListFields()}")
                # misc.log(f"r.message: {r.message}")
                # misc.log(f"type(r.message): {type(r.message)}")
                # misc.log(f"request: {str(request)}")
                # misc.log(f"context: {str(context)}")
                return r
            return grpc.unary_unary_rpc_method_handler(_handler,
                                                       request_deserializer=next_handler.request_deserializer,
                                                       response_serializer=next_handler.response_serializer, )


def interact_with_software(mp_queue, request, message_proto_name, context):
    """
        Interaction between the original software and gRPC server

        :param mp_queue: multiprocessing.Queue() for interaction between the original software and gRPC server
        :param request: request from gRPC client
        :param context: context from gRPC client
        :param message_proto_name: {Class name}.{method name} to be recognized on the original software side
        :return: vary. message to be sent back to gRPC client
    """
    try:
        mp_queue.put(
            {"message_proto_name": message_proto_name,
             "data": json_format.MessageToDict(request, preserving_proto_field_name=True,
                                               including_default_value_fields=True)})
        mp_queue.join()  # Block the process until q.task_done()
        r = mp_queue.get()
        mp_queue.task_done()
        if r["status"] == "ok":
            return r["data"]
        elif r["status"] == "error":
            context.set_details(r["message"])
            context.set_code(
                grpc.StatusCode.INVALID_ARGUMENT)  # HTTP: 400 https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto
            return r["message"]
    except Exception as ex:
        context.set_details(str(ex))
        context.set_code(
            grpc.StatusCode.UNKNOWN)  # HTTP: 500 https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto
        misc.log(traceback.format_exc())
        return str(ex)


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def __init__(self, q_dicts):
        self._q_dicts = q_dicts

    def NewTestSet(self, request, context):
        r = interact_with_software(mp_queue=self._q_dicts["main_queue"], request=request, context=context,
                                   message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return calculator_pb2.NewTestSet_response(message=r)

    def ChangeSettings(self, request, context):
        r = interact_with_software(mp_queue=self._q_dicts["main_queue"], request=request, context=context,
                                   message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return Empty()

    def DoMath(self, request, context):
        r = interact_with_software(mp_queue=self._q_dicts["main_queue"], request=request, context=context,
                                   message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return calculator_pb2.DoMath_response(message=r)

    def ListToDict(self, request, context):
        r = interact_with_software(mp_queue=self._q_dicts["main_queue"], request=request, context=context,
                                   message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return calculator_pb2.ListToDict_response(message=r)

    def DictToList(self, request, context):
        r = interact_with_software(mp_queue=self._q_dicts["main_queue"], request=request, context=context,
                                   message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return calculator_pb2.DictToList_response(message=r)

    def StartLongProcessStreaming(self, request, context):
        r = interact_with_software(mp_queue=self._q_dicts["main_queue"], request=request, context=context,
                                   message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        while True:
            feature = self._q_dicts["start_long_process_streaming"].get(block=True)
            if feature == settings.STOP_WORD:
                break
            else:
                yield calculator_pb2.StartLongProcessStreaming_response(message=feature)

    def StopLongProcessStreaming(self, request, context):
        r = interact_with_software(mp_queue=self._q_dicts["main_queue"], request=request, context=context,
                                   message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return Empty()


def serve(q_dicts):
    try:
        misc.log("gRPC Python server is running...")
        misc.log(f"address: {settings.GRPC_PORT}")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(q_dicts), server)
        server.add_insecure_port(settings.GRPC_PORT)
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)
