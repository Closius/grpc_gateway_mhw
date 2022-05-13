Overview:
---------

This is a Go-based HTTPS proxy server which implements RESTfull service for gRPC client 
and [Swagger](https://en.wikipedia.org/wiki/Swagger_(software)) interactive autodoc from which you 
can test gRPC requests using REST requests like GET, POST etc.

gRPC server ```../bin/run_software_with_python_server.bat``` serves on port ```50051``` over TCP/IP (not HTTP). Currently, without SSL. 
Go-based HTTPS proxy server translates requests/responses from HTTPS to gRPC there and back. It serves on [https://localhost:11000/api](https://localhost:11000/api)

Documentation: ```../bin/compile_all_protos.bat``` also generates 
swagger file ```third_party/OpenAPI/calculator.swagger.json```. This file defines Doc web page. 
The interactive, automatically generated documentation available on [https://localhost:11000](https://localhost:11000).

All commont env vars such as server port or grpc resr port are defined in ```./api/env_vars_common.txt```

> *Note*
> 
> It is the self-signed example. So don't worry if you see the warning message in your browser

Alternatives:
-------------

There is two alternatives: [gRPC-web](https://github.com/grpc/grpc-web) and [gRPC-gateway](https://github.com/grpc-ecosystem/grpc-gateway)

Description about differences: [https://jbrandhorst.com/post/grpc-in-the-browser/](https://jbrandhorst.com/post/grpc-in-the-browser/)

Here is the implementation of gRPC-gateway.

Original tutorial:
------------------

https://grpc-ecosystem.github.io/grpc-gateway/docs/tutorials/introduction/

Based on: https://github.com/johanbrandhorst/grpc-gateway-boilerplate/commit/521a9559341e6e081ff154ba03efd049990ef93d

Prerequisites:
--------------
    
    Go: https://go.dev/doc/install   (go1.18.1)

    git clone https://github.com/googleapis/googleapis  # https://github.com/googleapis/googleapis/tree/740f0727337b87ea29fd56802f0ba999bfbf15b5
    git clone https://github.com/grpc-ecosystem/grpc-gateway  # https://github.com/grpc-ecosystem/grpc-gateway/tree/2ce32afe5735d0bfa28ee3369e5975dfb8192313

    All commont env vars such as server port or grpc resr port are defined in ```./api/env_vars_common.txt```

Check before run:
-----------------


1. ```../proto/calculator.proto```:
   Here is the main definition of the API
   ```
   ...
    option go_package = "url_to_your_git_repo/grpc_client_web";
   ...
   ```
   this is the path to the repo where Go will take a module. Actually it can be any name, but better to set the URL to the repo. 
   Pay attention on this as well in ```gateway/gateway.go```, ```main.go```, ```go.mod```
2. Run ```go mod tidy``` to adjust packages and get necessary repos for Go acording to ```go.mod```
3. ```../bin/compile_all_protos.bat```:
   The key ```--openapiv2_out ../grpc_client_web/third_party/OpenAPI``` is responsible for generation of swagger file ```third_party/OpenAPI/calculator.swagger.json```
4. The reference to the swagger file is also exists in ```third_party/OpenAPI/index.html```
5. SSL certificate is located in ```insecure/insecure.go```
6. I set a not secure connection gRPC python server - REST proxy server. Check ```gateway/gateway.go```:
   ```
   ...
           grpc.WithTransportCredentials(grpc_insecure.NewCredentials()),
   // 		grpc.WithTransportCredentials(credentials.NewClientTLSFromCert(insecure.CertPool, "")),
   ...
   ```
   That is why you will see ```http: TLS handshake error from [::1]:52887: remote error: tls: unknown certificate``` in the output of REST proxy server.
   TODO: Setup SSL in gRPC Python server.
7. Set the port number to gRPC python server in ```main.go```
8. Set the port number REST proxy server and swagger doc in ```gateway/gateway.go```
9. Actually ```main.go``` and ```gateway/gateway.go``` can be merged...

Compile .proto and swagger file(s):
-----------------------------------

    ../bin/compile_all_protos.bat

Run:
----

1. Run main gRPC server ```../bin/run_software_with_python_server.bat```. Run on port ```50051```
2. Run RESTfull proxy server ```bin/run_rest_server.bat```. Run on ```https://localhost:11000/api```
3. Open the interactive doc in browser: [https://localhost:11000](https://localhost:11000). There you can also test requests
4. Test ```curl --insecure -X POST "https://localhost:11000/api/DoMath" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"a\": 2,  \"b\": 4,  \"operator\": \"+\"}"```
5. Test Streaming ```bin/curl_client_stream.bat```

third_party:
------------

Taken from https://github.com/johanbrandhorst/grpc-gateway-boilerplate/tree/master/third_party

This directory contains ("vendors") abbreviated copies of the following repositories:

* OpenAPI - https://github.com/swagger-api/swagger-ui 07a0416ff664583ff9f481cae7dace226c9f61ec (LICENSE, dist/)

The third_party/OpenAPI directory contains HTML, Javascript,
and CSS assets that dynamically generate Swagger documentation from a
Swagger-compliant API definition in ```third_party/OpenAPI/calculator.swagger.json```
file. The static assets are copied from
[this dist folder](https://github.com/swagger-api/swagger-ui/tree/master/dist)
of the OpenAPI-UI project. After copying, [`index.html`](./OpenAPI/index.html)
is edited to load the swagger file from the local server instead of the default petstore.

See the respective LICENSE files for each project for the applicable license terms.

insecure:
---------

> *Warning*
> 
> Generate your own SSL pairs before using in production. Better to get it from some Certificate Authority company. Siemens has it as well

Contains self signed certificate couple:

```
Subject Alternative Names: localhost, IP Address:0.0.0.0, IP Address:127.0.0.1
Organization: Acme Co
Valid From: February 22, 2018
Valid To: March 22, 2132
Issuer: Acme Co
Serial Number: 223e01b8eb50456c6f500e0251a2fe5a
```

Useful links:
-------------

https://cloud.google.com/apis/design

https://cloud.google.com/endpoints/docs/grpc/transcoding

https://github.com/grpc-ecosystem/grpc-gateway