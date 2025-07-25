#!/bin/bash

echo "🚀 Iniciando Backend Customer Support..."

cd backend
source venv/bin/activate

echo "📦 Instalando dependências..."
pip install -r requirements.txt

echo "🗄️ Populando banco de dados..."
python seed_data.py

echo "🌐 Iniciando servidor Flask na porta 5000..."
python src/main.py

