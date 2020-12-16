import React, {useEffect, useState} from 'react';
import { getUsers } from "../services/api";
import styled from "styled-components";
import ResourceItem from "../components/ResourceItem";


const UsersList = styled.ul`
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`

function Users() {
  const [users, setUsers] = useState([]);
  
  useEffect(() => {
    getUsers()
      .then(results => setUsers(results))
  }, [])
  
  const renderUsers = users.map((value, index) => <ResourceItem key={index} leftText={value.name} rightText={`${value.age} years`} />)
  
  return (
    <div>
      <h1>This is the Users page</h1>
      <UsersList>
        { renderUsers }
      </UsersList>
    </div>
  
  )
}

export default Users
