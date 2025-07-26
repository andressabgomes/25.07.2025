#!/usr/bin/env python3
"""
Aplicação Flask ultra-simples para Railway
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'secret-key-123'

# Configurar CORS
CORS(app, origins="*")

@app.route('/api/health')
def health_check():
    return jsonify({
        "status": "healthy", 
        "service": "Customer Support API",
        "message": "Backend funcionando!"
    }), 200

@app.route('/api/users')
def get_users():
    return jsonify([
        {"id": 1, "name": "Admin", "email": "admin@teste.com"},
        {"id": 2, "name": "Agente", "email": "agente@teste.com"}
    ]), 200

@app.route('/api/customers')
def get_customers():
    return jsonify([
        {"id": 1, "name": "Cliente 1", "email": "cliente1@teste.com"},
        {"id": 2, "name": "Cliente 2", "email": "cliente2@teste.com"}
    ]), 200

@app.route('/api/tickets')
def get_tickets():
    return jsonify([
        {"id": 1, "title": "Ticket 1", "status": "aberto"},
        {"id": 2, "title": "Ticket 2", "status": "fechado"}
    ]), 200

@app.route('/')
def home():
    return jsonify({
        "message": "Customer Support API - Railway",
        "status": "running",
        "endpoints": {
            "health": "/api/health",
            "users": "/api/users", 
            "customers": "/api/customers",
            "tickets": "/api/tickets"
        }
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Iniciando servidor na porta {port}")
    app.run(host='0.0.0.0', port=port, debug=False) 