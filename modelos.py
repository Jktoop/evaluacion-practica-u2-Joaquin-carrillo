from sqlalchemy import ForeignKey, String, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Equipo(Base):

    __tablename__ = "equipo"

    __table_args__ = (
        CheckConstraint("stock_disponible >= 0",name="stock_disponible_no_negativo"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    tipo: Mapped[str] = mapped_column(String(100), nullable=False)
    stock_disponible: Mapped[int] = mapped_column(nullable=False)

    prestamos: Mapped[list["Prestamo"]] = relationship(back_populates="equipo")

    def __repr__(self):
        return (
            f"Equipo(id={self.id}, nombre='{self.nombre}', "
            f"tipo='{self.tipo}', "
            f"stock_disponible={self.stock_disponible})"
        )


class Estudiante(Base):

    __tablename__ = "estudiante"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(100), nullable=False)

    prestamos: Mapped[list["Prestamo"]] = relationship(
        back_populates="estudiante"
    )

    def __repr__(self):
        return (
            f"Estudiante(id={self.id}, nombre='{self.nombre}', "
            f"correo='{self.correo}')"
        )


class Prestamo(Base):

    __tablename__ = "prestamo"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    equipo_id: Mapped[int] = mapped_column(
        ForeignKey("equipo.id"),
        nullable=False
    )

    estudiante_id: Mapped[int] = mapped_column(
        ForeignKey("estudiante.id"),
        nullable=False
    )

    fecha: Mapped[str] = mapped_column(String(100), nullable=False)
    cantidad: Mapped[int] = mapped_column(nullable=False)

    equipo: Mapped["Equipo"] = relationship(
        back_populates="prestamos"
    )

    estudiante: Mapped["Estudiante"] = relationship(
        back_populates="prestamos"
    )

    def __repr__(self):
        return (
            f"Prestamo(id={self.id}, equipo_id={self.equipo_id}, "
            f"estudiante_id={self.estudiante_id}, "
            f"fecha='{self.fecha}', cantidad={self.cantidad})"
        )