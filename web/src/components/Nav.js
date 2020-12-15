import React from 'react'
import {Link} from "react-router-dom";
import './Nav.css';

function Nav() {
  
  return (
    <nav className={'Nav'}>
      <Link className={'Nav-link'} to="/">Email</Link>
      <Link className={'Nav-link'} to="/users">Profile</Link>
    </nav>
  )
}

export default Nav;
