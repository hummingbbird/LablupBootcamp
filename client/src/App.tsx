import styled from "styled-components";
import ChatList from "./components/ChatList";
import { useState, useRef, useEffect } from "react";

interface MessageItem {
  type: string;
  message: string;
}
function App() {
  const [messages, setMessages] = useState<MessageItem[]>([]);
  const [content, setContent] = useState("");
  const userId = useRef(0);
  const wsRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    const socket = new WebSocket(`${process.env.SOCKET_URL}`);
    wsRef.current = socket;
    socket.onopen = () => {
      socket.send(JSON.stringify({ type: "join", message: `사용자${userId}` }));
    };

    socket.onmessage = (e) => {
      const data: MessageItem = JSON.parse(e.data);
      setMessages((prev) => [...prev, data]);
    };
    socket.onerror = console.error;
    return () => socket.close();
  }, []);

  const handleSubmit = () => {
    if (!content) return;
    if (wsRef.current) {
      wsRef.current.send(JSON.stringify({ type: "chat", message: content }));
    };
    setContent("");
  };

  return (
    <AppDiv>
      <AppWrapper>
        <HeaderDiv>
          <p>realtime webchat</p>
        </HeaderDiv>
        <ChatList />
        <InputDIv>
          <input
            value={content}
            onChange={(e) => {
              setContent(e.target.value);
            }}
          />
          <button type="submit" onClick={handleSubmit}>
            전송
          </button>
        </InputDIv>
      </AppWrapper>
    </AppDiv>
  );
}

export default App;

export const AppDiv = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
`;

export const AppWrapper = styled.div`
  display: flex;
  flex-direction: column;
  background-color: #2b2b2b;
  width: 55rem;
  height: 42rem;
  border: 1px solid black;
  color: white;

  div {
    display: flex;
    width: 100%;
    justify-content: center;
  }
`;

export const HeaderDiv = styled.div`
  flex-direction: column;
  align-items: center;
  background-color: #1f1f1fff;
  height: 10%;
  p {
    font-size: 1.5rem;
    font-weight: 500;
  }
`;

export const InputDIv = styled.div`
  background-color: #202020;
  height: 10%;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 0.5rem;

  button {
    justify-content: center;
    align-items: center;
    width: 12%;
    min-width: 48px;
    height: 60%;
    font-size: 1.2rem;
    border: none;
    border-radius: 8px;
    background-color: #323232;
    color: #eeefff;

    &:hover {
      cursor: pointer;
    }

    &:focus {
      border: none;
    }
  }

  input {
    width: 80%;
    height: 60%;
    background-color: #333333;
    border: none;
    border-radius: 10px;
    padding-left: 20px;
    font-size: 20px;
    color: white;
    outline: none;
  }
`;
