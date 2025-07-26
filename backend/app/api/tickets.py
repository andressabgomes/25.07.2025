"""
Tickets API routes
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID

from app.core.database import get_db
from app.core.security import verify_token
from app.schemas.ticket import TicketCreate, TicketUpdate, TicketResponse, TicketDetailResponse, TicketStats
from app.models.ticket import TicketStatus
from app.services.ticket_service import TicketService
from app.services.user_service import UserService

router = APIRouter(prefix="/tickets", tags=["Tickets"])
security = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    """
    Dependency to get current authenticated user
    """
    token_data = verify_token(credentials.credentials)
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = UserService.get_user_by_email(db, token_data.get("sub"))
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found or inactive",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user


@router.post("/", response_model=TicketDetailResponse)
async def create_ticket(
    ticket_data: TicketCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Create a new ticket
    """
    ticket = TicketService.create_ticket(db, ticket_data, current_user.id)
    # Reload with relationships
    ticket = TicketService.get_ticket_by_id(db, ticket.id)
    return ticket


@router.get("/", response_model=List[TicketDetailResponse])
async def get_tickets(
    skip: int = 0,
    limit: int = 100,
    status: Optional[TicketStatus] = Query(None, description="Filter tickets by status"),
    search: Optional[str] = Query(None, description="Search tickets by title or description"),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get list of tickets with optional filters
    """
    if search:
        tickets = TicketService.search_tickets(db, search, skip=skip, limit=limit)
    else:
        tickets = TicketService.get_tickets(db, skip=skip, limit=limit, status=status)
    return tickets


@router.get("/stats", response_model=TicketStats)
async def get_ticket_stats(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get ticket statistics
    """
    return TicketService.get_ticket_stats(db)


@router.get("/my-tickets", response_model=List[TicketDetailResponse])
async def get_my_tickets(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get tickets assigned to current user
    """
    tickets = TicketService.get_tickets_by_assignee(db, current_user.id, skip=skip, limit=limit)
    return tickets


@router.get("/customer/{customer_id}", response_model=List[TicketDetailResponse])
async def get_tickets_by_customer(
    customer_id: UUID,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get tickets by customer ID
    """
    tickets = TicketService.get_tickets_by_customer(db, customer_id, skip=skip, limit=limit)
    return tickets


@router.get("/{ticket_id}", response_model=TicketDetailResponse)
async def get_ticket(
    ticket_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Get ticket by ID
    """
    ticket = TicketService.get_ticket_by_id(db, ticket_id)
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found"
        )
    return ticket


@router.put("/{ticket_id}", response_model=TicketDetailResponse)
async def update_ticket(
    ticket_id: UUID,
    ticket_data: TicketUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Update ticket information
    """
    ticket = TicketService.update_ticket(db, ticket_id, ticket_data)
    if not ticket:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found"
        )
    
    # Reload with relationships
    ticket = TicketService.get_ticket_by_id(db, ticket.id)
    return ticket


@router.delete("/{ticket_id}")
async def delete_ticket(
    ticket_id: UUID,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    """
    Delete ticket
    """
    success = TicketService.delete_ticket(db, ticket_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Ticket not found"
        )
    
    return {"message": "Ticket deleted successfully"}

