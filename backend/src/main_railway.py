import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from src.lib.supabase import get_supabase_client

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'asdf#FGSgvasgf$5$WGT'

# Configurar CORS
CORS(app, origins="*")

# Health check endpoint
@app.route('/api/health')
def health_check():
    try:
        # Testar conexão com Supabase
        supabase = get_supabase_client()
        response = supabase.table('users').select('count').limit(1).execute()
        
        return jsonify({
            "status": "healthy", 
            "service": "Customer Support API",
            "database": "Supabase",
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
        supabase = get_supabase_client()
        response = supabase.table('users').select('*').execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/customers')
def get_customers():
    try:
        supabase = get_supabase_client()
        response = supabase.table('customers').select('*').execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/tickets')
def get_tickets():
    try:
        supabase = get_supabase_client()
        response = supabase.table('tickets').select('*, customer:customers(*)').execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return jsonify({
        "message": "Customer Support API - Supabase Integration",
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
    app.run(host='0.0.0.0', port=port, debug=False) 