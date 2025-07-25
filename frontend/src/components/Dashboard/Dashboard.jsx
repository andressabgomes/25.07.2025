import React, { useState, useEffect } from 'react';
import { 
  Plus, 
  MessageCircle, 
  TrendingUp, 
  TrendingDown,
  Clock,
  CheckCircle,
  AlertCircle,
  Users
} from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import apiService from '../../services/api';

const Dashboard = () => {
  const [stats, setStats] = useState(null);
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('proximos');

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    try {
      const [statsResponse, ticketsResponse] = await Promise.all([
        apiService.getTicketStats(),
        apiService.getTickets({ per_page: 10 })
      ]);
      
      setStats(statsResponse);
      setTickets(ticketsResponse.tickets || []);
    } catch (error) {
      console.error('Erro ao carregar dados:', error);
    } finally {
      setLoading(false);
    }
  };

  const formatChartData = () => {
    if (!stats?.monthly) return [];
    
    const months = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'];
    
    return stats.monthly.slice(0, 12).reverse().map(item => ({
      month: months[item.month - 1],
      abertos: item.open,
      concluidos: item.closed
    }));
  };

  const getMetrics = () => {
    if (!stats) return {};
    
    const chartData = formatChartData();
    const totalOpen = chartData.reduce((sum, item) => sum + item.abertos, 0);
    const totalClosed = chartData.reduce((sum, item) => sum + item.concluidos, 0);
    const avgOpen = Math.round(totalOpen / chartData.length);
    
    // Encontrar pico e vale
    const maxMonth = chartData.reduce((max, item) => 
      (item.abertos + item.concluidos) > (max.abertos + max.concluidos) ? item : max, chartData[0] || {});
    const minMonth = chartData.reduce((min, item) => 
      (item.abertos + item.concluidos) < (min.abertos + min.concluidos) ? item : min, chartData[0] || {});
    
    return {
      avgOpen,
      avgInterval: '3.2 dias',
      peak: { month: maxMonth.month, value: maxMonth.abertos + maxMonth.concluidos },
      valley: { month: minMonth.month, value: minMonth.abertos + minMonth.concluidos }
    };
  };

  const metrics = getMetrics();

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
          <h1 className="text-3xl font-bold text-foreground">Atendimento</h1>
          <p className="text-muted-foreground mt-1">Histórico de chamados</p>
        </div>
        <button className="btn-primary flex items-center gap-2">
          <Plus size={20} />
          Abrir novo chamado
        </button>
      </div>

      {/* Gráfico de Barras */}
      <div className="bg-card border border-border rounded-lg p-6">
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={formatChartData()}>
              <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
              <XAxis 
                dataKey="month" 
                stroke="var(--muted-foreground)"
                fontSize={12}
              />
              <YAxis 
                stroke="var(--muted-foreground)"
                fontSize={12}
                domain={[0, 5000]}
              />
              <Tooltip 
                contentStyle={{
                  backgroundColor: 'var(--card)',
                  border: '1px solid var(--border)',
                  borderRadius: '8px'
                }}
              />
              <Bar 
                dataKey="abertos" 
                fill="#e5e7eb" 
                name="Abertos"
                radius={[2, 2, 0, 0]}
              />
              <Bar 
                dataKey="concluidos" 
                fill="var(--caja-yellow)" 
                name="Concluídos"
                radius={[2, 2, 0, 0]}
              />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Métricas */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="metric-card">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
              <TrendingUp className="text-blue-600" size={20} />
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Média de chamados abertos</p>
              <p className="text-2xl font-bold">{metrics.avgOpen}</p>
            </div>
          </div>
        </div>

        <div className="metric-card">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
              <Clock className="text-green-600" size={20} />
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Intervalo médio</p>
              <p className="text-2xl font-bold">{metrics.avgInterval}</p>
            </div>
          </div>
        </div>

        <div className="metric-card">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-orange-100 rounded-lg flex items-center justify-center">
              <TrendingUp className="text-orange-600" size={20} />
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Pico de volume</p>
              <p className="text-2xl font-bold">{metrics.peak?.value}</p>
              <p className="text-xs text-muted-foreground">{metrics.peak?.month}</p>
            </div>
          </div>
        </div>

        <div className="metric-card">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
              <TrendingDown className="text-purple-600" size={20} />
            </div>
            <div>
              <p className="text-sm text-muted-foreground">Vale de volume</p>
              <p className="text-2xl font-bold">{metrics.valley?.value}</p>
              <p className="text-xs text-muted-foreground">{metrics.valley?.month}</p>
            </div>
          </div>
        </div>
      </div>

      {/* Abas de Atendimentos */}
      <div className="bg-card border border-border rounded-lg">
        <div className="border-b border-border">
          <div className="flex">
            <button
              onClick={() => setActiveTab('proximos')}
              className={`px-6 py-4 text-sm font-medium border-b-2 transition-colors ${
                activeTab === 'proximos'
                  ? 'border-primary text-primary'
                  : 'border-transparent text-muted-foreground hover:text-foreground'
              }`}
            >
              Próximos atendimentos
            </button>
            <button
              onClick={() => setActiveTab('recentes')}
              className={`px-6 py-4 text-sm font-medium border-b-2 transition-colors ${
                activeTab === 'recentes'
                  ? 'border-primary text-primary'
                  : 'border-transparent text-muted-foreground hover:text-foreground'
              }`}
            >
              Atendimentos recentes
            </button>
          </div>
        </div>

        <div className="p-6">
          <div className="space-y-4">
            {tickets.slice(0, 5).map((ticket) => (
              <div key={ticket.id} className="flex items-center justify-between p-4 border border-border rounded-lg hover:bg-accent/50 transition-colors">
                <div className="flex items-center gap-4">
                  <div className={`w-3 h-3 rounded-full ${
                    ticket.priority === 'urgente' ? 'bg-red-500' :
                    ticket.priority === 'alta' ? 'bg-orange-500' :
                    ticket.priority === 'media' ? 'bg-yellow-500' : 'bg-green-500'
                  }`} />
                  <div>
                    <h4 className="font-medium">{ticket.title}</h4>
                    <p className="text-sm text-muted-foreground">
                      {ticket.customer_name} • {new Date(ticket.created_at).toLocaleDateString('pt-BR')}
                    </p>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                    ticket.status === 'aberto' ? 'bg-blue-100 text-blue-800' :
                    ticket.status === 'em_andamento' ? 'bg-yellow-100 text-yellow-800' :
                    ticket.status === 'concluido' ? 'bg-green-100 text-green-800' :
                    'bg-gray-100 text-gray-800'
                  }`}>
                    {ticket.status.replace('_', ' ')}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Chatbot Flutuante */}
      <button className="fixed bottom-6 right-6 w-14 h-14 bg-primary text-primary-foreground rounded-full flex items-center justify-center shadow-lg hover:scale-105 transition-transform caja-shadow">
        <MessageCircle size={24} />
      </button>
    </div>
  );
};

export default Dashboard;

