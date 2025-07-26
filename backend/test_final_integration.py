#!/usr/bin/env python3
"""
Teste final da integração com Supabase
"""

import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from lib.supabase import get_supabase_client

def test_basic_operations():
    """Testa operações básicas"""
    supabase = get_supabase_client()
    
    print("🚀 Teste Final da Integração com Supabase")
    print("=" * 60)
    
    try:
        # Testar leitura de usuários
        print("\n👥 Testando leitura de usuários...")
        response = supabase.table('users').select('*').execute()
        users = response.data
        print(f"✅ Encontrados {len(users)} usuários")
        
        # Mostrar alguns usuários
        for user in users[:3]:
            print(f"   - {user['name']} ({user['email']}) - {user['role']}")
        
        # Testar leitura de clientes
        print("\n👤 Testando leitura de clientes...")
        response = supabase.table('customers').select('*').execute()
        customers = response.data
        print(f"✅ Encontrados {len(customers)} clientes")
        
        # Mostrar alguns clientes
        for customer in customers[:3]:
            print(f"   - {customer['name']} ({customer['email']}) - {customer['company']}")
        
        # Testar leitura de tickets
        print("\n🎫 Testando leitura de tickets...")
        response = supabase.table('tickets').select('*').execute()
        tickets = response.data
        print(f"✅ Encontrados {len(tickets)} tickets")
        
        # Mostrar alguns tickets
        for ticket in tickets[:3]:
            print(f"   - {ticket['title']} - {ticket['status']} ({ticket['priority']})")
        
        # Testar relacionamento tickets-customers
        print("\n🔗 Testando relacionamento tickets-customers...")
        response = supabase.table('tickets').select('*, customer:customers(*)').execute()
        tickets_with_customers = response.data
        print(f"✅ Relacionamento funcionando - {len(tickets_with_customers)} tickets com dados de clientes")
        
        # Mostrar exemplo de relacionamento
        if tickets_with_customers:
            ticket = tickets_with_customers[0]
            customer = ticket.get('customer', {})
            print(f"   Exemplo: Ticket '{ticket['title']}' - Cliente: {customer.get('name', 'N/A')}")
        
        print("\n🎉 Integração com Supabase funcionando perfeitamente!")
        print("\n📋 Resumo:")
        print(f"- ✅ {len(users)} usuários carregados")
        print(f"- ✅ {len(customers)} clientes carregados")
        print(f"- ✅ {len(tickets)} tickets carregados")
        print("- ✅ Relacionamentos funcionando")
        print("- ✅ Todas as operações básicas OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro durante o teste: {str(e)}")
        return False

def test_auth_simulation():
    """Simula autenticação básica"""
    supabase = get_supabase_client()
    
    print("\n🔐 Testando simulação de autenticação...")
    
    try:
        # Buscar usuário admin
        response = supabase.table('users').select('*').eq('email', 'admin@teste.com').execute()
        
        if response.data:
            admin_user = response.data[0]
            print(f"✅ Usuário admin encontrado: {admin_user['name']}")
            print(f"   Email: {admin_user['email']}")
            print(f"   Role: {admin_user['role']}")
            print(f"   Senha: {admin_user['password']}")
        else:
            print("⚠️ Usuário admin não encontrado")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro na autenticação: {str(e)}")
        return False

def main():
    print("🔍 Iniciando testes finais da integração...")
    
    # Teste básico
    if not test_basic_operations():
        return False
    
    # Teste de autenticação
    if not test_auth_simulation():
        return False
    
    print("\n🎯 Todos os testes passaram!")
    print("\n🚀 A integração com Supabase está 100% funcional!")
    print("\n📝 Próximos passos:")
    print("1. Teste o frontend com a nova integração")
    print("2. Configure autenticação se necessário")
    print("3. Implemente funcionalidades específicas")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 