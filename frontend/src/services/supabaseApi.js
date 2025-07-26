import { supabase } from '../lib/supabase.js'

class SupabaseApiService {
  constructor() {
    this.supabase = supabase
  }

  // Auth
  async login(email, password) {
    try {
      const { data, error } = await this.supabase.auth.signInWithPassword({
        email,
        password
      })

      if (error) throw error

      return {
        user: data.user,
        token: data.session?.access_token,
        success: true
      }
    } catch (error) {
      console.error('Erro no login:', error)
      throw new Error(error.message || 'Erro no login')
    }
  }

  async register(userData) {
    try {
      const { data, error } = await this.supabase.auth.signUp({
        email: userData.email,
        password: userData.password,
        options: {
          data: {
            name: userData.name,
            role: userData.role || 'agent'
          }
        }
      })

      if (error) throw error

      return {
        user: data.user,
        success: true
      }
    } catch (error) {
      console.error('Erro no registro:', error)
      throw new Error(error.message || 'Erro no registro')
    }
  }

  async logout() {
    try {
      const { error } = await this.supabase.auth.signOut()
      if (error) throw error
      return { success: true }
    } catch (error) {
      console.error('Erro no logout:', error)
      throw error
    }
  }

  async getCurrentUser() {
    try {
      const { data: { user }, error } = await this.supabase.auth.getUser()
      if (error) throw error
      return user
    } catch (error) {
      console.error('Erro ao obter usuário atual:', error)
      return null
    }
  }

  // Tickets
  async getTickets(params = {}) {
    try {
      let query = this.supabase
        .from('tickets')
        .select(`
          *,
          customer:customers(*),
          assigned_user:users(*)
        `)

      // Aplicar filtros
      if (params.status) {
        query = query.eq('status', params.status)
      }
      if (params.priority) {
        query = query.eq('priority', params.priority)
      }
      if (params.customer_id) {
        query = query.eq('customer_id', params.customer_id)
      }

      const { data, error } = await query.order('created_at', { ascending: false })

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao buscar tickets:', error)
      throw new Error(error.message || 'Erro ao buscar tickets')
    }
  }

  async getTicket(id) {
    try {
      const { data, error } = await this.supabase
        .from('tickets')
        .select(`
          *,
          customer:customers(*),
          assigned_user:users(*)
        `)
        .eq('id', id)
        .single()

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao buscar ticket:', error)
      throw new Error(error.message || 'Erro ao buscar ticket')
    }
  }

  async createTicket(ticketData) {
    try {
      const { data, error } = await this.supabase
        .from('tickets')
        .insert([ticketData])
        .select()
        .single()

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao criar ticket:', error)
      throw new Error(error.message || 'Erro ao criar ticket')
    }
  }

  async updateTicket(id, ticketData) {
    try {
      const { data, error } = await this.supabase
        .from('tickets')
        .update(ticketData)
        .eq('id', id)
        .select()
        .single()

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao atualizar ticket:', error)
      throw new Error(error.message || 'Erro ao atualizar ticket')
    }
  }

  async deleteTicket(id) {
    try {
      const { error } = await this.supabase
        .from('tickets')
        .delete()
        .eq('id', id)

      if (error) throw error
      return { success: true }
    } catch (error) {
      console.error('Erro ao deletar ticket:', error)
      throw new Error(error.message || 'Erro ao deletar ticket')
    }
  }

  async getTicketStats() {
    try {
      const { data, error } = await this.supabase
        .from('tickets')
        .select('status, priority')

      if (error) throw error

      const stats = {
        total: data.length,
        open: data.filter(t => t.status === 'open').length,
        closed: data.filter(t => t.status === 'closed').length,
        high: data.filter(t => t.priority === 'high').length,
        medium: data.filter(t => t.priority === 'medium').length,
        low: data.filter(t => t.priority === 'low').length
      }

      return stats
    } catch (error) {
      console.error('Erro ao buscar estatísticas:', error)
      throw new Error(error.message || 'Erro ao buscar estatísticas')
    }
  }

  // Customers
  async getCustomers(params = {}) {
    try {
      let query = this.supabase
        .from('customers')
        .select('*')

      if (params.search) {
        query = query.or(`name.ilike.%${params.search}%,email.ilike.%${params.search}%`)
      }

      const { data, error } = await query.order('created_at', { ascending: false })

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao buscar clientes:', error)
      throw new Error(error.message || 'Erro ao buscar clientes')
    }
  }

  async getCustomer(id) {
    try {
      const { data, error } = await this.supabase
        .from('customers')
        .select('*')
        .eq('id', id)
        .single()

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao buscar cliente:', error)
      throw new Error(error.message || 'Erro ao buscar cliente')
    }
  }

  async createCustomer(customerData) {
    try {
      const { data, error } = await this.supabase
        .from('customers')
        .insert([customerData])
        .select()
        .single()

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao criar cliente:', error)
      throw new Error(error.message || 'Erro ao criar cliente')
    }
  }

  async updateCustomer(id, customerData) {
    try {
      const { data, error } = await this.supabase
        .from('customers')
        .update(customerData)
        .eq('id', id)
        .select()
        .single()

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao atualizar cliente:', error)
      throw new Error(error.message || 'Erro ao atualizar cliente')
    }
  }

  async deleteCustomer(id) {
    try {
      const { error } = await this.supabase
        .from('customers')
        .delete()
        .eq('id', id)

      if (error) throw error
      return { success: true }
    } catch (error) {
      console.error('Erro ao deletar cliente:', error)
      throw new Error(error.message || 'Erro ao deletar cliente')
    }
  }

  // Users
  async getUsers(params = {}) {
    try {
      let query = this.supabase
        .from('users')
        .select('*')

      if (params.role) {
        query = query.eq('role', params.role)
      }

      const { data, error } = await query.order('created_at', { ascending: false })

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao buscar usuários:', error)
      throw new Error(error.message || 'Erro ao buscar usuários')
    }
  }

  async getUser(id) {
    try {
      const { data, error } = await this.supabase
        .from('users')
        .select('*')
        .eq('id', id)
        .single()

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao buscar usuário:', error)
      throw new Error(error.message || 'Erro ao buscar usuário')
    }
  }

  async createUser(userData) {
    try {
      const { data, error } = await this.supabase
        .from('users')
        .insert([userData])
        .select()
        .single()

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao criar usuário:', error)
      throw new Error(error.message || 'Erro ao criar usuário')
    }
  }

  async updateUser(id, userData) {
    try {
      const { data, error } = await this.supabase
        .from('users')
        .update(userData)
        .eq('id', id)
        .select()
        .single()

      if (error) throw error
      return data
    } catch (error) {
      console.error('Erro ao atualizar usuário:', error)
      throw new Error(error.message || 'Erro ao atualizar usuário')
    }
  }

  async deleteUser(id) {
    try {
      const { error } = await this.supabase
        .from('users')
        .delete()
        .eq('id', id)

      if (error) throw error
      return { success: true }
    } catch (error) {
      console.error('Erro ao deletar usuário:', error)
      throw new Error(error.message || 'Erro ao deletar usuário')
    }
  }
}

export default new SupabaseApiService() 