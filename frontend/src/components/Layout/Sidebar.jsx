import React from 'react';
import { 
  Home, 
  Ticket, 
  Users, 
  UserCheck, 
  BarChart3, 
  Settings,
  LogOut
} from 'lucide-react';
import { useAuth } from '../../contexts/AuthContext';

const Sidebar = ({ activeItem, onItemClick }) => {
  const { logout } = useAuth();

  const menuItems = [
    { id: 'dashboard', icon: Home, label: 'Dashboard' },
    { id: 'tickets', icon: Ticket, label: 'Tickets' },
    { id: 'customers', icon: Users, label: 'Clientes' },
    { id: 'users', icon: UserCheck, label: 'Usuários' },
    { id: 'reports', icon: BarChart3, label: 'Relatórios' },
    { id: 'settings', icon: Settings, label: 'Configurações' },
  ];

  const handleLogout = () => {
    logout();
  };

  return (
    <div className="fixed left-0 top-0 h-full w-16 bg-sidebar border-r border-sidebar-border flex flex-col items-center py-4 z-40">
      {/* Logo */}
      <div className="mb-8">
        <div className="w-10 h-10 caja-gradient rounded-lg flex items-center justify-center text-white font-bold text-lg">
          C
        </div>
      </div>

      {/* Menu Items */}
      <nav className="flex-1 flex flex-col gap-2">
        {menuItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeItem === item.id;
          
          return (
            <button
              key={item.id}
              onClick={() => onItemClick(item.id)}
              className={`sidebar-item ${isActive ? 'active' : ''}`}
              title={item.label}
            >
              <Icon size={20} />
              <div className="sidebar-tooltip">
                {item.label}
              </div>
            </button>
          );
        })}
      </nav>

      {/* Logout */}
      <button
        onClick={handleLogout}
        className="sidebar-item text-destructive hover:bg-destructive/10"
        title="Sair"
      >
        <LogOut size={20} />
        <div className="sidebar-tooltip">
          Sair
        </div>
      </button>
    </div>
  );
};

export default Sidebar;

