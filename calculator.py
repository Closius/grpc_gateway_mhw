import traceback
import time
import multiprocessing as mp
from datetime import datetime

from api.grpc_server_python import server
from api.grpc_server_python import misc
from api.grpc_server_python import settings


def _f_stream(seq, mp_queue_manage, mp_queue_results_streaming):
    misc.log(" - - - - Long Process Streaming started!")
    misc.log("This is an original software process (separate spawned process) which generates some data")
    misc.log(f"approx. duration: {len(seq)} seconds")
    is_not_interrupted = True
    for i in seq:
        misc.log(i)
        mp_queue_results_streaming.put(i)
        # yield i
        time.sleep(1)
        if not mp_queue_manage.empty():
            say = mp_queue_manage.get()
            mp_queue_results_streaming.put(say)
            mp_queue_results_streaming.put(settings.STOP_WORD)
            # yield say
            # yield " - - - - Long Process interrupted!"
            misc.log(f" - - - - Long Process Streaming interrupted! client said: {say}")
            is_not_interrupted = False
            break
    if is_not_interrupted:
        mp_queue_results_streaming.put(settings.STOP_WORD)
        misc.log(" - - - - Long Process Streaming finished without interruption!")


class Calculator(object):

    def __init__(self, name: str, identifier: int, options: dict = None):
        self.name = name
        self.identifier = identifier
        self.options = options
        self._test_set_number = 0
        # TODO: Warning!
        # There might be launched several streaming clients.
        # When you sent signal by this Queue to stop the signal,
        # it can be received by ANY of running process!
        # You have to stop process based on Client id
        self.mp_queue_manage_streaming = mp.Queue()

    def new_test_set(self):
        self._test_set_number += 1
        dn = f"    {self._test_set_number}: New test set: " + datetime.now().strftime("%H:%M:%S    ")
        n = len(dn)
        misc.log("")
        misc.log("\t*" + "-" * n + "*")
        misc.log("\t*" + " " * n + "*")
        misc.log("\t*" + dn + "*")
        misc.log("\t*" + " " * n + "*")
        misc.log("\t*" + "-" * n + "*")
        misc.log("")
        return self._test_set_number

    def change_settings(self, name, identifier, options=None):
        misc.log(f"Changing settings for project...")
        misc.log(f"\tCurrent settings:")
        misc.log(f"\t\tname: {self.name}")
        misc.log(f"\t\tidentifier: {self.identifier}")
        misc.log(f"\t\toptions: {self.options}")
        self.name = name
        self.identifier = identifier
        self.options = options
        misc.log(f"\tNew settings:")
        misc.log(f"\t\tname: {self.name}")
        misc.log(f"\t\tidentifier: {self.identifier}")
        misc.log(f"\t\toptions: {self.options}")
        misc.log(f"Changing settings for project... Done")
        misc.log(f"======================================")
        return None

    def do_math(self, a, b, operator):
        """
        :param a: 5
        :param b: 4.5
        :param operator: "+"
        :return: 9.5
        """
        misc.log(f"Doing math for project {self.name}...")
        misc.log(f"\ta: {a}")
        misc.log(f"\toperator: {operator}")
        misc.log(f"\tb: {b}")
        a_o = ["+", "-", "*", "/"]
        # if operator not in a_o:
        #     misc.log(f"Ooops.. you provided unsupported operator. Only {a_o} available. Try again")
        #     return
        r = eval(f"{a} {operator} {b}")
        misc.log(f"\t\tresult: {r}")
        misc.log(f"Doing math for project {self.name}... Done")
        misc.log(f"======================================")
        return r

    def list_to_dict(self, seq_k_str: list, seq_v_int: list):
        """
        :param seq_k_str: ["a", "b", "c"]
        :param seq_v_int: [1, 2, 3]
        :return: [
                    {'k': ['a'], 'v': [1]},
                    {'k': ['b'], 'v': [2]},
                    {'k': ['c'], 'v': [3]}
                ]
        """
        misc.log(f"List to dict for project {self.name}...")
        misc.log(f"\tseq_k_str: {seq_k_str}")
        misc.log(f"\tseq_v_int: {seq_v_int}")
        r = []
        for i in range(len(seq_v_int)):
            r.append({'k': [seq_k_str[i]], 'v': [seq_v_int[i]]})
        misc.log(f"\t\tresult: {r}")
        misc.log(f"List to dict for project {self.name}... Done")
        misc.log(f"======================================")
        return r

    def dict_to_list(self, dict_smpl: list):
        """
        :param dict_smpl: [
                    {'k': 'a', 'v': [1, 4]},
                    {'k': 'b', 'v': [7, 2, 2, 2, 5]},
                    {'k': 'c', 'v': [8, 5, 53]}
                ]
        :return: [
                    {'k': 'a', 'v': [1, 4, 1, 4]},
                    {'k': 'b', 'v': [7, 2, 2, 2, 5, 7, 2, 2, 2, 5 ]},
                    {'k': 'c', 'v': [8, 5, 53, 8, 5, 53]}
                ]
        """
        misc.log(f"Dict to list for project {self.name}...")
        misc.log(f"\tdict_smpl: {dict_smpl}")
        r = []
        for i in range(len(dict_smpl)):
            r.append({'k': dict_smpl[i]['k'],
                      'v': dict_smpl[i]['v']*2})
        misc.log(f"\t\tresult: {r}")
        misc.log(f"Dict to list for project {self.name}... Done")
        misc.log(f"======================================")
        return r

    def start_long_process_streaming(self, mp_queue_results_streaming, sequence: str):
        """
        Iterate over sequence, print each element each 1 second in a separate process

        :param sequence: "some string"
        """
        misc.log(f"Start Long Process Streaming for project {self.name}...")
        misc.log(f"\tsequence: {sequence}")
        _process = mp.Process(target=_f_stream, args=(sequence,
                                                      self.mp_queue_manage_streaming,
                                                      mp_queue_results_streaming))
        _process.start()
        misc.log(f"\t\tresult: Process is sending a stream to the client. Check client ")
        misc.log(f"Note: This gRPC server worker is busy until stream is finished")
        misc.log(f"======================================")

    def stop_long_process_streaming(self, say: str):
        """
        Interrupt a long process above with saying "say"

        :param say: "say something"
        """
        misc.log(f"Stop Long Process Streaming for project {self.name}...")
        misc.log(f"\tsay: {say}")
        self.mp_queue_manage_streaming.put(say, block=True)
        misc.log(f"\t\tresult: Process stopped.")
        misc.log(f"Stop Long Process Streaming for project {self.name}... Done")
        misc.log(f"======================================")


