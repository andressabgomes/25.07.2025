from src.models.user import db
from datetime import datetime

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='aberto')  # aberto, em_andamento, concluido, fechado
    priority = db.Column(db.String(10), default='media')  # baixa, media, alta, urgente
    category = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = db.Column(db.DateTime, nullable=True)
    
    # Chaves estrangeiras
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    
    # Relacionamentos
    assigned_user = db.relationship('User', backref='assigned_tickets', lazy=True)

    def __repr__(self):
        return f'<Ticket {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'category': self.category,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'resolved_at': self.resolved_at.isoformat() if self.resolved_at else None,
            'customer_id': self.customer_id,
            'customer_name': self.customer.name if self.customer else None,
            'assigned_to': self.assigned_to,
            'assigned_user_name': self.assigned_user.username if self.assigned_user else None
        }

