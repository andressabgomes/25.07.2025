import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
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

const Sidebar = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const menuItems = [
    { id: 'dashboard', icon: Home, label: 'Dashboard', path: '/dashboard' },
    { id: 'tickets', icon: Ticket, label: 'Tickets', path: '/tickets' },
    { id: 'customers', icon: Users, label: 'Clientes', path: '/customers' },
    { id: 'users', icon: UserCheck, label: 'Usuários', path: '/users' },
    { id: 'reports', icon: BarChart3, label: 'Relatórios', path: '/reports' },
    { id: 'settings', icon: Settings, label: 'Configurações', path: '/settings' },
  ];

  const handleLogout = () => {
    logout();
  };

  const handleItemClick = (path) => {
    navigate(path);
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
          const isActive = location.pathname === item.path || 
                          (item.path === '/dashboard' && location.pathname === '/');
          
          return (
            <button
              key={item.id}
              onClick={() => handleItemClick(item.path)}
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

