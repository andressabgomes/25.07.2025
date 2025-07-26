"use client"

import React, { createContext, useContext, useState, useEffect } from 'react'
import { apiClient } from '@/lib/api'

interface User {
  id: string
  email: string
  full_name: string
  role: string
  is_active: boolean
}

interface AuthContextType {
  user: User | null
  isLoading: boolean
  login: (email: string, password: string) => Promise<{ success: boolean; error?: string }>
  logout: () => void
  isAuthenticated: boolean
}

const AuthContext = createContext<AuthContextType | undefined>(undefined)

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    checkAuth()
  }, [])

  const checkAuth = async () => {
    const token = localStorage.getItem('token')
    if (!token) {
      setIsLoading(false)
      return
    }

    apiClient.setToken(token)
    const response = await apiClient.getCurrentUser()
    
    if (response.data) {
      setUser(response.data)
    } else {
      apiClient.clearToken()
    }
    
    setIsLoading(false)
  }

  const login = async (email: string, password: string) => {
    const response = await apiClient.login(email, password)
    
    if (response.data) {
      apiClient.setToken(response.data.access_token)
      const userResponse = await apiClient.getCurrentUser()
      
      if (userResponse.data) {
        setUser(userResponse.data)
        return { success: true }
      }
    }
    
    return { success: false, error: response.error || 'Login failed' }
  }

  const logout = () => {
    apiClient.clearToken()
    setUser(null)
  }

  const value = {
    user,
    isLoading,
    login,
    logout,
    isAuthenticated: !!user,
  }

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
}

export function useAuth() {
  const context = useContext(AuthContext)
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider')
  }
  return context
}

