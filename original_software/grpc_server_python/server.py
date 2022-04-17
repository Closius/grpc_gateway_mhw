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


def interact_with_software(mp_queue, request, message_proto_name):
    """
        Interaction between the original software and gRPC server

        :param mp_queue: multiprocessing.Queue() for interaction between the original software and gRPC server
        :param request: request from gRPC client
        :param message_proto_name: {Class name}.{method name} to be recognized on the original software side
        :return: vary. message to be sent back to gRPC client
    """
    # misc.log(f"METHOD: {message_proto_name}")
    # misc.log("server before self._mp_queue.put")
    try:
        mp_queue.put(
            {"message_proto_name": message_proto_name,
             "data": json_format.MessageToDict(request, preserving_proto_field_name=True)})
        mp_queue.join()  # Block the process until q.task_done()
        # misc.log("server after self._mp_queue.put")
        r = mp_queue.get()
        # misc.log(f"response from Software: {r}")
        # misc.log("server after self._mp_queue.get")
        mp_queue.task_done()
        return r
    except Exception:
        misc.log(traceback.format_exc())


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def __init__(self, mp_queue):
        self._mp_queue = mp_queue

    def NewTestSet(self, request, context):
        """
            :return: int
        """
        r = interact_with_software(mp_queue=self._mp_queue, request=request,
                        message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return calculator_pb2.NewTestSet_response(message=r)

    def ChangeSettings(self, request, context):
        """
            :param name: str
            :param identifier: int
            :param options: struct
            :return: Empty()
        """
        r = interact_with_software(mp_queue=self._mp_queue, request=request,
                        message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return Empty()

    def DoMath(self, request, context):
        """
            :param a: 5
            :param b: 4.5
            :param operator: "+"
            :return: 9.5
        """
        r = interact_with_software(mp_queue=self._mp_queue, request=request,
                        message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return calculator_pb2.DoMath_response(message=r)

    def ListToDict(self, request, context):
        """
        :param seq_k_str: ["a", "b", "c"]
        :param seq_v_int: [1, 2, 3]
        :return: [
                    {'k': ['a'], 'v': [1]},
                    {'k': ['b'], 'v': [2]},
                    {'k': ['c'], 'v': [3]}
                ]
        """
        r = interact_with_software(mp_queue=self._mp_queue, request=request,
                        message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return calculator_pb2.ListToDict_response(message=r)

    def DictToList(self, request, context):
        """
        :param dict_smpl: [
                    {'k': 'a', 'v': [1, 4]},
                    {'k': 'b', 'v': [7, 2, 2, 2, 5]},
                    {'k': 'c', 'v': [8, 5, 53]}
                ]
        :return: [
                    {'k': 'a', 'v': [1, 4]},
                    {'k': 'b', 'v': [7, 2, 2, 2, 5]},
                    {'k': 'c', 'v': [8, 5, 53]}
                ]
        """
        r = interact_with_software(mp_queue=self._mp_queue, request=request,
                        message_proto_name=f"{type(self).__name__}.{inspect.currentframe().f_code.co_name}")
        return calculator_pb2.DictToList_response(message=r)

    # def Streeming(self, request, context):
    #     pass


def serve(mp_queue):
    try:
        misc.log("gRPC Python server is running...")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(mp_queue), server)
        server.add_insecure_port(settings.GRPC_PORT)
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)
