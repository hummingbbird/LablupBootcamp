import styled from "styled-components";
import ChatItem from "./ChatItem";
const ChatList = () => {
  return (
    <ChatListDiv>
      <ChatItem content="maru: i'm maru" />
    </ChatListDiv>
  );
};

export default ChatList;

export const ChatListDiv = styled.div`
  display: flex;
  flex-direction: column;
  height: 80%;
  overflow-y: auto;

  &::-webkit-scrollbar {
    width: 5px;
  }

  &::-webkit-scrollbar-thumb {
    background: rgba(0, 0, 0, 0.2);
    border-radius: 3px;
    height: auto;
  }
`;

export const Tmp = styled.div`
  flex-shrink: 0;
  width: 100%;
  height: 100px;
`;
