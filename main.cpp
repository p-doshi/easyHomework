#include <iostream>
#include <cpprest/http_client.h>

using namespace std;
using namespace web;
using namespace web::http;
using namespace web::http::client;

int main() {
    // Create HTTP client
    http_client client(U("http://localhost:8080"));

    // Prepare HTTP request
    http_request request(methods::POST);
    request.set_request_uri(U("/"));
    request.headers().set_content_type(U("multipart/form-data"));

    // Send HTTP request
    client.request(request).then([](http_response response) {
        // Handle response
        if (response.status_code() == status_codes::OK) {
            auto json_body = response.extract_json().get();
            auto extracted_text = json_body["text"].as_string();
            cout << "Extracted text: " << extracted_text << endl;
            processtext(extracted_text)
        } else {
            cout << "Error: " << response.status_code() << endl;
        }
    }).wait();

    return 0;
}
