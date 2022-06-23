@echo off
@setlocal
rem Read common env vars from file
for /F "usebackq tokens=*" %%A in ("../../env_vars_common.txt") do set %%A
rem Clone google APIs if not already download
set GOOGLEAPIS_DIR=../../third_party_tools/googleapis
git clone https://github.com/googleapis/googleapis %GOOGLEAPIS_DIR%
rem Clone grpc-gateway if not already download
set GRPC_GATEWAY_DIR=../../third_party_tools/grpc-gateway
git clone https://github.com/grpc-ecosystem/grpc-gateway %GRPC_GATEWAY_DIR%
rem folder where you have .proto files
set PROTO_FOLDER=../../proto
rem I think it is better to use the same protoc.exe for building for different languages
rem at least the same version
echo "Compiling for grpc_server_python..."
call %_PYTHON% -m grpc_tools.protoc --python_out=../../grpc_server_python/proto_compiled ^
    --grpc_python_out=../../grpc_server_python/proto_compiled ^
    -I %PROTO_FOLDER% -I %GOOGLEAPIS_DIR% -I %GRPC_GATEWAY_DIR% ^
    %PROTO_FOLDER%/calculator.proto  ^
    %GRPC_GATEWAY_DIR%\protoc-gen-openapiv2\options\annotations.proto ^
    %GRPC_GATEWAY_DIR%\protoc-gen-openapiv2\options\openapiv2.proto ^
    %GRPC_GATEWAY_DIR%\internal\descriptor\apiconfig\apiconfig.proto ^
    %GRPC_GATEWAY_DIR%\internal\descriptor\openapiconfig\openapiconfig.proto
echo "Compiling for grpc_client_python..."
call %_PYTHON% -m grpc_tools.protoc --python_out=../../grpc_client_python/proto_compiled ^
    --grpc_python_out=../../grpc_client_python/proto_compiled ^
    -I %PROTO_FOLDER% -I %GOOGLEAPIS_DIR% -I %GRPC_GATEWAY_DIR% ^
    %PROTO_FOLDER%/calculator.proto ^
    %GRPC_GATEWAY_DIR%\protoc-gen-openapiv2\options\annotations.proto ^
    %GRPC_GATEWAY_DIR%\protoc-gen-openapiv2\options\openapiv2.proto ^
    %GRPC_GATEWAY_DIR%\internal\descriptor\apiconfig\apiconfig.proto ^
    %GRPC_GATEWAY_DIR%\internal\descriptor\openapiconfig\openapiconfig.proto
echo "Compiling for grpc_client_cpp..."
set OUTPUT_PROTO=../../grpc_client_cpp/src/proto_compiled
call %gRPC_INSTALL_DIR%\bin\protoc.exe ^
    --grpc_out=%OUTPUT_PROTO% ^
    --cpp_out=%OUTPUT_PROTO% ^
    --plugin=protoc-gen-grpc=%gRPC_INSTALL_DIR%\bin\grpc_cpp_plugin.exe ^
    -I %PROTO_FOLDER% -I %gRPC_INSTALL_DIR%\include -I %GOOGLEAPIS_DIR% -I %GRPC_GATEWAY_DIR% ^
    %PROTO_FOLDER%/calculator.proto ^
    %GOOGLEAPIS_DIR%\google\api\annotations.proto ^
    %GOOGLEAPIS_DIR%\google\api\http.proto ^
    %GOOGLEAPIS_DIR%\google\rpc\status.proto ^
    %GRPC_GATEWAY_DIR%\protoc-gen-openapiv2\options\annotations.proto ^
    %GRPC_GATEWAY_DIR%\protoc-gen-openapiv2\options\openapiv2.proto ^
    %GRPC_GATEWAY_DIR%\internal\descriptor\apiconfig\apiconfig.proto ^
    %GRPC_GATEWAY_DIR%\internal\descriptor\openapiconfig\openapiconfig.proto
echo "Compiling for grpc_client_web and Swagger file(s)..."
call %_PYTHON% -m grpc_tools.protoc ^
    -I %PROTO_FOLDER% -I %GOOGLEAPIS_DIR% -I %GRPC_GATEWAY_DIR% ^
    --go_out ../../grpc_client_web/proto_compiled --go_opt paths=source_relative ^
    --go-grpc_out ../../grpc_client_web/proto_compiled --go-grpc_opt paths=source_relative ^
    --grpc-gateway_out ../../grpc_client_web/proto_compiled --grpc-gateway_opt paths=source_relative ^
    --openapiv2_out ../../grpc_client_web/third_party/OpenAPI ^
    %PROTO_FOLDER%/calculator.proto
@endlocal
pause

