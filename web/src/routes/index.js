import React from 'react';
import { Route, Switch } from "react-router-dom";
import Members from "../pages/Members";
import Users from "../pages/Users";


export const HomeRoutes = () => {
  return (
    <Switch>
      <Route path="/members">
        <Members />
      </Route>
      <Route path="/">
        <Users />
      </Route>
    </Switch>
  )
}
