"""
Ticket service for business logic operations
"""

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, desc
from typing import List, Optional
from uuid import UUID
from datetime import datetime

from app.models.ticket import Ticket, TicketStatus
from app.models.customer import Customer
from app.models.user import User
from app.schemas.ticket import TicketCreate, TicketUpdate, TicketStats


class TicketService:
    """Ticket service class"""

    @staticmethod
    def create_ticket(db: Session, ticket_data: TicketCreate, created_by: UUID) -> Ticket:
        """
        Create a new ticket
        """
        db_ticket = Ticket(
            title=ticket_data.title,
            description=ticket_data.description,
            priority=ticket_data.priority,
            customer_id=ticket_data.customer_id,
            created_by=created_by
        )
        db.add(db_ticket)
        db.commit()
        db.refresh(db_ticket)
        return db_ticket

    @staticmethod
    def get_ticket_by_id(db: Session, ticket_id: UUID) -> Optional[Ticket]:
        """
        Get ticket by ID with relationships
        """
        return db.query(Ticket).options(
            joinedload(Ticket.customer),
            joinedload(Ticket.assigned_user),
            joinedload(Ticket.creator)
        ).filter(Ticket.id == ticket_id).first()

    @staticmethod
    def get_tickets(db: Session, skip: int = 0, limit: int = 100, status: Optional[TicketStatus] = None) -> List[Ticket]:
        """
        Get list of tickets with pagination and optional status filter
        """
        query = db.query(Ticket).options(
            joinedload(Ticket.customer),
            joinedload(Ticket.assigned_user),
            joinedload(Ticket.creator)
        )
        
        if status:
            query = query.filter(Ticket.status == status)
        
        return query.order_by(desc(Ticket.created_at)).offset(skip).limit(limit).all()

    @staticmethod
    def get_tickets_by_customer(db: Session, customer_id: UUID, skip: int = 0, limit: int = 100) -> List[Ticket]:
        """
        Get tickets by customer ID
        """
        return db.query(Ticket).options(
            joinedload(Ticket.customer),
            joinedload(Ticket.assigned_user),
            joinedload(Ticket.creator)
        ).filter(Ticket.customer_id == customer_id).order_by(desc(Ticket.created_at)).offset(skip).limit(limit).all()

    @staticmethod
    def get_tickets_by_assignee(db: Session, user_id: UUID, skip: int = 0, limit: int = 100) -> List[Ticket]:
        """
        Get tickets assigned to a specific user
        """
        return db.query(Ticket).options(
            joinedload(Ticket.customer),
            joinedload(Ticket.assigned_user),
            joinedload(Ticket.creator)
        ).filter(Ticket.assigned_to == user_id).order_by(desc(Ticket.created_at)).offset(skip).limit(limit).all()

    @staticmethod
    def update_ticket(db: Session, ticket_id: UUID, ticket_data: TicketUpdate) -> Optional[Ticket]:
        """
        Update ticket information
        """
        db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not db_ticket:
            return None

        update_data = ticket_data.dict(exclude_unset=True)
        
        # Set resolved_at timestamp when status changes to resolved
        if "status" in update_data and update_data["status"] == TicketStatus.RESOLVED:
            update_data["resolved_at"] = datetime.utcnow()
        
        for field, value in update_data.items():
            setattr(db_ticket, field, value)

        db.commit()
        db.refresh(db_ticket)
        return db_ticket

    @staticmethod
    def delete_ticket(db: Session, ticket_id: UUID) -> bool:
        """
        Delete ticket
        """
        db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
        if not db_ticket:
            return False

        db.delete(db_ticket)
        db.commit()
        return True

    @staticmethod
    def get_ticket_stats(db: Session) -> TicketStats:
        """
        Get ticket statistics
        """
        total_tickets = db.query(Ticket).count()
        open_tickets = db.query(Ticket).filter(Ticket.status == TicketStatus.OPEN).count()
        in_progress_tickets = db.query(Ticket).filter(Ticket.status == TicketStatus.IN_PROGRESS).count()
        resolved_tickets = db.query(Ticket).filter(Ticket.status == TicketStatus.RESOLVED).count()
        closed_tickets = db.query(Ticket).filter(Ticket.status == TicketStatus.CLOSED).count()

        # Calculate average resolution time
        avg_resolution_time = db.query(
            func.avg(
                func.extract('epoch', Ticket.resolved_at - Ticket.created_at) / 3600
            )
        ).filter(Ticket.resolved_at.isnot(None)).scalar()

        return TicketStats(
            total_tickets=total_tickets,
            open_tickets=open_tickets,
            in_progress_tickets=in_progress_tickets,
            resolved_tickets=resolved_tickets,
            closed_tickets=closed_tickets,
            avg_resolution_time_hours=avg_resolution_time
        )

    @staticmethod
    def search_tickets(db: Session, query: str, skip: int = 0, limit: int = 100) -> List[Ticket]:
        """
        Search tickets by title or description
        """
        search_filter = f"%{query}%"
        return db.query(Ticket).options(
            joinedload(Ticket.customer),
            joinedload(Ticket.assigned_user),
            joinedload(Ticket.creator)
        ).filter(
            (Ticket.title.ilike(search_filter)) |
            (Ticket.description.ilike(search_filter))
        ).order_by(desc(Ticket.created_at)).offset(skip).limit(limit).all()

