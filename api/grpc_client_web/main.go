package main

import (
	"flag"
	"io/ioutil"
	"os"

	"url_to_your_git_repo/grpc_client_web/gateway"
	"google.golang.org/grpc/grpclog"
)

var gRPC_serverAddress = flag.String(
	"grpc_server_address",
	"dns:///0.0.0.0:50051",
	"The address to the gRPC server, in the gRPC standard naming format. "+
		"See https://github.com/grpc/grpc/blob/master/doc/naming.md for more information.",
)

var api_REST_DOC_serverAddress = flag.String(
	"api_rest_doc_server_address",
	"0.0.0.0:11000",
	"The address to the RESTfull HTTPS proxy server and autodoc, in the gRPC standard naming format. "+
		"See https://github.com/grpc/grpc/blob/master/doc/naming.md for more information.",
)

var serve_http = flag.String(
	"serve_http",
	"false",
	"if true use HTTP instead of HTTPS",
)

func main() {
	flag.Parse()

	// Adds gRPC internal logs. This is quite verbose, so adjust as desired!
	log := grpclog.NewLoggerV2(os.Stdout, ioutil.Discard, ioutil.Discard)
	grpclog.SetLoggerV2(log)

	err := gateway.Run(*gRPC_serverAddress, *api_REST_DOC_serverAddress, *serve_http)
	log.Fatalln(err)
}