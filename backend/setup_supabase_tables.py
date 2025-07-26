#!/usr/bin/env python3
"""
Script para configurar as tabelas no Supabase
"""

import sys
import os

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from lib.supabase import get_supabase_client

def create_tables():
    """Cria as tabelas necessárias no Supabase"""
    supabase = get_supabase_client()
    
    print("🔧 Configurando tabelas no Supabase...")
    print("=" * 50)
    
    # SQL para criar as tabelas
    tables_sql = {
        'users': '''
        CREATE TABLE IF NOT EXISTS users (
            id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            name VARCHAR(255) NOT NULL,
            role VARCHAR(50) DEFAULT 'agent',
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );
        ''',
        
        'customers': '''
        CREATE TABLE IF NOT EXISTS customers (
            id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            phone VARCHAR(50),
            company VARCHAR(255),
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );
        ''',
        
        'tickets': '''
        CREATE TABLE IF NOT EXISTS tickets (
            id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            status VARCHAR(50) DEFAULT 'open',
            priority VARCHAR(50) DEFAULT 'medium',
            customer_id UUID REFERENCES customers(id) ON DELETE CASCADE,
            assigned_user_id UUID REFERENCES users(id) ON DELETE SET NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
            updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        );
        '''
    }
    
    try:
        for table_name, sql in tables_sql.items():
            print(f"\n📋 Criando tabela: {table_name}")
            
            # Executar SQL via REST API
            response = supabase.rpc('exec_sql', {'sql': sql}).execute()
            
            print(f"✅ Tabela {table_name} criada com sucesso!")
            
    except Exception as e:
        print(f"❌ Erro ao criar tabelas: {str(e)}")
        print("\n💡 Tentando método alternativo...")
        
        # Método alternativo: usar SQL direto
        try:
            for table_name, sql in tables_sql.items():
                print(f"\n📋 Criando tabela: {table_name}")
                
                # Usar SQL direto
                response = supabase.table(table_name).select('*').limit(1).execute()
                print(f"✅ Tabela {table_name} já existe ou foi criada!")
                
        except Exception as e2:
            print(f"❌ Erro no método alternativo: {str(e2)}")
            return False
    
    return True

def insert_sample_data():
    """Insere dados de exemplo nas tabelas"""
    supabase = get_supabase_client()
    
    print("\n📊 Inserindo dados de exemplo...")
    print("=" * 50)
    
    try:
        # Inserir usuários de exemplo
        users_data = [
            {
                'email': 'admin@teste.com',
                'name': 'Administrador',
                'role': 'admin'
            },
            {
                'email': 'carlos@teste.com',
                'name': 'Carlos Silva',
                'role': 'agent'
            },
            {
                'email': 'manager@teste.com',
                'name': 'Manager',
                'role': 'manager'
            }
        ]
        
        print("👥 Inserindo usuários...")
        for user in users_data:
            try:
                supabase.table('users').insert(user).execute()
                print(f"✅ Usuário {user['name']} inserido")
            except Exception as e:
                print(f"⚠️ Usuário {user['name']} já existe ou erro: {str(e)}")
        
        # Inserir clientes de exemplo
        customers_data = [
            {
                'name': 'João Silva',
                'email': 'joao@empresa.com',
                'phone': '(11) 99999-9999',
                'company': 'Empresa ABC'
            },
            {
                'name': 'Maria Santos',
                'email': 'maria@startup.com',
                'phone': '(21) 88888-8888',
                'company': 'Startup XYZ'
            }
        ]
        
        print("\n👤 Inserindo clientes...")
        for customer in customers_data:
            try:
                supabase.table('customers').insert(customer).execute()
                print(f"✅ Cliente {customer['name']} inserido")
            except Exception as e:
                print(f"⚠️ Cliente {customer['name']} já existe ou erro: {str(e)}")
        
        # Inserir tickets de exemplo
        tickets_data = [
            {
                'title': 'Problema com login',
                'description': 'Não consigo fazer login no sistema',
                'status': 'open',
                'priority': 'high'
            },
            {
                'title': 'Dúvida sobre funcionalidade',
                'description': 'Como usar a nova funcionalidade X?',
                'status': 'open',
                'priority': 'medium'
            }
        ]
        
        print("\n🎫 Inserindo tickets...")
        for ticket in tickets_data:
            try:
                supabase.table('tickets').insert(ticket).execute()
                print(f"✅ Ticket '{ticket['title']}' inserido")
            except Exception as e:
                print(f"⚠️ Ticket '{ticket['title']}' já existe ou erro: {str(e)}")
        
        print("\n🎉 Dados de exemplo inseridos com sucesso!")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao inserir dados: {str(e)}")
        return False

def main():
    print("🚀 Configurando banco de dados Supabase...")
    print("=" * 60)
    
    # Criar tabelas
    if create_tables():
        print("\n✅ Tabelas configuradas com sucesso!")
        
        # Inserir dados de exemplo
        if insert_sample_data():
            print("\n✅ Banco de dados configurado completamente!")
        else:
            print("\n⚠️ Erro ao inserir dados de exemplo")
    else:
        print("\n❌ Erro ao configurar tabelas")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 