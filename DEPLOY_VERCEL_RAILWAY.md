# 🚀 Deploy com Vercel + Railway Integrados

## 📋 Configuração Automática

Com a integração Vercel + Railway, o processo é muito mais simples!

## 🔧 Deploy no Railway (Backend)

### 1. Deploy Automático

1. **Acesse**: https://railway.app
2. **Clique em**: "New Project"
3. **Selecione**: "Deploy from GitHub repo"
4. **Escolha**: `andressabges/25.07.2025`
5. **Clique em**: "Deploy Now"

### 2. Configurar Variáveis de Ambiente

No Railway, vá para **Variables** e adicione:

```env
SUPABASE_URL=https://wevzbdepfqsryagiemcz.supabase.co
SUPABASE_ANON_KEY=sb_publishable_-1Jg5reJGbOE4-wojnO8Xw_wEa1tBXv
SECRET_KEY=sua-chave-secreta-super-forte
PORT=5000
```

### 3. Obter URL do Railway

Após o deploy, copie a URL gerada (ex: `https://customer-support-backend.railway.app`)

## 🌐 Deploy no Vercel (Frontend)

### 1. Deploy Automático

1. **Acesse**: https://vercel.com
2. **Clique em**: "New Project"
3. **Importe**: `andressabges/25.07.2025`
4. **Configure**:
   - Framework Preset: `Vite`
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`

### 2. Configurar Integração com Railway

No Vercel, após o deploy:

1. **Vá para**: Settings > Integrations
2. **Procure por**: Railway
3. **Conecte** sua conta Railway
4. **Selecione** o projeto Railway criado

### 3. Configurar Rewrites (Automático)

O Vercel automaticamente configurará os rewrites para o Railway:

```json
{
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "https://seu-projeto.railway.app/api/$1"
    }
  ]
}
```

## 🔗 Benefícios da Integração

### ✅ Automático:
- **Proxy de API**: `/api/*` → Railway automaticamente
- **Deploy sincronizado**: Mudanças no Railway atualizam o Vercel
- **Variáveis compartilhadas**: Configuração centralizada
- **Logs unificados**: Monitoramento em um só lugar

### ✅ URLs Simplificadas:
- **Frontend**: `https://seu-projeto.vercel.app`
- **API**: `https://seu-projeto.vercel.app/api/*` (proxy para Railway)
- **Backend direto**: `https://seu-projeto.railway.app`

## 🧪 Testes Pós-Deploy

### 1. Testar Integração

```bash
# Testar proxy do Vercel
curl https://seu-projeto.vercel.app/api/health

# Testar Railway diretamente
curl https://seu-projeto.railway.app/api/health
```

### 2. Testar Frontend

1. Acesse: `https://seu-projeto.vercel.app`
2. Teste login: `admin@teste.com` / `admin123`
3. Verifique se os dados carregam

## 🔧 Configuração Avançada

### Variáveis de Ambiente no Vercel

Se precisar de variáveis específicas:

```env
VITE_APP_NAME=Customer Support Cajá
VITE_APP_VERSION=1.0.0
```

### Domínio Personalizado

1. **No Vercel**: Settings > Domains
2. **Adicione** seu domínio
3. **Configure** DNS conforme instruções

## 📊 Monitoramento

### Vercel Analytics
- **Performance**: Métricas de carregamento
- **Erros**: Tracking automático
- **Uptime**: Monitoramento 24/7

### Railway Logs
- **Backend logs**: Em tempo real
- **Database**: Conexões e queries
- **Performance**: Métricas de API

## 🚀 Comandos Úteis

```bash
# Verificar status
vercel ls
railway status

# Ver logs
vercel logs
railway logs

# Redeploy
vercel --prod
railway up
```

## 🎯 Checklist Final

- [ ] Railway: Backend deployado
- [ ] Vercel: Frontend deployado
- [ ] Integração: Vercel + Railway conectados
- [ ] Proxy: `/api/*` funcionando
- [ ] Variáveis: Configuradas no Railway
- [ ] Testes: Health check OK
- [ ] Frontend: Login funcionando
- [ ] Supabase: Dados carregando

## 🔧 Solução de Problemas

### Proxy não funciona
```bash
# Verificar se a integração está ativa
# Verificar se o Railway está rodando
# Verificar logs no Vercel
```

### CORS Errors
```python
# Backend já está configurado com:
CORS(app, origins="*")
```

### Build falha
```bash
# Verificar se todas as dependências estão no package.json
# Verificar se o build command está correto
# Verificar logs de build
```

---

**🎉 Com a integração Vercel + Railway, o deploy é muito mais simples e robusto!** 