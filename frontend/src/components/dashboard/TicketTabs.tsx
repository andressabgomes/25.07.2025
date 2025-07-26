"use client"

import React, { useState } from 'react'
import { Plus, MessageCircle } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'

interface Ticket {
  id: string
  title: string
  customer: string
  priority: 'low' | 'medium' | 'high' | 'urgent'
  status: 'open' | 'in_progress' | 'resolved'
  time: string
}

const upcomingTickets: Ticket[] = [
  {
    id: '1',
    title: 'Problema de login no sistema',
    customer: 'João Silva',
    priority: 'high',
    status: 'open',
    time: '14:30'
  },
  {
    id: '2',
    title: 'Dúvida sobre funcionalidade',
    customer: 'Maria Santos',
    priority: 'medium',
    status: 'in_progress',
    time: '15:00'
  },
  {
    id: '3',
    title: 'Sistema lento para carregar',
    customer: 'Pedro Costa',
    priority: 'low',
    status: 'open',
    time: '15:30'
  }
]

const recentTickets: Ticket[] = [
  {
    id: '4',
    title: 'Erro ao gerar relatório',
    customer: 'Ana Oliveira',
    priority: 'medium',
    status: 'resolved',
    time: '13:45'
  },
  {
    id: '5',
    title: 'Solicitação de nova funcionalidade',
    customer: 'Carlos Lima',
    priority: 'low',
    status: 'resolved',
    time: '12:30'
  }
]

const priorityColors = {
  low: 'bg-blue-100 text-blue-800',
  medium: 'bg-yellow-100 text-yellow-800',
  high: 'bg-orange-100 text-orange-800',
  urgent: 'bg-red-100 text-red-800'
}

const statusColors = {
  open: 'bg-gray-100 text-gray-800',
  in_progress: 'bg-blue-100 text-blue-800',
  resolved: 'bg-green-100 text-green-800'
}

const TicketTabs = () => {
  const [activeTab, setActiveTab] = useState<'upcoming' | 'recent'>('upcoming')

  const renderTicketList = (tickets: Ticket[]) => (
    <div className="space-y-3">
      {tickets.map((ticket) => (
        <div key={ticket.id} className="p-4 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors">
          <div className="flex items-start justify-between">
            <div className="flex-1">
              <h4 className="font-medium text-gray-900 mb-1">{ticket.title}</h4>
              <p className="text-sm text-gray-600 mb-2">Cliente: {ticket.customer}</p>
              <div className="flex items-center space-x-2">
                <Badge className={priorityColors[ticket.priority]}>
                  {ticket.priority}
                </Badge>
                <Badge className={statusColors[ticket.status]}>
                  {ticket.status.replace('_', ' ')}
                </Badge>
              </div>
            </div>
            <div className="text-sm text-gray-500 ml-4">
              {ticket.time}
            </div>
          </div>
        </div>
      ))}
    </div>
  )

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-6">
      {/* Header com Abas */}
      <div className="flex items-center justify-between mb-6">
        <div className="flex space-x-1 bg-gray-100 rounded-lg p-1">
          <button
            onClick={() => setActiveTab('upcoming')}
            className={`px-4 py-2 text-sm font-medium rounded-md transition-colors ${
              activeTab === 'upcoming'
                ? 'bg-white text-gray-900 shadow-sm'
                : 'text-gray-600 hover:text-gray-900'
            }`}
          >
            Próximos atendimentos
          </button>
          <button
            onClick={() => setActiveTab('recent')}
            className={`px-4 py-2 text-sm font-medium rounded-md transition-colors ${
              activeTab === 'recent'
                ? 'bg-white text-gray-900 shadow-sm'
                : 'text-gray-600 hover:text-gray-900'
            }`}
          >
            Atendimentos recentes
          </button>
        </div>

        <Button className="bg-orange-500 hover:bg-orange-600 text-white">
          <Plus className="w-4 h-4 mr-2" />
          Abrir novo chamado
        </Button>
      </div>

      {/* Conteúdo das Abas */}
      <div className="min-h-[300px]">
        {activeTab === 'upcoming' && renderTicketList(upcomingTickets)}
        {activeTab === 'recent' && renderTicketList(recentTickets)}
      </div>

      {/* Avatar Flutuante */}
      <div className="fixed bottom-6 right-6">
        <Button 
          size="icon" 
          className="w-14 h-14 rounded-full bg-green-600 hover:bg-green-700 text-white shadow-lg"
        >
          <MessageCircle className="w-6 h-6" />
        </Button>
      </div>
    </div>
  )
}

export default TicketTabs

