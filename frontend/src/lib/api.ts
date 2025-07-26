const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

interface ApiResponse<T> {
  data?: T
  error?: string
}

class ApiClient {
  private baseURL: string
  private token: string | null = null

  constructor(baseURL: string = API_BASE_URL) {
    this.baseURL = baseURL
    this.token = typeof window !== 'undefined' ? localStorage.getItem('token') : null
  }

  setToken(token: string) {
    this.token = token
    if (typeof window !== 'undefined') {
      localStorage.setItem('token', token)
    }
  }

  clearToken() {
    this.token = null
    if (typeof window !== 'undefined') {
      localStorage.removeItem('token')
    }
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<ApiResponse<T>> {
    const url = `${this.baseURL}${endpoint}`
    
    const headers: HeadersInit = {
      'Content-Type': 'application/json',
      ...options.headers,
    }

    if (this.token) {
      headers.Authorization = `Bearer ${this.token}`
    }

    try {
      const response = await fetch(url, {
        ...options,
        headers,
      })

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}))
        return { error: errorData.detail || `HTTP ${response.status}` }
      }

      const data = await response.json()
      return { data }
    } catch (error) {
      return { error: error instanceof Error ? error.message : 'Network error' }
    }
  }

  // Auth endpoints
  async login(email: string, password: string) {
    return this.request<{ access_token: string; refresh_token: string; token_type: string }>('/api/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    })
  }

  async getCurrentUser() {
    return this.request<any>('/api/auth/me')
  }

  // Users endpoints
  async getUsers(skip = 0, limit = 100) {
    return this.request<any[]>(`/api/users?skip=${skip}&limit=${limit}`)
  }

  async createUser(userData: any) {
    return this.request<any>('/api/users', {
      method: 'POST',
      body: JSON.stringify(userData),
    })
  }

  // Customers endpoints
  async getCustomers(skip = 0, limit = 100, search?: string) {
    const params = new URLSearchParams({ skip: skip.toString(), limit: limit.toString() })
    if (search) params.append('search', search)
    
    return this.request<any[]>(`/api/customers?${params}`)
  }

  async createCustomer(customerData: any) {
    return this.request<any>('/api/customers', {
      method: 'POST',
      body: JSON.stringify(customerData),
    })
  }

  async updateCustomer(id: string, customerData: any) {
    return this.request<any>(`/api/customers/${id}`, {
      method: 'PUT',
      body: JSON.stringify(customerData),
    })
  }

  async deleteCustomer(id: string) {
    return this.request<any>(`/api/customers/${id}`, {
      method: 'DELETE',
    })
  }

  // Tickets endpoints
  async getTickets(skip = 0, limit = 100, status?: string, search?: string) {
    const params = new URLSearchParams({ skip: skip.toString(), limit: limit.toString() })
    if (status) params.append('status', status)
    if (search) params.append('search', search)
    
    return this.request<any[]>(`/api/tickets?${params}`)
  }

  async getTicketStats() {
    return this.request<any>('/api/tickets/stats')
  }

  async createTicket(ticketData: any) {
    return this.request<any>('/api/tickets', {
      method: 'POST',
      body: JSON.stringify(ticketData),
    })
  }

  async updateTicket(id: string, ticketData: any) {
    return this.request<any>(`/api/tickets/${id}`, {
      method: 'PUT',
      body: JSON.stringify(ticketData),
    })
  }

  async deleteTicket(id: string) {
    return this.request<any>(`/api/tickets/${id}`, {
      method: 'DELETE',
    })
  }

  // Health check
  async healthCheck() {
    return this.request<{ status: string; message: string; version: string }>('/health')
  }
}

export const apiClient = new ApiClient()
export default apiClient

