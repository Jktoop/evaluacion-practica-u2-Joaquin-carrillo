
from modelos import Equipo, Estudiante, Prestamo
from conexiones import session


def crear_prestamo(equipo_id, estudiante_id, fecha, cantidad):

    sesion = session()

    equipo = sesion.get(Equipo, equipo_id)
    estudiante = sesion.get(Estudiante, estudiante_id)

    if not equipo:
        print("Equipo no encontrado.")

    elif not estudiante:
        print("Estudiante no encontrado.")

    elif cantidad <= 0:
        print("La cantidad debe ser positiva.")

    elif cantidad > equipo.stock_disponible:
        print("No hay stock suficiente.")

    else:

        prestamo = Prestamo(
            equipo_id=equipo_id,
            estudiante_id=estudiante_id,
            fecha=fecha,
            cantidad=cantidad,
            estado="activo"
        )

        equipo.stock_disponible -= cantidad

        sesion.add(prestamo)
        sesion.commit()

        print("Préstamo registrado correctamente.")

    sesion.close()


def listar_prestamos():

    sesion = session()

    prestamos = sesion.query(Prestamo).all()

    if not prestamos:
        print("No hay préstamos registrados.")

    for prestamo in prestamos:
        print(prestamo)

    sesion.close()
