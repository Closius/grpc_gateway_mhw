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
            misc.log("---------------------------")
            misc.log("Test 1 StartLongProcessStreaming...")
            response_stream = stub.StartLongProcessStreaming(
                calculator_pb2.StartLongProcessStreaming_request(
                    sequence="Three Rings for the Elven-kings under the sky, " +
                             "Seven for the Dwarf-lords in their halls of stone, " +
                             "Nine for Mortal Men doomed to die, " +
                             "One for the Dark Lord on his dark throne " +
                             "In the Land of Mordor where the Shadows lie. " +
                             "One Ring to rule them all, One Ring to find them, " +
                             "One Ring to bring them all, and in the darkness bind them, " +
                             "In the Land of Mordor where the Shadows lie. "
                )
            )
            for response in response_stream:
                r = json_format.MessageToDict(response, preserving_proto_field_name=True,
                                              including_default_value_fields=True)
                misc.log(f"\tresponse: {r['message']}")
            misc.log(f"\t\t---- DONE ----")
        except grpc.RpcError as e:
            ex_mess(e)


if __name__ == '__main__':
    misc.log("gRPC Python client is running...")
    test()
    misc.log("---------------------------")
    misc.log(f"All tests PASSED")
