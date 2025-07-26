#!/usr/bin/env python3
"""
Script para testar a integração completa com Supabase
"""

import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from lib.supabase import get_supabase_client

def test_tables_exist():
    """Testa se as tabelas existem"""
    supabase = get_supabase_client()
    
    tables = ['users', 'customers', 'tickets']
    
    print("🔍 Verificando existência das tabelas...")
    print("=" * 50)
    
    for table in tables:
        try:
            response = supabase.table(table).select('*').limit(1).execute()
            print(f"✅ Tabela '{table}' existe")
        except Exception as e:
            print(f"❌ Tabela '{table}' não existe: {str(e)}")
            return False
    
    return True

def test_data_operations():
    """Testa operações básicas de dados"""
    supabase = get_supabase_client()
    
    print("\n📊 Testando operações de dados...")
    print("=" * 50)
    
    try:
        # Testar leitura de usuários
        print("\n👥 Testando leitura de usuários...")
        response = supabase.table('users').select('*').execute()
        print(f"✅ Encontrados {len(response.data)} usuários")
        
        # Testar leitura de clientes
        print("\n👤 Testando leitura de clientes...")
        response = supabase.table('customers').select('*').execute()
        print(f"✅ Encontrados {len(response.data)} clientes")
        
        # Testar leitura de tickets
        print("\n🎫 Testando leitura de tickets...")
        response = supabase.table('tickets').select('*').execute()
        print(f"✅ Encontrados {len(response.data)} tickets")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro nas operações de dados: {str(e)}")
        return False

def test_relationships():
    """Testa relacionamentos entre tabelas"""
    supabase = get_supabase_client()
    
    print("\n🔗 Testando relacionamentos...")
    print("=" * 50)
    
    try:
        # Testar join entre tickets e customers
        print("\n🎫 Testando relacionamento tickets-customers...")
        response = supabase.table('tickets').select('*, customer:customers(*)').execute()
        print(f"✅ Relacionamento tickets-customers funcionando")
        
        # Testar join entre tickets e users
        print("\n👥 Testando relacionamento tickets-users...")
        response = supabase.table('tickets').select('*, assigned_user:users(*)').execute()
        print(f"✅ Relacionamento tickets-users funcionando")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro nos relacionamentos: {str(e)}")
        return False

def main():
    print("🚀 Testando integração completa com Supabase...")
    print("=" * 60)
    
    # Testar existência das tabelas
    if not test_tables_exist():
        print("\n❌ Tabelas não encontradas. Execute o guia de configuração primeiro.")
        return False
    
    # Testar operações de dados
    if not test_data_operations():
        print("\n❌ Erro nas operações de dados.")
        return False
    
    # Testar relacionamentos
    if not test_relationships():
        print("\n❌ Erro nos relacionamentos.")
        return False
    
    print("\n🎉 Integração com Supabase funcionando perfeitamente!")
    print("\n📋 Resumo:")
    print("- ✅ Conexão estabelecida")
    print("- ✅ Tabelas criadas")
    print("- ✅ Operações de dados funcionando")
    print("- ✅ Relacionamentos configurados")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 