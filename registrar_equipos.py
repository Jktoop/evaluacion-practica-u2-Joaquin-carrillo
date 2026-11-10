
from modelos import Equipo, Prestamo
from conexiones import session


def crear_equipo(nombre, tipo, stock):

    sesion = session()

    equipo = Equipo(
        nombre=nombre,
        tipo=tipo,
        stock_disponible=stock
    )

    sesion.add(equipo)
    sesion.commit()

    print("Equipo registrado correctamente.")

    sesion.close()


def listar_equipos():

    sesion = session()

    equipos = sesion.query(Equipo).all()

    if not equipos:
        print("No hay equipos registrados.")

    for equipo in equipos:
        print(equipo)

    sesion.close()


def buscar_equipo(id):

    sesion = session()

    equipo = sesion.get(Equipo, id)

    if equipo:
        print(equipo)
    else:
        print("Equipo no encontrado.")

    sesion.close()


def actualizar_equipo(id, nombre, tipo, stock):

    sesion = session()

    equipo = sesion.get(Equipo, id)

    if equipo:
        equipo.nombre = nombre
        equipo.tipo = tipo
        equipo.stock_disponible = stock

        sesion.commit()

        print("Equipo actualizado correcttamente.")

    else:
        print("eqiupo no encontrado.")

    sesion.close()


def eliminar_equipo(id):

    sesion = session()

    equipo = sesion.get(Equipo, id)

    if equipo is None:
        print("Equipo no encontrado.")

    else:
        prestamo = sesion.query(Prestamo).filter(
            Prestamo.equipo_id == id
        ).first()

        if prestamo:
            print("No se puede eliminar el equipo.")
            print("Motivo: tiene préstamos asociados.")

        else:
            sesion.delete(equipo)
            sesion.commit()

            print("Equipo eliminado correctamente.")

    sesion.close()
