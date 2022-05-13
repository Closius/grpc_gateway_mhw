@echo off
@setlocal
rem Read common env vars from file
for /F "usebackq tokens=*" %%A in ("../../env_vars_common.txt") do set %%A
set "THIS_FOLDER=%~dp0"
rem set GRPC_VERBOSITY=debug
rem set GRPC_TRACE=all
rem %USERPROFILE%\.grpc_client_NAME_python\client_llloggg
set "PATH=%gRPC_INSTALL_DIR%\bin;%PATH%"
call "%THIS_FOLDER%\..\Release\client_cpp.exe" %GRPC_PORT%
@endlocal
pause
