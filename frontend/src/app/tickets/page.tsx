"use client"

import MainLayout from '@/components/layout/MainLayout'
import TicketTabs from '@/components/dashboard/TicketTabs'

export default function TicketsPage() {
  return (
    <MainLayout>
      <div className="space-y-6">
        {/* Cabeçalho da Página */}
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Chamados</h1>
          <p className="text-gray-600 mt-1">Gerenciamento de tickets</p>
        </div>

        {/* Abas de Tickets */}
        <TicketTabs />
      </div>
    </MainLayout>
  )
} 