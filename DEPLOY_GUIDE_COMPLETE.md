# 🚀 Guia Completo de Deploy - Railway + Vercel + Supabase

## 📋 Pré-requisitos

- ✅ Conta no Railway: https://railway.app
- ✅ Conta no Vercel: https://vercel.com
- ✅ Projeto Supabase configurado
- ✅ Código funcionando localmente

## 🔧 Deploy no Railway (Backend)

### 1. Preparar o Repositório

```bash
# Verificar se todos os arquivos estão commitados
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

### 2. Deploy no Railway

1. **Acesse**: https://railway.app
2. **Clique em**: "New Project"
3. **Selecione**: "Deploy from GitHub repo"
4. **Escolha o repositório**: `andressabgomes/25.07.2025`
5. **Clique em**: "Deploy Now"

### 3. Configurar Variáveis de Ambiente

No Railway, vá para **Variables** e adicione:

```env
SUPABASE_URL=https://wevzbdepfqsryagiemcz.supabase.co
SUPABASE_ANON_KEY=sb_publishable_-1Jg5reJGbOE4-wojnO8Xw_wEa1tBXv
SECRET_KEY=sua-chave-secreta-super-forte
PORT=5000
```

### 4. Obter URL do Railway

Após o deploy, copie a URL gerada (ex: `https://customer-support-backend.railway.app`)

## 🌐 Deploy no Vercel (Frontend)

### 1. Preparar Frontend

1. **Acesse**: https://vercel.com
2. **Clique em**: "New Project"
3. **Importe o repositório**: `andressabgomes/25.07.2025`
4. **Configure o projeto**:
   - Framework Preset: `Vite`
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`

### 2. Configurar Variáveis de Ambiente

No Vercel, vá para **Settings > Environment Variables** e adicione:

```env
VITE_API_URL=https://sua-url-railway.railway.app/api
VITE_APP_NAME=Customer Support Cajá
```

### 3. Deploy

Clique em **Deploy** e aguarde o build ser concluído.

## 🔗 Conectar Frontend e Backend

### 1. Atualizar URL da API

Após obter a URL do Railway, atualize no Vercel:

1. Vá para **Settings > Environment Variables**
2. Atualize `VITE_API_URL` com a URL real do Railway
3. Clique em **Redeploy**

### 2. Testar Integração

```bash
# Testar backend
curl https://sua-url-railway.railway.app/api/health

# Deve retornar:
{
  "status": "healthy",
  "service": "Customer Support API",
  "database": "Supabase",
  "connection": "OK"
}
```

## 🧪 Testes Pós-Deploy

### 1. Testar Backend

```bash
# Health check
curl https://sua-url-railway.railway.app/api/health

# Usuários
curl https://sua-url-railway.railway.app/api/users

# Clientes
curl https://sua-url-railway.railway.app/api/customers

# Tickets
curl https://sua-url-railway.railway.app/api/tickets
```

### 2. Testar Frontend

1. Acesse a URL do Vercel
2. Teste o login com: `admin@teste.com` / `admin123`
3. Verifique se os dados carregam do Supabase

## 🔧 Solução de Problemas

### Railway Issues

**Build falha:**
```bash
# Verificar logs no Railway
# Verificar se requirements.txt está correto
# Verificar se main_railway.py existe
```

**CORS Errors:**
```python
# Verificar se CORS está configurado
CORS(app, origins="*")
```

### Vercel Issues

**Build falha:**
```bash
# Verificar se package.json está correto
# Verificar se todas as dependências estão instaladas
# Verificar se VITE_API_URL está configurada
```

**API não conecta:**
```bash
# Verificar se a URL do Railway está correta
# Verificar se o backend está rodando
# Verificar logs no Railway
```

## 📊 URLs Finais

Após o deploy completo:

- **Frontend**: `https://seu-projeto.vercel.app`
- **Backend**: `https://seu-projeto.railway.app`
- **Supabase**: `https://wevzbdepfqsryagiemcz.supabase.co`

## 🎯 Checklist Final

- [ ] Backend deployado no Railway
- [ ] Frontend deployado no Vercel
- [ ] Variáveis de ambiente configuradas
- [ ] URLs conectadas corretamente
- [ ] Health check funcionando
- [ ] Login funcionando
- [ ] Dados carregando do Supabase

## 🚀 Comandos Úteis

```bash
# Verificar status do deploy
railway status
vercel ls

# Ver logs
railway logs
vercel logs

# Redeploy
railway up
vercel --prod
```

---

**Suporte**: Para dúvidas, consulte a documentação das plataformas ou abra uma issue no repositório. 