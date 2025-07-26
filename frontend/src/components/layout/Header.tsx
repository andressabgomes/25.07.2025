"use client"

import React from 'react'
import { Bell, ChevronDown, User } from 'lucide-react'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'

const Header = () => {
  return (
    <header className="bg-white border-b border-gray-200 px-6 py-4">
      <div className="flex items-center justify-between">
        {/* Logo e Informações da Empresa */}
        <div className="flex items-center space-x-6">
          {/* Logo Principal */}
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-lg">C</span>
            </div>
            <div className="text-gray-600 text-sm">+</div>
            <div className="w-8 h-8 bg-green-600 rounded-md flex items-center justify-center">
              <span className="text-white font-bold text-xs">P</span>
            </div>
          </div>

          {/* Informações da Unidade */}
          <div className="flex flex-col">
            <div className="flex items-center space-x-2">
              <span className="text-gray-900 font-medium">Unidade São Paulo</span>
              <ChevronDown className="w-4 h-4 text-gray-500" />
            </div>
            <span className="text-xs text-gray-500">CNPJ: 12.345.678/0001-90</span>
          </div>
        </div>

        {/* Ações do Usuário */}
        <div className="flex items-center space-x-4">
          {/* Notificações */}
          <div className="relative">
            <Button variant="ghost" size="icon" className="relative">
              <Bell className="w-5 h-5 text-gray-600" />
              <Badge 
                variant="destructive" 
                className="absolute -top-1 -right-1 w-5 h-5 p-0 flex items-center justify-center text-xs"
              >
                3
              </Badge>
            </Button>
          </div>

          {/* Perfil do Usuário */}
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center">
              <User className="w-4 h-4 text-gray-600" />
            </div>
            <ChevronDown className="w-4 h-4 text-gray-500" />
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header

