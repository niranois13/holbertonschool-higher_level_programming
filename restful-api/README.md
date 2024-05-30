# API Basics

This README is based on a series of questions asked by our SWE to introduce APIs.

## 1. What is an API?

An API or Application Programming Interface is a set of rules and protocols that allows one software application to interact with another. It defines the methods and data formats that applications can use to communicate with each other, facilitating the integration of different software systems.

## 2. What is a REST API?

A REST API is a web API that follows the principles of REST (Representational State Transfer API), an architectural style for designing networked applications. It uses standard HTTP methods like GET, POST, PUT, DELETE to perform actions on resources (such as data objects) identified by URLs. REST APIs typically communicate using JSON or XML formats and are widely used for building web services that are scalable, maintainable, and interoperable.

## 3. How to do an HTTP request to an API?

There are a few steps:
1. Choose the appropriate HTTP method (GET, POST, PUT, DELETE, etc.) for the action you want to perform.
2. Formulate the URL of the API endpoint you want to interact with. This URL usually includes the endpoint address and any necessary parameters.
3. If required by the API, include any necessary headers in your request.
4. For methods like POST or PUT, you may need to include a request body containing data to send to the API.
5. Use a programming language or a tool like cURL or Postman to send the HTTP request to the API endpoint.
6. Once the API processes your request, it sends back a response. This response typically includes a status code indicating the success or failure of the request, along with any data requested.
7. If the request was successful, parse the response data (which may be in JSON, XML, or another format) and extract the information you need.

## 4. What are the most used HTTP requests?

- **GET**: Used to retrieve data from the server.
- **POST**: Used to send data to the server to create or update a resource.
- **PUT**: Similar to POST, but typically used to update an existing resource on the server.
- **DELETE**: Used to request the removal of a resource from the server.
- **PATCH**: Similar to PUT, but instead, only the specified changes are applied.
- **OPTIONS**: Used to retrieve information about the communication options available for a resource or server.
- **HEAD**: Similar to GET, but the server only returns the headers of the response without the actual body content.

## 5. How to make HTTP requests using cURL?
// curl [option] [URL]
(See `man curl` for more info)

## 6. What's the use for APIs in software development?

- **Integration**: APIs allow different software systems to communicate and work together seamlessly. This integration enables developers to leverage existing services and functionalities in their own applications without having to reinvent the wheel.
- **Extension**: APIs provide a way for developers to extend the functionality of their applications by integrating third-party services and libraries. This allows them to add features such as payment processing, social media integration, mapping services, and more.
- **Data Access**: APIs enable applications to access data from various sources, including databases, web services, and other applications. This access to data allows developers to build applications that provide valuable information and insights to users.
- **Standardization**: APIs provide standardized interfaces for accessing services and data, making it easier for developers to understand and use them. This standardization promotes interoperability and simplifies the process of integrating different software systems.
- **Automation**: APIs enable automation by allowing applications to interact with each other programmatically. This automation can streamline workflows, improve efficiency, and reduce the need for manual intervention.
- **Scalability**: APIs facilitate the development of scalable software systems by decoupling different components and allowing them to communicate asynchronously. This architecture enables applications to handle increased load and adapt to changing requirements more effectively.

## 7. What are the differences between REST APIs and SOAP APIs?

- **Protocol**: REST APIs typically use HTTP/HTTPS protocols for communication. SOAP APIs can use a wider variety of protocols, including HTTP, SMTP, and others.
- **Message Format**: REST APIs use JSON or XML to transmit data between server and client. SOAP APIs use exclusively XML, with a standardized structure.
- **Interface Style**: REST APIs follow the principles of RESTful architecture. SOAP APIs follow a more rigid and standardized approach.
- **Usage**: REST APIs are considered easier to use due to simplicity and adherence to web standards. SOAP APIs can be more complex and require additional tooling and expertise for implementation and integration due to their strict adherence to standards.
- **Performance**: REST APIs tend to be more lightweight and performant. SOAP APIs may have more overhead due to their XML-based message format and additional features like security and reliability, which can impact performance.
- **Flexibility**: REST APIs are more flexible and adaptable to different client requirements and evolving system architectures. SOAP APIs are more rigid and may require more effort to modify or extend due to their strict adherence to standards and specifications.

In conclusion, the choice between REST and SOAP APIs depends on factors such as project requirements, existing infrastructure, developer expertise, and performance considerations. While REST APIs are more commonly used in modern web development due to their simplicity and flexibility, SOAP APIs are still prevalent in enterprise environments and scenarios where strict adherence to standards and specifications is required.

## 8. What is an authentication token and how is it generally used in APIs?

An authentication token (auth token) is a piece of data that is used to authenticate and authorize a user or application when making requests to an API. It serves as a means of proving the identity of the requester and granting access to the API's resources. Auth tokens are commonly used in APIs to manage user sessions and ensure secure communication.

## 9. How would you handle errors in an API response?
Handling errors in an API response involves returning appropriate HTTP status codes and meaningful error messages to the client. This helps the client understand what went wrong and how to possibly fix it.
For example:
// curl -X GET https://api.example.com/protected/resource

// HTTP/1.1 401 Unauthorized
// Content-Type: application/json
// {
//    "error": {
//        "code": 401,
//        "message": "Unauthorized access. Please provide a valid authentication token."
//    }
// }

## 10. What is the format JSON and why is it often used with APIs?

JSON, or JavaScript Object Notation, is a lightweight data-interchange format that's easy for humans to read and write and easy for machines to parse and generate. It uses a text format that is completely language-independent but uses conventions that are familiar to programmers of the C-family of languages. JSON's simplicity, readability, and wide support make it an excellent choice for transmitting data between clients and servers in web APIs.

## 11. How would you secure your APIs against unauthorized access?

There are many ways to secure APIs, on different levels. Here are two examples:
- **OAuth 2.0**: The industry-standard protocol for authentication. It will limit access to the API by the use of access-tokens that represent user authorization.
- **HTTPS**: Hypertext Transfer Protocol Secure, to encrypt data in transit, preventing interception and tampering by third parties.
- **CORS**: Cross-Origin Resource Sharing, is a mechanism that allows a web page to access restricted resources from a server on a domain different from the domain that served the web page. Therefore, with CORS you can control which domains can access your API.
