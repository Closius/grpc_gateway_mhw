#include <iostream>
#include <memory>
#include <string>

#include <grpcpp/grpcpp.h>
#include <google/protobuf/empty.pb.h>
#include <google/protobuf/util/json_util.h>

#include <calculator.pb.h>
#include <calculator.grpc.pb.h>


//using namespace grpc;
//using namespace calculator;
//using namespace std;


class CalculatorClient {
public:
    CalculatorClient(std::shared_ptr<grpc::Channel> channel) : _stub{ calculator::Calculator::NewStub(channel) } {}

    int32_t test_NewTestSet() {
        // Prepare request
        google::protobuf::Empty request;

        // Send request
        calculator::NewTestSet_response response;
        grpc::ClientContext context;
        grpc::Status status;
        status = _stub->NewTestSet(&context, request, &response);

        // Handle response
        if (status.ok()) {
            return response.message();
        }
        else {
            throw std::runtime_error(std::to_string(status.error_code()) + ": " + status.error_message());
        }
    }

    void test_ChangeSettings(std::string name, int32_t identifier, std::string opt_field1_str, float opt_field3_float,
        std::vector<std::string> opt_field5_rep_str, int32_t opt_field4_int = NULL /*optional*/, int32_t opt_field2_int = NULL /*optional*/) {
        // Prepare request
        calculator::ChangeSettings_request request;
        request.set_name(name);
        request.set_identifier(identifier);
        calculator::ChangeSettings_request::Options optoins_1;
        optoins_1.set_field1_str(opt_field1_str);
        optoins_1.set_field3_float(opt_field3_float);
        *optoins_1.mutable_field5_rep_str() = { opt_field5_rep_str.begin(), opt_field5_rep_str.end() }; // for (int j = 0; j < opt_field5_rep_str.size(); j++) { optoins_1.add_field5_rep_str(opt_field5_rep_str[j]); }
        if (opt_field4_int != NULL) { optoins_1.set_field4_int(opt_field4_int); }
        if (opt_field2_int != NULL) { optoins_1.set_field2_int(opt_field2_int); }
        request.mutable_options()->AddAllocated(&optoins_1); //https://developers.google.com/protocol-buffers/docs/reference/arenas#set-allocatedadd-allocatedrelease

        // Send request
        google::protobuf::Empty response;
        grpc::ClientContext context;
        grpc::Status status;
        status = _stub->ChangeSettings(&context, request, &response);
        request.mutable_options()->ReleaseLast(); //https://developers.google.com/protocol-buffers/docs/reference/arenas#set-allocatedadd-allocatedrelease


        // Handle response
        if (status.ok()) {
            return;
        }
        else {
            throw std::runtime_error(std::to_string(status.error_code()) + ": " + status.error_message());
        }
    }

    float test_DoMath(float a, float b, std::string operator__) {
        // Prepare request
        calculator::DoMath_request request;
        request.set_a(a);
        request.set_b(b);
        request.set_operator_(operator__); // 'operator' is a reserved word for C++, I think :)

        // Send request
        calculator::DoMath_response response;
        grpc::ClientContext context;
        grpc::Status status;
        status = _stub->DoMath(&context, request, &response);

        // Handle response
        if (status.ok()) {
            return response.message();
        }
        else {
            throw std::runtime_error(std::to_string(status.error_code()) + ": " + status.error_message());
        }
    }

    std::string test_ListToDict(std::vector<std::string> seq_k_str, std::vector<std::int32_t> seq_v_int) {
        // Prepare request
        calculator::ListToDict_request request;
        *request.mutable_seq_k_str() = { seq_k_str.begin(), seq_k_str.end() };
        *request.mutable_seq_v_int() = { seq_v_int.begin(), seq_v_int.end() };

        // Send request
        std::string json_string_response;
        calculator::ListToDict_response response;
        grpc::ClientContext context;
        grpc::Status status;
        status = _stub->ListToDict(&context, request, &response);
        request.mutable_seq_k_str()->UnsafeArenaReleaseLast();
        //request.mutable_seq_v_int()->ReleaseLast();

        google::protobuf::util::MessageToJsonString(response, &json_string_response);

        // Handle response
        if (status.ok()) {
            return json_string_response;
        }
        else {
            throw std::runtime_error(std::to_string(status.error_code()) + ": " + status.error_message());
        }
    }

    std::string test_DictToList(std::vector < std::string> keys, std::vector < std::vector<std::int32_t>> values) {
        // Prepare request
        calculator::DictToList_request request;
        std::vector<calculator::DictToList_request::DictMes > tmp_dictsss;
        tmp_dictsss.reserve(keys.size());
        tmp_dictsss.resize(keys.size());
        for (int j = 0; j < keys.size(); j++)
        {
            tmp_dictsss[j].set_k(keys[j]);
            *tmp_dictsss[j].mutable_v() = { values[j].begin(), values[j].end() };
            request.mutable_dict_smpl()->UnsafeArenaAddAllocated(&tmp_dictsss[j]);
        };

        // Send request
        std::string json_string_response;
        calculator::DictToList_response response;
        grpc::ClientContext context;
        grpc::Status status;
        status = _stub->DictToList(&context, request, &response);
        for (int j = keys.size() - 1; j >= 0; j--)
        {
            request.mutable_dict_smpl()->UnsafeArenaReleaseLast();
        };
        google::protobuf::util::MessageToJsonString(response, &json_string_response);

        // Handle response
        if (status.ok()) {
            return json_string_response;
        }
        else {
            throw std::runtime_error(std::to_string(status.error_code()) + ": " + status.error_message());
        }
    }

