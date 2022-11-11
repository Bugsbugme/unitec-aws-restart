import random
from socket import AF_INET, SOCK_STREAM, socket

random.seed(1234)

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(("localhost", 4096))
server_socket.listen()

while True:
    client, address = server_socket.accept()
    print(f"Received connection from: {client} --- {address}")

    request_bytes = client.recv(1024)
    # print(request_bytes)
    request_decoded = request_bytes.decode("utf-8")
    print(request_decoded)

    print("Sending response...")
    client.send(
        b"HTTP/1.1 200 OK\r\n\r\n<h1>I see you"
        + bytes([random.randint(48, 57)])
        + b"</h1>\r\n\r\n"
    )
    client.close()
    # print(AF_INET)
    # print(SOCK_STREAM)
