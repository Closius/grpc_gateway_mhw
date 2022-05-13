@echo off
@setlocal
rem Read common env vars from file
for /F "usebackq tokens=*" %%A in ("../env_vars_common.txt") do set %%A
rem git clone https://github.com/googleapis/googleapis
set GOOGLEAPIS_DIR=../third_party_tools/googleapis
rem set GRPC_VERBOSITY=debug
rem set GRPC_TRACE=api
set "PYTHONPATH=%GOOGLEAPIS_DIR%;..\grpc_server_python;..\grpc_server_python\proto_compiled"
call %_PYTHON% "..\..\calculator.py"
@endlocal
pause