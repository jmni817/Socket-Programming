실습(2) – 초간단 HTTP 유사 서버/클라이언트

• 서버는 GET request 수신 시 request message 내용(URL, header)과 관계없이 “HTTP/0.1 200 OK”와
같은 한 줄의 status line으로 (header는 0줄) 구성된 response message를 클라이언트에게 전송

• 서버는 POST request 수신 시 request message 내용(URL, header)과 관계없이 “HTTP/0.1 404 Not
Found”와 같은 한 줄의 status line으로 (header는 0줄) 구성된 response message를 클라이언트에게
전송

• 서버는 GET/POST 이외의 request message 수신 시 “HTTP/0.1 400 Bad Request”와 같은 한 줄의
status line으로 (header는 0줄) 구성된 response message 클라이언트에게 전송 후 프로세스 종료

• 서버는 request message 수신 시 화면에 수신한 message 크기(byte 단위) 출력 후 (줄바꿈 포함)

• 클라이언트는 GET, POST, DELETE request message를 순차적으로 전송 (각 request message는 HTTP 
형식에 부합해야 함)

• 클라이언트는 각 request를 전송 한 후 서버로부터 수신한 내용을 ASCII text 형식으로 화면에 출력

• UDP를 사용하는 서버/클라이언트 프로그램, TCP 를 사용하는 서버/클라이언트 프로그램 각각 작성
후 테스트