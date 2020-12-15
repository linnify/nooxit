import React from "react";
import Login from "../components/Login";
import {Route, Switch} from "react-router-dom";
import Nav from "../components/Nav";
import Profile from "./Profile";
import Email from "./Email";
import LoadingPage from "../components/LoadingPage";
import useAuth from "../hooks/auth";


function Home() {
  const [user, isLoading] = useAuth()
  const isLoggedIn = !!user;
  
  return (
    <div>
      { isLoading && <LoadingPage /> }
      
      { !isLoading && !isLoggedIn && <Login scope={'email'}/>}
      
      { !isLoading && isLoggedIn && <div>
        <Nav/>
        <Switch>
          <Route path="/users">
            <Profile isLoggedIn={isLoggedIn}/>
          </Route>
          <Route path="/">
            <Email isLoggedIn={isLoggedIn}/>
          </Route>
        </Switch>
      </div>
      }
    </div>
  )
}

export default Home
