# Network Architecture

<pre class='mermaid'>
flowchart LR
  hardware --implement--> protocol
  software --implement--> protocol
  protocols --provide--> interactions 
  interactions --total--> network_behaviour
</pre>

# HTTP protocol

<pre class='mermaid'>
flowchart LR
  HTTP_Protocol --defines--> HTTP_Message_Format
  HTTP_Protocol --defines--> HTTP_Methods
  HTTP_Methods --include--> GET
  HTTP_Methods --include--> POST
  HTTP_Methods --include--> PUT
  HTTP_Methods --include--> DELETE
  HTTP_Message_Format --consists of--> Start_Line
  Start_Line --includes--> HTTP_Methods
  Start_Line --includes--> URL
  Start_Line --includes--> HTTP_Version
  HTTP_Message_Format --consists of--> Headers
  HTTP_Message_Format --consists of--> Body
  GET --retrieves--> HTML_Data
  POST --retrieves--> JSON_Data
  Body --can contain--> HTML_Data
  Body --can contain--> JSON_Data
</pre>

# REST
architectural style
1. client-server architecture
    
    a. separation of concerns

2. stateless (server does not store information about client)
    
    why does that make it easy to scale? 
    
    does stateless create an extra burden on data transmission?
    
    security risk that all information is contained in message?

3. cacheable
    
    improves performance

4. layered system
    
    what are the layers?
    
    sounds like talking about interfaces.

5. code on demand (optional)
    
    server can send executable code to the client

# Fundamentals of Software Architecture notes

REST is a remote access protocol?

# Python Institute
## Rest 
- Representational State Transfer
- HTTP protocol is the data carrier used by REST

## Socket Domains
- Unix Domain

        programs working within one OS

- Internet Domain (INET)

        programs connected together using TCP/IP protocol stack

## Socket Address - INET Domain
Identified by pairs of values:
- IP Address (32 bits)
- Port number/Service Number (16 bits)

Why service number as synonym for port number? Many standard services came to use the same, constant socket number. e.g. HTTP usually uses port 80.

## TCP/IP protocol stack
<pre class='mermaid'>
flowchart LR
    subgraph Hierarchy
        direction BT
        IP --> UDP --> TCP
    end

    subgraph Connections["Connection Types"]
        oriented["
        connection-oriented (phone call)

            - TCP usually
            - roles not symmetrical
            - aware of other party
            - demands preliminary steps to connect and disconnect

        "]        
        less["connectionless (walkie talkie)

        - UDP usually
        - can be established ad-hoc
        - equal rights
        - unaware of other party
        "]
    end

</pre>

<pre class='mermaid'>
flowchart TB
networks --use--> protocols --"that pack, send and unpack" --> data 

subgraph data["data"]
    datagram[/datagram/] 
end

subgraph IP_guarantees["IP protocol does not guarantee the datagram will"]
    A[reach node]
    B[be intact]
    D[declare losses]
    C[maintain sending order]
end

IP_guarantees .- low["very low level"]

subgraph TCP_guarantees["TCP protocol guarantees the datagram will"]
    E[reaches node]
    F[data intact]
    G[declares failures]
    uses_TCP["used for data safety over efficiency (WWW, REST, mail transfer)"]
end

subgraph UDP["UDP protocol"]
    faster
    less["less reliable"]
    uses["used for DNS, DHCP (response time critical)"]
end

UDP --"does not use".- handshakes

TCP_guarantees --uses.- handshakes["handshakes"]

datagram -.- IP_guarantees
datagram -.- TCP_guarantees
datagram -.- UDP

</pre>

# Basic socket module class diagram
<pre class='mermaid'>
classDiagram

Socket --> SocketType
Socket --> AddressFamily
Socket --> SocketProtocol

ClientSocket <|-- TCPClientSocket
TCPClientSocket --> InternetSocket

ClientSocket <|-- UDPSocket
UDPSocket --> InternetSocket

InternetSocket <|-- StreamSocket
InternetSocket <|-- DatagramSocket

StreamSocket --> SocketStream

class SocketType {
  SOCK_STREAM
  SOCK_DGRAM
  SOCK_RAW
  ...
}

class AddressFamily {
  AF_INET
  AF_INET6
  AF_UNIX
  ...
}

class SocketProtocol {
  IPPROTO_TCP
  IPPROTO_UDP
  IPPROTO_RAW
  ...
}
</pre>