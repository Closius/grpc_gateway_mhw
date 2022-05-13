
Prerequisites
-------------

    https://github.com/grpc/grpc/blob/master/BUILDING.md#windows

    Visual Studio 2019
    Git
    CMake
    nasm and add it to PATH (choco install nasm) - required by boringssl
    (Optional) Install Ninja (choco install ninja)

    https://github.com/googleapis/googleapis for HTTP transcoding (REST)

Build & install gRPC
--------------------

gRPC sould be built from source and installed. The installation means just copying certain files (particularly .h and .lib) into convenient organisation 

    cd D:\distr\cpp\grpc   # this is just empty folder
    git clone --recurse-submodules -b v1.45.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc
    cd grpc

gRPC_INSTALL_DIR - is a dir, where gRPC buil files will be organized after build and install. These folders/files you can use in you C++ project. For convenience it is set in ```./api/env_vars_common.txt```

    cd cmake
    mkdir build
    cd build
    mkdir installed
    cd installed
    mkdir bin
    cd ..  
    set gRPC_INSTALL_DIR=D:\distr\cpp\grpc\cmake\build\installed

Add to PATH: NASM (```C:\Program Files\NASM```), ```%gRPC_INSTALL_DIR%\bin```, Cmake (```C:\Program Files\CMake\bin```)

> **NOTE** ```%gRPC_INSTALL_DIR%\bin``` is not really necessary to add to PATH on this step

> **NOTE** This is my PATH:
>
>   - D:\distr\cpp\grpc\cmake\build\installed\bin
>   - C:\Program Files\NASM
>   - C:\Program Files\CMake\bin
>   - C:\WINDOWS\system32
>   - C:\WINDOWS
>   - C:\WINDOWS\System32\Wbem
>   - C:\WINDOWS\System32\WindowsPowerShell\v1.0\
>   - C:\WINDOWS\System32\OpenSSH\
>   - C:\Program Files (x86)\Common Files\Pulse Secure\VC142.CRT\X64\
>   - C:\Program Files (x86)\Common Files\Pulse Secure\VC142.CRT\X86\
>   - C:\Program Files (x86)\Pulse Secure\VC142.CRT\X64\
>   - C:\Program Files (x86)\Pulse Secure\VC142.CRT\X86\
>   - C:\Program Files\Zulu\zulu-8-jre\bin
>   - C:\Program Files\IcedTeaWeb\WebStart\bin
>   - C:\Program Files\Git\cmd
>   - C:\Program Files\dotnet\
>   - C:\Program Files\Siemens\NX2007\CAPITALINTEGRATION\capitalnxremote\
>   - C:\Program Files\TortoiseSVN\bin
>   - C:\Program Files\Docker\Docker\resources\bin
>   - C:\ProgramData\DockerDesktop\version-bin
>   - C:\Users\mdkk4v\AppData\Local\Microsoft\WindowsApps
>   - D:\distr


    cmake -DgRPC_INSTALL=ON -DgRPC_MSVC_STATIC_RUNTIME=ON  -DgRPC_ABSL_PROVIDER=module  -DgRPC_CARES_PROVIDER=module  -DgRPC_PROTOBUF_PROVIDER=module  -DgRPC_RE2_PROVIDER=module  -DgRPC_SSL_PROVIDER=module  -DgRPC_ZLIB_PROVIDER=module -DCMAKE_INSTALL_PREFIX=%gRPC_INSTALL_DIR% ..\.. > cmake_1_log.txt
    cmake --build . --config Release > cmake_build_log.txt
    cmake --install . --config Release > cmake_install_log.txt

Please see the reference of the content of ```%gRPC_INSTALL_DIR%``` in ```misc/gRPC_INSTALL_DIR_tree.txt``` 

googleapis
----------

The project assume that we are using HTTP transcoding for comunication by REST with gRPC. https://cloud.google.com/endpoints/docs/grpc/transcoding

For this reason you have to install some extentions https://github.com/googleapis/googleapis

Actiually this C++ client doesn't use this calls, but I'm not sure.

    git clone https://github.com/googleapis/googleapis.git 
    set GOOGLEAPIS_DIR=<path to this folder>\googleapis

Then edit ```GOOGLEAPIS_DIR``` in ```../bin/compile_all_protos.bat``` or ```./api/env_vars_common.txt```. 

> **NOTE**
>   
>   You will need only tree files (already in .bat file):
>   
>       %GOOGLEAPIS_DIR%\google\api\annotations.proto 
>       %GOOGLEAPIS_DIR%\google\api\http.proto 
>       %GOOGLEAPIS_DIR%\google\rpc\status.proto
>   
>   After compiling you will see ```.cc``` and ```.h``` files in ```src/proto_compiled```

Build .proto with protoc
------------------------

Do not edit manually anything in ```src/proto_compiled```. These files are generated automatically by calling ```../bin/compile_all_protos.bat```

Cmake build
-----------

Alternatively you can build using Cmake: https://github.com/grpc/grpc/tree/master/src/cpp#fetchcontent


Run
---

```bin/run_cpp_client.bat```


Reference projects
------------------

https://github.com/plasticbox/grpc-windows

https://github.com/leimao/gRPC-Examples