import os

IS_DEBUG = True
VERSION = "0.0.1"
GRPC_PORT = "localhost:50051"
LOG_FOLDER = os.path.join(os.path.expanduser('~'), ".grpc_client_NAME_python")
LOG_FILENAME = "grpc_client_python.log"
