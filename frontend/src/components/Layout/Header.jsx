import React, { useState } from 'react';
import { 
  Bell, 
  ChevronDown, 
  User,
  MapPin,
  Building2
} from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';

const Header = () => {
  const { user, logout } = useAuth();
  const [showUserMenu, setShowUserMenu] = useState(false);
  const [showUnitMenu, setShowUnitMenu] = useState(false);

  return (
    <header className="fixed top-0 left-16 right-0 h-16 bg-card border-b border-border flex items-center justify-between px-6 z-30">
      {/* Logo e Informações da Empresa */}
      <div className="flex items-center gap-6">
        {/* Logo Principal */}
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 caja-gradient rounded-md flex items-center justify-center text-white font-bold">
            CS
          </div>
          <span className="font-semibold text-lg">Customer Support</span>
        </div>

        {/* Logo Parceiro */}
        <div className="flex items-center gap-2 text-muted-foreground">
          <div className="w-6 h-6 bg-muted rounded flex items-center justify-center">
            <Building2 size={14} />
          </div>
          <span className="text-sm">Cajá</span>
        </div>

        {/* Informações da Unidade */}
        <div className="relative">
          <button
            onClick={() => setShowUnitMenu(!showUnitMenu)}
            className="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-accent transition-colors"
          >
            <div className="text-left">
              <div className="flex items-center gap-1 text-sm font-medium">
                <MapPin size={14} />
                Unidade Recife
                <ChevronDown size={14} />
              </div>
              <div className="text-xs text-muted-foreground">
                CNPJ: 12.345.678/0001-90
              </div>
            </div>
          </button>

          {showUnitMenu && (
            <div className="absolute top-full left-0 mt-1 w-64 bg-popover border border-border rounded-lg shadow-lg py-2 z-50">
              <div className="px-3 py-2 border-b border-border">
                <div className="text-sm font-medium">Unidades Disponíveis</div>
              </div>
              <button className="w-full text-left px-3 py-2 hover:bg-accent text-sm">
                <div className="font-medium">Unidade Recife</div>
                <div className="text-xs text-muted-foreground">CNPJ: 12.345.678/0001-90</div>
              </button>
              <button className="w-full text-left px-3 py-2 hover:bg-accent text-sm">
                <div className="font-medium">Unidade São Paulo</div>
                <div className="text-xs text-muted-foreground">CNPJ: 12.345.678/0001-91</div>
              </button>
              <button className="w-full text-left px-3 py-2 hover:bg-accent text-sm">
                <div className="font-medium">Unidade Rio de Janeiro</div>
                <div className="text-xs text-muted-foreground">CNPJ: 12.345.678/0001-92</div>
              </button>
            </div>
          )}
        </div>
      </div>

      {/* Ações do Usuário */}
      <div className="flex items-center gap-4">
        {/* Notificações */}
        <button className="relative p-2 rounded-lg hover:bg-accent transition-colors">
          <Bell size={20} />
          <span className="absolute -top-1 -right-1 w-5 h-5 bg-destructive text-white text-xs rounded-full flex items-center justify-center">
            3
          </span>
        </button>

        {/* Menu do Usuário */}
        <div className="relative">
          <button
            onClick={() => setShowUserMenu(!showUserMenu)}
            className="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-accent transition-colors"
          >
            <div className="w-8 h-8 bg-primary rounded-full flex items-center justify-center text-primary-foreground font-medium">
              {user?.username?.charAt(0).toUpperCase()}
            </div>
            <div className="text-left">
              <div className="text-sm font-medium">{user?.username}</div>
              <div className="text-xs text-muted-foreground capitalize">{user?.role}</div>
            </div>
            <ChevronDown size={14} />
          </button>

          {showUserMenu && (
            <div className="absolute top-full right-0 mt-1 w-48 bg-popover border border-border rounded-lg shadow-lg py-2 z-50">
              <div className="px-3 py-2 border-b border-border">
                <div className="text-sm font-medium">{user?.username}</div>
                <div className="text-xs text-muted-foreground">{user?.email}</div>
              </div>
              <button className="w-full text-left px-3 py-2 hover:bg-accent text-sm flex items-center gap-2">
                <User size={16} />
                Perfil
              </button>
              <button 
                onClick={logout}
                className="w-full text-left px-3 py-2 hover:bg-accent text-sm text-destructive"
              >
                Sair
              </button>
            </div>
          )}
        </div>
      </div>
    </header>
  );
};

export default Header;

