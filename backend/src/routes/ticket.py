from flask import Blueprint, jsonify, request
from src.models.ticket import Ticket, db
from src.models.customer import Customer
from src.models.user import User
from datetime import datetime
from sqlalchemy import func, extract

ticket_bp = Blueprint('ticket', __name__)

@ticket_bp.route('/tickets', methods=['GET'])
def get_tickets():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        status = request.args.get('status')
        priority = request.args.get('priority')
        search = request.args.get('search', '')
        
        query = Ticket.query
        
        if status:
            query = query.filter(Ticket.status == status)
        
        if priority:
            query = query.filter(Ticket.priority == priority)
        
        if search:
            query = query.join(Customer).filter(
                Ticket.title.contains(search) |
                Ticket.description.contains(search) |
                Customer.name.contains(search)
            )
        
        tickets = query.order_by(Ticket.created_at.desc()).paginate(
            page=page,
            per_page=per_page,
            error_out=False
        )
        
        return jsonify({
            'tickets': [ticket.to_dict() for ticket in tickets.items],
            'total': tickets.total,
            'pages': tickets.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ticket_bp.route('/tickets', methods=['POST'])
def create_ticket():
    try:
        data = request.get_json()
        
        required_fields = ['title', 'description', 'customer_id']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} é obrigatório'}), 400
        
        # Verificar se cliente existe
        customer = Customer.query.get(data['customer_id'])
        if not customer:
            return jsonify({'error': 'Cliente não encontrado'}), 404
        
        ticket = Ticket(
            title=data['title'],
            description=data['description'],
            customer_id=data['customer_id'],
            priority=data.get('priority', 'media'),
            category=data.get('category'),
            assigned_to=data.get('assigned_to')
        )
        
        db.session.add(ticket)
        db.session.commit()
        
        return jsonify(ticket.to_dict()), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ticket_bp.route('/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    try:
        ticket = Ticket.query.get_or_404(ticket_id)
        return jsonify(ticket.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ticket_bp.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    try:
        ticket = Ticket.query.get_or_404(ticket_id)
        data = request.get_json()
        
        ticket.title = data.get('title', ticket.title)
        ticket.description = data.get('description', ticket.description)
        ticket.status = data.get('status', ticket.status)
        ticket.priority = data.get('priority', ticket.priority)
        ticket.category = data.get('category', ticket.category)
        ticket.assigned_to = data.get('assigned_to', ticket.assigned_to)
        
        # Se status mudou para concluído, definir data de resolução
        if data.get('status') == 'concluido' and ticket.resolved_at is None:
            ticket.resolved_at = datetime.utcnow()
        
        ticket.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify(ticket.to_dict()), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ticket_bp.route('/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    try:
        ticket = Ticket.query.get_or_404(ticket_id)
        db.session.delete(ticket)
        db.session.commit()
        
        return '', 204
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ticket_bp.route('/tickets/stats', methods=['GET'])
def get_ticket_stats():
    try:
        # Estatísticas gerais
        total_tickets = Ticket.query.count()
        open_tickets = Ticket.query.filter(Ticket.status.in_(['aberto', 'em_andamento'])).count()
        closed_tickets = Ticket.query.filter(Ticket.status == 'concluido').count()
        
        # Tickets por mês (últimos 12 meses)
        monthly_stats = db.session.query(
            extract('month', Ticket.created_at).label('month'),
            extract('year', Ticket.created_at).label('year'),
            func.count(Ticket.id).label('total'),
            func.sum(func.case([(Ticket.status == 'concluido', 1)], else_=0)).label('closed'),
            func.sum(func.case([(Ticket.status.in_(['aberto', 'em_andamento']), 1)], else_=0)).label('open')
        ).group_by(
            extract('year', Ticket.created_at),
            extract('month', Ticket.created_at)
        ).order_by(
            extract('year', Ticket.created_at).desc(),
            extract('month', Ticket.created_at).desc()
        ).limit(12).all()
        
        # Tickets por prioridade
        priority_stats = db.session.query(
            Ticket.priority,
            func.count(Ticket.id).label('count')
        ).group_by(Ticket.priority).all()
        
        # Tickets por status
        status_stats = db.session.query(
            Ticket.status,
            func.count(Ticket.id).label('count')
        ).group_by(Ticket.status).all()
        
        return jsonify({
            'general': {
                'total': total_tickets,
                'open': open_tickets,
                'closed': closed_tickets
            },
            'monthly': [
                {
                    'month': stat.month,
                    'year': stat.year,
                    'total': stat.total,
                    'closed': stat.closed or 0,
                    'open': stat.open or 0
                }
                for stat in monthly_stats
            ],
            'by_priority': [
                {'priority': stat.priority, 'count': stat.count}
                for stat in priority_stats
            ],
            'by_status': [
                {'status': stat.status, 'count': stat.count}
                for stat in status_stats
            ]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

