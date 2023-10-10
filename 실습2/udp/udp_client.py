from socket import *

# 서버 설정
serverName = '127.0.0.1'
serverPort = 12000

# udp 소켓 생성
clientSocket = socket(AF_INET, SOCK_DGRAM)

# 각각의 요청 메시지 전송
requestMessages = ["GET /index.html HTTP/1.1",
                    "POST /submit_data HTTP/1.1",
                    "DELETE /delete_resource HTTP/1.1"]

for requestMessage in requestMessages:
    clientSocket.sendto(requestMessage.encode(), (serverName, serverPort))

    # 서버로부터 응답 수신 및 출력
    response, _ = clientSocket.recvfrom(1024)
    print(response.decode())

clientSocket.close()