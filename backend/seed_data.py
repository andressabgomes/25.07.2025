"""
Script to seed the database with test data
"""

import asyncio
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app.models.user import User, UserRole
from app.models.customer import Customer
from app.models.ticket import Ticket, TicketStatus, TicketPriority
from app.core.security import get_password_hash
import uuid


def create_test_data():
    """Create test data for the application"""
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Check if admin user already exists
        existing_admin = db.query(User).filter(User.email == "admin@teste.com").first()
        if existing_admin:
            print("Test data already exists!")
            return
        
        # Create admin user
        admin_user = User(
            email="admin@teste.com",
            password_hash=get_password_hash("admin123"),
            full_name="Administrador",
            role=UserRole.ADMIN,
            is_active=True
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        print(f"Created admin user: {admin_user.email}")
        
        # Create agent user
        agent_user = User(
            email="agente@teste.com",
            password_hash=get_password_hash("agente123"),
            full_name="Agente de Suporte",
            role=UserRole.AGENT,
            is_active=True
        )
        db.add(agent_user)
        db.commit()
        db.refresh(agent_user)
        print(f"Created agent user: {agent_user.email}")
        
        # Create manager user
        manager_user = User(
            email="gestor@teste.com",
            password_hash=get_password_hash("gestor123"),
            full_name="Gestor de Suporte",
            role=UserRole.MANAGER,
            is_active=True
        )
        db.add(manager_user)
        db.commit()
        db.refresh(manager_user)
        print(f"Created manager user: {manager_user.email}")
        
        # Create test customers
        customers_data = [
            {
                "name": "João Silva",
                "email": "joao.silva@email.com",
                "phone": "(11) 99999-1111",
                "company": "Empresa ABC Ltda"
            },
            {
                "name": "Maria Santos",
                "email": "maria.santos@email.com",
                "phone": "(11) 99999-2222",
                "company": "Tech Solutions"
            },
            {
                "name": "Pedro Costa",
                "email": "pedro.costa@email.com",
                "phone": "(11) 99999-3333",
                "company": "Inovação Digital"
            },
            {
                "name": "Ana Oliveira",
                "email": "ana.oliveira@email.com",
                "phone": "(11) 99999-4444",
                "company": "Consultoria XYZ"
            },
            {
                "name": "Carlos Lima",
                "email": "carlos.lima@email.com",
                "phone": "(11) 99999-5555",
                "company": "StartUp Moderna"
            }
        ]
        
        customers = []
        for customer_data in customers_data:
            customer = Customer(**customer_data)
            db.add(customer)
            customers.append(customer)
        
        db.commit()
        print(f"Created {len(customers)} test customers")
        
        # Create test tickets
        tickets_data = [
            {
                "title": "Problema de login no sistema",
                "description": "Usuário não consegue fazer login no sistema. Aparece mensagem de erro 'credenciais inválidas' mesmo com dados corretos.",
                "priority": TicketPriority.HIGH,
                "status": TicketStatus.OPEN,
                "customer_id": customers[0].id,
                "created_by": admin_user.id,
                "assigned_to": agent_user.id
            },
            {
                "title": "Dúvida sobre funcionalidade",
                "description": "Cliente tem dúvidas sobre como utilizar a funcionalidade de relatórios do sistema.",
                "priority": TicketPriority.MEDIUM,
                "status": TicketStatus.IN_PROGRESS,
                "customer_id": customers[1].id,
                "created_by": agent_user.id,
                "assigned_to": agent_user.id
            },
            {
                "title": "Sistema lento para carregar",
                "description": "Sistema está muito lento para carregar as páginas, especialmente na área de relatórios.",
                "priority": TicketPriority.LOW,
                "status": TicketStatus.OPEN,
                "customer_id": customers[2].id,
                "created_by": admin_user.id
            },
            {
                "title": "Erro ao gerar relatório",
                "description": "Erro 500 ao tentar gerar relatório mensal. O sistema retorna erro interno.",
                "priority": TicketPriority.MEDIUM,
                "status": TicketStatus.RESOLVED,
                "customer_id": customers[3].id,
                "created_by": manager_user.id,
                "assigned_to": agent_user.id
            },
            {
                "title": "Solicitação de nova funcionalidade",
                "description": "Cliente solicita implementação de notificações por email para novos tickets.",
                "priority": TicketPriority.LOW,
                "status": TicketStatus.RESOLVED,
                "customer_id": customers[4].id,
                "created_by": admin_user.id,
                "assigned_to": manager_user.id
            }
        ]
        
        for ticket_data in tickets_data:
            ticket = Ticket(**ticket_data)
            db.add(ticket)
        
        db.commit()
        print(f"Created {len(tickets_data)} test tickets")
        
        print("\n=== Test Data Created Successfully ===")
        print("Login credentials:")
        print("Admin: admin@teste.com / admin123")
        print("Agent: agente@teste.com / agente123")
        print("Manager: gestor@teste.com / gestor123")
        
    except Exception as e:
        print(f"Error creating test data: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    create_test_data()

