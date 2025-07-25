#!/bin/bash

echo "🚀 Iniciando Frontend Customer Support..."

cd frontend

echo "📦 Instalando dependências..."
pnpm install

echo "🌐 Iniciando servidor de desenvolvimento na porta 5173..."
pnpm run dev --host

