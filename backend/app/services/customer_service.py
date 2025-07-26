"""
Customer service for business logic operations
"""

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from uuid import UUID

from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate


class CustomerService:
    """Customer service class"""

    @staticmethod
    def create_customer(db: Session, customer_data: CustomerCreate) -> Customer:
        """
        Create a new customer
        """
        try:
            db_customer = Customer(
                name=customer_data.name,
                email=customer_data.email,
                phone=customer_data.phone,
                company=customer_data.company
            )
            db.add(db_customer)
            db.commit()
            db.refresh(db_customer)
            return db_customer
        except IntegrityError:
            db.rollback()
            raise ValueError("Email already registered")

    @staticmethod
    def get_customer_by_id(db: Session, customer_id: UUID) -> Optional[Customer]:
        """
        Get customer by ID
        """
        return db.query(Customer).filter(Customer.id == customer_id).first()

    @staticmethod
    def get_customer_by_email(db: Session, email: str) -> Optional[Customer]:
        """
        Get customer by email
        """
        return db.query(Customer).filter(Customer.email == email).first()

    @staticmethod
    def get_customers(db: Session, skip: int = 0, limit: int = 100) -> List[Customer]:
        """
        Get list of customers with pagination
        """
        return db.query(Customer).offset(skip).limit(limit).all()

    @staticmethod
    def update_customer(db: Session, customer_id: UUID, customer_data: CustomerUpdate) -> Optional[Customer]:
        """
        Update customer information
        """
        db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
        if not db_customer:
            return None

        update_data = customer_data.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(db_customer, field, value)

        try:
            db.commit()
            db.refresh(db_customer)
            return db_customer
        except IntegrityError:
            db.rollback()
            raise ValueError("Email already registered")

    @staticmethod
    def delete_customer(db: Session, customer_id: UUID) -> bool:
        """
        Delete customer
        """
        db_customer = db.query(Customer).filter(Customer.id == customer_id).first()
        if not db_customer:
            return False

        db.delete(db_customer)
        db.commit()
        return True

    @staticmethod
    def search_customers(db: Session, query: str, skip: int = 0, limit: int = 100) -> List[Customer]:
        """
        Search customers by name, email, or company
        """
        search_filter = f"%{query}%"
        return db.query(Customer).filter(
            (Customer.name.ilike(search_filter)) |
            (Customer.email.ilike(search_filter)) |
            (Customer.company.ilike(search_filter))
        ).offset(skip).limit(limit).all()

