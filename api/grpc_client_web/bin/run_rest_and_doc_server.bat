@echo off
@setlocal
rem Read common env vars from file
for /F "usebackq tokens=*" %%A in ("../../env_vars_common.txt") do set %%A
cd ..
call go run main.go --grpc_server_address "dns:///0.0.0.0:%GRPC_PORT%" --api_rest_doc_server_address "0.0.0.0:%GRPC_REST_PORT%"
@endlocal
pause