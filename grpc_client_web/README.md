Overview
--------

https://cloud.google.com/apis/design

https://cloud.google.com/endpoints/docs/grpc/transcoding

Original tutorial:

https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/introduction/

https://github.com/grpc-ecosystem/grpc-gateway


Prerequisites
-------------
    
    Go: https://go.dev/doc/install   (go1.18.1)

    pip install googleapis-common-protos
    git clone https://github.com/googleapis/googleapis

    git clone https://github.com/grpc-ecosystem/grpc-gateway

Install:
--------

    go mod tidy


Compile .proto
--------------

    grpc_api_for_software\original_software\proto\compile.bat

Run:
----

1. Run main gRPC server ```\original_software\grpc_server_python\bin\run_server.bat```. Run on ```localhost:50051```
2. Run ```go run restful_server.go```. Run on ```localhost:8090```
3. Test ```curl -X POST -k http://localhost:8090/domath -d "{\"a\":4, \"b\": 20, \"operator\":\"+\"}"```