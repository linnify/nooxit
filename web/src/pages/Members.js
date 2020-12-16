import React from 'react';
import {getMembers} from "../services/api";
import styled from 'styled-components'
import ResourceItem from "../components/ResourceItem";
import ErrorMessage from "../components/ErrorMessage";
import {useApiResource} from "../hooks/api-resource";

const MemberList = styled.ul`
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`

function Members() {
  const [members, error] = useApiResource(getMembers)
  const renderMembers = members.map((value, index) => <ResourceItem key={index} leftText={value.team} rightText={value.role} />)
  
  return (
    <div>
      <h1>This is the Members page</h1>
      <ErrorMessage message={error}/>
      <MemberList>
        { renderMembers }
      </MemberList>
    </div>
  )
}

export default Members
