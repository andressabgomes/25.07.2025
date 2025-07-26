"use client"

import MainLayout from '@/components/layout/MainLayout'
import TicketStats from '@/components/dashboard/TicketStats'
import TicketTabs from '@/components/dashboard/TicketTabs'

export default function DashboardPage() {
  return (
    <MainLayout>
      <div className="space-y-6">
        {/* Cabeçalho da Página */}
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>
          <p className="text-gray-600 mt-1">Visão geral do sistema</p>
        </div>

        {/* Gráfico de Estatísticas */}
        <TicketStats />

        {/* Abas de Tickets */}
        <TicketTabs />
      </div>
    </MainLayout>
  )
} 