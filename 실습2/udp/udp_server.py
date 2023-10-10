from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The server is ready to receive")

while True:
    # 클라이언트로부터 요청 메시지 수신
    message, clientAddress = serverSocket.recvfrom(2048)
    requestMessage = message.decode()

    # 요청 처리 및 응답 전송
    if "GET" in requestMessage:
        requestMessage = "HTTP/0.1 200 OK"
    elif "POST" in requestMessage:
        requestMessage = "HTTP/0.1 404 Not Found"
    else:
        requestMessage = "HTTP/0.1 400 Bad Request"

    print(f"Received {len(message)} bytes from {clientAddress}")

    serverSocket.sendto(requestMessage.encode(), clientAddress)