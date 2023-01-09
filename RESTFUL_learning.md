# HTTP

<pre class='mermaid'>
    flowchart LR

    HTTP_protocol --defines--> HTTP_Methods
    HTTP_protocol --defines--> HTTP_Message

    HTTP_Methods --> GET
    HTTP_Methods --> PUT
    HTTP_Methods --> POST
    HTTP_Methods --> DELETE

    HTTP_Message ---> Start_Line
    HTTP_Message ---> Header
    HTTP_Message ---> Body
</pre>

# Socket Address - INET

<pre class='mermaid'>
    flowchart LR
    socket[socket address] --> IP
    socket --> port["port/16-bit service number"]
</pre>

# TCP/IP stack

<pre class='mermaid'>
flowchart

subgraph hierarcy
    direction BT
    IP --> UDP --> TCP
end

subgraph network["networks"]
    networks --use--> protocols --"to pack, unpack and send" --> datagrams    
end

subgraph differences["protocols have different properties"]
    direction TB
    IP_desc["IP
    very low level
    may not arrive
    may not maintain order
    may not arrive whole
    does not declare losses"]
    UDP_desc["UDP
    no handshake
    use case: response time critical"]
    TCP_desc["TCP
    uses handshake
    guarantees arrival
    use case: data transmission"]
end
</pre>

# Connection-oriented vs Connectionless

<pre class='mermaid'>
flowchart
subgraph connection["connection-oriented"]
    asymmetrical
    aware["aware of other party"]
    demands["demands preliminary steps to connect and disconnect"]
end

subgraph connectionless["connectionless"]
    equal
    no_demands["no demands - can be established ad hoc"]
    unaware["unaware of other party"]
end
</pre>

# How to fetch a document from a HTTP server

<pre class='mermaid'>
    flowchart LR
        start([start])
        stop([stop])

        %% core steps
        create_socket
        connect_socket
        request
        receive
        close

        %% Execution Path
        start --> create_socket --> connect_socket --> request --> receive --> close --> stop
</pre>

<pre class='mermaid'>
    sequenceDiagram
        participant client as HTTP client
        participant server as HTTP server

        client ->> server : handshake
        server -->> client : handshake
        client ->> server : request
        server -->> client : response
</pre>

# HTTP verbs

## GET and example HTTP request message

`GET` asks the server to send a particular document.

        GET / HTTP/1.1\r\n
        Host: www.site.com\r\n
        Connection: close\r\n
        \r\n

<pre class='mermaid'>
flowchart TB
subgraph FourthLine["Fourth Line"]
    break4["empty line is a request terminator"]
end

subgraph ThirdLine["Third Line"]
    text3["Connection: close\r\n"]
end

subgraph SecondLine["Second Line"]
    text2["Host: www.site.com\r\n"]
end

subgraph FirstLine["First Line"]
    text1["GET / HTTP/1.1\r\n"]
    verb["GET is the HTTP method"]
    URI["/ is the Uniform Resource Identifier"]
    version["HTTP/1.1 is the HTTP version"]
    break["\rn indicates line break"]
end

Headers["Request Headers
 name: value"]

 Headers .-> SecondLine
 Headers .-> ThirdLine
</pre>

# socket_instance.shutdown(CONSTANT) meanings
- `SHUT_RD` : shut the client's read connection
- `SHUT_WR` : shut the client's write connection
- `SHUT_RDWR` : shut the client's read and write connections


# Errors

## socket.gaierror
`socket.connect()` uses low-level `getaddrinfo()`, which can fail if:
- address is syntatically correct but doesn't exist
- address is malformed

consequently, `socket.connect()` can throw

- `socket.gaierror`

## ConnectionRefusedError
When a connection to a remote server requires the server's acceptance, and the
connection is refused, `socket_.connect()` can raise a `ConnectionRefusedError`.
This normally happens when the service is not provided by the server.

## socket.timeout 
A socket.timeout exception is raised when the server's reaction doesn't occur
in a reasonable time. The time period is set by `settimeout()`.

<pre class='mermaid'>
sequenceDiagram
  participant Client
  participant Server
  participant Socket Class
  Client ->> Socket Class: 1. socket()
  Socket Class -->> Client: 2. socket
  Client ->> Socket Class: 3. bind(address)
  Socket Class -->> Client: 4. None
  Client ->> Socket Class: 5. listen(backlog) 'backlog' = max queue size
  Socket Class -->> Client: 6. None
  Server ->> Socket Class: 7. socket()
  Socket Class -->> Server: 8. socket
  Server ->> Socket Class: 9. connect(address)
  Socket Class -->> Server: 10. None
  Client ->> Socket Class: 11. accept()
  Socket Class -->> Client: 12. connection, address
  Server ->> Socket Class: 13. send(bytes)
  Socket Class -->> Server: 14. number of bytes sent
  Client ->> Socket Class: 15. recv(bufsize)
  Socket Class -->> Client: 16. received bytes
  Client ->> Socket Class: 17. close()
  Socket Class -->> Client: 18. None
  Server ->> Socket Class: 19. close()
  Socket Class -->> Server: 20. None


</pre>


