#!/usr/bin/env python3
"""
Customer Support API - Versão Simplificada
"""

import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key'

# CORS
CORS(app, origins="*")

@app.route('/api/health')
def health_check():
    """Health check da aplicação"""
    return jsonify({
        "status": "healthy",
        "service": "Customer Support API",
        "version": "2.0.0",
        "message": "Backend funcionando!"
    }), 200

@app.route('/')
def home():
    """Página inicial"""
    return jsonify({
        "message": "Customer Support API - v2.0",
        "status": "running",
        "version": "2.0.0",
        "endpoints": {
            "health": "/api/health",
            "auth": {
                "login": "/api/auth/login",
                "verify": "/api/auth/verify"
            },
            "users": "/api/users",
            "customers": "/api/customers",
            "tickets": "/api/tickets"
        }
    }), 200

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login do usuário"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        # Dados mock para teste
        users = [
            {"id": 1, "name": "Admin", "email": "admin@teste.com", "password": "admin123", "role": "admin"},
            {"id": 2, "name": "Agente", "email": "carlos@teste.com", "password": "123456", "role": "agent"}
        ]
        
        for user in users:
            if user['email'] == email and user['password'] == password:
                return jsonify({
                    "success": True,
                    "user": {
                        "id": user['id'],
                        "name": user['name'],
                        "email": user['email'],
                        "role": user['role']
                    },
                    "token": f"mock-token-{user['id']}"
                }), 200
        
        return jsonify({
            "success": False,
            "error": "Credenciais inválidas"
        }), 401
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Erro no login: {str(e)}"
        }), 500

@app.route('/api/users')
def get_users():
    """Lista todos os usuários"""
    users = [
        {"id": 1, "name": "Admin", "email": "admin@teste.com", "role": "admin"},
        {"id": 2, "name": "Agente", "email": "carlos@teste.com", "role": "agent"}
    ]
    return jsonify(users), 200

@app.route('/api/customers')
def get_customers():
    """Lista todos os clientes"""
    customers = [
        {"id": 1, "name": "Cliente 1", "email": "cliente1@teste.com", "company": "Empresa A"},
        {"id": 2, "name": "Cliente 2", "email": "cliente2@teste.com", "company": "Empresa B"}
    ]
    return jsonify(customers), 200

@app.route('/api/tickets')
def get_tickets():
    """Lista todos os tickets"""
    tickets = [
        {
            "id": 1, 
            "title": "Problema com login", 
            "status": "aberto", 
            "priority": "alta",
            "customer_name": "João Silva",
            "created_at": "2024-01-15T10:30:00Z"
        },
        {
            "id": 2, 
            "title": "Erro no sistema de pagamento", 
            "status": "fechado", 
            "priority": "media",
            "customer_name": "Maria Santos",
            "created_at": "2024-01-10T14:20:00Z"
        }
    ]
    return jsonify(tickets), 200

@app.route('/api/tickets/<int:ticket_id>')
def get_ticket_details(ticket_id):
    """Obtém detalhes de um ticket específico"""
    # Dados mock expandidos para detalhes do ticket
    tickets_details = {
        1: {
            "id": 1,
            "title": "Problema com login",
            "description": "Cliente relatou dificuldades para acessar o sistema. Erro aparece após inserir credenciais válidas.",
            "status": "aberto",
            "priority": "alta",
            "customer": {
                "id": 1,
                "name": "João Silva",
                "email": "joao@empresa.com",
                "phone": "(11) 99999-9999",
                "company": "Empresa ABC"
            },
            "assigned_to": "Carlos Agente",
            "created_at": "2024-01-15T10:30:00Z",
            "updated_at": "2024-01-16T14:20:00Z",
            "notes": [
                {
                    "id": 1,
                    "author": "Carlos Agente",
                    "content": "Ticket recebido e em análise. Verificando logs do sistema.",
                    "created_at": "2024-01-15T10:35:00Z"
                },
                {
                    "id": 2,
                    "author": "João Silva",
                    "content": "Problema persiste. Tentei limpar cache do navegador conforme orientação.",
                    "created_at": "2024-01-16T09:15:00Z"
                }
            ]
        },
        2: {
            "id": 2,
            "title": "Erro no sistema de pagamento",
            "description": "Sistema apresenta erro 500 ao processar pagamentos via cartão de crédito.",
            "status": "fechado",
            "priority": "media",
            "customer": {
                "id": 2,
                "name": "Maria Santos",
                "email": "maria@empresa.com",
                "phone": "(11) 88888-8888",
                "company": "Empresa XYZ"
            },
            "assigned_to": "Ana Desenvolvedora",
            "created_at": "2024-01-10T14:20:00Z",
            "updated_at": "2024-01-12T16:45:00Z",
            "notes": [
                {
                    "id": 3,
                    "author": "Ana Desenvolvedora",
                    "content": "Identificado problema na integração com gateway de pagamento. Correção aplicada.",
                    "created_at": "2024-01-12T16:45:00Z"
                }
            ]
        }
    }
    
    ticket = tickets_details.get(ticket_id)
    if not ticket:
        return jsonify({"error": "Ticket não encontrado"}), 404
    
    return jsonify(ticket), 200

@app.route('/api/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    """Atualiza um ticket"""
    try:
        data = request.get_json()
        
        # Aqui normalmente atualizaria no banco de dados
        # Por enquanto, apenas retorna sucesso
        
        return jsonify({
            "success": True,
            "message": "Ticket atualizado com sucesso",
            "ticket_id": ticket_id,
            "updated_fields": data
        }), 200
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"Erro ao atualizar ticket: {str(e)}"
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Iniciando Customer Support API v2.0 na porta {port}")
    print(f"📁 Diretório: {os.getcwd()}")
    
    app.run(host='0.0.0.0', port=port, debug=False) 