    void test_StartLongProcessStreaming(std::string sequence) {
        calculator::StartLongProcessStreaming_request request;
        request.set_sequence(sequence);

        calculator::StartLongProcessStreaming_response response;
        grpc::ClientContext context;

        std::unique_ptr<grpc::ClientReader<calculator::StartLongProcessStreaming_response> > reader(
            _stub->StartLongProcessStreaming(&context, request));

        while (reader->Read(&response)) {
            std::cout << response.message() << std::endl;
        }
        grpc::Status status = reader->Finish();
        if (status.ok()) {
            std::cout << "StartLongProcessStreaming rpc succeeded." << std::endl;
        }
        else {
            std::cout << "StartLongProcessStreaming rpc failed." << std::endl;
        }
    }

private:
    std::unique_ptr<calculator::Calculator::Stub> _stub;
};

int main(int argc, char** argv) {
    std::cout << "gRPC port: " << argv[1] << std::endl;
    std::string server_address{ "localhost:" + std::string(argv[1]) };
    CalculatorClient client{ grpc::CreateChannel(server_address, grpc::InsecureChannelCredentials()) };
    std::cout << "----------------------------------------------------------------------" << std::endl;
    std::cout << "Test1 NewTestSet: " << std::endl;
    std::cout << "\tResponse: " << client.test_NewTestSet() << std::endl;
    std::cout << " Passed" << std::endl;
    std::cout << "----------------------------------------------------------------------" << std::endl;
    std::cout << "Test2 ChangeSettings: ";
    try {
        client.test_ChangeSettings(
            "Hey",          /*name*/
            231,            /*identifier*/
            "sdfsdv",       /*opt_field1_str*/
            5555.34,        /*opt_field3_float*/
            { "ds", "hj" }, /*opt_field5_rep_str*/
            43,             /*opt_field4_int, optional*/
            987             /*opt_field2_int, optional*/
        );
    }
    catch (const std::exception& e) {
        std::cout << "Exception: " << e.what() << std::endl;
    }
    std::cout << " Passed" << std::endl;
    std::cout << "----------------------------------------------------------------------" << std::endl;
    std::cout << "Test3 ChangeSettings: ";
    try {
        client.test_ChangeSettings(
            "Bye",                      /*name*/
            777,                        /*identifier*/
            "GHGVHsdfsdv",              /*opt_field1_str*/
            111.34                      /*opt_field3_float*/,
            { "III", "kbhvgh", "vxth" }  /*opt_field5_rep_str*/
        );
    }
    catch (const std::exception& e) {
        std::cout << "Exception: " << e.what() << std::endl;
    }
    std::cout << " Passed" << std::endl;
    std::cout << "----------------------------------------------------------------------" << std::endl;
    std::cout << "Test4 DoMath: " << std::endl;
    try {
        std::cout << "\tResponse: " << client.test_DoMath(
            5.3 /*a*/,
            8.1 /*b*/,
            "+" /*operator*/) << std::endl;
    }
    catch (const std::exception& e) {
        std::cout << "Exception: " << e.what() << std::endl;
    }
    std::cout << " Passed" << std::endl;
    std::cout << "----------------------------------------------------------------------" << std::endl;
    std::cout << "Test5 DoMath with exception: " << std::endl;
    try {
        std::cout << "\tResponse: " << client.test_DoMath(
            5.3     /*a*/,
            8.1     /*b*/,
            "sd+"   /*operator*/) << std::endl;
    }
    catch (const std::exception& e) {
        std::cout << "Exception: " << e.what() << std::endl;
    }
    std::cout << " Passed" << std::endl;
    std::cout << "----------------------------------------------------------------------" << std::endl;
    std::cout << "Test6 ListToDict: " << std::endl;
    try {
        std::cout << "\tResponse: " << client.test_ListToDict(
            { "a", "b", "c" }     /*seq_k_str*/,
            { 1, 2, 3 }           /*seq_v_int*/) << std::endl;
    }
    catch (const std::exception& e) {
        std::cout << "Exception: " << e.what() << std::endl;
    }
    std::cout << " Passed" << std::endl;
    std::cout << "----------------------------------------------------------------------" << std::endl;
    std::cout << "Test7 DictToList: " << std::endl;
    try {
        std::cout << "\tResponse: " << client.test_DictToList(
            { "a", "b", "c" }                           /*keys*/,
            { {1, 2, 3}, {44,22,33}, {0,3,0,0,22,2} }   /*values*/) << std::endl;
    }
    catch (const std::exception& e) {
        std::cout << "Exception: " << e.what() << std::endl;
    }
    std::cout << " Passed" << std::endl;
    std::cout << "----------------------------------------------------------------------" << std::endl;
    std::cout << "Test8 StartLongProcessStreaming: " << std::endl;
    client.test_StartLongProcessStreaming("Three Rings for the Elven-kings under the sky, Seven for the Dwarf-lords in their halls of stone, \
        Nine for Mortal Men doomed to die, One for the Dark Lord on his dark throne In the Land of Mordor where the Shadows lie. \
        One Ring to rule them all, One Ring to find them, One Ring to bring them all, and in the darkness bind them, In the Land \
        of Mordor where the Shadows lie.");
    std::cout << "-------------------------------- all --------------------------------------" << std::endl;
    std::cout << "All tests PASSED" << std::endl;


    return 0;
}