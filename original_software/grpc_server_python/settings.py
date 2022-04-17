import os

IS_DEBUG = True
VERSION = "0.0.1"
GRPC_PORT = "[::]:50051"
LOG_FOLDER = os.path.join(os.path.expanduser('~'), ".grpc_server_NAME_python")
LOG_FILENAME = "grpc_server.log"
