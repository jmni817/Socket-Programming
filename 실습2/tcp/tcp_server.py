# 서버는 연결을 수락하고 요청 메시지를 받은 후
# 요청에 따라 응답을 생성하고 클라이언트에게 전송합니다.

from socket import *
serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print ('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    requestMessage = connectionSocket.recv(1024).decode()

    if "GET" in requestMessage:
        responseMessage = "HTTP/0.1 200 OK\r\n\r\nHello, this is the server!"
    elif "POST" in requestMessage:
        responseMessage = "HTTP/0.1 404 Not Found\r\n\r\nResource not found!"
    else:
        responseMessage = "HTTP/0.1 400 Bad Request\r\n\r\nBad request!"

    print(f"Received {len(requestMessage)} bytes from {addr}")

    connectionSocket.send(responseMessage.encode())
    connectionSocket.close()