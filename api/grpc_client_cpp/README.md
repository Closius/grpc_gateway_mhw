
Prerequisites
-------------

    https://github.com/grpc/grpc/blob/master/BUILDING.md#windows

    Visual Studio 2019
    Git
    CMake
    nasm and add it to PATH (choco install nasm) - required by boringssl
    (Optional) Install Ninja (choco install ninja)

    https://github.com/googleapis/googleapis for HTTP transcoding (REST)

in VS project:

    src/proto_compiled/google <-- https://github.com/googleapis/googleapis 
    src/proto_compiled/internal <-- https://github.com/grpc-ecosystem/grpc-gateway
    src/proto_compiled/protoc-gen-openapiv2 <-- https://github.com/grpc-ecosystem/grpc-gateway

Build & install gRPC
--------------------


    bin/install_grpc_cpp.bat


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