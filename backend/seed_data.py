#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from src.main import app
from src.models.user import User, db
from src.models.customer import Customer
from src.models.ticket import Ticket
from datetime import datetime, timedelta
import random

def seed_database():
    with app.app_context():
        # Limpar dados existentes
        db.drop_all()
        db.create_all()
        
        print("Criando usuários...")
        
        # Criar usuário admin
        admin = User(
            username='admin',
            email='admin@teste.com',
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        
        # Criar agentes
        agent1 = User(
            username='carlos.silva',
            email='carlos@teste.com',
            role='agent'
        )
        agent1.set_password('123456')
        db.session.add(agent1)
        
        agent2 = User(
            username='ana.santos',
            email='ana@teste.com',
            role='agent'
        )
        agent2.set_password('123456')
        db.session.add(agent2)
        
        manager = User(
            username='joao.manager',
            email='manager@teste.com',
            role='manager'
        )
        manager.set_password('123456')
        db.session.add(manager)
        
        db.session.commit()
        
        print("Criando clientes...")
        
        # Criar clientes
        customers_data = [
            {'name': 'João Silva', 'email': 'joao.silva@email.com', 'phone': '(11) 99999-1111', 'company': 'Tech Solutions Ltda'},
            {'name': 'Maria Santos', 'email': 'maria.santos@email.com', 'phone': '(11) 99999-2222', 'company': 'Inovação Digital'},
            {'name': 'Pedro Oliveira', 'email': 'pedro.oliveira@email.com', 'phone': '(11) 99999-3333', 'company': 'StartUp Brasil'},
            {'name': 'Ana Costa', 'email': 'ana.costa@email.com', 'phone': '(11) 99999-4444', 'company': 'Consultoria Plus'},
            {'name': 'Carlos Ferreira', 'email': 'carlos.ferreira@email.com', 'phone': '(11) 99999-5555', 'company': 'Empresa ABC'},
            {'name': 'Lucia Mendes', 'email': 'lucia.mendes@email.com', 'phone': '(11) 99999-6666', 'company': 'Negócios Online'},
            {'name': 'Roberto Lima', 'email': 'roberto.lima@email.com', 'phone': '(11) 99999-7777', 'company': 'Soluções Web'},
            {'name': 'Fernanda Rocha', 'email': 'fernanda.rocha@email.com', 'phone': '(11) 99999-8888', 'company': 'Digital Corp'}
        ]
        
        customers = []
        for customer_data in customers_data:
            customer = Customer(**customer_data)
            customers.append(customer)
            db.session.add(customer)
        
        db.session.commit()
        
        print("Criando tickets...")
        
        # Criar tickets
        ticket_templates = [
            {
                'title': 'Problema de login no sistema',
                'description': 'Usuário não consegue fazer login no sistema. Aparece mensagem de erro "credenciais inválidas" mesmo com senha correta.',
                'category': 'Acesso',
                'priority': 'alta'
            },
            {
                'title': 'Dúvida sobre funcionalidade de relatórios',
                'description': 'Cliente gostaria de saber como gerar relatórios personalizados no sistema e exportar para Excel.',
                'category': 'Dúvida',
                'priority': 'media'
            },
            {
                'title': 'Sistema está muito lento',
                'description': 'O sistema está demorando muito para carregar as páginas, especialmente na área de relatórios.',
                'category': 'Performance',
                'priority': 'alta'
            },
            {
                'title': 'Erro ao salvar dados',
                'description': 'Ao tentar salvar informações do cliente, aparece erro 500 e os dados não são salvos.',
                'category': 'Bug',
                'priority': 'urgente'
            },
            {
                'title': 'Solicitação de nova funcionalidade',
                'description': 'Cliente solicita implementação de notificações por email quando um ticket é atualizado.',
                'category': 'Melhoria',
                'priority': 'baixa'
            },
            {
                'title': 'Problema na integração com API',
                'description': 'A integração com a API externa está retornando erro 401 - Unauthorized.',
                'category': 'Integração',
                'priority': 'alta'
            },
            {
                'title': 'Dúvida sobre configuração',
                'description': 'Como configurar as permissões de usuário para diferentes níveis de acesso?',
                'category': 'Configuração',
                'priority': 'media'
            },
            {
                'title': 'Backup não está funcionando',
                'description': 'O backup automático não está sendo executado há 3 dias.',
                'category': 'Sistema',
                'priority': 'urgente'
            }
        ]
        
        statuses = ['aberto', 'em_andamento', 'concluido', 'fechado']
        agents = [agent1.id, agent2.id, manager.id]
        
        # Criar tickets dos últimos 12 meses
        for month_offset in range(12):
            base_date = datetime.now() - timedelta(days=30 * month_offset)
            
            # Criar entre 15 a 45 tickets por mês
            tickets_count = random.randint(15, 45)
            
            for i in range(tickets_count):
                template = random.choice(ticket_templates)
                customer = random.choice(customers)
                
                # Data aleatória dentro do mês
                created_date = base_date - timedelta(
                    days=random.randint(0, 29),
                    hours=random.randint(0, 23),
                    minutes=random.randint(0, 59)
                )
                
                status = random.choice(statuses)
                resolved_date = None
                
                # Se ticket está concluído, definir data de resolução
                if status == 'concluido':
                    resolved_date = created_date + timedelta(
                        days=random.randint(1, 7),
                        hours=random.randint(0, 23)
                    )
                
                ticket = Ticket(
                    title=f"{template['title']} #{i+1}",
                    description=template['description'],
                    category=template['category'],
                    priority=template['priority'],
                    status=status,
                    customer_id=customer.id,
                    assigned_to=random.choice(agents) if random.random() > 0.2 else None,
                    created_at=created_date,
                    updated_at=created_date,
                    resolved_at=resolved_date
                )
                
                db.session.add(ticket)
        
        db.session.commit()
        
        print("Dados de teste criados com sucesso!")
        print("\nCredenciais de acesso:")
        print("Admin: admin@teste.com / admin123")
        print("Agente 1: carlos@teste.com / 123456")
        print("Agente 2: ana@teste.com / 123456")
        print("Manager: manager@teste.com / 123456")

if __name__ == '__main__':
    seed_database()