if __name__ == '__main__':
    misc.log("")
    misc.log("")
    misc.log("")
    misc.log("")
    misc.log("")
    misc.log("\tRun original software loop...")
    misc.log("")
    original_SOFTWARE = Calculator(name="Init_Name", identifier=0)
    close_app = False
    q_dicts = {
        "main_queue": mp.JoinableQueue(),
        "start_long_process_streaming": mp.JoinableQueue()
    }
    server_process = mp.Process(target=server.serve, args=(q_dicts,))
    server_process.start()
    while not close_app:
        request = q_dicts["main_queue"].get(block=True)
        misc.log(f"message_proto_name: {request['message_proto_name']}")
        try:
            if request["message_proto_name"] == "CalculatorServicer.NewTestSet":
                response = original_SOFTWARE.new_test_set()
            elif request["message_proto_name"] == "CalculatorServicer.ChangeSettings":
                response = original_SOFTWARE.change_settings(**request["data"])
            elif request["message_proto_name"] == "CalculatorServicer.DoMath":
                response = original_SOFTWARE.do_math(**request["data"])
            elif request["message_proto_name"] == "CalculatorServicer.ListToDict":
                response = original_SOFTWARE.list_to_dict(**request["data"])
            elif request["message_proto_name"] == "CalculatorServicer.DictToList":
                response = original_SOFTWARE.dict_to_list(**request["data"])
            elif request["message_proto_name"] == "CalculatorServicer.StartLongProcessStreaming":
                response = original_SOFTWARE.start_long_process_streaming(
                    mp_queue_results_streaming=q_dicts["start_long_process_streaming"], **request["data"])
            elif request["message_proto_name"] == "CalculatorServicer.StopLongProcessStreaming":
                response = original_SOFTWARE.stop_long_process_streaming(**request["data"])

            response = {"data": response, "status": "ok"}
        except Exception as ex:
            response = {"message": str(ex), "status": "error"}
            misc.log(traceback.format_exc())

        q_dicts["main_queue"].task_done()  # Unblock the process. Let certain method in process continue to process response in q
        q_dicts["main_queue"].put(response)
        q_dicts["main_queue"].join()
        # close_app = True
        misc.log("\tWaiting for next request...")
        misc.log("")
