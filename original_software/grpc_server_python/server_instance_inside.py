import inspect
import traceback
from concurrent import futures

import grpc
from google.protobuf.empty_pb2 import Empty
from google.protobuf import json_format

import calculator
import proto_compiled.calculator_pb2 as calculator_pb2
import proto_compiled.calculator_pb2_grpc as calculator_pb2_grpc
import misc
import settings


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def __init__(self, calculator_instance):
        self._calculator_instance = calculator_instance

    def NewTestSet(self, request, context):
        r = self._calculator_instance.new_test_set()
        return calculator_pb2.NewTestSet_response(message=r)

    def ChangeSettings(self, request, context):
        """
            :param name: str
            :param identifier: int
            :param options: struct
            :return: None
        """
        self._calculator_instance.change_settings(
            name=request.name,
            identifier=request.identifier,
            options=request.options)
        return Empty()

    def DoMath(self, request, context):
        """
            :param a: 5
            :param b: 4.5
            :param operator: "+"
            :return: 9.5
        """
        r = self._calculator_instance.do_math(
            a=request.a,
            b=request.b,
            operator=request.operator)
        return calculator_pb2.DoMath_response(message=r)

    def ListToDict(self, request, context):
        """
        :param seq_k: ["a", "b", "c"]
        :param seq_v: [1, 2, 3]
        :return: {"a": 1, "b": 2, "c": 3}
        """
        r = self._calculator_instance.list_to_dict(
            seq_k=request.seq_k,
            seq_v=request.seq_v)
        return calculator_pb2.ListToDict_response(message=r)

    def DictToList(self, request, context):
        """
        :param dict_smpl: {1: 2, 3: 4, 5: 6}
        :return: [(1, 2), (3, 4), (5, 6)]
        """
        r = self._calculator_instance.list_to_dict(
            dict_smpl=request.dict_smpl)
        return calculator_pb2.DictToList_response(message=r)

    # def Streeming(self, request, context):
    #     pass


def serve(calc_inst):
    try:
        misc.log("gRPC Python server is running...")
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        # Passing instance to server - not good idea because server is multithreaded..
        calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(calculator_instance=calc_inst), server)
        server.add_insecure_port(settings.GRPC_PORT)
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    c_i = calculator.Calculator(name="Init_Name", identifier=0)
    serve(calc_inst=c_i)
