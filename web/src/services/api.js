import {getAuthHeader} from "../helpers/utils";
import {API_HOST} from "../helpers/constants";
const axios = require('axios')

export async function getProfile() {
  const url = `${API_HOST}/auth/profile`
  const response = await axios.get(url, { headers: getAuthHeader() })
  return response.data
}

export async function getMembers() {
  const url = `${API_HOST}/members`
  const response = await axios.get(url, { headers: getAuthHeader() })
  return response.data
}

export async function getUsers() {
  const url = `${API_HOST}/users`
  const response = await axios.get(url, { headers: getAuthHeader() })
  return response.data
}
