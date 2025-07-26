# Customer Support - Sistema de Atendimento ao Cliente

Sistema fullstack de atendimento ao cliente com design moderno, performance e escalabilidade.

## 🚀 Tecnologias

### Frontend
- **Next.js 15** - Framework React com TypeScript
- **Tailwind CSS** - Framework CSS utilitário
- **Recharts** - Biblioteca de gráficos
- **Lucide React** - Ícones modernos
- **Radix UI** - Componentes acessíveis

### Backend
- **FastAPI** - Framework Python moderno e rápido
- **SQLAlchemy 2.0** - ORM Python
- **Pydantic** - Validação de dados
- **JWT** - Autenticação segura
- **PostgreSQL** - Banco de dados relacional

### Infraestrutura
- **Docker** - Containerização
- **Docker Compose** - Orquestração de containers
- **PostgreSQL 15** - Banco de dados

## 🎨 Design

### Paleta de Cores (Tema Cajá)
- **Amarelo**: #FFD33D (Primary)
- **Verde**: #2E7D32 (Success)
- **Laranja**: #FFAB40 (Accent)
- **Cinza/Branco**: Neutros

### Layout
- **Header**: Logo + Unidade + Notificações + Perfil
- **Sidebar**: 64px com ícones e tooltips
- **Área Principal**: Dashboard com gráficos e métricas

## 📊 Funcionalidades

### Autenticação
- Login com JWT
- Controle de acesso por roles (Admin, Agent, Manager)
- Refresh tokens

### Dashboard
- Gráfico de barras (chamados abertos vs concluídos)
- Métricas em tempo real
- Abas de próximos e recentes atendimentos

### CRUD Completo
- **Usuários**: Gestão de usuários do sistema
- **Clientes**: Cadastro e gestão de clientes
- **Tickets**: Sistema completo de chamados

### Sistema de Tickets
- Status: Aberto, Em Progresso, Resolvido
- Prioridades: Baixa, Média, Alta, Urgente
- Atribuição de responsáveis
- Histórico de interações

## 🛠️ Instalação e Execução

### Pré-requisitos
- Docker e Docker Compose
- Node.js 20+ (para desenvolvimento)
- Python 3.11+ (para desenvolvimento)

### Execução com Docker (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/andressabgomes/25.07.2025.git
cd customer-support

# Execute com Docker Compose
docker-compose up -d

# Acesse a aplicação
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# Documentação API: http://localhost:8000/docs
```

### Execução em Desenvolvimento

#### Backend
```bash
cd backend

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env

# Execute o banco de dados
docker-compose up postgres -d

# Popule com dados de teste
python seed_data.py

# Execute o servidor
PYTHONPATH=/path/to/backend python -m uvicorn app.main:app --reload
```

#### Frontend
```bash
cd frontend

# Instale as dependências
npm install

# Execute o servidor de desenvolvimento
npm run dev
```

## 🔐 Dados de Teste

### Usuários
- **Admin**: admin@teste.com / admin123
- **Agente**: agente@teste.com / agente123
- **Gestor**: gestor@teste.com / gestor123

### Clientes
- João Silva (Empresa ABC Ltda)
- Maria Santos (Tech Solutions)
- Pedro Costa (Inovação Digital)
- Ana Oliveira (Consultoria XYZ)
- Carlos Lima (StartUp Moderna)

## 📡 API Endpoints

### Autenticação
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Usuário atual
- `POST /api/auth/refresh` - Refresh token

### Usuários
- `GET /api/users` - Listar usuários
- `POST /api/users` - Criar usuário
- `GET /api/users/{id}` - Obter usuário
- `PUT /api/users/{id}` - Atualizar usuário
- `DELETE /api/users/{id}` - Deletar usuário

### Clientes
- `GET /api/customers` - Listar clientes
- `POST /api/customers` - Criar cliente
- `GET /api/customers/{id}` - Obter cliente
- `PUT /api/customers/{id}` - Atualizar cliente
- `DELETE /api/customers/{id}` - Deletar cliente

### Tickets
- `GET /api/tickets` - Listar tickets
- `POST /api/tickets` - Criar ticket
- `GET /api/tickets/{id}` - Obter ticket
- `PUT /api/tickets/{id}` - Atualizar ticket
- `DELETE /api/tickets/{id}` - Deletar ticket
- `GET /api/tickets/stats` - Estatísticas

## 🚀 Deploy

### Manus Platform
O projeto está configurado para deploy automático na plataforma Manus:

```bash
# Frontend
npm run build
# Deploy via Manus frontend service

# Backend
# Deploy via Manus backend service
```

### Docker Production
```bash
# Build das imagens
docker-compose -f docker-compose.prod.yml build

# Execute em produção
docker-compose -f docker-compose.prod.yml up -d
```

## 📁 Estrutura do Projeto

```
customer-support/
├── backend/                 # API FastAPI
│   ├── app/
│   │   ├── api/            # Rotas da API
│   │   ├── core/           # Configurações
│   │   ├── models/         # Modelos SQLAlchemy
│   │   ├── schemas/        # Schemas Pydantic
│   │   └── services/       # Lógica de negócio
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/               # App Next.js
│   ├── src/
│   │   ├── app/           # App Router
│   │   ├── components/    # Componentes React
│   │   ├── contexts/      # Contextos React
│   │   └── lib/          # Utilitários
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml     # Orquestração
└── README.md
```

## 🔧 Configuração

### Variáveis de Ambiente

#### Backend (.env)
```env
DATABASE_URL=postgresql://postgres:postgres123@localhost:5432/customer_support
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

#### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 🧪 Testes

```bash
# Backend
cd backend
pytest

# Frontend
cd frontend
npm test
```

## 📈 Métricas e Monitoramento

- Health checks configurados
- Logs estruturados
- Métricas de performance
- Monitoramento de erros

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🆘 Suporte

Para suporte, entre em contato através dos issues do GitHub ou email.

---

**Customer Support v2.0** - Sistema moderno de atendimento ao cliente com foco em performance e escalabilidade.

