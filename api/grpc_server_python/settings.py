import os

IS_DEBUG = True
VERSION = "0.0.1"
GRPC_PORT = f"[::]:{os.environ['GRPC_PORT']}"
LOG_FOLDER = os.path.join(os.path.expanduser('~'), ".grpc_server_NAME_python")
LOG_FILENAME = "grpc_server.log"
STOP_WORD = "f50ec0b7-f960-400d-91f0-c42a6d44e3d0"
