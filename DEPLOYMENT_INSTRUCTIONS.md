# 🚀 Instruções de Deploy - Customer Support Cajá

## 📋 Pré-requisitos
- Conta no GitHub (já configurada)
- Conta no Railway.app
- Conta no Vercel.com

## 🔧 Deploy do Backend (Railway)

### 1. Acesse Railway.app
- Vá para https://railway.app
- Faça login com sua conta GitHub

### 2. Crie um Novo Projeto
- Clique em "New Project"
- Selecione "Deploy from GitHub repo"
- Escolha o repositório: `andressabgomes/25.07.2025`

### 3. Configuração Automática
- Railway detectará automaticamente o projeto Flask
- O deploy será iniciado usando as configurações do `railway.json`
- Aguarde o deploy ser concluído (cerca de 2-5 minutos)

### 4. Obtenha a URL do Backend
- Após o deploy, Railway fornecerá uma URL como:
  `https://seu-projeto-production.up.railway.app`
- **IMPORTANTE**: Anote esta URL, você precisará dela para o frontend

### 5. Teste o Backend
- Acesse: `https://sua-url-railway.app/api/health`
- Deve retornar: `{"status": "healthy", "service": "Customer Support API"}`

## ⚛️ Deploy do Frontend (Vercel)

### 1. Acesse Vercel.com
- Vá para https://vercel.com
- Faça login com sua conta GitHub

### 2. Importe o Projeto
- Clique em "New Project"
- Selecione o repositório: `andressabgomes/25.07.2025`
- Clique em "Import"

### 3. Configure as Variáveis de Ambiente
**IMPORTANTE**: Antes de fazer o deploy, configure:
- `VITE_API_URL`: Cole a URL do Railway (ex: `https://sua-url-railway.app/api`)

### 4. Configurações de Build
- Framework Preset: `Vite`
- Build Command: `cd frontend && pnpm install && pnpm run build`
- Output Directory: `frontend/dist`
- Install Command: `pnpm install`

### 5. Deploy
- Clique em "Deploy"
- Aguarde o build ser concluído (cerca de 2-5 minutos)

## 🔄 Atualizando a URL do Backend

Após obter a URL do Railway, você precisa atualizar o frontend:

### Opção 1: Via Vercel Dashboard
1. Vá para o projeto no Vercel
2. Clique em "Settings" > "Environment Variables"
3. Adicione: `VITE_API_URL` = `https://sua-url-railway.app/api`
4. Clique em "Redeploy" para aplicar as mudanças

### Opção 2: Via Código (Recomendado)
1. Edite o arquivo `frontend/.env.production`
2. Substitua `https://your-railway-backend-url.railway.app/api` pela URL real
3. Faça commit e push:
```bash
git add .
git commit -m "Update production API URL"
git push origin main
```
4. Vercel fará o redeploy automaticamente

## 🧪 Testando a Aplicação

### 1. Teste o Backend
- URL: `https://sua-url-railway.app/api/health`
- Deve retornar status "healthy"

### 2. Teste o Frontend
- URL: `https://seu-projeto.vercel.app`
- Faça login com: `admin@teste.com` / `admin123`
- Verifique se o dashboard carrega corretamente

### 3. Teste a Integração
- Verifique se o login funciona
- Confirme se os dados são carregados do backend
- Teste criação de tickets e clientes

## 🔧 Solução de Problemas

### CORS Errors
Se houver erros de CORS:
1. Verifique se o backend está configurado com `CORS(app, origins="*")`
2. Confirme se a URL da API está correta no frontend

### Build Errors no Vercel
1. Verifique se todas as dependências estão no `package.json`
2. Confirme se o comando de build está correto
3. Verifique os logs de build no Vercel

### Database Issues no Railway
1. Railway usa SQLite por padrão (adequado para demonstração)
2. Para produção real, considere PostgreSQL
3. Os dados de teste são criados automaticamente

## 📊 URLs Finais

Após o deploy completo, você terá:

- **Frontend**: `https://seu-projeto.vercel.app`
- **Backend API**: `https://seu-projeto.railway.app`
- **Health Check**: `https://seu-projeto.railway.app/api/health`

## 🔐 Contas de Demonstração

- **Admin**: admin@teste.com / admin123
- **Agente**: carlos@teste.com / 123456
- **Manager**: manager@teste.com / 123456

## 🎯 Próximos Passos

1. **Domínio Personalizado**: Configure um domínio próprio no Vercel
2. **Monitoramento**: Configure alertas para uptime
3. **Analytics**: Adicione Google Analytics ou similar
4. **Backup**: Configure backup automático do banco de dados

---

**Suporte**: Para dúvidas, consulte a documentação das plataformas ou abra uma issue no repositório.

