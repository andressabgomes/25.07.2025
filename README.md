# Customer Support Cajá - v2.0

Sistema de Customer Support com arquitetura limpa e design tropical da marca Cajá.

## 🚀 Nova Arquitetura

### ✅ **Melhorias Implementadas:**

- **Arquitetura Limpa**: Separação clara de responsabilidades
- **Camada de Serviços**: Lógica de negócio isolada
- **Configuração Centralizada**: Gerenciamento de ambiente
- **Factory Pattern**: Criação de aplicação flexível
- **Tratamento de Erros**: Respostas padronizadas
- **Documentação**: Código bem documentado

### 📁 **Estrutura do Projeto:**

```
├── backend/
│   ├── app.py              # Aplicação principal
│   ├── config/             # Configurações
│   │   └── __init__.py
│   ├── services/           # Camada de serviços
│   │   ├── __init__.py
│   │   ├── supabase_service.py
│   │   ├── auth_service.py
│   │   ├── ticket_service.py
│   │   ├── customer_service.py
│   │   └── user_service.py
│   ├── models/             # Modelos de dados
│   ├── routes/             # Rotas (legado)
│   └── requirements.txt
├── frontend/               # Aplicação React
├── nixpacks.toml          # Configuração Railway
├── vercel.json            # Configuração Vercel
└── env.example            # Variáveis de ambiente
```

## 🛠️ **Tecnologias:**

### Backend:
- **Flask**: Framework web
- **Supabase**: Banco de dados
- **Python 3.9**: Linguagem
- **Arquitetura Limpa**: Padrões de design

### Frontend:
- **React**: Framework UI
- **Vite**: Build tool
- **Tailwind CSS**: Estilização
- **Shadcn/ui**: Componentes

## 🚀 **Deploy:**

### Railway (Backend):
```bash
# Variáveis de ambiente necessárias:
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SECRET_KEY=your-secret-key
FLASK_ENV=production
```

### Vercel (Frontend):
- Deploy automático via GitHub
- Proxy configurado para Railway

## 📋 **Endpoints:**

### Health Check:
```
GET /api/health
```

### Autenticação:
```
POST /api/auth/login
POST /api/auth/verify
```

### Dados:
```
GET /api/users
GET /api/customers
GET /api/tickets
GET /api/tickets/stats
```

## 🔧 **Desenvolvimento Local:**

### Backend:
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend:
```bash
cd frontend
npm install
npm run dev
```

## 🎯 **Próximos Passos:**

1. ✅ **Implementar JWT** para autenticação
2. ✅ **Adicionar validação** de dados
3. ✅ **Implementar cache** Redis
4. ✅ **Adicionar logs** estruturados
5. ✅ **Criar testes** automatizados

## 📞 **Suporte:**

Para dúvidas ou problemas, abra uma issue no GitHub.

---

**Desenvolvido com ❤️ pela equipe Cajá**

