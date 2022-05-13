import grpc
from google.protobuf.empty_pb2 import Empty
from google.protobuf import json_format

import proto_compiled.calculator_pb2 as calculator_pb2
import proto_compiled.calculator_pb2_grpc as calculator_pb2_grpc
import misc
import settings


def test():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    def ex_mess(e):
        misc.log('-- client.py grpc.RpcError error:')
        misc.log(f"\tcode: {e.code()}")
        misc.log(f"\tdebug_error_string: {e.debug_error_string()}")
        misc.log(f"\tdetails: {e.details()}")
        # misc.log(f"\texception: {e.exception()}")

    with grpc.insecure_channel(settings.GRPC_PORT) as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)

        try:
            r = stub.NewTestSet(Empty())
            misc.log("")
            misc.log("")
            misc.log(f"\t\t{r.message}: New test set...")
            misc.log("")
            misc.log("")
        except grpc.RpcError as e:
            ex_mess(e)
        # ---------------------------------------------------------------------------------------------------------
        try:
            misc.log("---------------------------")
            misc.log("Test 1 ChangeSettings...")
            stub.ChangeSettings(calculator_pb2.ChangeSettings_request(
                name='test1',
                identifier=23,
                options=[{"field1_str": "field1_str_test",
                          "field2_int": 235,  # optional
                          "field3_float": 155.235,
                          "field4_int": 89,  # optional
                          "field5_rep_str": ["a", "b", "c"]
                          }]
            ))
        except grpc.RpcError as e:
            ex_mess(e)
        # ---------------------------------------------------------------------------------------------------------
        try:
            misc.log("---------------------------")
            misc.log("Test 2 ChangeSettings...")
            stub.ChangeSettings(calculator_pb2.ChangeSettings_request(
                name='test2',
                identifier=563,
                options=[{"field1_str": "field1_str_test2",
                          "field2_int": 666,  # optional
                          "field3_float": 666.235,
                          "field5_rep_str": ["a1", "b1", "c1"]
                          }]
            ))
        except grpc.RpcError as e:
            ex_mess(e)
        # ---------------------------------------------------------------------------------------------------------
        try:
            misc.log("---------------------------")
            misc.log("Test 3 ChangeSettings...")
            stub.ChangeSettings(calculator_pb2.ChangeSettings_request(
                name='test3',
                identifier=888
            ))
        except grpc.RpcError as e:
            ex_mess(e)
        # ---------------------------------------------------------------------------------------------------------
        try:
            misc.log("---------------------------")
            misc.log("Test 4 DoMath...")
            r = stub.DoMath(calculator_pb2.DoMath_request(
                a=5,
                b=0,
                operator="This is CAUSE AN ERROR"
            ))
            misc.log(f"\t\tResponse: {r.message}")
        except grpc.RpcError as e:
            ex_mess(e)
        # ---------------------------------------------------------------------------------------------------------
        try:
            misc.log("---------------------------")
            misc.log("Test 5 DoMath...")
            r = stub.DoMath(calculator_pb2.DoMath_request(
                a=5,
                b=1,
                operator="+"
            ))
            misc.log(f"\t\tResponse: {r.message}")
        except grpc.RpcError as e:
            ex_mess(e)
        # ---------------------------------------------------------------------------------------------------------
        try:
            misc.log("---------------------------")
            misc.log("Test 6 ListToDict...")
            r = stub.ListToDict(calculator_pb2.ListToDict_request(
                seq_k_str=("a", "b", "c"),
                seq_v_int=(1, 2, 3)
            ))
            r = json_format.MessageToDict(r, preserving_proto_field_name=True,
                                          including_default_value_fields=True)
            misc.log(f"\t\tResponse: {r['message']}")
        except grpc.RpcError as e:
            ex_mess(e)
        # ---------------------------------------------------------------------------------------------------------
        try:
            misc.log("---------------------------")
            misc.log("Test 7 DictToList...")
            r = stub.DictToList(calculator_pb2.DictToList_request(
                dict_smpl=[
                    {'k': 'a', 'v': [1, 4]},
                    {'k': 'b', 'v': [7, 2, 2, 2, 5]},
                    {'k': 'c', 'v': [8, 5, 53]}
                ],
            ))
            r = json_format.MessageToDict(r, preserving_proto_field_name=True,
                                          including_default_value_fields=True)
            misc.log(f"\t\tResponse: {r['message']}")
        except grpc.RpcError as e:
            ex_mess(e)


if __name__ == '__main__':
    misc.log("gRPC Python client is running...")
    test()
    misc.log("------------all---------------")
    misc.log(f"All tests PASSED")
