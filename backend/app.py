#!/usr/bin/env python3
"""
Customer Support API - Aplicação Principal Refatorada
"""

import os
from flask import Flask, jsonify, request
from flask_cors import CORS

from config import get_config
from services import (
    supabase_service,
    AuthService,
    TicketService,
    CustomerService,
    UserService
)

def create_app():
    """Factory function para criar a aplicação Flask"""
    app = Flask(__name__)
    
    # Configuração
    config = get_config()
    app.config.from_object(config)
    
    # CORS
    CORS(app, origins=config.CORS_ORIGINS)
    
    # Registrar rotas
    register_routes(app)
    
    return app

def register_routes(app):
    """Registra todas as rotas da aplicação"""
    
    @app.route('/api/health')
    def health_check():
        """Health check da aplicação"""
        supabase_status = supabase_service.test_connection()
        
        return jsonify({
            "status": "healthy",
            "service": "Customer Support API",
            "version": "2.0.0",
            "supabase": supabase_status,
            "message": "Backend funcionando com arquitetura limpa!"
        }), 200
    
    @app.route('/')
    def home():
        """Página inicial"""
        return jsonify({
            "message": "Customer Support API - Arquitetura Limpa",
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
                "tickets": "/api/tickets",
                "tickets_stats": "/api/tickets/stats"
            }
        }), 200
    
    # Rotas de Autenticação
    @app.route('/api/auth/login', methods=['POST'])
    def login():
        """Login do usuário"""
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            
            if not email or not password:
                return jsonify({
                    "success": False,
                    "error": "Email e senha são obrigatórios"
                }), 400
            
            result = AuthService.login(email, password)
            
            if result["success"]:
                return jsonify(result), 200
            else:
                return jsonify(result), 401
                
        except Exception as e:
            return jsonify({
                "success": False,
                "error": f"Erro no login: {str(e)}"
            }), 500
    
    @app.route('/api/auth/verify', methods=['POST'])
    def verify_token():
        """Verifica token de autenticação"""
        try:
            data = request.get_json()
            token = data.get('token')
            
            if not token:
                return jsonify({
                    "success": False,
                    "error": "Token é obrigatório"
                }), 400
            
            result = AuthService.verify_token(token)
            return jsonify(result), 200
            
        except Exception as e:
            return jsonify({
                "success": False,
                "error": f"Erro na verificação: {str(e)}"
            }), 500
    
    # Rotas de Usuários
    @app.route('/api/users')
    def get_users():
        """Lista todos os usuários"""
        try:
            users = UserService.get_all_users()
            return jsonify(users), 200
        except Exception as e:
            return jsonify({
                "error": f"Erro ao buscar usuários: {str(e)}"
            }), 500
    
    # Rotas de Clientes
    @app.route('/api/customers')
    def get_customers():
        """Lista todos os clientes"""
        try:
            customers = CustomerService.get_all_customers()
            return jsonify(customers), 200
        except Exception as e:
            return jsonify({
                "error": f"Erro ao buscar clientes: {str(e)}"
            }), 500
    
    # Rotas de Tickets
    @app.route('/api/tickets')
    def get_tickets():
        """Lista todos os tickets"""
        try:
            tickets = TicketService.get_all_tickets()
            return jsonify(tickets), 200
        except Exception as e:
            return jsonify({
                "error": f"Erro ao buscar tickets: {str(e)}"
            }), 500
    
    @app.route('/api/tickets/stats')
    def get_ticket_stats():
        """Estatísticas dos tickets"""
        try:
            stats = TicketService.get_ticket_stats()
            return jsonify(stats), 200
        except Exception as e:
            return jsonify({
                "error": f"Erro ao buscar estatísticas: {str(e)}"
            }), 500

# Criar aplicação
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Iniciando Customer Support API v2.0 na porta {port}")
    print(f"📁 Diretório: {os.getcwd()}")
    print(f"🔧 Ambiente: {os.environ.get('FLASK_ENV', 'development')}")
    
    app.run(host='0.0.0.0', port=port, debug=False) 