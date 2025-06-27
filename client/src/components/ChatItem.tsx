import styled from "styled-components";

type ChatItemProps = {
    content: string;
}
const ChatItem = ({content}:ChatItemProps) => {
  return (
    <ChatItemDiv>
        {content}
    </ChatItemDiv>
  );
};

export default ChatItem;

export const ChatItemDiv = styled.div`
    display: flex;
    justify-content: start;
    align-items: start;
    font-size: 20px;
`;
