import styled from 'styled-components';

const Container = styled.div`
  display: flex;
  padding: 64px 0;
  justify-content: center;
  align-items: center;
  flex-direction: column;
`

const LoginButton = styled.button`
  margin-top: 32px;
  background-color: #f66e46;
  color: white;
  font-size: 16px;
  padding: 8px 16px;
  border-radius: 8px;
  outline: none;
  cursor: pointer;
  border: 0;
`

function Login() {
  
  return (
    <Container>
      <div>You are not logged in. Click on Login Button</div>
      
      <LoginButton>
        Login
      </LoginButton>
    </Container>
  )
}

export default Login
