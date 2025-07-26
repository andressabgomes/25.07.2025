"use client"

import MainLayout from '@/components/layout/MainLayout'

export default function ReportsPage() {
  return (
    <MainLayout>
      <div className="space-y-6">
        {/* Cabeçalho da Página */}
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Relatórios</h1>
          <p className="text-gray-600 mt-1">Análises e estatísticas</p>
        </div>

        {/* Conteúdo dos Relatórios */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="text-center text-gray-500">
            <p>Módulo de relatórios em desenvolvimento</p>
            <p className="text-sm mt-2">Funcionalidade será implementada em breve</p>
          </div>
        </div>
      </div>
    </MainLayout>
  )
} 