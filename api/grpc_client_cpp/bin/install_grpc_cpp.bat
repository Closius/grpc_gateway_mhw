@echo off
@setlocal
set "__NASM=C:\Program Files\NASM"
set "__cmake=C:\Program Files\CMake\bin"
rem Read common env vars from file
for /F "usebackq tokens=*" %%A in ("../../env_vars_common.txt") do set %%A
set "THIS_FOLDER=%~dp0"
git clone --recurse-submodules -b v1.45.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc %gRPC_CPP_DIR%
mkdir %gRPC_CPP_DIR%\cmake\build
mkdir %gRPC_CPP_DIR%\cmake\build\installed
mkdir %gRPC_CPP_DIR%\cmake\build\installed\bin
set "PATH=%__NASM%;%__cmake%;%gRPC_INSTALL_DIR%\bin;%PATH%"
echo "cmake | See log: %THIS_FOLDER%\cmake_log.txt"
cmake -DgRPC_INSTALL=ON -DgRPC_MSVC_STATIC_RUNTIME=ON  -DgRPC_ABSL_PROVIDER=module  -DgRPC_CARES_PROVIDER=module  -DgRPC_PROTOBUF_PROVIDER=module  -DgRPC_RE2_PROVIDER=module  -DgRPC_SSL_PROVIDER=module  -DgRPC_ZLIB_PROVIDER=module -DCMAKE_INSTALL_PREFIX=%gRPC_INSTALL_DIR% -S %gRPC_CPP_DIR% -B %gRPC_CPP_DIR%\cmake\build > %THIS_FOLDER%\cmake_log.txt
echo "cmake --build | See log: %THIS_FOLDER%\cmake_build_log.txt"
cmake --build %gRPC_CPP_DIR%\cmake\build --config Release > %THIS_FOLDER%\cmake_build_log.txt
echo "cmake --install | See log: %THIS_FOLDER%\cmake_install_log.txt"
cmake --install %gRPC_CPP_DIR%\cmake\build --config Release > %THIS_FOLDER%\cmake_install_log.txt
echo "Instalation completed. ALL DONE"
echo IMPORTANT: go to https://sourceforge.net/projects/boost/files/boost-binaries/1.64.0/ download boost_1_64_0-msvc-14.1-64.exe and install into ..\..\third_party_tools\boost_1_64_0
@endlocal
pause