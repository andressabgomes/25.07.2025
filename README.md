# Customer Support - Sistema Cajá

Sistema fullstack completo de atendimento ao cliente com design tropical da marca Cajá, desenvolvido com Flask (backend) e React + Tailwind (frontend).

## 🎨 Características do Design

### Interface Tropical Cajá
- **Paleta de cores**: Amarelo vibrante (#FFD33D), verde folha (#2E7D32), laranja suave (#FFAB40)
- **Layout responsivo** com sidebar compacta (64px) e header corporativo
- **Microinterações** suaves e feedback visual em todos os estados
- **Tipografia moderna** e amigável para melhor experiência do usuário

### Componentes Principais
- **Sidebar vertical** com ícones, tooltips e indicador de item ativo
- **Header corporativo** com logos, informações da unidade e menu do usuário
- **Dashboard** com gráficos comparativos e métricas de atendimento
- **Chatbot flutuante** para suporte instantâneo

## 🏗️ Arquitetura

### Backend (Flask)
- **Porta**: 5000
- **Estrutura modular**: models/, routes/, main.py
- **Autenticação**: JWT com middleware de segurança
- **Banco de dados**: SQLite com SQLAlchemy
- **API RESTful** com CORS habilitado

### Frontend (React + Tailwind)
- **Porta**: 5173
- **Componentização clara** e reutilizável
- **Gráficos interativos** com Recharts
- **Responsividade garantida** para desktop e mobile
- **Gerenciamento de estado** com Context API

## 🚀 Como Executar

### Pré-requisitos
- Python 3.11+
- Node.js 20+
- pnpm

### Iniciando o Backend
```bash
chmod +x start_backend.sh
./start_backend.sh
```

### Iniciando o Frontend
```bash
chmod +x start_frontend.sh
./start_frontend.sh
```

### Acesso
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:5000/api

## 👥 Contas de Demonstração

| Tipo | Email | Senha | Descrição |
|------|-------|-------|-----------|
| Admin | admin@teste.com | admin123 | Acesso completo ao sistema |
| Agente | carlos@teste.com | 123456 | Agente de atendimento |
| Agente | ana@teste.com | 123456 | Agente de atendimento |
| Manager | manager@teste.com | 123456 | Gerente de equipe |

## 📊 Funcionalidades

### Dashboard
- **Gráfico de barras** comparativo (abertos vs concluídos)
- **Métricas de performance**: média, intervalo, picos e vales
- **Abas interativas**: próximos e recentes atendimentos
- **Botão de ação** para novos chamados

### Gestão de Tickets
- **CRUD completo** de tickets
- **Filtros por status** e prioridade
- **Atribuição de agentes**
- **Histórico de atualizações**

### Gestão de Clientes
- **Cadastro de clientes** com informações completas
- **Histórico de tickets** por cliente
- **Busca e paginação**

### Gestão de Usuários
- **Controle de acesso** por roles (admin, agent, manager)
- **Autenticação segura** com JWT
- **Perfis de usuário** personalizáveis

## 🛠️ Tecnologias Utilizadas

### Backend
- **Flask 2.3.3** - Framework web
- **SQLAlchemy 3.0.5** - ORM para banco de dados
- **Flask-CORS 4.0.0** - Suporte a CORS
- **PyJWT 2.8.0** - Autenticação JWT
- **Werkzeug 2.3.7** - Utilitários WSGI

### Frontend
- **React 18** - Biblioteca de interface
- **Tailwind CSS** - Framework de estilos
- **Recharts** - Biblioteca de gráficos
- **Lucide React** - Ícones modernos
- **Vite** - Build tool e dev server

## 📁 Estrutura do Projeto

```
Customer_Support/
├── backend/
│   ├── src/
│   │   ├── models/          # Modelos de dados
│   │   ├── routes/          # Rotas da API
│   │   ├── static/          # Arquivos estáticos
│   │   └── main.py          # Ponto de entrada
│   ├── venv/                # Ambiente virtual
│   ├── requirements.txt     # Dependências Python
│   └── seed_data.py         # Script de dados de teste
├── frontend/
│   ├── src/
│   │   ├── components/      # Componentes React
│   │   ├── contexts/        # Contextos (Auth, etc)
│   │   ├── services/        # Serviços de API
│   │   └── assets/          # Recursos estáticos
│   ├── public/              # Arquivos públicos
│   └── package.json         # Dependências Node.js
├── start_backend.sh         # Script de inicialização backend
├── start_frontend.sh        # Script de inicialização frontend
└── README.md               # Esta documentação
```

## 🎯 Próximos Passos

### Melhorias Sugeridas
1. **Notificações em tempo real** com WebSockets
2. **Upload de arquivos** em tickets
3. **Relatórios avançados** com exportação
4. **Chat interno** entre agentes
5. **Integração com APIs externas** (email, SMS)

### Deploy em Produção
1. **Backend**: Usar Gunicorn + Nginx
2. **Frontend**: Build estático com CDN
3. **Banco de dados**: PostgreSQL ou MySQL
4. **Monitoramento**: Logs e métricas de performance

## 📝 Licença

Este projeto foi desenvolvido como demonstração de sistema fullstack moderno com design tropical da marca Cajá.

---

**Desenvolvido com ❤️ para a marca Cajá**

