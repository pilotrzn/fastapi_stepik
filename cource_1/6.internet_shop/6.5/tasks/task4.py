from sqlalchemy import ForeignKey, Integer, String, Date
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship


class Base(DeclarativeBase): ...


class Project(Base):
    __tablename__ = "projects"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(150), nullable=False)
    start_date = mapped_column(Date, nullable=False)

    employees = relationship(
        "Employee", secondary="participations", back_populates="projects", viewonly=True
    )


class Employee(Base):
    __tablename__ = "employees"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(100), nullable=False)
    email = mapped_column(String(120), unique=True, nullable=False)

    projects = relationship(
        "Project", secondary="participations", back_populates="employees", viewonly=True
    )


class Participation(Base):
    __tablename__ = "participations"

    project_id = mapped_column(Integer, ForeignKey("projects.id"), primary_key=True)
    employee_id = mapped_column(Integer, ForeignKey("employees.id"), primary_key=True)

    role = mapped_column(String(50), nullable=False)
