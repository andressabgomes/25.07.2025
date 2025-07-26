"""
Serviço de tickets
"""

from typing import List, Dict, Any, Optional
from .supabase_service import supabase_service

class TicketService:
    """Serviço para operações de tickets"""
    
    @staticmethod
    def get_all_tickets() -> List[Dict[str, Any]]:
        """Busca todos os tickets"""
        return supabase_service.get_tickets()
    
    @staticmethod
    def get_ticket_by_id(ticket_id: int) -> Optional[Dict[str, Any]]:
        """Busca um ticket específico"""
        tickets = supabase_service.get_tickets()
        
        for ticket in tickets:
            if ticket.get('id') == ticket_id:
                return ticket
        
        return None
    
    @staticmethod
    def get_ticket_stats() -> Dict[str, Any]:
        """Retorna estatísticas dos tickets"""
        tickets = supabase_service.get_tickets()
        
        total = len(tickets)
        open_tickets = len([t for t in tickets if t.get('status') == 'aberto'])
        closed_tickets = len([t for t in tickets if t.get('status') == 'fechado'])
        
        return {
            "total": total,
            "open": open_tickets,
            "closed": closed_tickets,
            "open_percentage": round((open_tickets / total * 100) if total > 0 else 0, 1)
        }
    
    @staticmethod
    def create_ticket(ticket_data: Dict[str, Any]) -> Dict[str, Any]:
        """Cria um novo ticket"""
        # Em produção, implementar criação no Supabase
        return {
            "success": True,
            "message": "Ticket criado com sucesso",
            "ticket": {
                "id": 999,
                **ticket_data,
                "status": "aberto"
            }
        }
    
    @staticmethod
    def update_ticket(ticket_id: int, ticket_data: Dict[str, Any]) -> Dict[str, Any]:
        """Atualiza um ticket"""
        # Em produção, implementar atualização no Supabase
        return {
            "success": True,
            "message": "Ticket atualizado com sucesso",
            "ticket": {
                "id": ticket_id,
                **ticket_data
            }
        }
    
    @staticmethod
    def delete_ticket(ticket_id: int) -> Dict[str, Any]:
        """Deleta um ticket"""
        # Em produção, implementar deleção no Supabase
        return {
            "success": True,
            "message": "Ticket deletado com sucesso"
        } 