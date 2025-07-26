"use client"

import MainLayout from '@/components/layout/MainLayout'

export default function CalendarPage() {
  return (
    <MainLayout>
      <div className="space-y-6">
        {/* Cabeçalho da Página */}
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Calendário</h1>
          <p className="text-gray-600 mt-1">Agenda e eventos</p>
        </div>

        {/* Conteúdo do Calendário */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="text-center text-gray-500">
            <p>Calendário em desenvolvimento</p>
            <p className="text-sm mt-2">Funcionalidade será implementada em breve</p>
          </div>
        </div>
      </div>
    </MainLayout>
  )
} 