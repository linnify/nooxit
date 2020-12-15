import React, {useState} from 'react';
import './App.css';
import logo from './assets/logo.png';
import {  BrowserRouter as Router, Link, Route, Switch} from "react-router-dom";
import Email from "./pages/Email";
import Profile from "./pages/Profile";
import Nav from "./components/Nav";
import Login from "./components/Login";

function App() {
  
  const [isLoggedIn, setIsLoggedIn] = useState(true);
  
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
  
      { !isLoggedIn && <Login />}
      
      { isLoggedIn && <Router>
        <div>
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
      </Router>}
    </div>
  );
}

export default App;
