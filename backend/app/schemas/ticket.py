"""
Ticket schemas for data validation and serialization
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID

from app.models.ticket import TicketStatus, TicketPriority
from app.schemas.customer import CustomerResponse
from app.schemas.user import UserResponse


class TicketBase(BaseModel):
    """Base ticket schema"""
    title: str = Field(..., min_length=5, max_length=200)
    description: str = Field(..., min_length=10)
    priority: TicketPriority = TicketPriority.MEDIUM


class TicketCreate(TicketBase):
    """Schema for creating a ticket"""
    customer_id: UUID


class TicketUpdate(BaseModel):
    """Schema for updating a ticket"""
    title: Optional[str] = Field(None, min_length=5, max_length=200)
    description: Optional[str] = Field(None, min_length=10)
    status: Optional[TicketStatus] = None
    priority: Optional[TicketPriority] = None
    assigned_to: Optional[UUID] = None


class TicketResponse(TicketBase):
    """Schema for ticket response"""
    id: UUID
    status: TicketStatus
    customer_id: UUID
    assigned_to: Optional[UUID] = None
    created_by: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class TicketDetailResponse(TicketResponse):
    """Schema for detailed ticket response with relationships"""
    customer: CustomerResponse
    assigned_user: Optional[UserResponse] = None
    creator: UserResponse

    class Config:
        from_attributes = True


class TicketStats(BaseModel):
    """Schema for ticket statistics"""
    total_tickets: int
    open_tickets: int
    in_progress_tickets: int
    resolved_tickets: int
    closed_tickets: int
    avg_resolution_time_hours: Optional[float] = None

