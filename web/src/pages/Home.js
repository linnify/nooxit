import React from "react";
import Login from "../components/Login";
import { Route, Switch } from "react-router-dom";
import Nav from "../components/Nav";
import Members from "./Members";
import Users from "./Users";
import LoadingPage from "../components/LoadingPage";
import useAuth from "../hooks/auth";
import UserDetails from "../components/UserDetails";


function Home() {
  const [user, isLoading, logout] = useAuth()
  const onLogout = () => logout()
  
  return (
    <div>
      { isLoading && <LoadingPage /> }
      
      { !isLoading && !user && <Login scopes={['email', 'profile', 'groups']}/>}
      
      { !isLoading && user && <div>
        <UserDetails user={user} logout={onLogout}/>
        
        <Nav/>
        
        <Switch>
          <Route path="/members">
            <Members />
          </Route>
          <Route path="/">
            <Users />
          </Route>
        </Switch>
      </div>
      }
    </div>
  )
}

export default Home
