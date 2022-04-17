@echo off
@setlocal
set "THIS_FOLDER=%~dp0"
rem git clone https://github.com/googleapis/googleapis
set GOOGLEAPIS_DIR=D:\personal\github\distr\googleapis
rem git clone https://github.com/grpc-ecosystem/grpc-gateway
set GRPC_GATEWAY_DIR=D:\personal\github\distr\gateway\grpc-gateway
echo "Compiling for grpc_server_python..."
call C:\Python388\python.exe -m grpc_tools.protoc -I. --python_out=../grpc_server_python/proto_compiled --grpc_python_out=../grpc_server_python/proto_compiled -I=%GOOGLEAPIS_DIR% -I=%GRPC_GATEWAY_DIR% --include_imports --descriptor_set_out=api_descriptor.pb calculator.proto
echo "Compiling for grpc_client_python..."
call C:\Python388\python.exe -m grpc_tools.protoc -I. --python_out=../../grpc_client_python/proto_compiled --grpc_python_out=../../grpc_client_python/proto_compiled -I=%GOOGLEAPIS_DIR% -I=%GRPC_GATEWAY_DIR% --include_imports --descriptor_set_out=api_descriptor.pb calculator.proto
echo "Compiling for grpc_client_cpp..."
set gRPC_INSTALL_DIR=D:\personal\github\distr\cpp\grpc\cmake\build\installed
set OUTPUT_PROTO=../../grpc_client_cpp/src/proto_compiled
%gRPC_INSTALL_DIR%\bin\protoc.exe calculator.proto %GOOGLEAPIS_DIR%\google\api\annotations.proto %GOOGLEAPIS_DIR%\google\api\http.proto %GOOGLEAPIS_DIR%\google\rpc\status.proto %GRPC_GATEWAY_DIR%\protoc-gen-openapiv2\options\annotations.proto %GRPC_GATEWAY_DIR%\protoc-gen-openapiv2\options\openapiv2.proto --grpc_out=%OUTPUT_PROTO% --plugin=protoc-gen-grpc=%gRPC_INSTALL_DIR%\bin\grpc_cpp_plugin.exe -I=%THIS_FOLDER% -I=%gRPC_INSTALL_DIR%\include  -I=%GOOGLEAPIS_DIR% -I %GRPC_GATEWAY_DIR% --include_imports --descriptor_set_out=api_descriptor.pb
%gRPC_INSTALL_DIR%\bin\protoc.exe calculator.proto %GOOGLEAPIS_DIR%\google\api\annotations.proto %GOOGLEAPIS_DIR%\google\api\http.proto %GOOGLEAPIS_DIR%\google\rpc\status.proto %GRPC_GATEWAY_DIR%\protoc-gen-openapiv2\options\annotations.proto %GRPC_GATEWAY_DIR%\protoc-gen-openapiv2\options\openapiv2.proto --cpp_out=%OUTPUT_PROTO% -I=%THIS_FOLDER% -I=%gRPC_INSTALL_DIR%\include  -I=%GOOGLEAPIS_DIR% -I %GRPC_GATEWAY_DIR% --descriptor_set_out=api_descriptor.pb
echo "Compiling for grpc_client_web..."
call C:\Python388\python.exe -m grpc_tools.protoc -I . -I %GOOGLEAPIS_DIR% -I %GRPC_GATEWAY_DIR% --go_out ../../grpc_client_web/proto_compiled --go_opt paths=source_relative --go-grpc_out ../../grpc_client_web/proto_compiled --go-grpc_opt paths=source_relative --grpc-gateway_out ../../grpc_client_web/proto_compiled --grpc-gateway_opt paths=source_relative calculator.proto
@endlocal
pause

