import styled from "styled-components";

function App() {
  return (
    <AppDiv>
      <AppWrapper>
        <HeaderDiv>
          <p>realtime webchat</p>
        </HeaderDiv>
        <ChatDiv />
        <InputDIv>
          <input />
          <button>전송</button>
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
  background-color: #ace1fc;
  width: 50vw;
  height: 70vh;
  border: 1px solid black;

  div {
    display: flex;
    width: 100%;
    align-items: center;
    justify-content: center;
  }
`;

export const HeaderDiv = styled.div`
  flex-direction: column;
  height: 5vh;
  p {
    font-size: 1.5rem;
    font-weight: 500;
  }
`;

export const ChatDiv = styled.div`
  flex-direction: column;
  height: 58vh;
  border: 1px solid red;
`;

export const InputDIv = styled.div`
  background-color: #ffffff;
  height: 7vh;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 0.5rem;

  button {
    justify-content: center;
    align-items: center;
    width: 16%;
    height: 60%;
    font-size: 1.4rem;
    border: none;
    border-radius: 8px;
    background-color: #60430e;
    color: #eeefff;
  }

  input {
    width: 75%;
    height: 60%;
    background-color: #ececec56;
    border: none;
    border-radius: 50px;
    padding-left: 20px;
    font-size: 20px;
    &:focus {
    }
  }
`;
