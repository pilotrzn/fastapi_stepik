from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase): ...


class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)

    orders: Mapped[list["Order"]] = relationship(
        "Order", back_populates="customers", uselist=True
    )


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    order_number: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    total_amount: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    customer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("customers.id"), nullable=False
    )

    customers: Mapped["Customer"] = relationship("Customer", back_populates="orders")
