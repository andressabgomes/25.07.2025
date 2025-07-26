import React, { useState } from 'react';
import { 
  Settings as SettingsIcon, 
  User, 
  Bell, 
  Shield, 
  Palette, 
  Database,
  Mail,
  Save,
  Eye,
  EyeOff,
  Building,
  Globe,
  Clock,
  Users
} from 'lucide-react';

const Settings = () => {
  const [activeTab, setActiveTab] = useState('profile');
  const [showPassword, setShowPassword] = useState(false);
  const [settings, setSettings] = useState({
    // Perfil
    name: 'Admin',
    email: 'admin@teste.com',
    phone: '(11) 99999-9999',
    currentPassword: '',
    newPassword: '',
    confirmPassword: '',
    
    // Notificações
    emailNotifications: true,
    pushNotifications: true,
    ticketUpdates: true,
    systemAlerts: true,
    weeklyReports: false,
    
    // Sistema
    companyName: 'Customer Support - Cajá',
    companyEmail: 'contato@caja.com',
    timezone: 'America/Sao_Paulo',
    language: 'pt-BR',
    autoAssignment: true,
    ticketAutoClose: 7,
    
    // Aparência
    theme: 'light',
    sidebarCollapsed: false,
    compactMode: false,
    
    // Segurança
    twoFactorAuth: false,
    sessionTimeout: 30,
    passwordExpiry: 90
  });

  const handleInputChange = (field, value) => {
    setSettings(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const handleSave = (section) => {
    // Aqui faria a chamada para salvar as configurações
    console.log(`Salvando configurações de ${section}:`, settings);
    // Simular sucesso
    alert(`Configurações de ${section} salvas com sucesso!`);
  };

  const tabs = [
    { id: 'profile', label: 'Perfil', icon: User },
    { id: 'notifications', label: 'Notificações', icon: Bell },
    { id: 'system', label: 'Sistema', icon: Database },
    { id: 'appearance', label: 'Aparência', icon: Palette },
    { id: 'security', label: 'Segurança', icon: Shield }
  ];

  const renderProfileTab = () => (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-semibold mb-4">Informações Pessoais</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Nome</label>
            <input
              type="text"
              value={settings.name}
              onChange={(e) => handleInputChange('name', e.target.value)}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Email</label>
            <input
              type="email"
              value={settings.email}
              onChange={(e) => handleInputChange('email', e.target.value)}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Telefone</label>
            <input
              type="tel"
              value={settings.phone}
              onChange={(e) => handleInputChange('phone', e.target.value)}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
            />
          </div>
        </div>
      </div>

      <div>
        <h3 className="text-lg font-semibold mb-4">Alterar Senha</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Senha Atual</label>
            <div className="relative">
              <input
                type={showPassword ? "text" : "password"}
                value={settings.currentPassword}
                onChange={(e) => handleInputChange('currentPassword', e.target.value)}
                className="w-full p-3 pr-10 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3 top-1/2 transform -translate-y-1/2 text-muted-foreground hover:text-foreground"
              >
                {showPassword ? <EyeOff size={16} /> : <Eye size={16} />}
              </button>
            </div>
          </div>
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Nova Senha</label>
            <input
              type="password"
              value={settings.newPassword}
              onChange={(e) => handleInputChange('newPassword', e.target.value)}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Confirmar Senha</label>
            <input
              type="password"
              value={settings.confirmPassword}
              onChange={(e) => handleInputChange('confirmPassword', e.target.value)}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
            />
          </div>
        </div>
      </div>

      <button 
        onClick={() => handleSave('perfil')}
        className="btn-primary flex items-center gap-2"
      >
        <Save size={16} />
        Salvar Alterações
      </button>
    </div>
  );

  const renderNotificationsTab = () => (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-semibold mb-4">Preferências de Notificação</h3>
        <div className="space-y-4">
          {[
            { key: 'emailNotifications', label: 'Notificações por Email', description: 'Receber notificações importantes por email' },
            { key: 'pushNotifications', label: 'Notificações Push', description: 'Notificações em tempo real no navegador' },
            { key: 'ticketUpdates', label: 'Atualizações de Tickets', description: 'Ser notificado sobre mudanças nos tickets' },
            { key: 'systemAlerts', label: 'Alertas do Sistema', description: 'Notificações sobre problemas técnicos' },
            { key: 'weeklyReports', label: 'Relatórios Semanais', description: 'Receber resumo semanal por email' }
          ].map((item) => (
            <div key={item.key} className="flex items-center justify-between p-4 border border-border rounded-lg">
              <div>
                <h4 className="font-medium">{item.label}</h4>
                <p className="text-sm text-muted-foreground">{item.description}</p>
              </div>
              <label className="relative inline-flex items-center cursor-pointer">
                <input
                  type="checkbox"
                  checked={settings[item.key]}
                  onChange={(e) => handleInputChange(item.key, e.target.checked)}
                  className="sr-only peer"
                />
                <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/20 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
              </label>
            </div>
          ))}
        </div>
      </div>

      <button 
        onClick={() => handleSave('notificações')}
        className="btn-primary flex items-center gap-2"
      >
        <Save size={16} />
        Salvar Preferências
      </button>
    </div>
  );

  const renderSystemTab = () => (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-semibold mb-4">Configurações da Empresa</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Nome da Empresa</label>
            <input
              type="text"
              value={settings.companyName}
              onChange={(e) => handleInputChange('companyName', e.target.value)}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Email da Empresa</label>
            <input
              type="email"
              value={settings.companyEmail}
              onChange={(e) => handleInputChange('companyEmail', e.target.value)}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
            />
          </div>
        </div>
      </div>

      <div>
        <h3 className="text-lg font-semibold mb-4">Configurações Regionais</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Fuso Horário</label>
            <select
              value={settings.timezone}
              onChange={(e) => handleInputChange('timezone', e.target.value)}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
            >
              <option value="America/Sao_Paulo">São Paulo (GMT-3)</option>
              <option value="America/New_York">Nova York (GMT-5)</option>
              <option value="Europe/London">Londres (GMT+0)</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Idioma</label>
            <select
              value={settings.language}
              onChange={(e) => handleInputChange('language', e.target.value)}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
            >
              <option value="pt-BR">Português (Brasil)</option>
              <option value="en-US">English (US)</option>
              <option value="es-ES">Español</option>
            </select>
          </div>
        </div>
      </div>

      <div>
        <h3 className="text-lg font-semibold mb-4">Configurações de Tickets</h3>
        <div className="space-y-4">
          <div className="flex items-center justify-between p-4 border border-border rounded-lg">
            <div>
              <h4 className="font-medium">Atribuição Automática</h4>
              <p className="text-sm text-muted-foreground">Atribuir tickets automaticamente aos agentes disponíveis</p>
            </div>
            <label className="relative inline-flex items-center cursor-pointer">
              <input
                type="checkbox"
                checked={settings.autoAssignment}
                onChange={(e) => handleInputChange('autoAssignment', e.target.checked)}
                className="sr-only peer"
              />
              <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/20 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
            </label>
          </div>
          
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Fechamento Automático (dias)</label>
            <input
              type="number"
              value={settings.ticketAutoClose}
              onChange={(e) => handleInputChange('ticketAutoClose', parseInt(e.target.value))}
              className="w-full md:w-48 p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
              min="1"
              max="30"
            />
            <p className="text-sm text-muted-foreground mt-1">Tickets resolvidos serão fechados automaticamente após este período</p>
          </div>
        </div>
      </div>

      <button 
        onClick={() => handleSave('sistema')}
        className="btn-primary flex items-center gap-2"
      >
        <Save size={16} />
        Salvar Configurações
      </button>
    </div>
  );

  const renderAppearanceTab = () => (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-semibold mb-4">Tema</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            { value: 'light', label: 'Claro', description: 'Tema claro padrão' },
            { value: 'dark', label: 'Escuro', description: 'Tema escuro para ambientes com pouca luz' },
            { value: 'auto', label: 'Automático', description: 'Segue a preferência do sistema' }
          ].map((theme) => (
            <div
              key={theme.value}
              className={`p-4 border rounded-lg cursor-pointer transition-colors ${
                settings.theme === theme.value 
                  ? 'border-primary bg-primary/5' 
                  : 'border-border hover:border-primary/50'
              }`}
              onClick={() => handleInputChange('theme', theme.value)}
            >
              <div className="flex items-center gap-2 mb-2">
                <div className={`w-4 h-4 rounded-full border-2 ${settings.theme === theme.value ? 'border-primary bg-primary' : 'border-border'}`}>
                  {settings.theme === theme.value && (
                    <div className="w-full h-full rounded-full bg-white scale-50"></div>
                  )}
                </div>
                <h4 className="font-medium">{theme.label}</h4>
              </div>
              <p className="text-sm text-muted-foreground">{theme.description}</p>
            </div>
          ))}
        </div>
      </div>

      <div>
        <h3 className="text-lg font-semibold mb-4">Layout</h3>
        <div className="space-y-4">
          <div className="flex items-center justify-between p-4 border border-border rounded-lg">
            <div>
              <h4 className="font-medium">Sidebar Compacta</h4>
              <p className="text-sm text-muted-foreground">Reduzir o tamanho da barra lateral</p>
            </div>
            <label className="relative inline-flex items-center cursor-pointer">
              <input
                type="checkbox"
                checked={settings.sidebarCollapsed}
                onChange={(e) => handleInputChange('sidebarCollapsed', e.target.checked)}
                className="sr-only peer"
              />
              <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/20 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
            </label>
          </div>

          <div className="flex items-center justify-between p-4 border border-border rounded-lg">
            <div>
              <h4 className="font-medium">Modo Compacto</h4>
              <p className="text-sm text-muted-foreground">Reduzir espaçamentos e tamanhos de elementos</p>
            </div>
            <label className="relative inline-flex items-center cursor-pointer">
              <input
                type="checkbox"
                checked={settings.compactMode}
                onChange={(e) => handleInputChange('compactMode', e.target.checked)}
                className="sr-only peer"
              />
              <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/20 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
            </label>
          </div>
        </div>
      </div>

      <button 
        onClick={() => handleSave('aparência')}
        className="btn-primary flex items-center gap-2"
      >
        <Save size={16} />
        Salvar Preferências
      </button>
    </div>
  );

  const renderSecurityTab = () => (
    <div className="space-y-6">
      <div>
        <h3 className="text-lg font-semibold mb-4">Autenticação</h3>
        <div className="space-y-4">
          <div className="flex items-center justify-between p-4 border border-border rounded-lg">
            <div>
              <h4 className="font-medium">Autenticação de Dois Fatores</h4>
              <p className="text-sm text-muted-foreground">Adicionar uma camada extra de segurança ao login</p>
            </div>
            <label className="relative inline-flex items-center cursor-pointer">
              <input
                type="checkbox"
                checked={settings.twoFactorAuth}
                onChange={(e) => handleInputChange('twoFactorAuth', e.target.checked)}
                className="sr-only peer"
              />
              <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary/20 rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-primary"></div>
            </label>
          </div>
        </div>
      </div>

      <div>
        <h3 className="text-lg font-semibold mb-4">Sessão</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Timeout da Sessão (minutos)</label>
            <input
              type="number"
              value={settings.sessionTimeout}
              onChange={(e) => handleInputChange('sessionTimeout', parseInt(e.target.value))}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
              min="5"
              max="480"
            />
            <p className="text-sm text-muted-foreground mt-1">Tempo de inatividade antes do logout automático</p>
          </div>
          
          <div>
            <label className="block text-sm font-medium text-muted-foreground mb-2">Expiração da Senha (dias)</label>
            <input
              type="number"
              value={settings.passwordExpiry}
              onChange={(e) => handleInputChange('passwordExpiry', parseInt(e.target.value))}
              className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
              min="30"
              max="365"
            />
            <p className="text-sm text-muted-foreground mt-1">Período para renovação obrigatória da senha</p>
          </div>
        </div>
      </div>

      <button 
        onClick={() => handleSave('segurança')}
        className="btn-primary flex items-center gap-2"
      >
        <Save size={16} />
        Salvar Configurações
      </button>
    </div>
  );

  const renderTabContent = () => {
    switch (activeTab) {
      case 'profile':
        return renderProfileTab();
      case 'notifications':
        return renderNotificationsTab();
      case 'system':
        return renderSystemTab();
      case 'appearance':
        return renderAppearanceTab();
      case 'security':
        return renderSecurityTab();
      default:
        return renderProfileTab();
    }
  };

  return (
    <div className="space-y-6">
      {/* Cabeçalho */}
      <div>
        <h1 className="text-3xl font-bold text-foreground flex items-center gap-3">
          <SettingsIcon size={32} />
          Configurações
        </h1>
        <p className="text-muted-foreground mt-1">Gerencie suas preferências e configurações do sistema</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* Sidebar de Tabs */}
        <div className="lg:col-span-1">
          <div className="bg-card border border-border rounded-lg p-4">
            <nav className="space-y-2">
              {tabs.map((tab) => {
                const Icon = tab.icon;
                return (
                  <button
                    key={tab.id}
                    onClick={() => setActiveTab(tab.id)}
                    className={`w-full flex items-center gap-3 px-3 py-2 rounded-lg text-left transition-colors ${
                      activeTab === tab.id
                        ? 'bg-primary text-primary-foreground'
                        : 'hover:bg-accent text-foreground'
                    }`}
                  >
                    <Icon size={18} />
                    {tab.label}
                  </button>
                );
              })}
            </nav>
          </div>
        </div>

        {/* Conteúdo Principal */}
        <div className="lg:col-span-3">
          <div className="bg-card border border-border rounded-lg p-6">
            {renderTabContent()}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Settings;

