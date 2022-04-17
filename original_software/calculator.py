import multiprocessing as mp
from datetime import datetime

from grpc_server_python import server
from grpc_server_python import misc


class Calculator(object):

    def __init__(self, name: str, identifier: int, options: dict = None):
        self.name = name
        self.identifier = identifier
        self.options = options
        self._test_set_number = 0

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
        misc.log(f"\ta: {operator}")
        misc.log(f"\ta: {b}")
        a_o = ["+", "-", "*", "/"]
        if operator not in a_o:
            misc.log(f"Ooops.. you provided unsupported operator. Only {a_o} available. Try again")
            return
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
                    {'k': 'a', 'v': [1, 4]},
                    {'k': 'b', 'v': [7, 2, 2, 2, 5]},
                    {'k': 'c', 'v': [8, 5, 53]}
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

    # def streeming(self, dict_smpl: dict):
    #     pass


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
    q = mp.JoinableQueue()
    server_process = mp.Process(target=server.serve, args=(q,))
    server_process.start()
    while not close_app:
        if not q.empty():
            # misc.log("Message received!")
            # Note: We have One-To-One interaction. ONE instance of ROMBuilder has ONE gRPC server
            # But server has several threads....  NEED TO CHECK!!!
            # What about streeming RPC???
            request = q.get()
            misc.log(f"message_proto_name: {request['message_proto_name']}")
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

            q.task_done()  # Unblock the process. Let certain method in process continue to process response in q
            q.put(response)
            q.join()
            # close_app = True
            misc.log("\tWaiting for next request...")
            misc.log("")
