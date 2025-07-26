# 🚀 Guia de Configuração do Supabase

## 📋 Passos para Configurar o Banco de Dados

### 1. Acesse o Painel do Supabase
- Vá para: https://supabase.com/dashboard
- Faça login na sua conta
- Selecione o projeto: `fkhjspuygbheanjxqnin`

### 2. Configure as Tabelas

#### Tabela: `users`
```sql
CREATE TABLE users (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'agent',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Tabela: `customers`
```sql
CREATE TABLE customers (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    company VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

#### Tabela: `tickets`
```sql
CREATE TABLE tickets (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'open',
    priority VARCHAR(50) DEFAULT 'medium',
    customer_id UUID REFERENCES customers(id) ON DELETE CASCADE,
    assigned_user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
```

### 3. Como Criar as Tabelas

1. **No painel do Supabase:**
   - Vá para **SQL Editor**
   - Clique em **New Query**
   - Cole o SQL de cada tabela
   - Clique em **Run**

2. **Ou via Table Editor:**
   - Vá para **Table Editor**
   - Clique em **New Table**
   - Configure cada coluna manualmente

### 4. Configurar RLS (Row Level Security)

Para cada tabela, execute:

```sql
-- Habilitar RLS
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE customers ENABLE ROW LEVEL SECURITY;
ALTER TABLE tickets ENABLE ROW LEVEL SECURITY;

-- Políticas básicas (permitir tudo para teste)
CREATE POLICY "Allow all" ON users FOR ALL USING (true);
CREATE POLICY "Allow all" ON customers FOR ALL USING (true);
CREATE POLICY "Allow all" ON tickets FOR ALL USING (true);
```

### 5. Inserir Dados de Exemplo

Após criar as tabelas, execute:

```sql
-- Inserir usuários (com senhas)
INSERT INTO users (email, name, role, password) VALUES
('admin@teste.com', 'Administrador', 'admin', 'admin123'),
('carlos@teste.com', 'Carlos Silva', 'agent', '123456'),
('manager@teste.com', 'Manager', 'manager', '123456');

-- Inserir clientes
INSERT INTO customers (name, email, phone, company) VALUES
('João Silva', 'joao@empresa.com', '(11) 99999-9999', 'Empresa ABC'),
('Maria Santos', 'maria@startup.com', '(21) 88888-8888', 'Startup XYZ');

-- Inserir tickets
INSERT INTO tickets (title, description, status, priority) VALUES
('Problema com login', 'Não consigo fazer login no sistema', 'open', 'high'),
('Dúvida sobre funcionalidade', 'Como usar a nova funcionalidade X?', 'open', 'medium');
```

### 6. Testar a Integração

Após configurar as tabelas, execute:

```bash
cd backend
python3 test_supabase.py
```

## 🔑 Credenciais Configuradas

- **URL**: `https://fkhjspuygbheanjxqnin.supabase.co`
- **Anon Key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZraGpzcHV5Z2JoZWFuanhxbmluIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTMyOTc3OTMsImV4cCI6MjA2ODg3Mzc5M30.B709GO5wds-lOb1fEwib38eTGCdgSOsTt771ipMkXC0`
- **Publishable Key**: `sb_publishable_n8J2U_j-YBC4m6BiZaVFjQ_Aix2xr4d`

## ✅ Status da Integração

- ✅ **Conexão**: Funcionando
- ⏳ **Tabelas**: Aguardando criação manual
- ⏳ **Dados**: Aguardando inserção
- ⏳ **Testes**: Aguardando configuração completa

## 🎯 Próximos Passos

1. Criar as tabelas no painel do Supabase
2. Inserir dados de exemplo
3. Testar a integração completa
4. Configurar autenticação se necessário

---

**Nota**: As tabelas precisam ser criadas manualmente no painel do Supabase, pois o usuário anônimo não tem permissão para criar tabelas via API. 