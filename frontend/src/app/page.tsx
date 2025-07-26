"use client"

import { useAuth } from '@/contexts/AuthContext'
import MainLayout from '@/components/layout/MainLayout'
import TicketStats from '@/components/dashboard/TicketStats'
import TicketTabs from '@/components/dashboard/TicketTabs'
import LoginForm from '@/components/auth/LoginForm'

export default function Home() {
  const { isAuthenticated, isLoading } = useAuth()

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-lg">Carregando...</div>
      </div>
    )
  }

  if (!isAuthenticated) {
    return <LoginForm />
  }

  return (
    <MainLayout>
      <div className="space-y-6">
        {/* Cabeçalho da Página */}
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Atendimento</h1>
          <p className="text-gray-600 mt-1">Histórico de chamados</p>
        </div>

        {/* Gráfico de Estatísticas */}
        <TicketStats />

        {/* Abas de Tickets */}
        <TicketTabs />
      </div>
    </MainLayout>
  )
}

