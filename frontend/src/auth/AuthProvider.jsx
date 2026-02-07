import { createContext, useContext, useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { login as apiLogin, register as apiRegister } from '../api'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [token, setToken] = useState(() => {
    try { return localStorage.getItem('access_token') } catch { return null }
  })
  const [user, setUser] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    try { if (token) localStorage.setItem('access_token', token); else localStorage.removeItem('access_token') } catch {}
  }, [token])

  async function login(email, password) {
    const res = await apiLogin(email, password)
    setToken(res.access_token)
    // optionally fetch user profile here
    navigate('/')
    return res
  }

  async function register(payload) {
    const user = await apiRegister(payload)
    return user
  }

  function logout() {
    setToken(null)
    setUser(null)
    navigate('/')
  }

  return (
    <AuthContext.Provider value={{ token, user, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth() {
  return useContext(AuthContext)
}
