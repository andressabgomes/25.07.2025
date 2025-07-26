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
        {"id": 1, "title": "Ticket 1", "status": "aberto", "priority": "alta"},
        {"id": 2, "title": "Ticket 2", "status": "fechado", "priority": "média"}
    ]
    return jsonify(tickets), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Iniciando Customer Support API v2.0 na porta {port}")
    print(f"📁 Diretório: {os.getcwd()}")
    
    app.run(host='0.0.0.0', port=port, debug=False) 