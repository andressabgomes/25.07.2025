"use client"

import React, { useState } from 'react'
import { 
  LayoutDashboard, 
  Ticket, 
  Calendar, 
  DollarSign, 
  BarChart3, 
  MessageSquare, 
  HelpCircle, 
  CheckSquare 
} from 'lucide-react'
import { cn } from '@/lib/utils'

interface SidebarItem {
  icon: React.ElementType
  label: string
  active?: boolean
  href?: string
}

const sidebarItems: SidebarItem[] = [
  { icon: LayoutDashboard, label: 'Dashboard', href: '/dashboard' },
  { icon: Ticket, label: 'Chamados', active: true, href: '/tickets' },
  { icon: Calendar, label: 'Calendário', href: '/calendar' },
  { icon: DollarSign, label: 'Financeiro', href: '/financial' },
  { icon: BarChart3, label: 'Relatórios', href: '/reports' },
  { icon: MessageSquare, label: 'Comunicados', href: '/announcements' },
  { icon: HelpCircle, label: 'Suporte', href: '/support' },
  { icon: CheckSquare, label: 'Tarefas', href: '/tasks' },
]

const Sidebar = () => {
  const [hoveredItem, setHoveredItem] = useState<string | null>(null)

  return (
    <aside className="w-16 bg-white border-r border-gray-200 flex flex-col items-center py-6">
      <nav className="flex flex-col space-y-4">
        {sidebarItems.map((item, index) => {
          const Icon = item.icon
          const isActive = item.active
          const isHovered = hoveredItem === item.label

          return (
            <div
              key={index}
              className="relative group"
              onMouseEnter={() => setHoveredItem(item.label)}
              onMouseLeave={() => setHoveredItem(null)}
            >
              <button
                className={cn(
                  "w-10 h-10 rounded-lg flex items-center justify-center transition-all duration-200",
                  isActive 
                    ? "bg-orange-100 text-orange-600 border-2 border-orange-300" 
                    : "text-gray-500 hover:bg-gray-100 hover:text-gray-700"
                )}
              >
                <Icon className="w-5 h-5" />
              </button>

              {/* Tooltip */}
              {isHovered && (
                <div className="absolute left-14 top-1/2 transform -translate-y-1/2 z-50">
                  <div className="bg-gray-900 text-white text-xs px-2 py-1 rounded whitespace-nowrap">
                    {item.label}
                    <div className="absolute left-0 top-1/2 transform -translate-y-1/2 -translate-x-1 w-0 h-0 border-t-2 border-b-2 border-r-2 border-transparent border-r-gray-900"></div>
                  </div>
                </div>
              )}
            </div>
          )
        })}
      </nav>
    </aside>
  )
}

export default Sidebar

