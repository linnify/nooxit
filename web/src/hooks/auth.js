import {useLocation} from "react-router-dom";
import {useEffect, useState} from "react";
const queryString = require('query-string');

const LOCAL_STORAGE_TOKEN = 'auth-token'

/**
 * Hook for checking if the current user is authenticated
 * First check if the URL has the token set in the query params
 * If not check if we already have the token in the local storage
 *
 * If the URL has a token in the query param, grab the token and set the user
 */
function useAuth() {
  
  const initialUser = getLocalUser();
  const [isLoading, setIsLoading] = useState(true);
  const [user, setUser] = useState(initialUser)
  const location = useLocation()
  
  useEffect(() => {
    const parsed = queryString.parse(location.search);
    if (parsed.token) {
      setUser(parsed.token)
      setLocalUser(parsed.token)
    }
    
    setIsLoading(false);
  }, [])
  
  function getLocalUser() {
    const userAsString = localStorage.getItem(LOCAL_STORAGE_TOKEN)
    if (userAsString) {
      return JSON.parse(userAsString)
    }
  }
  
  function setLocalUser(user) {
    localStorage.setItem(LOCAL_STORAGE_TOKEN, JSON.stringify(user))
  }
  
  return [user, isLoading]
}

export default useAuth
