import React, { useState, useEffect } from 'react';
import { 
  ArrowLeft,
  Calendar,
  Clock,
  User,
  Building,
  Mail,
  Phone,
  AlertCircle,
  MessageSquare,
  Edit,
  Save,
  X,
  Plus
} from 'lucide-react';
import { useParams, useNavigate } from 'react-router-dom';
import apiService from '../../services/api';

const TicketDetails = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [ticket, setTicket] = useState(null);
  const [loading, setLoading] = useState(true);
  const [editing, setEditing] = useState(false);
  const [newNote, setNewNote] = useState('');
  const [editForm, setEditForm] = useState({
    status: '',
    priority: '',
    assigned_to: ''
  });

  useEffect(() => {
    loadTicketDetails();
  }, [id]);

  const loadTicketDetails = async () => {
    try {
      const response = await apiService.getTicket(id);
      setTicket(response);
      setEditForm({
        status: response.status,
        priority: response.priority,
        assigned_to: response.assigned_to
      });
    } catch (error) {
      console.error('Erro ao carregar detalhes do ticket:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleSaveChanges = async () => {
    try {
      await apiService.updateTicket(id, editForm);
      
      setTicket(prev => ({
        ...prev,
        ...editForm,
        updated_at: new Date().toISOString()
      }));
      
      setEditing(false);
    } catch (error) {
      console.error('Erro ao atualizar ticket:', error);
    }
  };

  const handleAddNote = async () => {
    if (!newNote.trim()) return;
    
    try {
      // Aqui faria a chamada para adicionar a nota
      const note = {
        id: Date.now(),
        author: 'Usuário Atual',
        content: newNote,
        created_at: new Date().toISOString()
      };
      
      setTicket(prev => ({
        ...prev,
        notes: [...prev.notes, note]
      }));
      
      setNewNote('');
    } catch (error) {
      console.error('Erro ao adicionar nota:', error);
    }
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'aberto':
        return 'bg-blue-100 text-blue-800';
      case 'em_andamento':
        return 'bg-yellow-100 text-yellow-800';
      case 'concluido':
        return 'bg-green-100 text-green-800';
      case 'fechado':
        return 'bg-gray-100 text-gray-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  const getPriorityColor = (priority) => {
    switch (priority) {
      case 'urgente':
        return 'bg-red-100 text-red-800';
      case 'alta':
        return 'bg-orange-100 text-orange-800';
      case 'media':
        return 'bg-yellow-100 text-yellow-800';
      case 'baixa':
        return 'bg-green-100 text-green-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
      </div>
    );
  }

  if (!ticket) {
    return (
      <div className="text-center py-12">
        <AlertCircle size={48} className="mx-auto mb-4 text-muted-foreground" />
        <h2 className="text-xl font-semibold mb-2">Ticket não encontrado</h2>
        <p className="text-muted-foreground mb-4">O ticket solicitado não existe ou foi removido.</p>
        <button onClick={() => navigate('/tickets')} className="btn-primary">
          Voltar para tickets
        </button>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Cabeçalho */}
      <div className="flex items-center gap-4">
        <button 
          onClick={() => navigate(-1)}
          className="p-2 hover:bg-accent rounded-lg transition-colors"
        >
          <ArrowLeft size={20} />
        </button>
        <div className="flex-1">
          <h1 className="text-3xl font-bold text-foreground">Ticket #{ticket.id}</h1>
          <p className="text-muted-foreground mt-1">{ticket.title}</p>
        </div>
        <div className="flex items-center gap-2">
          {!editing ? (
            <button 
              onClick={() => setEditing(true)}
              className="btn-secondary flex items-center gap-2"
            >
              <Edit size={16} />
              Editar
            </button>
          ) : (
            <div className="flex gap-2">
              <button 
                onClick={handleSaveChanges}
                className="btn-primary flex items-center gap-2"
              >
                <Save size={16} />
                Salvar
              </button>
              <button 
                onClick={() => setEditing(false)}
                className="btn-secondary flex items-center gap-2"
              >
                <X size={16} />
                Cancelar
              </button>
            </div>
          )}
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Coluna Principal */}
        <div className="lg:col-span-2 space-y-6">
          {/* Detalhes do Ticket */}
          <div className="bg-card border border-border rounded-lg p-6">
            <h2 className="text-lg font-semibold mb-4">Detalhes do Ticket</h2>
            
            <div className="space-y-4">
              <div>
                <label className="text-sm font-medium text-muted-foreground">Descrição</label>
                <p className="mt-1 text-foreground">{ticket.description}</p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="text-sm font-medium text-muted-foreground">Status</label>
                  {editing ? (
                    <select
                      value={editForm.status}
                      onChange={(e) => setEditForm(prev => ({ ...prev, status: e.target.value }))}
                      className="mt-1 w-full p-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
                    >
                      <option value="aberto">Aberto</option>
                      <option value="em_andamento">Em Andamento</option>
                      <option value="concluido">Concluído</option>
                      <option value="fechado">Fechado</option>
                    </select>
                  ) : (
                    <div className="mt-1">
                      <span className={`px-3 py-1 rounded-full text-xs font-medium ${getStatusColor(ticket.status)}`}>
                        {ticket.status.replace('_', ' ')}
                      </span>
                    </div>
                  )}
                </div>

                <div>
                  <label className="text-sm font-medium text-muted-foreground">Prioridade</label>
                  {editing ? (
                    <select
                      value={editForm.priority}
                      onChange={(e) => setEditForm(prev => ({ ...prev, priority: e.target.value }))}
                      className="mt-1 w-full p-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
                    >
                      <option value="baixa">Baixa</option>
                      <option value="media">Média</option>
                      <option value="alta">Alta</option>
                      <option value="urgente">Urgente</option>
                    </select>
                  ) : (
                    <div className="mt-1">
                      <span className={`px-3 py-1 rounded-full text-xs font-medium ${getPriorityColor(ticket.priority)}`}>
                        {ticket.priority}
                      </span>
                    </div>
                  )}
                </div>
              </div>

              <div>
                <label className="text-sm font-medium text-muted-foreground">Atribuído para</label>
                {editing ? (
                  <input
                    type="text"
                    value={editForm.assigned_to}
                    onChange={(e) => setEditForm(prev => ({ ...prev, assigned_to: e.target.value }))}
                    className="mt-1 w-full p-2 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input"
                  />
                ) : (
                  <p className="mt-1 text-foreground">{ticket.assigned_to}</p>
                )}
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                  <label className="text-sm font-medium text-muted-foreground">Criado em</label>
                  <div className="mt-1 flex items-center gap-2 text-foreground">
                    <Calendar size={16} />
                    {new Date(ticket.created_at).toLocaleString('pt-BR')}
                  </div>
                </div>

                <div>
                  <label className="text-sm font-medium text-muted-foreground">Última atualização</label>
                  <div className="mt-1 flex items-center gap-2 text-foreground">
                    <Clock size={16} />
                    {new Date(ticket.updated_at).toLocaleString('pt-BR')}
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Histórico de Notas */}
          <div className="bg-card border border-border rounded-lg p-6">
            <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <MessageSquare size={20} />
              Histórico de Interações
            </h2>

            <div className="space-y-4 mb-6">
              {ticket.notes.map((note) => (
                <div key={note.id} className="border border-border rounded-lg p-4">
                  <div className="flex items-center justify-between mb-2">
                    <span className="font-medium text-foreground">{note.author}</span>
                    <span className="text-sm text-muted-foreground">
                      {new Date(note.created_at).toLocaleString('pt-BR')}
                    </span>
                  </div>
                  <p className="text-foreground">{note.content}</p>
                </div>
              ))}
            </div>

            {/* Adicionar Nova Nota */}
            <div className="border-t border-border pt-4">
              <label className="text-sm font-medium text-muted-foreground">Adicionar nota</label>
              <div className="mt-2 space-y-3">
                <textarea
                  value={newNote}
                  onChange={(e) => setNewNote(e.target.value)}
                  placeholder="Digite sua nota aqui..."
                  rows={3}
                  className="w-full p-3 border border-border rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent bg-input resize-none"
                />
                <button 
                  onClick={handleAddNote}
                  disabled={!newNote.trim()}
                  className="btn-primary flex items-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <Plus size={16} />
                  Adicionar nota
                </button>
              </div>
            </div>
          </div>
        </div>

        {/* Sidebar - Informações do Cliente */}
        <div className="space-y-6">
          <div className="bg-card border border-border rounded-lg p-6">
            <h2 className="text-lg font-semibold mb-4 flex items-center gap-2">
              <User size={20} />
              Informações do Cliente
            </h2>

            <div className="space-y-4">
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 bg-gradient-to-br from-green-500 to-green-600 rounded-full flex items-center justify-center text-white font-semibold text-lg">
                  {ticket.customer.name.charAt(0).toUpperCase()}
                </div>
                <div>
                  <h3 className="font-semibold text-foreground">{ticket.customer.name}</h3>
                  <p className="text-sm text-muted-foreground">{ticket.customer.company}</p>
                </div>
              </div>

              <div className="space-y-3">
                <div className="flex items-center gap-2 text-sm">
                  <Mail size={16} className="text-muted-foreground" />
                  <span className="text-foreground">{ticket.customer.email}</span>
                </div>
                
                <div className="flex items-center gap-2 text-sm">
                  <Phone size={16} className="text-muted-foreground" />
                  <span className="text-foreground">{ticket.customer.phone}</span>
                </div>
                
                <div className="flex items-center gap-2 text-sm">
                  <Building size={16} className="text-muted-foreground" />
                  <span className="text-foreground">{ticket.customer.company}</span>
                </div>
              </div>

              <button className="w-full btn-secondary text-sm">
                Ver perfil completo
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TicketDetails;

