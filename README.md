gRPC based API for some Software
================================

gRPC based API for some software

Description
-----------

    ```grpc_client_cpp``` - gRPC client in C++
    ```grpc_client_python``` - gRPC client in Python
    ```grpc_client_web``` - gRPC client Web
    ```original_software``` - original software + gRPC server


Prerequisites
-------------

python 3.8.8

grpcio             1.44.0
grpcio-tools       1.44.0
protobuf           3.19.4

But I think it will work on higher versions

Quick start
-----------

1. Install all prerequisites
2. Clone this repo
3. Run ```original_software/proto/compile.bat```. All .proto files in ```original_software/proto``` will be compiled in apropriate disr (```grpc_client_python/proto_compiled```, ```grpc_client_python/proto_compiled``` etc.)
4. Launch the original software with the server: ```original_software/bin/run_software_with_python_server.bat```
5. You will see the output in CLI and a log file for the server here: ```%USERPROFILE%\.grpc_server_NAME_python\grpc_server.log```
6. In a separate CLI run the client, for example ```grpc_client_python/bin/run_client.bat```
5. You will see the output in CLI and a log file for the client here: ```%USERPROFILE%\.grpc_cleint_NAME_python\grpc_client_python.log```. Also you will see effects in server CLI

googleapis
----------

The project assume that we are using HTTP transcoding for comunication by REST with gRPC. https://cloud.google.com/endpoints/docs/grpc/transcoding

For this reason you have to install some extentions https://github.com/googleapis/googleapis (I used https://github.com/googleapis/googleapis/tree/004b289eebc86f663d4f9b3aec9a9bc6df49dd8d)

    git clone https://github.com/googleapis/googleapis.git 
    set GOOGLEAPIS_DIR=<path to this folder>\googleapis

Then edit ```GOOGLEAPIS_DIR``` in ```grpc_api_for_software\original_software\proto\compile.bat```. 

> **NOTE**
>   
>   You will need only tree files (already in .bat file):
>   
>       %GOOGLEAPIS_DIR%\google\api\annotations.proto 
>       %GOOGLEAPIS_DIR%\google\api\http.proto 
>       %GOOGLEAPIS_DIR%\google\rpc\status.proto
>   
>   After compiling you will see automatically generated source files for certain language in ```src\proto_compiled``` in apropriate client or server. And ```api_descriptor.pb``` in ```grpc_api_for_software\original_software\proto```

Build .proto with protoc
------------------------

Do not edit manually anything in ```src\proto_compiled``` (in apropriate client or server). This files are generated automatically by calling ```grpc_api_for_software\original_software\proto\compile.bat```