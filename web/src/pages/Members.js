import React, {useEffect, useState} from 'react';
import {getMembers} from "../services/api";
import styled from 'styled-components'
import ResourceItem from "../components/ResourceItem";

const MemberList = styled.ul`
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`

function Members(props) {
  const [members, setMembers] = useState([]);
  
  useEffect(() => {
    getMembers()
      .then(results => setMembers(results))
      .catch(error => {
        console.log(error)
      })
  }, [])
  
  const renderMembers = members.map((value, index) => {
    return <ResourceItem key={index} leftText={value.team} rightText={value.role} />
  })
  
  return (
    <div>
      <h1>This is the Members page</h1>
      
      <MemberList>
        { renderMembers }
      </MemberList>
    </div>
  )
}

export default Members
