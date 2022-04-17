@echo off
@setlocal
set "THIS_FOLDER=%~dp0"
rem set GRPC_VERBOSITY=debug
rem set GRPC_TRACE=all
rem %USERPROFILE%\.grpc_client_NAME_python\client_llloggg
set gRPC_INSTALL_DIR=D:\personal\github\distr\cpp\grpc\cmake\build\installed
set "PATH=%gRPC_INSTALL_DIR%\bin;%PATH%"
call "%THIS_FOLDER%\..\Release\client_cpp.exe"
@endlocal
pause
