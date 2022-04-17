@echo off
@setlocal
set "THIS_FOLDER=%~dp0"
set "GOOGLEAPIS_DIR=D:\personal\github\distr\googleapis"
rem set GRPC_VERBOSITY=debug
rem set GRPC_TRACE=api
rem %USERPROFILE%\.grpc_server_NAME_python\server_llloggg
rem set "PATH=%GOOGLEAPIS_DIR%;%PATH%"
set "PYTHONPATH=%GOOGLEAPIS_DIR%;..\grpc_server_python;..\grpc_server_python\proto_compiled"
call C:\Python388\python.exe "%THIS_FOLDER%\..\calculator.py"
@endlocal
pause