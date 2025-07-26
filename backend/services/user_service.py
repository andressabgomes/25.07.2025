"""
Serviço de usuários
"""

from typing import List, Dict, Any, Optional
from .supabase_service import supabase_service

class UserService:
    """Serviço para operações de usuários"""
    
    @staticmethod
    def get_all_users() -> List[Dict[str, Any]]:
        """Busca todos os usuários"""
        return supabase_service.get_users()
    
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
        """Busca um usuário específico"""
        users = supabase_service.get_users()
        
        for user in users:
            if user.get('id') == user_id:
                return user
        
        return None
    
    @staticmethod
    def create_user(user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria um novo usuário"""
        # Em produção, implementar criação no Supabase
        return {
            "success": True,
            "message": "Usuário criado com sucesso",
            "user": {
                "id": 999,
                **user_data
            }
        }
    
    @staticmethod
    def update_user(user_id: int, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Atualiza um usuário"""
        # Em produção, implementar atualização no Supabase
        return {
            "success": True,
            "message": "Usuário atualizado com sucesso",
            "user": {
                "id": user_id,
                **user_data
            }
        }
    
    @staticmethod
    def delete_user(user_id: int) -> Dict[str, Any]:
        """Deleta um usuário"""
        # Em produção, implementar deleção no Supabase
        return {
            "success": True,
            "message": "Usuário deletado com sucesso"
        } 