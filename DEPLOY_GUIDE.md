# Guia de Deploy - Customer Support Cajá

Este guia fornece instruções detalhadas para fazer o deploy do sistema Customer Support em diferentes ambientes.

## 🚀 Deploy Local (Desenvolvimento)

### Requisitos
- Python 3.11+
- Node.js 20+
- pnpm
- Git

### Passos
1. **Clone o projeto**
```bash
git clone <repository-url>
cd Customer_Support
```

2. **Inicie o backend**
```bash
./start_backend.sh
```

3. **Inicie o frontend** (em outro terminal)
```bash
./start_frontend.sh
```

4. **Acesse a aplicação**
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000

## 🌐 Deploy em Produção

### Opção 1: Servidor VPS/Dedicado

#### Backend (Flask + Gunicorn)
```bash
# 1. Instalar dependências do sistema
sudo apt update
sudo apt install python3-pip python3-venv nginx

# 2. Configurar aplicação
cd /var/www/customer-support
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt gunicorn

# 3. Configurar Gunicorn
gunicorn --bind 0.0.0.0:5000 src.main:app

# 4. Configurar Nginx
sudo nano /etc/nginx/sites-available/customer-support
```

**Configuração Nginx:**
```nginx
server {
    listen 80;
    server_name seu-dominio.com;

    location /api {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        root /var/www/customer-support/frontend/dist;
        try_files $uri $uri/ /index.html;
    }
}
```

#### Frontend (Build Estático)
```bash
# 1. Build da aplicação
cd frontend
pnpm install
pnpm run build

# 2. Copiar arquivos para Nginx
sudo cp -r dist/* /var/www/customer-support/frontend/dist/
```

### Opção 2: Docker

#### Dockerfile Backend
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend/ .
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.main:app"]
```

#### Dockerfile Frontend
```dockerfile
FROM node:20-alpine as build

WORKDIR /app
COPY frontend/package*.json ./
RUN npm install

COPY frontend/ .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
```

#### Docker Compose
```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    
  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
```

### Opção 3: Serviços Cloud

#### Vercel (Frontend)
```bash
# 1. Instalar Vercel CLI
npm i -g vercel

# 2. Deploy
cd frontend
vercel --prod
```

#### Heroku (Backend)
```bash
# 1. Criar Procfile
echo "web: gunicorn src.main:app" > Procfile

# 2. Deploy
heroku create customer-support-api
git push heroku main
```

#### Railway (Fullstack)
```bash
# 1. Conectar repositório
railway login
railway link

# 2. Deploy automático via Git
git push origin main
```

## 🔧 Configurações de Produção

### Variáveis de Ambiente

#### Backend (.env)
```env
FLASK_ENV=production
SECRET_KEY=sua-chave-secreta-super-forte
DATABASE_URL=postgresql://user:pass@host:port/db
CORS_ORIGINS=https://seu-dominio.com
```

#### Frontend (.env.production)
```env
VITE_API_URL=https://api.seu-dominio.com
VITE_APP_NAME=Customer Support Cajá
```

### Banco de Dados

#### PostgreSQL (Produção)
```bash
# 1. Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib

# 2. Criar banco
sudo -u postgres createdb customer_support

# 3. Atualizar connection string
DATABASE_URL=postgresql://user:password@localhost/customer_support
```

#### Migração de Dados
```python
# Script de migração
from src.main import app
from src.models.user import db

with app.app_context():
    db.create_all()
    # Executar seed_data.py se necessário
```

## 🔒 Segurança

### SSL/HTTPS
```bash
# Certbot para SSL gratuito
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d seu-dominio.com
```

### Firewall
```bash
# UFW básico
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

### Backup
```bash
# Script de backup automático
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump customer_support > backup_$DATE.sql
aws s3 cp backup_$DATE.sql s3://seu-bucket/backups/
```

## 📊 Monitoramento

### Logs
```bash
# Logs do Gunicorn
gunicorn --access-logfile access.log --error-logfile error.log

# Logs do Nginx
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

### Métricas
- **Uptime**: Usar serviços como UptimeRobot
- **Performance**: New Relic, DataDog
- **Erros**: Sentry para tracking de erros

## 🚨 Troubleshooting

### Problemas Comuns

#### CORS Errors
```python
# Verificar configuração CORS no backend
CORS(app, origins=["https://seu-dominio.com"])
```

#### Database Connection
```bash
# Verificar conexão PostgreSQL
psql -h localhost -U user -d customer_support
```

#### Build Errors
```bash
# Limpar cache e reinstalar
rm -rf node_modules package-lock.json
npm install
```

### Comandos Úteis
```bash
# Verificar processos
ps aux | grep gunicorn
ps aux | grep nginx

# Reiniciar serviços
sudo systemctl restart nginx
sudo systemctl restart gunicorn

# Verificar logs
journalctl -u nginx
journalctl -u gunicorn
```

## 📈 Otimizações

### Performance
- **Gzip**: Habilitar compressão no Nginx
- **CDN**: CloudFlare para assets estáticos
- **Caching**: Redis para cache de sessões
- **Database**: Índices e query optimization

### Escalabilidade
- **Load Balancer**: Nginx ou HAProxy
- **Multiple Workers**: Gunicorn com múltiplos workers
- **Database Replica**: Read replicas para PostgreSQL

---

**Suporte**: Para dúvidas sobre deploy, consulte a documentação ou abra uma issue no repositório.

