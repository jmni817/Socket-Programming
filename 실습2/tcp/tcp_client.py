# 클라이언트는 요청 메시지를 전송하고 서버로부터 응답을 받아 출력합니다.
# 요청 메시지에 따라 서버가 다른 응답을 생성하게 됩니다.

from socket import *

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

requestMessages = ["GET /index.html HTTP/1.1",
                   "POST /submit_data HTTP/1.1",
                   "DELETE /delete_resource HTTP/1.1"]

for requestMessage in requestMessages:
    clientSocket.send(requestMessage.encode())

    responseMessage = clientSocket.recv(1024).decode()
    print(responseMessage)

clientSocket.close()