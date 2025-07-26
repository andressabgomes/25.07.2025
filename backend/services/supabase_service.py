"""
Serviço para integração com Supabase
"""

import os
from typing import Optional, Dict, Any, List
from supabase import create_client, Client

class SupabaseService:
    """Serviço para operações com Supabase"""
    
    def __init__(self):
        self.client: Optional[Client] = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Inicializa o cliente Supabase"""
        url = os.environ.get('SUPABASE_URL')
        key = os.environ.get('SUPABASE_ANON_KEY')
        
        if url and key:
            try:
                self.client = create_client(url, key)
                print("✅ Supabase client inicializado com sucesso")
            except Exception as e:
                print(f"❌ Erro ao inicializar Supabase: {e}")
                self.client = None
        else:
            print("⚠️ Supabase não configurado")
            self.client = None
    
    def is_available(self) -> bool:
        """Verifica se o Supabase está disponível"""
        return self.client is not None
    
    def test_connection(self) -> Dict[str, Any]:
        """Testa a conexão com Supabase"""
        if not self.is_available():
            return {"success": False, "error": "Supabase não configurado"}
        
        try:
            # Teste simples de conexão
            response = self.client.table('users').select('count').limit(1).execute()
            return {"success": True, "message": "Conexão OK"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_users(self) -> List[Dict[str, Any]]:
        """Busca todos os usuários"""
        if not self.is_available():
            return []
        
        try:
            response = self.client.table('users').select('*').execute()
            return response.data or []
        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
            return []
    
    def get_customers(self) -> List[Dict[str, Any]]:
        """Busca todos os clientes"""
        if not self.is_available():
            return []
        
        try:
            response = self.client.table('customers').select('*').execute()
            return response.data or []
        except Exception as e:
            print(f"Erro ao buscar clientes: {e}")
            return []
    
    def get_tickets(self) -> List[Dict[str, Any]]:
        """Busca todos os tickets"""
        if not self.is_available():
            return []
        
        try:
            response = self.client.table('tickets').select('*, customer:customers(*)').execute()
            return response.data or []
        except Exception as e:
            print(f"Erro ao buscar tickets: {e}")
            return []
    
    def authenticate_user(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        """Autentica um usuário"""
        if not self.is_available():
            return None
        
        try:
            # Busca usuário por email
            response = self.client.table('users').select('*').eq('email', email).execute()
            
            if response.data:
                user = response.data[0]
                # Verifica senha (em produção, usar hash)
                if user.get('password') == password:
                    return user
            
            return None
        except Exception as e:
            print(f"Erro na autenticação: {e}")
            return None

# Instância global do serviço
supabase_service = SupabaseService() 