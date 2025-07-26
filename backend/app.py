#!/usr/bin/env python3
"""
Aplicação Flask simplificada para Railway
"""

import os
import sys

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from flask import Flask, jsonify
from flask_cors import CORS

try:
    from lib.supabase import get_supabase_client
    SUPABASE_AVAILABLE = True
except ImportError:
    SUPABASE_AVAILABLE = False
    print("⚠️ Supabase não disponível")

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'asdf#FGSgvasgf$5$WGT'

# Configurar CORS
CORS(app, origins="*")

@app.route('/api/health')
def health_check():
    try:
        if SUPABASE_AVAILABLE:
            # Testar conexão com Supabase
            supabase = get_supabase_client()
            response = supabase.table('users').select('count').limit(1).execute()
            
            return jsonify({
                "status": "healthy", 
                "service": "Customer Support API",
                "database": "Supabase",
                "connection": "OK"
            }), 200
        else:
            return jsonify({
                "status": "healthy", 
                "service": "Customer Support API",
                "database": "Not configured",
                "connection": "OK"
            }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "service": "Customer Support API", 
            "error": str(e)
        }), 500

@app.route('/api/users')
def get_users():
    try:
        if SUPABASE_AVAILABLE:
            supabase = get_supabase_client()
            response = supabase.table('users').select('*').execute()
            return jsonify(response.data), 200
        else:
            return jsonify({"error": "Supabase not configured"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/customers')
def get_customers():
    try:
        if SUPABASE_AVAILABLE:
            supabase = get_supabase_client()
            response = supabase.table('customers').select('*').execute()
            return jsonify(response.data), 200
        else:
            return jsonify({"error": "Supabase not configured"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/tickets')
def get_tickets():
    try:
        if SUPABASE_AVAILABLE:
            supabase = get_supabase_client()
            response = supabase.table('tickets').select('*, customer:customers(*)').execute()
            return jsonify(response.data), 200
        else:
            return jsonify({"error": "Supabase not configured"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return jsonify({
        "message": "Customer Support API - Railway",
        "status": "running",
        "supabase": SUPABASE_AVAILABLE,
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