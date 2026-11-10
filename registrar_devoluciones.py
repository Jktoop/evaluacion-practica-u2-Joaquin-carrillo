
from modelos import Equipo, Prestamo
from conexiones import session

def buscar_prestamo(id):

    sesion = session()

    prestamo = sesion.get(Prestamo, id)

    if prestamo:
        print(prestamo)
    else:
        print("Préstamo no encontrado.")

    sesion.close()


def devolver_prestamo(id):

    sesion = session()
    prestamo = sesion.get(Prestamo, id)

    if not prestamo:
        print("Préstamo no encontrado.")

    elif prestamo.estado == "devuelto":
        print("eset prestamo ya fue devuelto.")

    else:

        equipo = sesion.get(Equipo, prestamo.equipo_id)

        prestamo.estado = "devuelto"
        equipo.stock_disponible += prestamo.cantidad

        sesion.commit()

        print("Devolución realizada correctamente.")

    sesion.close()
