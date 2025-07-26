import React, { useState, useEffect } from 'react';
import { 
  Users as CustomersIcon, 
  Search, 
  Filter, 
  Plus,
  Mail,
  Building,
  Phone,
  Calendar
} from 'lucide-react';
import apiService from '../../services/api';

const Customers = () => {
  const [customers, setCustomers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCompany, setFilterCompany] = useState('all');

  useEffect(() => {
    loadCustomers();
  }, []);

  const loadCustomers = async () => {
    try {
      const response = await apiService.getCustomers();
      setCustomers(response);
    } catch (error) {
      console.error('Erro ao carregar clientes:', error);
    } finally {
      setLoading(false);
    }
  };

  const filteredCustomers = customers.filter(customer => {
    const matchesSearch = customer.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         customer.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
                         (customer.company && customer.company.toLowerCase().includes(searchTerm.toLowerCase()));
    const matchesCompany = filterCompany === 'all' || customer.company === filterCompany;
    return matchesSearch && matchesCompany;
  });

  const uniqueCompanies = [...new Set(customers.map(c => c.company).filter(Boolean))];

  const getCompanyColor = (company) => {
    const colors = [
      'bg-blue-100 text-blue-800',
      'bg-green-100 text-green-800',
      'bg-purple-100 text-purple-800',
      'bg-orange-100 text-orange-800',
      'bg-pink-100 text-pink-800'
    ];
    const index = company ? company.length % colors.length : 0;
    return colors[index];
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Cabeçalho */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-foreground flex items-center gap-3">
            <CustomersIcon size={32} />
            Clientes
          </h1>
          <p className="text-muted-foreground mt-1">Gerenciar clientes do sistema</p>
        </div>
        <button className="btn-primary flex items-center gap-2">
          <Plus size={20} />
          Novo cliente
        </button>
      </div>

      {/* Filtros e Busca */}
      <div className="bg-card border border-border rounded-lg p-6">
        <div className="flex flex-col sm:flex-row gap-4">
          {/* Busca */}
          <div className="flex-1">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground" size={20} />
              <input
                type="text"
                placeholder="Buscar por nome, email ou empresa..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full pl-10 pr-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
              />
            </div>
          </div>

          {/* Filtro por Empresa */}
          <div className="sm:w-48">
            <div className="relative">
              <Filter className="absolute left-3 top-1/2 transform -translate-y-1/2 text-muted-foreground" size={20} />
              <select
                value={filterCompany}
                onChange={(e) => setFilterCompany(e.target.value)}
                className="w-full pl-10 pr-4 py-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input appearance-none"
              >
                <option value="all">Todas as empresas</option>
                {uniqueCompanies.map((company) => (
                  <option key={company} value={company}>{company}</option>
                ))}
              </select>
            </div>
          </div>
        </div>
      </div>

      {/* Lista de Clientes */}
      <div className="bg-card border border-border rounded-lg">
        <div className="p-6 border-b border-border">
          <h2 className="text-lg font-semibold">
            {filteredCustomers.length} cliente{filteredCustomers.length !== 1 ? 's' : ''} encontrado{filteredCustomers.length !== 1 ? 's' : ''}
          </h2>
        </div>

        <div className="divide-y divide-border">
          {filteredCustomers.length === 0 ? (
            <div className="p-8 text-center text-muted-foreground">
              <CustomersIcon size={48} className="mx-auto mb-4 opacity-50" />
              <p>Nenhum cliente encontrado</p>
            </div>
          ) : (
            filteredCustomers.map((customer) => (
              <div key={customer.id} className="p-6 hover:bg-accent/50 transition-colors cursor-pointer">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-4">
                    {/* Avatar */}
                    <div className="w-12 h-12 bg-gradient-to-br from-green-500 to-green-600 rounded-full flex items-center justify-center text-white font-semibold text-lg">
                      {customer.name.charAt(0).toUpperCase()}
                    </div>

                    {/* Informações do cliente */}
                    <div>
                      <h3 className="font-semibold text-foreground">{customer.name}</h3>
                      <div className="flex items-center gap-4 text-sm text-muted-foreground mt-1">
                        <div className="flex items-center gap-1">
                          <Mail size={14} />
                          {customer.email}
                        </div>
                        {customer.phone && (
                          <div className="flex items-center gap-1">
                            <Phone size={14} />
                            {customer.phone}
                          </div>
                        )}
                      </div>
                    </div>
                  </div>

                  {/* Empresa e Data */}
                  <div className="flex flex-col items-end gap-2">
                    {customer.company && (
                      <span className={`px-3 py-1 rounded-full text-xs font-medium flex items-center gap-1 ${getCompanyColor(customer.company)}`}>
                        <Building size={12} />
                        {customer.company}
                      </span>
                    )}
                    {customer.created_at && (
                      <div className="flex items-center gap-1 text-xs text-muted-foreground">
                        <Calendar size={12} />
                        Cliente desde {new Date(customer.created_at).toLocaleDateString('pt-BR')}
                      </div>
                    )}
                  </div>
                </div>
              </div>
            ))
          )}
        </div>
      </div>

      {/* Estatísticas */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="metric-card">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
              <CustomersIcon className="text-blue-600" size={20} />
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Total de clientes</p>
              <p className="text-2xl font-bold">{customers.length}</p>
            </div>
          </div>
        </div>

        <div className="metric-card">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
              <Building className="text-green-600" size={20} />
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Empresas</p>
              <p className="text-2xl font-bold">{uniqueCompanies.length}</p>
            </div>
          </div>
        </div>

        <div className="metric-card">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
              <Calendar className="text-purple-600" size={20} />
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Novos este mês</p>
              <p className="text-2xl font-bold">
                {customers.filter(c => {
                  if (!c.created_at) return false;
                  const created = new Date(c.created_at);
                  const now = new Date();
                  return created.getMonth() === now.getMonth() && created.getFullYear() === now.getFullYear();
                }).length}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Customers;

