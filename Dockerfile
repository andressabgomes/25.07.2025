FROM python:3.11-slim

WORKDIR /app

# Copiar requirements primeiro para cache de layers
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação
COPY . .

# Criar diretório para banco de dados
RUN mkdir -p backend/src/database

# Expor porta
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python3", "app.py"]

