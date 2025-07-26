import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from src.models.user import db
from src.routes.user import user_bp
from src.routes.auth import auth_bp
from src.routes.customer import customer_bp
from src.routes.ticket import ticket_bp

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'asdf#FGSgvasgf$5$WGT'

# Configurar CORS
CORS(app, origins="*")

# Registrar blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(customer_bp, url_prefix='/api')
app.register_blueprint(ticket_bp, url_prefix='/api')

# Configuração do banco de dados
database_url = os.environ.get('DATABASE_URL')
if database_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Importar todos os modelos para criar as tabelas
from src.models.customer import Customer
from src.models.ticket import Ticket

db.init_app(app)
with app.app_context():
    db.create_all()

# Health check endpoint
@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy", "service": "Customer Support API"}), 200

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return jsonify({"message": "Customer Support API", "status": "running"}), 200

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return jsonify({"message": "Customer Support API", "status": "running"}), 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)
