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

  useEffect(() => {
    if (!token) {
      setUser(null)
      return
    }
    // decode JWT payload (unsafe client-side parse) to get sub as user id
    try {
      const parts = token.split('.')
      if (parts.length >= 2) {
        const payload = parts[1]
        const b64 = payload.replace(/-/g, '+').replace(/_/g, '/')
        const json = decodeURIComponent(atob(b64).split('').map(function(c) {
          return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
        }).join(''))
        const obj = JSON.parse(json)
        setUser({ id: obj.sub })
      }
    } catch {
      setUser(null)
    }
  }, [token])

  async function login(email, password) {
    const res = await apiLogin(email, password)
    setToken(res.access_token)
    navigate('/')
    return res
  }

  async function register(payload) {
    const user = await apiRegister(payload)
    // auto-login after successful register
    try {
      const loginRes = await apiLogin(payload.email, payload.password)
      setToken(loginRes.access_token)
      navigate('/')
    } catch {
      // ignore login failure, return created user
    }
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
