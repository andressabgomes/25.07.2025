"use client"

import React from 'react'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'

const data = [
  { month: 'Jan', abertos: 45, concluidos: 38 },
  { month: 'Fev', abertos: 52, concluidos: 41 },
  { month: 'Mar', abertos: 38, concluidos: 45 },
  { month: 'Abr', abertos: 61, concluidos: 52 },
  { month: 'Mai', abertos: 55, concluidos: 58 },
  { month: 'Jun', abertos: 42, concluidos: 48 },
]

const TicketStats = () => {
  return (
    <div className="bg-white rounded-lg border border-gray-200 p-6">
      <div className="mb-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-2">
          Chamados por Mês
        </h3>
        <p className="text-sm text-gray-600">
          Comparativo entre chamados abertos e concluídos
        </p>
      </div>

      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
            <XAxis 
              dataKey="month" 
              axisLine={false}
              tickLine={false}
              tick={{ fontSize: 12, fill: '#6b7280' }}
            />
            <YAxis 
              axisLine={false}
              tickLine={false}
              tick={{ fontSize: 12, fill: '#6b7280' }}
            />
            <Tooltip 
              contentStyle={{
                backgroundColor: '#fff',
                border: '1px solid #e5e7eb',
                borderRadius: '8px',
                boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)'
              }}
            />
            <Bar 
              dataKey="abertos" 
              fill="#FFAB40" 
              name="Abertos"
              radius={[4, 4, 0, 0]}
            />
            <Bar 
              dataKey="concluidos" 
              fill="#2E7D32" 
              name="Concluídos"
              radius={[4, 4, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* Métricas */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6 pt-6 border-t border-gray-200">
        <div className="text-center">
          <div className="text-2xl font-bold text-gray-900">48</div>
          <div className="text-xs text-gray-600">Média de chamados abertos</div>
        </div>
        <div className="text-center">
          <div className="text-2xl font-bold text-gray-900">2.3h</div>
          <div className="text-xs text-gray-600">Intervalo médio entre atendimentos</div>
        </div>
        <div className="text-center">
          <div className="text-2xl font-bold text-green-600">Mar</div>
          <div className="text-xs text-gray-600">Mês com menor volume</div>
        </div>
        <div className="text-center">
          <div className="text-2xl font-bold text-orange-600">Abr</div>
          <div className="text-xs text-gray-600">Mês com maior volume</div>
        </div>
      </div>
    </div>
  )
}

export default TicketStats

