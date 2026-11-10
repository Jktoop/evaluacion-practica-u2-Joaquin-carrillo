
from modelos import Base
from conexiones import engine
from registrar_equipos import crear_equipo, listar_equipos, buscar_equipo, actualizar_equipo, eliminar_equipo
from registrar_estudiantes import crear_estudiante, listar_estudiantes
from registrar_prestamos import crear_prestamo, listar_prestamos
from registrar_devoluciones import buscar_prestamo, devolver_prestamo



Base.metadata.create_all(engine)



def leer_numero(mensaje):

    while True:

        try:
            numero = int(input(mensaje))
            return numero

        except ValueError:
            print("Debe ingresar un número válido.")


def menu_equipos():

    while True:

        print("\n===== MENU EQUIPOS =====")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Buscar equipo por ID")
        print("4. Actualizar equipo")
        print("5. Eliminar equipo")
        print("6. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            nombre = input("Nombre del equipo: ")
            tipo = input("Tipo de equipo: ")
            stock = leer_numero("Stock disponible: ")

            crear_equipo(nombre, tipo, stock)

        elif opcion == "2":

            listar_equipos()

        elif opcion == "3":

            id_equipo = leer_numero("Ingrese el ID: ")

            buscar_equipo(id_equipo)

        elif opcion == "4":

            id_equipo = leer_numero("Ingrese el ID: ")
            nombre = input("Nuevo nombre: ")
            tipo = input("Nuevo tipo: ")
            stock = leer_numero("Nuevo stock: ")

            actualizar_equipo(
                id_equipo,
                nombre,
                tipo,
                stock
            )

        elif opcion == "5":

            id_equipo = leer_numero("Ingrese el ID: ")

            eliminar_equipo(id_equipo)

        elif opcion == "6":

            break

        else:

            print("Opción incorrecta.")



def menu_estudiantes():

    while True:

        print("\n===== MENU ESTUDIANTES =====")
        print("1. Registrar estudiante")
        print("2. Listar estudiantes")
        print("3. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            nombre = input("Nombre del estudiante: ")
            correo = input("Correo: ")

            crear_estudiante(nombre, correo)

        elif opcion == "2":

            listar_estudiantes()

        elif opcion == "3":

            break

        else:

            print("Opción incorrecta.")



def menu_prestamos():

    while True:

        print("\n===== MENU PRESTAMOS =====")
        print("1. Registrar préstamo")
        print("2. Listar préstamos")
        print("3. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            equipo_id = leer_numero("ID del equipo: ")

            estudiante_id = leer_numero("ID del estudiante: ")

            fecha = input("Fecha del préstamo: ")

            cantidad = leer_numero("Cantidad: ")

            crear_prestamo(
                equipo_id,
                estudiante_id,
                fecha,
                cantidad
            )

        elif opcion == "2":

            listar_prestamos()

        elif opcion == "3":

            break

        else:

            print("Opción incorrecta.")


def menu_devoluciones():

    while True:

        print("\n===== MENU DEVOLUCIONES =====")
        print("1. Buscar préstamo por ID")
        print("2. Registrar devolución")
        print("3. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            id_prestamo = leer_numero(
                "Ingrese el ID del préstamo: "
            )

            buscar_prestamo(id_prestamo)

        elif opcion == "2":

            id_prestamo = leer_numero(
                "Ingrese el ID del préstamo: "
            )

            devolver_prestamo(id_prestamo)

        elif opcion == "3":

            break

        else:

            print("Opción incorrecta.")


def menu_principal():

    while True:

        print("\n================================")
        print("       SISTEMA DE PRESTAMOS")
        print("================================")
        print("1. Gestionar equipos")
        print("2. Gestionar estudiantes")
        print("3. Gestionar préstamos")
        print("4. Gestionar devoluciones")
        print("5. Salir")
        print("================================")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            menu_equipos()

        elif opcion == "2":

            menu_estudiantes()

        elif opcion == "3":

            menu_prestamos()

        elif opcion == "4":

            menu_devoluciones()

        elif opcion == "5":

            print("Saliendo del sistema...")
            break

        else:

            print("Opción incorrecta.")


if __name__ == "__main__":
    menu_principal()


