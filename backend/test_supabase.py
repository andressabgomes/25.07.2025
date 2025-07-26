#!/usr/bin/env python3
"""
Script para testar a integração com o Supabase
"""

import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from lib.supabase import test_connection, get_supabase_client

def main():
    print("🔍 Testando integração com Supabase...")
    print("=" * 50)
    
    # Testar conexão
    success, message = test_connection()
    
    if success:
        print("✅ " + message)
        print("\n📊 Testando operações básicas...")
        
        # Obter cliente
        supabase = get_supabase_client()
        
        try:
            # Testar consulta de usuários
            print("\n👥 Testando consulta de usuários...")
            response = supabase.table('users').select('*').limit(5).execute()
            print(f"✅ Encontrados {len(response.data)} usuários")
            
            # Testar consulta de tickets
            print("\n🎫 Testando consulta de tickets...")
            response = supabase.table('tickets').select('*').limit(5).execute()
            print(f"✅ Encontrados {len(response.data)} tickets")
            
            # Testar consulta de clientes
            print("\n👤 Testando consulta de clientes...")
            response = supabase.table('customers').select('*').limit(5).execute()
            print(f"✅ Encontrados {len(response.data)} clientes")
            
            print("\n🎉 Todos os testes passaram! Supabase está funcionando corretamente.")
            
        except Exception as e:
            print(f"❌ Erro durante os testes: {str(e)}")
            return False
            
    else:
        print("❌ " + message)
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 