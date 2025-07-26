#!/usr/bin/env python3
"""
Script de inicialização simples para Railway
"""

import os
import sys

def main():
    print("🚀 Iniciando Customer Support API...")
    
    # Verificar diretório atual
    print(f"📁 Diretório atual: {os.getcwd()}")
    print(f"📁 Conteúdo: {os.listdir('.')}")
    
    # Verificar se backend existe
    if os.path.exists('backend'):
        print("✅ Diretório backend encontrado")
        print(f"📁 Conteúdo backend: {os.listdir('backend')}")
    else:
        print("❌ Diretório backend não encontrado")
        return 1
    
    # Verificar se app.py existe
    app_file = os.path.join('backend', 'app.py')
    if os.path.exists(app_file):
        print(f"✅ Arquivo encontrado: {app_file}")
    else:
        print(f"❌ Arquivo não encontrado: {app_file}")
        return 1
    
    # Verificar variáveis de ambiente
    print("\n🔧 Variáveis de ambiente:")
    print(f"   PORT: {os.environ.get('PORT', '5000')}")
    print(f"   SUPABASE_URL: {os.environ.get('SUPABASE_URL', 'Não definida')}")
    print(f"   SUPABASE_ANON_KEY: {'Definida' if os.environ.get('SUPABASE_ANON_KEY') else 'Não definida'}")
    
    # Importar e executar app
    print("\n🚀 Importando aplicação...")
    try:
        sys.path.insert(0, os.path.join(os.getcwd(), 'backend'))
        from app import app
        
        port = int(os.environ.get('PORT', 5000))
        print(f"🌐 Iniciando servidor na porta {port}")
        
        app.run(host='0.0.0.0', port=port, debug=False)
        
    except Exception as e:
        print(f"❌ Erro ao iniciar aplicação: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main()) 