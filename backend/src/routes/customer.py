from flask import Blueprint, jsonify, request
from src.models.customer import Customer, db

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        search = request.args.get('search', '')
        
        query = Customer.query
        
        if search:
            query = query.filter(
                Customer.name.contains(search) | 
                Customer.email.contains(search) |
                Customer.company.contains(search)
            )
        
        customers = query.paginate(
            page=page, 
            per_page=per_page, 
            error_out=False
        )
        
        return jsonify({
            'customers': [customer.to_dict() for customer in customers.items],
            'total': customers.total,
            'pages': customers.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.get_json()
        
        if not data.get('name') or not data.get('email'):
            return jsonify({'error': 'Nome e email são obrigatórios'}), 400
        
        # Verificar se email já existe
        if Customer.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email já cadastrado'}), 400
        
        customer = Customer(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            company=data.get('company')
        )
        
        db.session.add(customer)
        db.session.commit()
        
        return jsonify(customer.to_dict()), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)
        return jsonify(customer.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)
        data = request.get_json()
        
        # Verificar se email já existe (exceto o próprio cliente)
        if data.get('email') and data['email'] != customer.email:
            if Customer.query.filter_by(email=data['email']).first():
                return jsonify({'error': 'Email já cadastrado'}), 400
        
        customer.name = data.get('name', customer.name)
        customer.email = data.get('email', customer.email)
        customer.phone = data.get('phone', customer.phone)
        customer.company = data.get('company', customer.company)
        
        db.session.commit()
        
        return jsonify(customer.to_dict()), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        customer = Customer.query.get_or_404(customer_id)
        
        # Verificar se há tickets associados
        if customer.tickets:
            return jsonify({'error': 'Não é possível excluir cliente com tickets associados'}), 400
        
        db.session.delete(customer)
        db.session.commit()
        
        return '', 204
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

