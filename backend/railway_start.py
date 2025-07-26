#!/usr/bin/env python3
"""
Script de inicialização para Railway
"""

import os
import sys
import subprocess

def main():
    print("🚀 Iniciando Customer Support API no Railway...")
    
    # Verificar se estamos no diretório correto
    current_dir = os.getcwd()
    print(f"📁 Diretório atual: {current_dir}")
    
    # Verificar se o arquivo main_railway.py existe
    main_file = os.path.join(current_dir, 'src', 'main_railway.py')
    if not os.path.exists(main_file):
        print(f"❌ Arquivo não encontrado: {main_file}")
        return 1
    
    print(f"✅ Arquivo encontrado: {main_file}")
    
    # Verificar variáveis de ambiente
    print("\n🔧 Verificando variáveis de ambiente:")
    print(f"   PORT: {os.environ.get('PORT', '5000')}")
    print(f"   SUPABASE_URL: {os.environ.get('SUPABASE_URL', 'Não definida')}")
    print(f"   SUPABASE_ANON_KEY: {'Definida' if os.environ.get('SUPABASE_ANON_KEY') else 'Não definida'}")
    
    # Iniciar a aplicação
    print("\n🚀 Iniciando aplicação Flask...")
    try:
        # Executar o arquivo main_railway.py
        os.execv(sys.executable, [sys.executable, main_file])
    except Exception as e:
        print(f"❌ Erro ao iniciar aplicação: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 