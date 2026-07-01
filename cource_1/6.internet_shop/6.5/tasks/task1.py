from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase): ...


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    student_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    grades: Mapped[list["Grade"]] = relationship("Grade", back_populates="student")


class Grade(Base):
    __tablename__ = "grades"

    id: Mapped[int] = mapped_column(primary_key=True)
    value: Mapped[int] = mapped_column(Integer, nullable=False)
    subject: Mapped[str] = mapped_column(String(50), nullable=False)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id"))

    student: Mapped["Student"] = relationship("Student", back_populates="grades")
