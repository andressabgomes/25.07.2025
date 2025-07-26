"""
Serviço de autenticação
"""

from typing import Optional, Dict, Any
from .supabase_service import supabase_service

class AuthService:
    """Serviço para operações de autenticação"""
    
    @staticmethod
    def login(email: str, password: str) -> Dict[str, Any]:
        """Realiza login do usuário"""
        try:
            user = supabase_service.authenticate_user(email, password)
            
            if user:
                return {
                    "success": True,
                    "user": {
                        "id": user.get('id'),
                        "name": user.get('name'),
                        "email": user.get('email'),
                        "role": user.get('role', 'user')
                    },
                    "token": f"mock-token-{user.get('id')}"  # Em produção, usar JWT
                }
            else:
                return {
                    "success": False,
                    "error": "Credenciais inválidas"
                }
        except Exception as e:
            return {
                "success": False,
                "error": f"Erro no login: {str(e)}"
            }
    
    @staticmethod
    def verify_token(token: str) -> Dict[str, Any]:
        """Verifica se um token é válido"""
        # Em produção, implementar verificação JWT
        if token and token.startswith('mock-token-'):
            return {"success": True, "valid": True}
        
        return {"success": True, "valid": False}
    
    @staticmethod
    def get_user_by_token(token: str) -> Optional[Dict[str, Any]]:
        """Busca usuário pelo token"""
        # Em produção, decodificar JWT
        if token and token.startswith('mock-token-'):
            user_id = token.replace('mock-token-', '')
            users = supabase_service.get_users()
            
            for user in users:
                if str(user.get('id')) == user_id:
                    return {
                        "id": user.get('id'),
                        "name": user.get('name'),
                        "email": user.get('email'),
                        "role": user.get('role', 'user')
                    }
        
        return None 