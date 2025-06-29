# 🚀 Lablup Bootcamp 

![client screen](https://github.com/user-attachments/assets/e43a3500-bdfa-4bd9-874d-cc31e7ea6db4)

python 비동기 라이브러리 asyncio, aiohttp, redis-py를 사용하여 realtime webchat 프로그램을 구현한다.

<br>

## 1. 폴더 구조
```
│
├── app/
│     ├── client.py    # Redis 비동기 Pub/Sub 클라이언트
│     └── server.py    # 웹소켓 및 HTTP 서버(Aiohttp)
│
├── static/
│     ├── index.html   # 채팅 프론트엔드
│     └── style.css    # 스타일 css 파일
│
├── Dockerfile         # 서버용 도커 이미지 빌드 설정
├── docker-compose.yml # 도커 컨테이너 한 번에 관리
├── requirements.txt   # 파이썬 의존성 파일
```

<br>

## 2. 실행 흐름
1. 웹 브라우저 접속
* 사용자는 `http://localhost:8080`으로 접속
* `index.html`, `style.css` 정적 파일 제공

2. 닉네임 연결 및 WebSocket 연결
* 닉네임 연결 후 `ws://localhost:8080/ws`로 WebSocket 연결 시작

3. 채팅 메시지 송수신
* 사용자 메시지 전송 시 `sendMessage` 함수를 통해 Websocket으로 서버에 전송
* 서버는 해당 메시지 Redis 채널에 publish
* Redis 구독중인 서버가 비동기적으로 새 메시지 감지 후 모든 접속자에게 메시지 전달
* 연결된 모든 사용자에게 새 메시지 실시간 전송
  
4. 사용자 입퇴장 관리
* 입장 시 `join`, 퇴장 시 `leave` 타입 메시지 전송하여 적절한 메시지 broadcast


<br>

## 3. 실행 방법
1. git clone
   
```
$ git clone https://github.com/hummingbbird/LablupBootcamp.git
```
<br>
2. docker compose

```
$ docker-compose up -d --build
``` 
<br>
3. localhost 접속 <br>

http://localhost:8080/